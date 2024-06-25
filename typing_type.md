In Python, you can introduce types using type hints (also known as type annotations) to indicate the expected types of variables, function arguments, and return values. Type hints were introduced in PEP 484 and are available in Python 3.5 and later. While type hints do not enforce type checking at runtime, they provide valuable information to developers and tools such as linters and IDEs, helping to catch potential type-related errors early in the development process.

Here's an overview of how to use type hints in Python:

### Basic Type Hints

1. **Variables**:
   You can annotate the type of a variable using the colon (:) followed by the type.

    ```python
    age: int = 25
    name: str = "Alice"
    is_student: bool = True
    ```

2. **Function Arguments and Return Values**:
   You can annotate the types of function arguments and the return value using the colon (:) and the arrow (->).

    ```python
    def greet(name: str) -> str:
        return f"Hello, {name}!"

    def add(a: int, b: int) -> int:
        return a + b
    ```

### Common Type Hints

-   **Basic Types**: `int`, `float`, `str`, `bool`
-   **None Type**: `None`
-   **Any Type**: `Any` (from the `typing` module)

    ```python
    from typing import Any

    def process(data: Any) -> None:
        print(data)
    ```

-   **Lists and Tuples**: `List`, `Tuple` (from the `typing` module)

    ```python
    from typing import List, Tuple

    def process_list(numbers: List[int]) -> List[int]:
        return [n * 2 for n in numbers]

    def process_tuple(data: Tuple[int, str]) -> str:
        return f"Number: {data[0]}, String: {data[1]}"
    ```

-   **Dictionaries**: `Dict` (from the `typing` module)

    ```python
    from typing import Dict

    def process_dict(data: Dict[str, int]) -> None:
        for key, value in data.items():
            print(f"{key}: {value}")
    ```

-   **Optional Type**: `Optional` (from the `typing` module)

    ```python
    from typing import Optional

    def process_optional(data: Optional[str]) -> None:
        if data:
            print(data)
        else:
            print("No data provided")
    ```

-   **Union Type**: `Union` (from the `typing` module) for specifying multiple possible types

    ```python
    from typing import Union

    def process_union(data: Union[int, str]) -> None:
        if isinstance(data, int):
            print(f"Integer: {data}")
        else:
            print(f"String: {data}")
    ```

### Advanced Type Hints

-   **Custom Types**: Use `TypeVar` to define generic types

    ```python
    from typing import TypeVar, List

    T = TypeVar('T')

    def get_first_element(elements: List[T]) -> T:
        return elements[0]
    ```

-   **Callable**: Use `Callable` to specify types of functions

    ```python
    from typing import Callable

    def process_function(func: Callable[[int, int], int], a: int, b: int) -> int:
        return func(a, b)

    def add(a: int, b: int) -> int:
        return a + b

    print(process_function(add, 2, 3))  # Output: 5
    ```

-   **TypedDict**: Define a dictionary with a fixed set of keys and associated types (available in Python 3.8+)

    ```python
    from typing import TypedDict

    class Person(TypedDict):
        name: str
        age: int

    def process_person(person: Person) -> None:
        print(f"Name: {person['name']}, Age: {person['age']}")

    person = Person(name="Alice", age=30)
    process_person(person)
    ```

### Checking Types

While type hints do not enforce types at runtime, you can use tools like `mypy` to perform static type checking.

1. **Install mypy**:

    ```sh
    pip install mypy
    ```

2. **Run mypy on your script**:
    ```sh
    mypy your_script.py
    ```

### Example Script with Type Hints

Here's a complete example that combines various type hints:

```python
from typing import List, Dict, Union, Optional

def extract_data() -> List[Dict[str, Union[int, str]]]:
    return [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"},
        {"id": 3, "name": "Charlie"},
    ]

def transform_data(data: List[Dict[str, Union[int, str]]]) -> List[Dict[str, Union[int, str]]]:
    for record in data:
        record["name"] = record["name"].upper()
    return data

def load_data(data: List[Dict[str, Union[int, str]]]) -> None:
    for record in data:
        print(f"Loading record: {record}")

def etl_pipeline(file_path: Optional[str] = None) -> None:
    data = extract_data()
    transformed_data = transform_data(data)
    load_data(transformed_data)

if __name__ == "__main__":
    etl_pipeline()
```

In this example, type hints help clarify the expected types of data throughout the ETL pipeline, improving code readability and maintainability.
