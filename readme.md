# YouTube Search

An app that fetchs latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.

#### <a href="https://drive.google.com/file/d/1hypSTZQY0bPol01-hxB3MLjw-1G4OKAT/view?usp=sharing" target="_blank"> Demo Video </a>

## Frameworks/Libraries

1. Django + Django Rest Framework(DRF)
2. Postgres (Database)
3. Celery + Redis (Async Executor Combo)


## Prerequisite for setup

1. Python
2. <a href="https://pypi.org/project/pipenv/" target="_blank">Pipenv</a>
3. Redis

## Setup 

Create .env using .env.template file

```
$ cp .env.template .env
```
Create a database in Postgres and poplate values in .env. Follow the instructions below to create user and database
```
$ sudo -u postgres psql
```
Run below commands inside postgres shell
```
CREATE DATABASE video_serach_db;
```
```
CREATE USER test_user WITH PASSWORD 'password';
```
```
GRANT ALL PRIVILEGES ON DATABASE video_serach_db TO test_user;
```
```
ALTER ROLE test_user SET client_encoding TO 'utf8';
```
```

ALTER ROLE test_user SET default_transaction_isolation TO 'read committed';
```
```

ALTER ROLE test_user SET timezone TO 'UTC';

```

Create virtual enviorment and install dependencies

```
$ pipenv install --dev
```

Make sure your redis service is running, you can check that using ping
```
$ redis-cli ping
```
Populate Celery Values in .env, on local can use these values

```
CELERY_BROKER_URL='redis://localhost:6379'
CELERY_RESULT_BACKEND='redis://localhost:6379'
```


Make migrate and create super user
```
$ python manage.py migrate
``` 
```
$ python manage.py createsuperuser
``` 

Open <a href="http://127.0.0.1:8000/admin">Django admin</a> and add a new periodic task with desired name and Task (registered) to be selected is fetch_latest_video

![Alt text](/static/periodic_task_reference.png)

You must add API_KEY to be able to fetch records, you can do it via admin and  POST API too


Start the celery worker and beat with loglevel info
```
$ celery -A simpletask worker -l info
```
```
$ celery -A simpletask beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler

```
You will see videos being populated in the database periodically (in every 10 seconds)

## APIs

#### <a href="https://www.postman.com/poker-planner-phase2/workspace/public/collection/26266601-74191c05-8367-424b-a2a0-2f61a45d0cc4?action=share&creator=26266601" target="_blank"> Postman Collection </a>

### Add New YouTube API Key (POST)

 
 - Endpoint: {BASE_URL}/api/video/api-key/
 - Payload: 

    ```json
    {
        "key": "<your-key-here>"
    }
    ```

### List All Videos (GET)

 
 - Endpoint: {BASE_URL}/api/video/
 - Params:
    ```
    page: <page_number> (default: 1)

    page_size: <records_per_page> (default: 10)
    ```

### Search Videos (GET)

 
 - Endpoint: {BASE_URL}/api/video/search/
 - Params:
    ```
    query: <search-query-for-videos>

    page: <page_number> (default: 1)
    
    page_size: <records_per_page> (default: 10)
    ```

### Note

- This was not dockerized due to time contraint and I was not having enough knowledge about docker. I did tried but it all went in vain. Please let me know if you face any issue in legacy setup.
