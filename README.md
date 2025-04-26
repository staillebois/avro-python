# avro-python

This project demonstrates how to serialize data into Avro format using the Confluent Kafka Python library and a Schema Registry.

## Prerequisites

- Python 3.7 or higher
- Confluent Kafka Python library with Avro and Schema Registry support
- A running instance of Confluent Schema Registry

## Installation

1. Clone this repository.
2. Install the required dependencies using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

## Files

- deser.py: The main script for serializing user data into Avro format.
- user.avsc: The Avro schema definition for the User record.
- user.avro: The output file where serialized Avro data is written.

## Usage

1. Ensure the Schema Registry is running and accessible at the URL specified in deser.py (http://localhost:8081 by default).
2. Run the script:
    ```bash
    python deser.py
    ```
3. The serialized Avro data will be written to `user.avro`, and the deserialized data will be printed to the console.

## Avro Schema

The Avro schema is defined in `user.avsc`:

```json
{
  "namespace": "example.avro",
  "type": "record",
  "name": "User",
  "fields": [
    {"name": "name", "type": "string"},
    {"name": "favorite_number", "type": ["int", "null"]},
    {"name": "favorite_color", "type": ["string", "null"]}
  ]
}
```

## Example Data

The script serializes the following user data:

- User 1: `{"name": "Ben", "favorite_number": 7, "favorite_color": "red"}`
- User 2: `{"name": "Alice", "favorite_number": 42}`

## Output

### Serialization

The serialized Avro data is written to `user.avro`. You can use tools like `avro-tools` or a compatible library to inspect the serialized data.

### Deserialization

The script reads the serialized data from `user.avro` and deserializes it back into Python objects. The deserialized data is printed to the console in the following format:

```plaintext
Deserialized data: {'name': 'Ben', 'favorite_number': 7, 'favorite_color': 'red'}
```
```plaintext
Deserialized data: {'name': 'Alice', 'favorite_number': 42, 'favorite_color': None}
```