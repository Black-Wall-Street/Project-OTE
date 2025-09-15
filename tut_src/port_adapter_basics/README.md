# 🧱 Port-Adapter (Hexagonal) Architecture in Python

This project is a beginner-friendly, educational walkthrough of **Port-Adapter (aka Hexagonal) Architecture** using Python. It demonstrates clean separation between business logic, interfaces, and infrastructure. In this example we create a mini comment section database. You get to see the process of external information flowing into the hexagon, further processing within the hexagon, and the outbound flow of this data.

---

## 📐 Project Structure

```bash
port_adapter_basics/
├── domain/                    # Central source folder (the 'hexagon')
│   ├── ports/                # Inbound/Outbound interfaces (contracts)
│   │   └── comment_repository_port.py
│   ├── adapters/             # Implementations of outbound ports
│   │   └── in_memory_repository.py
│   ├── services/             # Application use cases
│   │   └── create_comment_service.py
│   ├── models/               # Domain entities and value objects
│   │   ├── comment.py
│   │   ├── author.py
│   │   └── content.py
│   └── logic/                # Entry points and demos
│       ├── cli.py
│       └── walkthrough.py
└── tests/                    # Pytest-based unit + integration tests
    ├── test_author.py
    ├── test_content.py
    ├── test_comment_service.py
    ├── test_comment_service_mock.py
    └── test_in_memory_repository.py
```

---

## 🧭 Step-by-Step Breakdown

### 1. **Define the Domain Layer**

**Purpose:** Isolate business logic and domain rules.

#### Files:

- `models/comment.py`: Defines the `Comment` entity.
- `models/author.py`: Value object with validation.
- `models/content.py`: Value object for comment content.

### 2. **Define Port Interfaces**

**Purpose:** Abstractions that allow communication between the core domain and external components.

#### File:

- `ports/comment_repository_port.py`: Defines `save()` and `get_by_id()` methods.

### 3. **Implement Services and Adapters**

#### Files:

- `services/create_comment_service.py`: Application service that wires together inputs, domain logic, and repository calls.
- `adapters/in_memory_repository.py`: In-memory repository to simulate persistence.

### 4. **Build Entry Points**

#### Files:

- `logic/cli.py`: A simple CLI to interact with the architecture.
- `logic/walkthrough.py`: An annotated terminal walkthrough showing the **full data flow** step-by-step (see below).

---

## 🧪 Running Tests

### Setup

Ensure you are in the root project folder (`port_adapter_basics`) and have all `__init__.py` files in place.

### Run Tests

```bash
# Option 1 (recommended)
PYTHONPATH=domain pytest tests/

# Option 2 (if using conftest.py with sys.path)
pytest tests/
```

### Test Coverage

- Value object behavior (`test_author.py`, `test_content.py`)
- Service logic with real adapter (`test_comment_service.py`)
- Adapter in isolation (`test_in_memory_repository.py`)
- Service behavior with mocked repository (`test_comment_service_mock.py`)

---

## 🧪 `walkthrough.py`: Visual Data Flow

### 🔍 Purpose

To **visually demonstrate** how data flows through each part of the hexagonal architecture:

1. CLI receives raw input (Primary Adapter)
2. Service (Inbound Port) creates value objects and entities
3. Comment entity constructed (inside the Hexagon)
4. Repository port is called (Outbound Port)
5. In-memory adapter saves the comment (Outbound Adapter)

### 🏃 Run It:

```bash
cd port_adapter_basics/
python -m domain.logic.walkthrough
```

> 🧠 This script uses emojis and step-by-step messages to show each architectural layer in action.

---

## ⚠️ Common Pitfalls & Errors

### 1. `ModuleNotFoundError: No module named 'domain'`

**Fix:** Run using:

```bash
PYTHONPATH=domain pytest tests/
```

Or set `sys.path` in `tests/conftest.py`

### 2. `ImportError: cannot import name 'CommentRepositoryPort'`

**Fix:** Ensure you're importing from the correct file:

```python
from ports.comment_repository_port import CommentRepositoryPort
```

Or expose it in `ports/__init__.py` with:

```python
from .comment_repository_port import CommentRepositoryPort
```

### 3. `Error while finding module specification for 'logic.walkthrough'`

**Fix:** Must run from the project root:

```bash
python -m domain.logic.walkthrough
```

---

### 4. To reiterate make sure **init**.py files are present in every folder marking folders as python packages

## 🧠 What You’ve Learned

- Clean architectural separation
- Testing each layer independently
- Inversion of control using ports
- Practical benefits of modular design
- How to visually trace execution in hexagonal systems

---

Enjoy hacking on clean architecture! 🧱✨
