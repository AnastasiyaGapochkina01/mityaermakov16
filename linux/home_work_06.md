# Часть 1
1) В директории `linux-home-works` из [первой домашки](https://github.com/AnastasiyaGapochkina01/mityaermakov16/blob/main/linux/home_work_01.md) 
создать следующую структуру директорий
```
time-app/
├── docs
├── logs
├── src
│   └── docker
└── tests
    ├── auto
    └── unit
```
2) Создать файлы
- `docs/readme.md`
- `src/app.py` с содержимым
```python
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, FileResponse
import datetime
import random
import os

app = FastAPI()

LOG_DIR = "./logs"
LOG_FILE = f"{LOG_DIR}/time-app.log"

# Генерация случайных IP, метода, user-agent
methods = ["GET", "POST", "PUT", "DELETE"]
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "curl/7.68.0",
    "PostmanRuntime/7.26.10",
    "HTTPie/2.4.0",
    "python-requests/2.25.1"
]

def fake_log_entry():
    ip = f"{random.randint(10, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"
    method = random.choice(methods)
    user_agent = random.choice(user_agents)
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"{now} {ip} {method} {user_agent}\n"

@app.get("/")
async def root():
    now = datetime.datetime.now()
    return JSONResponse({
        "date": now.strftime("%Y-%m-%d"),
        "time": now.strftime("%H:%M:%S")
    })

@app.get("/logs")
async def logs():
    os.makedirs(LOG_DIR, exist_ok=True)
    # Генерируем 5 фейковых строк лога
    with open(LOG_FILE, "w") as f:
        for _ in range(5):
            f.write(fake_log_entry())
    return FileResponse(path=LOG_FILE, media_type="text/plain", filename="time-app.log")

@app.get("/longlog")
async def longlog():
    services = {
        "postgresql": [
            '2025-11-04 15:41:02 postgres[7205]: connection authorized: user=admin database=main',
            '2025-11-04 15:41:03 postgres[7205]: query executed: SELECT * FROM users;',
            '2025-11-04 15:41:05 postgres[7205]: user logged out: user=admin',
            '2025-11-04 15:41:07 postgres[7205]: backup started',
            '2025-11-04 15:41:09 postgres[7205]: checkpoint complete'
        ],
        "redis": [
            '2025-11-04 15:41:10 redis[21133]: Accepted connection from 127.0.0.1:51284',
            '2025-11-04 15:41:12 redis[21133]: SET key1 value1',
            '2025-11-04 15:41:14 redis[21133]: DEL key1',
            '2025-11-04 15:41:15 redis[21133]: SAVE completed',
            '2025-11-04 15:41:16 redis[21133]: Connection closed'
        ],
        "systemd": [
            '2025-11-04 15:41:17 systemd: Started Time App FastAPI Service.',
            '2025-11-04 15:41:18 systemd: Reloading.',
            '2025-11-04 15:41:19 systemd: Stopping Time App FastAPI Service.',
            '2025-11-04 15:41:20 systemd: Session 1 of user admin started.',
            '2025-11-04 15:41:22 systemd: Service restarted.'
        ],
        "docker": [
            '2025-11-04 15:41:23 dockerd: Container time-app started.',
            '2025-11-04 15:41:24 dockerd: Image pulled fastapi:latest.',
            '2025-11-04 15:41:25 dockerd: Container time-app stopped.',
            '2025-11-04 15:41:26 dockerd: Network created bridge0.',
            '2025-11-04 15:41:27 dockerd: Volume logs attached.'
        ]
    }

    os.makedirs(LOG_DIR, exist_ok=True)
    with open(f"{LOG_DIR}/large.log", "w") as f:
        for service, logs in services.items():
            f.write(f"====== {service.upper()} LOGS ======\n")
            for log in logs:
                f.write(log + "\n")
            f.write("\n")
    return {"status": "logs generated"}
```
- `tests/unit/test_app.py` с содержимым
```python
from fastapi.testclient import TestClient
from app import app
import re

client = TestClient(app)

def test_root_json():
    resp = client.get("/")
    assert resp.status_code == 200
    data = resp.json()
    # Проверка формата даты и времени
    assert re.match(r"\d{4}-\d{2}-\d{2}", data["date"])
    assert re.match(r"\d{2}:\d{2}:\d{2}", data["time"])

def test_logs_generation():
    resp = client.get("/logs")
    assert resp.status_code == 200
    log_content = resp.content.decode()
    lines = log_content.strip().split("\n")
    assert len(lines) == 5
    assert all(re.match(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} [\d\.]+ [A-Z]+ .+", line) for line in lines)
```
3) Установить пакет `python3-venv` (с помощью apt)
4) В корневой директории **проекта** выполнить
```bash
python3 -m venv venv
source venv/bin/activate
python3 -m pip install fastapi uvicorn pytest
```
5) Написать systemd unit-файл для запуска `src/app.py`; команда для запуска: `$PATH_TO_PROJECT/venv/bin/uvicorn app:app --port 9100`; запустить созданный сервис; проверить его работоспособность
```bash
curl 127.0.0.1:9100/
curl 127.0.0.1:9100/logs
```
примеры ответов
```bash
$ curl 127.0.0.1:9100
{"date":"2025-11-04","time":"12:37:12"}

$ curl 127.0.0.1:9100/logs
2025-11-04 12:37:16 121.141.190.242 DELETE PostmanRuntime/7.26.10
2025-11-04 12:37:16 89.161.163.253 PUT Mozilla/5.0 (Windows NT 10.0; Win64; x64)
2025-11-04 12:37:16 249.40.44.98 POST HTTPie/2.4.0
2025-11-04 12:37:16 254.195.168.218 GET curl/7.68.0
2025-11-04 12:37:16 193.129.25.64 PUT HTTPie/2.4.0
```
6) Проверить, что в директории `logs` появился файлик `time-app.log`
7) В файле `logs/time-app.log` найти все записи о GET запросах
8) Выполнить команду
```bash
$ curl 127.0.0.1:9100/longlog
```
9) Проверить, что в директории `logs` появился файлик `large.log`
10) В файле `logs/large.log` 
- найти записи о старте и остановке контейнера `time-app`
- вывести только имена сервисов, которые записали свои логи в файл `logs/large.log`

11) Определить модель процессора, используя в качестве источника данных файл /proc/cpuinfo
12) Вывести список всех портов в состоянии LISTEN на ВМ
13) Найти процесс запущенного выше приложения и вывести его PID
14) Из вывода команды `ip -4 -o a` вывести _только_ ip-адреса
15) Отфильтровать из вывода команды `dmesg` только ошибки
