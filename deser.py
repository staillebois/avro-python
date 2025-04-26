from confluent_kafka.serialization import SerializationContext, MessageField
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.avro import AvroSerializer

schema_path = "user.avsc"
schema_registry_url = "http://localhost:8081"
output_file_path = "user.avro"
kafka_topic = "user_topic"

schema_registry_conf = {'url': schema_registry_url}
schema_registry_client = SchemaRegistryClient(schema_registry_conf)

with open(schema_path) as f:
        schema_str = f.read()

avro_serializer = AvroSerializer(schema_registry_client,schema_str)

user1 = {"name": "Ben", "favorite_number": 7, "favorite_color": "red"}
user2 = {"name": "Alice", "favorite_number": 42}

byte1 = avro_serializer(user1, SerializationContext(kafka_topic, MessageField.VALUE))
byte2 = avro_serializer(user1, SerializationContext(kafka_topic, MessageField.VALUE))

with open(output_file_path, "wb") as output_file:
    output_file.write(byte1 + byte2)

print(f"Serialized data written to {output_file_path}")