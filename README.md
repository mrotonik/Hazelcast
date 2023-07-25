# Hazelcast




<h1 align="center">Проект Мікросервісів</h1>

<p align="center">
  <strong>Три мікросервіси, що взаємодіють через HTTP</strong>
</p>

<p align="center">
  <a href="#about">Про проект</a> •
  <a href="#architecture">Архітектура</a> •
  <a href="#installation">Інсталяція</a> •
  <a href="#usage">Використання</a> •
  <a href="#dp">Демонтрація проекту</a> •
</p>

---

<h2 id="about">Про проект</h2>

<p>Цей проект демонструє реалізацію трьох мікросервісів, що взаємодіють між собою за допомогою протоколу HTTP. Мікросервіси включають:</p>

<ul>
  <li><strong>facade-service</strong>: отримує POST/GET запити від клієнта.</li>
  <li><strong>logging-service 1-3</strong>: зберігає повідомлення в розподіленій карті за допомогою Hazelcast.</li>
  <li><strong>messages-service</strong>: виступає заглушкою і повертає статичне повідомлення.</li>
</ul>

<p>Клієнт взаємодіє з facade-service, який випадковим чином вибирає екземпляр logging-service для операцій запису та читання повідомлень.</p>

<h2 id="architecture">Архітектура</h2>

<p>Архітектура складається з трьох окремих веб-додатків, які можна запускати незалежно:</p>

<ul>
  <li><strong>facade-service</strong>: побудований з використанням FastAPI, отримує POST/GET запити від клієнта та взаємодіє з logging-service та messages-service.</li>
  <li><strong>logging-service</strong>: також побудований з використанням FastAPI, зберігає повідомлення в розподіленій карті за допомогою Hazelcast.</li>
  <li><strong>messages-service</strong>: побудований з використанням FastAPI, виступає заглушкою та повертає статичне повідомлення.</li>
</ul>

<h2 id="installation">Інсталяція</h2>

<p>Для запуску цих мікросервісів локально виконайте наступні кроки:</p>

<ol>
  <li>Склонуйте репозиторій:</li>
</ol>

<pre><code>git clone https://github.com/mrotonik/Hazelcast
</code></pre>

<ol start="2">
  <li>Встановіть залежності для кожного мікросервісу. Перейдіть до кожної папки мікросервісу (facade-service, logging-service1,logging-service2,logging-service3, messages-service) та виконайте команду:</li>
</ol>

<pre><code>pip install -r requirements.txt
</code></pre>

<ol start="3">
  <li>Налаштуйте та сконфігуруйте Hazelcast:</li>
</ol>

<ul>
  <li>Завантажте та встановіть Hazelcast, дотримуючись інструкцій на <a href="http://hazelcast.org/download/">офіційному веб-сайті</a>.</li>
  <li>Налаштуйте члени кластера Hazelcast в кожному мікросервісі, вказавши відповідну IP-адресу та номер порту в конфігурації <code>cluster_members</code>.</li>
</ul>

<ol start="4">
  <li>Запустіть кожен мікросервіс, виконавши команди в окремих термінальних вікнах:</li>
</ol>

<pre><code>uvicorn facade-service:app --port 5000
uvicorn logging-service_1:app --port 5001
uvicorn logging-service_2:app --port 5005
uvicorn logging-service_2:app --port 5006
uvicorn messages-service:app --port 5002
</code></pre>

<p>Переконайтеся, що ви оновлюєте номери портів, якщо це необхідно.</p>

<h2 id="usage">Використання</h2>

<p>Після запуску мікросервісів ви можете взаємодіяти з ними за допомогою HTTP POST та GET запитів. Для цього ви можете використовувати test.py</p>

<h3>Потік запитів HTTP POST:</h3>

<ol>
  <li>Відправте POST-запит до facade-service з текстовим повідомленням:</li>
</ol>

<pre><code>import requests

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
# Вимкнення одного/двох екземплярів logging-service
# Вимкніть сервіс, який працює на порті 5005 або 5006

response = requests.get("http://localhost:5000/message")
print(response.json())
</code></pre>











<h2 id="dp">Демонстрація проекту</h2>
    <figure>
  <img src="https://github.com/mrotonik/mrotonik/blob/master/laba2.gif" />
</figure>

<pre>
