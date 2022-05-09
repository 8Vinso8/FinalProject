FROM python:3.10.4-alpine
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /backend
WORKDIR /backend

RUN pip install --upgrade pip
COPY ./requirements.txt /backend/
RUN pip install -r requirements.txt
COPY . /backend/

EXPOSE 8000