# Asl Elektro City — незавершённый проект

**Статус: разработка не завершена и отложена. Публичное демо приостановлено; проект пока не включён в портфолио готовых работ.**

Учебное Django-приложение с интерфейсами для заказов, товаров, сотрудников и истории продаж. Демонстрирует серверную обработку форм, работу с моделями и шаблонами, а также административную панель.

## Стек и структура

Python, Django, SQLite, HTML/CSS/JavaScript и WhiteNoise. `asilbek/` содержит предметные модели и представления, `accounts/` — вход, `templates/` — страницы, `static/` — оформление.

## Локальный запуск

```bash
python -m venv .venv
pip install -r requirements.txt
```

Активируйте виртуальное окружение перед установкой. Задайте `DJANGO_SETTINGS_MODULE=admin.render_settings` и собственный случайный `DJANGO_SECRET_KEY` в окружении. Затем:

```bash
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py createsuperuser
python manage.py runserver
```

В Windows переменные можно задать через `$env:DJANGO_SETTINGS_MODULE='admin.render_settings'` и `$env:DJANGO_SECRET_KEY='ваш-случайный-секрет'`. Откройте `http://localhost:8000/`; Django admin доступен на `/admin/`.

## Статус

Приложение представляет учебный прототип и требует доработок отдельных сценариев входа и форм перед реальным использованием. Для публичной демонстрации используется новая пустая SQLite-база; старые данные и `.env` в новую публикацию не включаются.

Render-конфигурация: build `pip install -r requirements.txt && python manage.py collectstatic --noinput`; start `python manage.py migrate --noinput && gunicorn admin.wsgi:application --bind 0.0.0.0:$PORT`. Нужны `DJANGO_SETTINGS_MODULE=admin.render_settings` и `DJANGO_SECRET_KEY`.

SQLite на бесплатном эфемерном диске не обеспечивает сохранность данных между развёртываниями. Для рабочего внедрения необходимы постоянная база и файловое хранилище.
