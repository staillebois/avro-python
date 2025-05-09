from confluent_kafka.serialization import SerializationContext, MessageField
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.avro import AvroSerializer, AvroDeserializer

schema_path = "user.avsc"
schema_registry_url = "http://localhost:8081"
output_file_path = "user.avro"
kafka_topic = "user_topic"

schema_registry_conf = {'url': schema_registry_url}
schema_registry_client = SchemaRegistryClient(schema_registry_conf)

with open(schema_path) as f:
        schema_str = f.read()

avro_serializer = AvroSerializer(schema_registry_client,schema_str)

users = {
     "users": [
          {"name": "Ben", "favorite_number": 7, "favorite_color": "red"},
          {"name": "Alice", "favorite_number": 42, "favorite_color": "blue"}
        ]
    }

# Serialization
bytes = avro_serializer(users, SerializationContext(kafka_topic, MessageField.VALUE))

with open(output_file_path, "wb") as output_file:
    output_file.write(bytes)

print(f"Serialized data written to {output_file_path}")

# Deserialization
avro_deserializer = AvroDeserializer(schema_registry_client, schema_str)
with open(output_file_path, "rb") as input_file:
    data = input_file.read()
    deserialized_data = avro_deserializer(data, SerializationContext(kafka_topic, MessageField.VALUE))
    print(f"Deserialized data: {deserialized_data}")
