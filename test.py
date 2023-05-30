import requests
import uuid

# Генеруємо uuid для нашого повідомлення
msg_uuid = uuid.uuid4()

# Запит GET до facade-service
get_response = requests.get('http://localhost:5000')
print("GET Response:")
print(get_response.text)

# Запит POST до facade-service
post_response = requests.post('http://localhost:5000', json={"uuid": str(msg_uuid), "msg": "Hello, world!"})
print("POST Response:")
print(post_response.text)

# Запит GET до logging-service
get_response = requests.get('http://localhost:5001')
print("GET Response from logging service:")
print(get_response.text)

# Запит GET до message-service
get_response = requests.get('http://localhost:5002')
print("GET Response from message service:")
print(get_response.text)
