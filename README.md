![Kickstart Coding Logo](./apps/core/static/images/kickstart_coding_logo.png)

# Kickstart Coding: Django Project Starter

This is an example start project for [Kickstart Coding](http://kickstartcoding.com/)
Django projects.

It provides a solid foundation for building a Django project that's ready to
launch to Heroku or similar web-hosting service.


## About

### Features

* Bootstrap 4: It's all set-up with Bootstrap 4 templates, a few example pages,
  and `django-bootstrap4` for easily bootstrap-based forms

* Accounts:
    * Log-in and sign-up pages
    * Custom user class
    * User profile page and user editing page

* Heroku support: It's one `git push` away from publishing to the world

* Pipenv: It's set-up to use Pipfile

* Code standards: This was created to be a happy medium between the default
  `django-admin` starting template and heavier weight scaffolding such as
  Audrey / Daniel Greenfield's
  [Django Cookiecutter](https://github.com/pydanny/cookiecutter-django),
  which might be better for larger projects

* Easy development:
    * Separate `local` and `production` settings
    * While for bigger projects production / dev parity is vitally important,
      this is great for getting started with smaller projects
    * Use Sqlite locally and postgres in production
    * `django-debug-toolbar` -- great debugging tool


### Who is this for

* This is for **new Python/Django programmers**, including **coding class
  students** who want a solid start for a Django project that uses SQLite when
  developing locally, and is ready to deploy Heroku provisioned Postgres
  database.

* The documentation assumes you already have fundamental Python, Django, Bash
  and Heroku knowledge. If you are new to Heroku, read our [Heroku Getting
  Started guide](http://github.com/kickstartcoding/heroku-getting-started/).
If you are new to Postgres, read our [Postgres Getting Started guide
  ](https://github.com/kickstartcoding/postgres-getting-started).

* The documentation *does not* explicitly support Windows. It assumes you use
  either **macOS** or a **GNU/Linux** distribution such as Ubuntu. That said,
  it might work.

> This was original created for Kickstart Coding, the affordable,
> inclusive, and intensive coding course teaching cutting-edge Python /
> Django and JavaScript / React web development in Oakland, CA.
> [Learn more and enroll here.](http://kickstartcoding.com/?utm_source=github&utm_campaign=cheatsheets)


## Development

* Prereq: [You have Pipenv installed.
  ](https://github.com/kickstartcoding/pipenv-getting-started) You have Django
  admin installed globally (macOS type `pip3 install django`, Ubuntu GNU/Linux,
  type `sudo pip3 install django`)

### Running locally

1. Assuming `mycoolproject` is the name of your project, you should start a new
project using this template as follows:
```
django-admin startproject --template=https://github.com/kickstartcoding/django-kcproject-starter/archive/master.zip mycoolproject
```

2. Go into the newly created project, and use `pipenv` to get your virtualenv
setup:
```
cd mycoolproject
pipenv shell
pipenv install --dev
```

3. Migrate to create the SQLite database:
```
python manage.py migrate
```

4. Get the server running:
```
python manage.py runserver
```

### File structure

Directory structure description below:

```python
[name_of_project]/
    - config/
        - base.py          # Stores most settings
        - local.py         # Stores settings only for local dev
        - production.py    # Stores settings only used by production (e.g. Heroku)
    - urls.py              # Global urls.py, in turn includes urls.py in apps

- apps/                    # A directory to store all our custom apps
    - accounts/            # An example custom app that includes sign-up and log-in
        - models.py        # Customized user class is here
        - urls.py          # URLs for sign-up and log-in pages
        - views.py         # Views for sign-up and log-in pages
        - forms.py         # Form for editing user profile
        - templates/       # Base template
    - core/                # An example custom app that has some static pages
        - static/          # Static files
        - templates/       # Static files
        - etc
- manage.py                # Entry point
- Pipfile                  # Development requirements
```


## Production


### Provisioning on Heroku

1. Creating a new Heroku app & Postgres Database (only need to do this once per
Heroku):
```bash
heroku create # Create a Heroku app (only run this if you haven't already)
heroku addons:create heroku-postgresql:hobby-dev
```

2. Confirm that the database is working by connecting to it with the
command-line client:
```bash
heroku pg:psql
```

3. Push to Heroku
```bash
git push heroku master
```


5. Run the migrations on the remote Postgres database. That can be done as
follows:
```bash
heroku run python manage.py migrate
```

6. Your site should be ready to go!

----------------------

## Going further

### Mailgun-powered email

Add env variables to Heroku as such:
    * MAILGUN_API_KEY
    * MAILGUN_DOMAIN

Then, add the following to your production.py:

    # Anymail (Mailgun)
    # ------------------------------------------------------------------------------
    # https://anymail.readthedocs.io/en/stable/installation/#installing-anymail
    INSTALLED_APPS += ['anymail']  # noqa F405
    EMAIL_BACKEND = 'anymail.backends.mailgun.EmailBackend'
    # https://anymail.readthedocs.io/en/stable/installation/#anymail-settings-reference
    ANYMAIL = {
        'MAILGUN_API_KEY': env('MAILGUN_API_KEY'),
        'MAILGUN_SENDER_DOMAIN': env('MAILGUN_DOMAIN')
    }


### AWS S3

AWS S3 is great for handling uploaded files. Typically, this is exactly what
you need: AWS supports as many and as large of files that your users might want
to upload.

- Use AWS:
    - Setup AWS and get your keys (follow this guide:
        https://devcenter.heroku.com/articles/s3#s3-setup)
    - Configure your keys using heroku config:add for each of the
        AWS settings specified by config/settings/production.py

