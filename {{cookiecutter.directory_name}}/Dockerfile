FROM python:3.7

LABEL maintainer="{{cookiecutter.maintainer_name}} <{{cookiecutter.maintainer_email}}>"

WORKDIR /home

COPY ./{{cookiecutter.project_name}} ./{{cookiecutter.project_name}}
COPY requirements.txt Makefile /home/

RUN make requirements

CMD ["python", "-m", "{{cookiecutter.project_name}}", "serve"]
