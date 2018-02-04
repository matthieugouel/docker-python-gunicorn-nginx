# Docker Image : python-gunicorn-nginx

[![Build Status](https://travis-ci.org/MatthieuGouel/docker-python-gunicorn-nginx.svg?branch=master)](https://travis-ci.org/MatthieuGouel/docker-python-gunicorn-nginx)
[![Docker Build Status](https://img.shields.io/docker/build/matthieugouel/python-gunicorn-nginx.svg)](https://hub.docker.com/r/matthieugouel/python-gunicorn-nginx)
[![Docker Automated build](https://img.shields.io/docker/automated/matthieugouel/python-gunicorn-nginx.svg)](https://github.com/MatthieuGouel/docker-python-gunicorn-nginx)

This image contains Nginx and Gunicorn on top of Python3 docker image.
These two software are managed with Supervisor.

## Usage

The entry point of your application must be named as **run.py**. Moreover, the instance in that file must be called **app**.
Also, by default the worker class used is Gevent.

You can include a custom Gunicorn configuration file into your application. By default the configuration file must be name as **gunicorn.config.py**

## Dockerfile example

Here is an example of a Dockerfile using that image :

```
FROM matthieugouel/python-gunicorn-nginx:latest
MAINTAINER Matthieu Gouel

# Copy the application
COPY . /app

# Install application requirements
RUN pip install -U pip
RUN pip install -r /app/requirements.txt
```

There is also a Flask demo application in the *app* folder of this repository.

## Build and run

First, build your image based on your Dockerfile.

```
docker build -t prod_api .
```

Then, you can run a container like this :

```
docker run -p 127.0.0.1:8000:80 prod_api
```

And finally access it with curl for instance :

```
curl localhost:8000
```
