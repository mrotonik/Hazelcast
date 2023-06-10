import requests

# HTTP POST-запити для запису 10 повідомлень через facade-service
messages = ["msg1", "msg2", "msg3", "msg4", "msg5", "msg6", "msg7", "msg8", "msg9", "msg10"]
for msg in messages:
    response = requests.post("http://localhost:5000/message", json={"msg": msg})
    print(response.json())


response = requests.get("http://localhost:5000/message")
print(response.json())

# Вимкнення одного/двох екземплярів logging-service
# Вимкніть сервіс, який працює на порті 5005 або 5006

response = requests.get("http://localhost:5000/message")
print(response.json())
