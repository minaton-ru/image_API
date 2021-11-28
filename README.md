# Метод API для загрузки нескольких изображений  

Используется Django Rest Framework  
 
Загрузка нескольких изображений через API.  
Загруженные файлы сохраняются в директорию `\media\images`  
Файл сохраняется с уникальным именем.  
В файле views.py строка 9 - декоратор для авторизации пользователя (строка заккоментирована).  

## Описание API  
Метод POST  
URL - `http://127.0.0.1:8000/upload/`  
BODY -  список file: [путь к загружаемому файлу]  

## Запуск проекта  
Скопировать файлы  
```pip install -r requirements.txt```  
```python manage.py makemigrations```  
```python manage.py migrate```  
```python manage.py runserver```  

## Проверка работы метода API  
### Postman  
Метод POST  
URL - `http://127.0.0.1:8000/upload/`  
BODY:  
Key - file  
Value - [путь к загружаемому файлу]  

### Модуль Requests
```images = [('file', ('имяфайла.gif', open('/путь/к/файлу/имяфайла.gif', 'rb'))), ('file', ('имяфайла2.gif', open('/путь/к/файлу/имяфайла2.gif', 'rb')))]```  
```response = requests.request("POST", "http://127.0.0.1:8000/upload/", files=images)```  
```print(response.text)```  
