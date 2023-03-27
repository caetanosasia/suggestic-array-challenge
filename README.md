# Django and Docker example

This is my example Django setup using Docker for local development.

The Django files (in `myproject/`) are a very minimal initial project and app
simply to indicate that things are working. Replace it with your own more
useful code!

This README should:

1. Guide you through getting the Docker container up and running,
2. provide a little explanation as to how it's configured, and
3. provide some basic commands on how to work with it.

It might also give the impression I understand 100% how everything works; this is an illusion but, nevertheless, things do seem to work.


## 1. Build and run the container

1. Install Docker, e.g. [Docker for Mac](https://docs.docker.com/docker-for-mac/install/).

2. Download this repository.

3. Optional: In `docker-compose.yml` change the two `container_name` values from `myproject_db` and `myproject_web` to something that makes sense for your project. e.g. `weblog_db` and `weblog_web` if your project is called weblog.

4. If you did that you'll also need to change `myproject_web` in the two scripts within the `/scripts/` directory.

5. Create a `.env` file at the same level as this README, containing the following. This will be used by Docker.

    ```
    # Environment settings for local development.

    POSTGRES_USER=mydatabaseuser
    POSTGRES_PASSWORD=mypassword
    POSTGRES_DB=mydatabase
    POSTGRES_HOST=myproject_db

    DJANGO_SETTINGS_MODULE=myproject.myproject.settings.development
    ```

    **Note:** If you changed `myproject_db` in the previous step, you should change the `POSTGRES_HOST` value to match it in the `.env` file. You can change the other postgres settings if you like, but it's not required.

6. On the command line, within this directory, do this to build the image and
   start the container:

        docker-compose build

7. If that's successful you can then start it up. This will start up the database and web server, and display the Django `runserver` logs:

        docker-compose up

8. Open http://0.0.0.0:8000 in your browser.


### Run tests

    ./scripts/run-tests.sh
