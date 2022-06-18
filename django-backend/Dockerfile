FROM python:3.10.4-alpine
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /backend
WORKDIR /backend

RUN pip install --upgrade pip
COPY ./requirements.txt /backend/
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev \
    && apk add libffi-dev
RUN pip install -r requirements.txt
COPY . /backend/

EXPOSE 8000