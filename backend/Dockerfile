
FROM python:3.11.9-alpine3.19

RUN apk add --update gcc
RUN apk update --no-cache \
&& apk add build-base postgresql-dev libpq --no-cache --virtual .build-deps

WORKDIR /app

COPY . /app

COPY ./requeriments.txt /app/requeriments.txt

RUN pip install --no-cache-dir --upgrade -r /app/requeriments.txt

EXPOSE 8000

COPY ./main.py /app/

CMD ["fastapi", "run", "main.py", "--port", "8000"]



