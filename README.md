<h3 align="center">IOT Devices - Crud, Notification Service</h3>
<div align="center">

<a><img alt="Django Version" src="https://img.shields.io/badge/django-3.2-green"></a>
<a><img alt="djangorest" src="https://img.shields.io/badge/djangorestframework-0"></a>
<a><img alt="django-signal" src="https://img.shields.io/badge/djangosignal-blue"></a>
<a><img alt="node" src="https://img.shields.io/node/v/npm?color=blue&label=node&logo=nodejs&logoColor=green"/></a>
<a><img alt="redis" src="https://img.shields.io/badge/redis-green"></a>


</div>


<p align="center"> Iot devices are fetching temperature reading from sensor and updating the database.
    <br> 
</p>


## Tech Stack
- [django](https://djangoproject.com/), [djangorestframework](https://djangorestframework.com/),
- [django-signal](https://docs.djangoproject.com/en/3.2/topics/signals/)
- [redis](https://redis.io/), [redis-py](https://github.com/andymccurdy/redis-py)
- [nodejs](https://nodejs.org/en/)

## Requirements
- [Docker](https://www.docker.com/)

## Getting Started
- Clone the repo<br />
  `git clone https://github.com/mehdirazajaffri/interel-test`
- cd root folder and run `docker-compose up`
- Django Admin (http://localhost:8000/admin)
- Web socket connection `ws://localhost:3000/`

## Architecture

![](docs/interel.png)

## Project Overview and Screenshots

- Django Admin Panel - written in admin.py (http://localhost:8000/admin)
- username: admin , password: admin123
![](docs/admin.png)

- Redoc Api Documentation (http://localhost:8000/redoc)
- Swagger Api Documentation (http://localhost:8000/swagger)
![](docs/redoc.png)
![](docs/swagger.png)

I am generating swagger Api documentation using third party package `drf-yasg`, for some api's query params are not listed,

- Docker Insight
![](docs/docker.png)

