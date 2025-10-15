# Доп теория
1) Общие сведения: https://youtu.be/fmVI9Q2LavI
2) Изврат с контейнерами и systemd: https://youtu.be/M7qLOcwZqJM
3) Запуск приложения: https://www.youtube.com/watch?v=2V6PHRAB2t4 (тут unit-файл пишется примерно с 7:10, но если есть время/желание можно поглядеть все)
# Часть 1
1) Установить nginx, если он еще не установлен
2) Посмотреть статус демона nginx
3) Остановить nginx
4) Запустить nginx
5) Убрать nginx из автозагрузки
6) Вернуть nginx в автозагрузку
7) "Замаскировать" nginx, попробовать перезапустить/остановить/запустить nginx; снять с nginx "маскировку"
# Часть 2
1) Установить на ВМ php
2) В директории /opt создать папку rot13
3) В директории /opt/rot13 создать файл с именем rot13-server.php с кодом
```
<?php
$sock = socket_create(AF_INET, SOCK_DGRAM, SOL_UDP);
socket_bind($sock, '0.0.0.0', 10000);
for (;;) {
  socket_recvfrom($sock, $message, 1024, 0, $ip, $port);
  $reply = str_rot13($message);
  socket_sendto($sock, $reply, strlen($reply), 0, $ip, $port);
}
```
4) Запустить сервер командой php rot13-server.php и проверить что сервер работает: выполнить nc -u 127.0.0.1 10000 и ввести Hello World
5) Написать юнит-файл для запуска rot13-server.php как сервиса

# Часть 3 (сложная)
1) Установить redis ([install-redis-on-linux](https://redis.io/docs/latest/operate/oss_and_stack/install/install-redis/install-redis-on-linux/)) - ссылка доступна под VPN
2) Посмотреть статус демона redis
3) Запустить второй экземпляр демона redis, написав systemd unit

# Часть 4 (сложная)
Развернуть Python-веб-сервер, настроить управление через systemd

Код сервера
```python
from http.server import SimpleHTTPRequestHandler, HTTPServer
import os

os.chdir("/srv/webapp/content")
server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
```

#### Требования
1) Сервер запущен как systemd демон с правами пользователя `webadmin`
2) Пользователь `webadmin` не имеет shell-доступпа и является членом группы `webgroup`
3) Код сервера расположен в директории `/opt/srv/webapp`; в той же диреткории лежит `content/index.html` с содержимым
```html
<!DOCTYPE html>
<html>
<head>
    <title>Приветствие</title>
    <style>
        .greeting {
            border: 5px solid orange; 
            padding: 20px; 
            font-size: 48px;
            text-align: center; 
            margin: 50px auto; 
            width: fit-content;
            border-radius: 15px;
            background-color: #fff8f0; 
            font-family: Arial, sans-serif;
            box-shadow: 0 0 15px rgba(255, 165, 0, 0.3); 
        }
    </style>
</head>
<body>
    <div class="greeting">Hello, DOS-29-ONL! You are amazing!</div>
</body>
</html>
```
Проверка осуществляется командой `curl http://localhost:8000`
