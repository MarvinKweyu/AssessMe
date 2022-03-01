<h1 style="text-align: center;"><span style="font-weight:bold">AssessMe</span></h1>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
[![Python Version](https://img.shields.io/badge/python-3.7-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-2.2-brightgreen.svg)](https://djangoproject.com)
[![CircleCI](https://circleci.com/gh/MarvinKweyu/AssessMe.svg?style=svg)](https://circleci.com/gh/MarvinKweyu/AssessMe)
![Release](https://img.shields.io/github/v/release/MarvinKweyu/AssessMe?include_prereleases)
![Contributors](https://img.shields.io/github/contributors/MarvinKweyu/AssessMe)
![Downloads](https://img.shields.io/github/downloads/MarvinKweyu/AssessMe/total?style=flat)
[![View](http://hits.dwyl.com/MarvinKweyu/AssessMe.svg)](http://hits.dwyl.com/MarvinKweyu/AssessMe)


 >An applicaition that allows teachers to create quizzes and students to
 take the quiz in relation to their interests



 # Table of Contents
 - [ Key features](#Features)

 - [ Running AssessMe locally ](#Setup)

 - [Contributions](#Contributions)


 - [License](#License)



## Features
---

- Password management
- Quiz timer
- Teacher download results option


# Setup
### Downloading the latest release.

Knab yourself the latest release version from the page
[release page](https://github.com/MarvinKweyu/AssessMe/releases)


---
### Docker Development

In the root directory of the project, run the following command:

```bash
docker-compose up --build

```

### Bare metal development


Create Virtual Env and Install the requirements:

```bash
cd AssessMe
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
Create a database:
```bash
cd AssessMe
python manage.py migrate --settings=assessme.settings.dev
```
Load use case data to work with.
```bash
python manage.py loaddata use_case_data.json --settings=assessme.settings.dev
``` 

Finally, run the development server:

```bash
python manage.py runserver --settings=assessme.settings.dev
```

The project will be available at http://127.0.0.1:8000, Login using::

**Teacher**

username: `teacher`
password: `teacher`

**Student**

username: `student`
password: `student`


## Contributions
---
Contributions are welcome.
Do remember to take a look at the project [contribution guidelines](./CONTRIBUTING.md)


## The AssessMe Contributor Board



<div align="center">
    <a href="https://github.com/MarvinKweyu/AssessMe/graphs/contributors">
        <img alt="contributors' avatars" src="https://contrib.rocks/image?repo=MarvinKweyu/AssessMe" />
    </a>
</div>


## License
---

This project was inspired by [suhail's](https://github.com/suhailvs/django-schools) work on the django quiz application and is released under the [MIT License](https://github.com/MarvinKweyu/AssessMe/blob/master/LICENSE).


