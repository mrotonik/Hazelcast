# Hazelcast
<img src="https://github.com/mrotonik/mrotonik/blob/master/edit2.png" alt="альтернативный текст">

<title>Опис проекту</title>
<style>
    body {
        font-family: Arial, sans-serif;
        max-width: 800px;
        margin: 0 auto;
        padding: 20px;
    }

    h1 {
        color: #333;
    }

    p {
        margin-bottom: 10px;
    }

    code {
        background-color: #f5f5f5;
        padding: 2px 4px;
        color: #333;
    }
</style>
</head>
<body>
<h1>Розподілений сервіс</h1>

<h2>Опис проекту</h2>
<p>Даний проект є прикладом реалізації простого розподіленого сервісу, який складається з трьох мікросервісів:</p>
<ul>
    <li><strong>facade-service</strong> - сервіс, що приймає HTTP POST/GET запити від клієнта</li>
    <li><strong>logging-service</strong> - сервіс, що зберігає отримані повідомлення в пам'яті та надає доступ до них</li>
    <li><strong>message-service</strong> - сервіс, що надає статичний текст повідомлення</li>
</ul>

<h2>Використані технології</h2>
<ul>
    <li>Python</li>
    <li>FastAPI - фреймворк для побудови веб-додатків</li>
    <li>Hazelcast - розподілене сховище даних</li>
</ul>

<h2>Запуск проекту</h2>
<ol>
    <li>Встановіть необхідні залежності, використовуючи команду <code>pip install -r requirements.txt</code></li>
    <li>Запустіть кожен сервіс окремо, виконавши відповідні скрипти:</li>
    <ul>
        <li>facade-service: <code>python facade_service.py</code></li>
        <li>logging-service: <code>python logging_service.py</code></li>
        <li>message-service: <code>python message_service.py</code></li>
    </ul>
    <li>Надсилайте HTTP запити до <code>localhost</code> на відповідні порти, щоб взаємодіяти з сервісами</li>
</ol>

<h2>Структура проекту</h2>
<pre>
