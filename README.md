# AccuKnox Technical Assignments

This repository contains solutions for the technical assessment, divided into two parts: Django Signals (Assignment 1) and a custom Python class (Assignment 2).

## Repository Structure

```text
accuknox_assingment/
├── assingment_1/          # Django Project (Signals)
│   ├── django_signals/    # Project settings
│   ├── pizzastore/        # App with signal proofs
│   └── manage.py
│
└── assingment_2/          # Python Script (Custom Class)
    └── main.py
````

## Assignment 1: Django Signals

Located in `assingment_1/`, this Django project demonstrates that standard Django signals are synchronous, run in the same thread, and share the caller's database transaction.

### Setup & Running

1.  **Navigate to the directory:**
    ```bash
    cd assingment_1
    ```
2.  **Install dependencies:**
    ```bash
    pip install django
    ```
3.  **Initialize Database:**
    ```bash
    python manage.py makemigrations pizzastore
    python manage.py migrate
    ```
4.  **Start Server:**
    ```bash
    python manage.py runserver
    ```

### Testing Views

Once the server is running, visit these URLs to see the proofs in your console terminal:

  * **Synchronous Test:** `http://127.0.0.1:8000/pizzastore/test-sync/`
    *(Waits 3 seconds for signal before finishing response)*
  * **Thread Test:** `http://127.0.0.1:8000/pizzastore/test-thread/`
    *(Prints identical thread IDs for Main and Signal)*
  * **Transaction Test:** `http://127.0.0.1:8000/pizzastore/test-transaction/`
    *(Signal raises exception, causing total rollback of the order)*

-----

## Assignment 2: Custom Python Class

Located in `assingment_2/`, this script defines a `Rectangle` class that can be iterated over to yield its length and width in a specific dictionary format.

### Running the Script

1.  **Navigate to the directory:**
    ```bash
    cd ../assingment_2
    ```
2.  **Execute the file:**
    ```bash
    python main.py
    ```

### Expected Output

```text
Creating a Rectangle(10, 5)
Iterating over the rectangle:
{'length': 10}
{'width': 5}
```

```
```
