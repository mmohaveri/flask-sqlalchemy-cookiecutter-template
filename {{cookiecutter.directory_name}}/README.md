# {{cookiecutter.project_title}}

{{cookiecutter.project_description}}

## Development

### Installing requirements

`{{cookiecutter.project_name}}` uses Python3.6 or higher. You can install all requirements using `make requirements`.
We highly suggest using [virtualenv](https://virtualenv.pypa.io/en/latest/) in order to avoid conflicts with other projects.

### Running locally

After installing dependencies simply run `python -m {{cookiecutter.project_name}}` in root directory of the project.
This will run {{cookiecutter.project_name}} package and shows you options it provides.

### Building docker image locally

You can build docker image locally, so you'll be able to test your code in an environment more similar to production.
