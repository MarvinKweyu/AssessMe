# AssessMe

[![Python Version](https://img.shields.io/badge/python-3.7-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-2.2-brightgreen.svg)](https://djangoproject.com)

 In this Django app, teachers can create quizzes and students can sign up and take quizzes related to their interests.

## Running the Project Locally

First, clone the repository to your local machine:

```bash
git clone https://github.com/MarvinKweyu/AssessMe.git
```

Create Virtual Env and Install the requirements:

```bash
cd AssessMe
python3 -m venv env
source ./env/bin/activate
pip install -r requirements.txt
```
Create a database:
```bash
cd AssessMe
python manage.py migrate 
```
Load use case data to work with.
```bash
python manage.py loaddata use_case_data.json
``` 

Finally, run the development server:

```bash
python manage.py runserver
```

The project will be available at http://127.0.0.1:8000, Login using::

**Teacher**

username: `sumee`
password: `sumee1911`

**Student**

username: `suhail`
password: `sumee1910`


## Contributions
Contributions are welcome.
Do remember to take a look at the project [contribution guidelines](./CONTRIBUTING.md)

## License
The project is based on [suhail](https://github.com/suhailvs/django-schools)

The source code is released under the [MIT License](https://github.com/MarvinKweyu/AssessMe/blob/master/LICENSE).
