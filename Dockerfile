# Pull base image 
FROM python:3.8


# set environment variables

ENV  PYTHONDONTWRITEBYTECODE 1
ENV PYHTONUNBUFFERED 1

# Set work directory
WORKDIR /code


# Install dependencies

COPY Pipfile Pipfile.lock /code/

RUN pip install pipenv && pipenv install --system

# Copy project

COPY . /code/