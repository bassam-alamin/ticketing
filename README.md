# Ticketing-template 
Ticketing APP

Prerequisites:
1. Make sure you have postgresql and redis installed on your machine
2. Create a database that you will replace it on the .env

How To Run:
1. Download all requirements from the requirements.txt file
    ``` pip install -r requirements.txt```

2. Copy contents of .env.example to your .env file and replace with the respective details

3. Run the server locally
    ```python manage.py runserver```

4. Run migrations
    ``` python manage.py migrate```

5. Start Celery Worker
    ``` celery -A ticketing worker -l INFO```

6. Start Celery Beat
    ``` celery -A ticketing beat -l INFO```


To view Api endpoints:
On Your browser enter
 [127.0.0.1:8000/developer/docs](http://127.0.0.1:8000/developer/docs)

 
<img width="1367" alt="Screenshot 2024-07-17 at 01 56 15" src="https://github.com/user-attachments/assets/17007873-06af-4955-9fcb-8cf447fbdd4b">

To run tests:
    ```python manage.py test```

Or run specific app tests:
    ```python manage.py test app_name```

