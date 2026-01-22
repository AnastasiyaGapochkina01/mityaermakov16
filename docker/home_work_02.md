1) Запустить приложение python (flask) + redis через compose. Структура проекта
```
cache-app/
├── compose.yml
├── app/
│   ├── Dockerfile
│   └── app.py
└── requirements.txt
```
содержимое файла
- **`app.py`**
```python
from flask import Flask
import redis, os, datetime
app = Flask(__name__)
r = redis.Redis(host='redis', port=6379)

@app.route('/')
def hello():
    count = r.incr('hits')
    return f'<h1>Hello Docker Compose! Посещений: {count}</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```
- **`requirements.txt`**
```
flask
redis
```
- **Dockerfile и compose.yml**  написать самостоятельно

2) Запустить с помощью docker compose приложение https://github.com/AnastasiyaGapochkina01/cyberpunk-devops
3) Запустить с помощью docker compose приложение https://github.com/AnastasiyaGapochkina01/http-py
