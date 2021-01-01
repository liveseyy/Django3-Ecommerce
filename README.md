Репозиторий интернет-магазина на Django 3.
Установка (для пользователей операционных систем семейства MacOs/Linux):

1. Открыть терминал или консоль и перейти в нужную Вам директорию
2. Прописать команду git clone git@github.com:liveseyy/Django3-Ecommerce.git
3. Если Вы используете https, то: git clone https://github.com/liveseyy/Django3-Ecommerce.git
4. Прописать следующие команды:
python3 -m venv ДиректорияВиртуальногоОкружения
source ДиректорияВиртуальногоОкружения/bin/activate
Перейти в директорию Django3-Ecommerce

pip install -r requirements.txt
python manage.py migrate


Запустить сервер - python manage.py runserver

Не забудьте создать директорию media, куда будут сохраняться изображения для товара