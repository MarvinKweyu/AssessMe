FROM python:3.9.6-alpine
WORKDIR /usr/src/assessme

# env variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# deps
RUN apk update 
RUN apk add postgresql-dev gcc musl-dev python3-dev libffi-dev openssl-dev

# app deps
RUN pip install --upgrade pip
COPY ./requirements.txt .

RUN pip install -r requirements.txt

# entrypoint
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/assessme/entrypoint.sh


COPY . .

# run entrypoint
ENTRYPOINT [ "/usr/src/assessme/entrypoint.sh" ]
