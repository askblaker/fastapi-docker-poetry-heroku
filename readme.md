# Deploying dockerized fastAPI to Heroku

## With poetry and docker-compose

[FastAPI](https://fastapi.tiangolo.com/)  
[Docker / Docker-Compose](https://www.docker.com/)  
[Heroku](https://www.heroku.com/)  
[Poetry](https://python-poetry.org/)

1. Clone this repo. Set up and push to heroku.

```bash
git clone git@github.com:askblaker/fastapi-docker-poetry-heroku.git
cd fastapi-docker-poetry-heroku
heroku create <your-app-name>
heroku git:remote <your-app-name>
heroku stack:set container
git push heroku main
```

2.  Enjoy your fastAPI at https://your-app-name.herokuapp.com

3.  Adding packages

```
cd fastapi-docker-poetry-heroku
poetry install
poetry add pandas
```

or with docker run:

```
docker-compose run api poetry add pandas
```

4. To run locally, use `docker-compose up`and `docker-compose down`. To build use `docker-compose build`
