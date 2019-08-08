# AssessmentApplication

[![Python Version](https://img.shields.io/badge/python-3.6-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-2.2-brightgreen.svg)](https://djangoproject.com)
<!-- [![CircleCI](https://circleci.com/gh/suhailvs/django-schools.svg?style=svg)](https://circleci.com/gh/suhailvs/django-schools) -->

 In this Django app, teachers can create quizzes and students can sign up and take quizzes related to their interests.




## Running the Project Locally

First, clone the repository to your local machine:

```bash
git clone https://github.com/MarvinKweyu/AssessmentApplication.git
```

Create Virtual Env and Install the requirements:

```bash
cd AssessmentApplication
python3 -m venv env
source ./env/bin/activate
pip install -r requirements.txt
```

Create the database:

```bash
cd AssessmentApplication
python manage.py migrate
```

Load datas, some questions, a **teacher**(user: `sumee`,pass: `sumee1910`) and a **student**(user: `suhail`,pass: `sumee1910`) 
```bash
python manage.py loaddata datas.json
```

Finally, run the development server:

```bash
python manage.py runserver
```

The project will be available at http://127.0.0.1:8000, Login using::

**Teacher**

username: `sumee`
password: `sumee1910`

**Student**

username: `suhail`
password: `sumee1910`


## License
The project is a fork of [suhail](https://github.com/suhailvs/django-schools)

The source code is released under the [MIT License](https://github.com/sibtc/django-multiple-user-types-example/blob/master/LICENSE).
