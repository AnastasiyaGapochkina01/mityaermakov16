Запустить в docker приложение https://github.com/AnastasiyaGapochkina01/demo-app/tree/main

Требования
1) Проект запущен с помощью docker compose
2) Приложение НЕ публикует свои порты на хост
3) Доступ к приложению осуществляется через nginx
4) Для проекта должна быть создана отдельная docker сеть
5) Конфигурационный файл nginx НЕ пробрасываеется через bind mount в compose, а "запекается" в image
6) На контейнер приложения в comspose повесить healthcheck
