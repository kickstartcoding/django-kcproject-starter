![Kickstart Coding Logo](./apps/core/static/images/kickstart_coding_logo.png)

# Kickstart Coding: Django Project Starter

This is an example start project for [Kickstart Coding](http://kickstartcoding.com/)
Django projects.

It provides a solid foundation for building a Django project that's ready to
launch to Heroku or similar web-hosting service.


## Features

* Bootstrap 4: It's all set-up with Bootstrap 4 templates, a few example pages,
  and `django-bootstrap4` for easily bootstrap-based forms

* Accounts: It includes a log-in, sign-up, and profile editing page ready-to-go.

* Custom user class: It features a custom user class

* Heroku support: It's one `git push` away from publishing to the world

* Pipenv: It's set-up to use Pipfile

* Easy development:
    * Separate `local` and `production` settings
    * While for bigger projects production / dev parity is vitally important,
      this is great for getting started with smaller projects
    * Use Sqlite locally and postgres in production
    * `django-debug-toolbar` -- great debugging tool


## Who is this for

* This is for **new Python/Django programmers**, including **coding class
  students** who want a solid start for a Django project that uses SQLite when
  developing locally, and is ready to deploy Heroku provisioned Postgres
  database.

* The documentation assumes you already have fundamental Python, Django, Bash
  and Heroku knowledge. If you are new to Heroku, read our [Heroku Getting
  Started guide](http://github.com/kickstartcoding/heroku-getting-started/).

* The documentation *does not* explicitly support Windows. It assumes you use
  either **macOS** or **Ubuntu GNU/Linux**.

> This was original created for Kickstart Coding, the affordable,
> inclusive, and intensive coding course teaching cutting-edge Python /
> Django and JavaScript / React web development in Oakland, CA.
> [Learn more and enroll here.](http://kickstartcoding.com/?utm_source=github&utm_campaign=cheatsheets)


## Getting started

* Prereq: [You have Pipenv installed.
  ](https://github.com/kickstartcoding/pipenv-getting-started) You have Django
  admin installed globally (macOS type `pip3 install django`, Ubuntu GNU/Linux,
  type `sudo pip3 install django`)

1. Assuming `mycoolproject` is the name of your project, you should start a new
project using this template as follows:

    django-admin startproject --template=https://github.com/kickstartcoding/django-kcproject-starter/archive/master.zip mycoolproject


2. Go into the newly created project, and use `pipenv` to get your virtualenv
setup:

    cd mycoolproject
    pipenv shell
    pipenv install --dev

3. Migrate to create the SQLite database:

    python manage.py migrate

4. Get the server running:

    python manage.py runserver

## Tour of files

Directory structure description below:

```python
[name_of_project]/
    - config/
        - base.py          # Stores most settings
        - local.py         # Stores settings only for local dev
        - production.py    # Stores settings only used by production (e.g. Heroku)
    - urls.py              # Global urls.py, in turn includes urls.py in apps
    - static/              # Static files
- apps/                    # A directory to store all our custom apps
    - accounts/            # An example custom app that includes sign-up and log-in
        - models.py        # Customized user class goes here
        - urls.py          # URLs for sign-up and log-in pages
        - views.p          # Views for sign-up and log-in pages
    - homepage/            # An example custom app that has some static pages
        - etc
```


## Launching to Heroku

* Prereq: [You have Heroku and Postgres installed and set-up.
  ](https://github.com/kickstartcoding/postgres-getting-started)

### Provisioning on Heroku


1. Local installation (only need to do once)
    * Ubuntu Linux: `sudo apt-get install postgresql-client`
    * macOS: `brew install postgres`

2. Creating a new Heroku Postgres Database (only need to do this once per
Heroku):
```bash
heroku create # Create a Heroku app (only run this if you haven't already)
heroku addons:create heroku-postgresql:hobby-dev
```

3. Confirm that the database is working by connecting to it with the
command-line client:
```bash
heroku pg:psql
```

4. Push to Heroku
```bash
git push heroku master
```


5. Once Heroku & Django is properly configured for Django and you've pushed it,
you'll need to run the migrations on the remote Postgres database. That can be
done as follows:
```bash
heroku run python manage.py migrate
```

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

