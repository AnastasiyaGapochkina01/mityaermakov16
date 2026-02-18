1) Написать пайплайн, состоящий из этапов
- build: job должна выводить строку "Run build on hostname", где hostname - hostname контейнера, в котором запустилась job
- test: job должна выводить строку "Run tests..."
- deploy: job должна выводить строку "Run deploy"
2) Написать пайплайн для сборки и тестирования модуля python из репозитория https://github.com/AnastasiyaGapochkina01/calculate-py-module

Этапы пайплайна
- scan: сканирование на уязвимости
```bash
pip install -e .
pip install -r requirements.txt
bandit -r app/ -f json -o bandit_results.json || true
```
- tests: тестирование
```bash
PYTHONPATH=src pytest -v tests/ --junitxml=test-results.xml
```
- release: сборка модуля с сохранением результата в артефакты
```bash
python setup.py sdist bdist_wheel
ls -la dist/ || echo "Папка dist не существует"
```
