"""
Demo RAG Pipeline — End-to-End Example
Skill: rag-engineer

Usage:
    python demo_rag_pipeline.py build "02_Process/sgk_antigravity.md"
    python demo_rag_pipeline.py search "KWSR là gì?"
    python demo_rag_pipeline.py search "Cách tạo Skill" --top-k 3

Yêu cầu:
    pip install langchain langchain-community faiss-cpu sentence-transformers
"""

import argparse
import os
import pickle
import sys
from pathlib import Path

# === CONFIGURATION ===
INDEX_DIR = Path("03_Outputs/faiss_index")
INDEX_FILE = INDEX_DIR / "index.faiss"
METADATA_FILE = INDEX_DIR / "metadata.pkl"
CHUNK_SIZE = 4000  # ~4KB per chunk (optimal range 2-8KB)
CHUNK_OVERLAP = 400
EMBEDDING_MODEL = "keepitreal/vietnamese-sbert"


def build_index(markdown_path):
    """Build FAISS index from a Markdown file."""
    from langchain.text_splitter import MarkdownTextSplitter
    from langchain_community.embeddings import HuggingFaceEmbeddings
    from langchain_community.vectorstores import FAISS

    # Step 1: Read markdown
    print(f"📂 Đọc file: {markdown_path}")
    with open(markdown_path, "r", encoding="utf-8") as f:
        content = f.read()
    print(f"   Kích thước: {len(content):,} ký tự")

    # Step 2: Chunk with MarkdownTextSplitter
    splitter = MarkdownTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
    )
    chunks = splitter.create_documents([content])
    print(f"✂️  Chia thành {len(chunks)} chunks (target: {CHUNK_SIZE} chars)")

    # Step 3: Validate chunk sizes
    sizes = [len(c.page_content) for c in chunks]
    print(f"   Min: {min(sizes):,} | Max: {max(sizes):,} | Avg: {sum(sizes)//len(sizes):,}")

    too_small = sum(1 for s in sizes if s < 500)
    too_large = sum(1 for s in sizes if s > 15000)
    if too_small:
        print(f"   ⚠️ {too_small} chunks < 500 chars (quá nhỏ)")
    if too_large:
        print(f"   🔴 {too_large} chunks > 15KB (cần split thêm)")

    # Step 4: Add metadata
    for i, chunk in enumerate(chunks):
        chunk.metadata["source"] = str(markdown_path)
        chunk.metadata["chunk_id"] = i
        chunk.metadata["char_count"] = len(chunk.page_content)

    # Step 5: Build FAISS index
    print(f"\n🔧 Loading embedding model: {EMBEDDING_MODEL}")
    embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL,
        model_kwargs={"device": "cpu"},
    )

    print("📊 Building FAISS index...")
    vectorstore = FAISS.from_documents(chunks, embeddings)

    # Step 6: Save
    INDEX_DIR.mkdir(parents=True, exist_ok=True)
    vectorstore.save_local(str(INDEX_DIR))

    # Save chunk metadata separately for inspection
    meta = [{"id": i, "chars": len(c.page_content), "preview": c.page_content[:100]}
            for i, c in enumerate(chunks)]
    with open(METADATA_FILE, "wb") as f:
        pickle.dump(meta, f)

    print(f"\n✅ Index saved: {INDEX_DIR}")
    print(f"   Chunks: {len(chunks)} | Index size: {INDEX_FILE.stat().st_size:,} bytes")


def search_index(query, top_k=3):
    """Search the FAISS index."""
    from langchain_community.embeddings import HuggingFaceEmbeddings
    from langchain_community.vectorstores import FAISS

    if not INDEX_FILE.exists():
        print("❌ Chưa có index. Chạy: python demo_rag_pipeline.py build <file.md>")
        sys.exit(1)

    # Load
    embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL,
        model_kwargs={"device": "cpu"},
    )
    vectorstore = FAISS.load_local(
        str(INDEX_DIR), embeddings, allow_dangerous_deserialization=True
    )

    # Search
    print(f"🔎 Query: \"{query}\"")
    print(f"   Top-K: {top_k}\n")

    results = vectorstore.similarity_search_with_score(query, k=top_k)

    for i, (doc, score) in enumerate(results, 1):
        relevance = "🟢" if score < 0.5 else ("🟡" if score < 1.0 else "🔴")
        print(f"--- [{i}] {relevance} Score: {score:.4f} ---")
        print(f"Source: {doc.metadata.get('source', 'N/A')}")
        print(f"Chunk #{doc.metadata.get('chunk_id', '?')} ({doc.metadata.get('char_count', '?')} chars)")
        # Print first 300 chars as preview
        preview = doc.page_content[:300].replace("\n", " ")
        print(f"Preview: {preview}...")
        print()

    # Anti-hallucination reminder
    print("💡 Nhắc: Chỉ trả lời dựa trên context trên. Nếu không đủ thông tin → nói rõ.")


def main():
    parser = argparse.ArgumentParser(description="RAG Pipeline Demo (rag-engineer skill)")
    subparsers = parser.add_subparsers(dest="command")

    # Build command
    build_parser = subparsers.add_parser("build", help="Build FAISS index từ file Markdown")
    build_parser.add_argument("filepath", help="Đường dẫn file .md")

    # Search command
    search_parser = subparsers.add_parser("search", help="Tìm kiếm trong index")
    search_parser.add_argument("query", help="Câu hỏi tìm kiếm")
    search_parser.add_argument("--top-k", type=int, default=3, help="Số kết quả (mặc định: 3)")

    args = parser.parse_args()

    # Fix encoding for Windows
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

    if args.command == "build":
        build_index(args.filepath)
    elif args.command == "search":
        search_index(args.query, args.top_k)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
