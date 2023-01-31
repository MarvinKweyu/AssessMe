FROM python:3.9.6-alpine
WORKDIR /myapp

# env variables
ENV PYTHONUNBUFFERED 1
# prevent pyc file creation
ENV PYTHONDONTWRITEBYTECODE 1

# deps
RUN apk update && apk add postgresql-dev gcc musl-dev python3-dev libffi-dev openssl-dev

# app deps
RUN pip install --upgrade pip
COPY ./requirements.txt .

RUN pip install -r requirements.txt

# entrypoint
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /myapp/entrypoint.sh


COPY . .

# run entrypoint
ENTRYPOINT [ "/myapp/entrypoint.sh" ]
