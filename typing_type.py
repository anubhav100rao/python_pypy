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
