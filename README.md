## 1. Build and run the container

1. Install Docker, e.g. [Docker for Mac](https://docs.docker.com/docker-for-mac/install/).

2. Download this repository.

3. Optional: In `docker-compose.yml` change the two `container_name` values from `myproject_db_1` and `myproject_api` to something that makes sense for your project. e.g. `weblog_db` and `weblog_web` if your project is called weblog.

4. If you did that you'll also need to change `myproject_api` in the two scripts within the `/scripts/` directory.

5. Create a `.env` file at the same level as this README, containing the following. This will be used by Docker.

    ```
    # Environment settings for local development.

    POSTGRES_USER=mydatabaseuser
    POSTGRES_PASSWORD=mypassword
    POSTGRES_DB=mydatabase
    POSTGRES_HOST=myproject_db

    DJANGO_SETTINGS_MODULE=myproject.myproject.settings.development
    ```

    **Note:** If you changed `myproject_db_1` in the previous step, you should change the `POSTGRES_HOST` value to match it in the `.env` file. You can change the other postgres settings if you like, but it's not required.

6. On the command line, within this directory, do this to build the image and
   start the container:

        docker-compose build

7. If that's successful you can then start it up. This will start up the database and web server, and display the Django `runserver` logs:

        docker-compose up

8. Open http://0.0.0.0:8000 in your browser.


## 2. Ongoing work

Every time you come to work on the site:

    docker-compose up

To access the shell in the web container:

    docker exec -it myproject_api sh

To create migrations: 

    pipenv run ./manage.py makemigrations

To migrate:

    pipenv run ./manage.py migrate

So, to create your Django project's superuser:

    pipenv run ./manage.py createsuperuser

If you want see more commands:

    pipenv run ./manage.py help

### Run tests

Inside docker shell:

    pipenv run ./manage.py test

Curl from test endpoint:

    curl --location 'http://0.0.0.0:8000/normalize-array/' \
    --header 'Content-Type: application/json' \
    --data '{"input": [1, 2, [3, 4, [5, 6], 7], 8, 10]}'