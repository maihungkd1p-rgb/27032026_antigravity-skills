---
name: error-handling-patterns
description: Master error handling patterns across languages including exceptions, Result types, error propagation, and graceful degradation to build resilient applications. Use when implementing error handling, designing APIs, debugging production issues, or improving application reliability.
---

# Error Handling Patterns

Build resilient applications with robust error handling strategies that gracefully handle failures and provide excellent debugging experiences.

## When to Use This Skill
- Implementing error handling in new features
- Designing error-resilient APIs
- Debugging production issues
- Improving application reliability
- Creating better error messages for users and developers
- Implementing retry and circuit breaker patterns
- Handling async/concurrent errors
- Building fault-tolerant distributed systems

## Core Concepts

### 1. Error Handling Philosophies
**Exceptions vs Result Types:**
- **Exceptions:** Traditional try-catch, disrupts control flow (Java, Python, TS)
- **Result Types:** Explicit success/failure, functional approach (Rust, Elm)
- **Error Codes:** C-style, requires discipline (Go, C)
- **Option/Maybe Types:** For nullable values

**When to Use Each:**
- **Exceptions:** Unexpected errors, exceptional conditions
- **Result Types:** Expected errors, validation failures
- **Panics/Crashes:** Unrecoverable errors, programming bugs

### 2. Error Categories
**Recoverable Errors:**
- Network timeouts, Missing files, Invalid user input, API rate limits

**Unrecoverable Errors:**
- Out of memory, Stack overflow, Programming bugs (null pointer, etc.)

## Language-Specific Patterns

### Python Error Handling
**Custom Exception Hierarchy:**
```python
class ApplicationError(Exception):
    """Base exception for all application errors."""
    def __init__(self, message: str, code: str = None, details: dict = None):
        super().__init__(message)
        self.code = code
        self.details = details or {}
        self.timestamp = datetime.utcnow()

class ValidationError(ApplicationError):
    pass

class NotFoundError(ApplicationError):
    pass

class ExternalServiceError(ApplicationError):
    def __init__(self, message: str, service: str, **kwargs):
        super().__init__(message, **kwargs)
        self.service = service
```

**Context Managers for Cleanup:**
```python
from contextlib import contextmanager

@contextmanager
def database_transaction(session):
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise
    finally:
        session.close()
```

**Retry with Exponential Backoff:**
```python
def retry(max_attempts=3, backoff_factor=2.0, exceptions=(Exception,)):
    # ... implementation ...
```

### TypeScript/JavaScript Error Handling
**Custom Error Classes:**
```typescript
class ApplicationError extends Error {
  constructor(
    message: string,
    public code: string,
    public statusCode: number = 500,
    public details?: Record<string, any>,
  ) {
    super(message);
    this.name = this.constructor.name;
    Error.captureStackTrace(this, this.constructor);
  }
}
```

**Result Type Pattern:**
```typescript
type Result<T, E = Error> = { ok: true; value: T } | { ok: false; error: E };

function Ok<T>(value: T): Result<T, never> { return { ok: true, value }; }
function Err<E>(error: E): Result<never, E> { return { ok: false, error }; }
```

### Rust & Go Patterns
(Refer to full documentation for Result/Option types in Rust and Explicit Error Returns in Go)

## Universal Patterns

### Pattern 1: Circuit Breaker
Prevent cascading failures in distributed systems.
- **States**: CLOSED (Normal), OPEN (Failing), HALF_OPEN (Testing)
- **Logic**: Fails fast if threshold reached, retries after timeout.

### Pattern 2: Error Aggregation
Collect multiple errors instead of failing on first error (e.g., form validation).
```typescript
class ErrorCollector {
  private errors: Error[] = [];
  add(error: Error) { this.errors.push(error); }
  throw() { if (this.errors.length > 0) throw new AggregateError(this.errors); }
}
```

### Pattern 3: Graceful Degradation
Provide fallback functionality when errors occur.
```python
def get_user_profile(user_id):
    return with_fallback(
        primary=lambda: fetch_from_cache(user_id),
        fallback=lambda: fetch_from_database(user_id)
    )
```

## Best Practices
1.  **Fail Fast:** Validate input early.
2.  **Preserve Context:** Include stack traces, metadata.
3.  **Meaningful Messages:** Explain what happened and how to fix it.
4.  **Log Appropriately:** Error = log, expected failure = don't spam.
5.  **Clean Up Resources:** Use try-finally, context managers.
6.  **Don't Swallow Errors:** Log or re-throw.

## Common Pitfalls
- `except Exception` hiding bugs.
- Empty catch blocks.
- Logging AND re-throwing (duplicate logs).
- "Error occurred" generic messages.
