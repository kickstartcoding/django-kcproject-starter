![Kickstart Coding Logo](./apps/core/static/images/kickstart_coding_logo.png)

# Kickstart Coding: Django Project Starter

This is an example start project for [Kickstart Coding](https://kickstartcoding.com/)
Django projects.

It provides a solid foundation for building a Django project that's ready to
launch to Heroku or similar web-hosting service.


## About

### Features

* Clean, simple, and up-to-date: Only a few changes from the officia `django-admin startproject`

* Bootstrap 4: It's all set-up with Bootstrap 4.4.1 CSS, a few example pages,
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
    * Use Sqlite locally and postgres in production
    * While for bigger projects production / dev parity is vitally important,
      this is great for getting started with smaller projects

* Misc nice stuff:
    * `django-debug-toolbar` -- great debugging tool
    * Error pages

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

> This was originally created for Kickstart Coding, the cutting-edge,
> personalized, and affordable "custom-paced" full-stack online coding program.
> [Learn more and enroll in our Python / Django, JavaScript / React web
> development, and career development courses
> here.](http://kickstartcoding.com/?utm_source=github&utm_campaign=djprojectstarter)


## Development

* Prereqs: [1) You have Pipenv
  installed.](https://github.com/kickstartcoding/pipenv-getting-started) 2) You
  have Django admin installed globally (macOS type `pip3 install django`,
  Ubuntu GNU/Linux, type `sudo pip3 install django`)

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
pipenv install --skip-lock --dev
```

**Note:** It's probably okay if you get errors while installing `psycopg2`
and/or `gunicorn`, such as `'ERROR: Command errored out with exit status 1:
python setup.py egg_info Check the logs for full command output.'`.  These
packages are not needed for development. That's why we have `--skip-lock` 
specified to prevent these errors from stopping the installation.

3. This starter project *does not* include migrations. Make migrations as such:
```
python manage.py makemigrations accounts
```

4. Run the migrations to actually create the SQLite database:
```
python manage.py migrate
```

5. Get the server running:
```
python manage.py runserver
```

### Setting up with GitHub repo

1. Create a new repo on GitHub, and *BE SURE TO NOT* check "initialize with
README.md" or `.gitignore` or anything. You want to make a *truly blank repo*
for these steps to work without a hiccup.  Just fill in the name and
description, and nothing else.

2. Now, initialize and push the code we have by running this in the
command-line:

```bash
ls # Ensure you are "next to" the manage.py, etc
git init # Initalize this
git add -A # Add all your files
git commit -m "first" # Make a commit
```

3. Finally, link up your local repository with the git one, and push.  Follow
the instructions provided on the github.com page. They will look a little like
this, except instead of `janeqhacker/mycoolproject` it will be whatever your
username is and your repo name is:

```bash
git remote add origin git@github.com:janeqhacker/mycoolproject.git
git push -u origin master
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
        - forms.py         # Form for editing user profile, sign-up
        - templates/       # Templates for user profile stuff
    - core/                # An example custom app that has some static pages
        - static/          # Static files
        - templates/       # Core templates, including base templates
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

2. *Optional:* Confirm that the database is working by connecting to it with the
command-line client (`Ctrl+D` to exit):
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

6. Your site should work! View it in your browser.

7. You'll also want to add a `SECRET_KEY` to Heroku to make your site secure:
```bash
heroku config:set SECRET_KEY=randomly hit keys
```

NOTE: Where it says "randomly hit keys", do just that!  Just type a really long
random series of letters and numbers. You'll never have to remember it again.

----------------------


## Troubleshooting


### Issue: `django-admin startproject` fails

If you get an error like this while trying to do the initial `startproject`:

    CommandError: couldn't download URL https://github.com/kickstartcoding/django-kcproject-starter/archive/master.zip to master.zip
    <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1108)>

#### Work around

1. Go to https://github.com/kickstartcoding/django-kcproject-starter

2. Click the button `[Clone or download v]`, then click `[Download Zip]`

3. Save the `django-kcproject-starter-master.zip` file somewhere, such as in
your `~/Downloads` directory, or in the directory you are working

4. Now, run the same command as before (again using `mycoolproject` as the
example name), except referencing the downloaded copy. Example commands below:

```bash
#  If you saved it in ~/Downloads, then do:
django-admin startproject --template=~/Downloads/django-kcproject-starter-master.zip mycoolproject

#  If you saved it in the current directory:
django-admin startproject --template=./django-kcproject-starter-master.zip mycoolproject
```


#### Solution

This can happen to some users, often on macOS, and has to do with SSL
certificates and/or Python3 having some installation issues. To properly solve
this issue, you may need to upgrade your Python3 installation, and/or add
updated certificates. This can be tricky and OS-specific, so consider using the
work-around above.


### Issue: `pipenv install --dev` fails on `psycopg2` and/or `gunicorn`

You might get large error messages while installing these packages. It might
look like:

        'ERROR: Command errored out with exit status 1: python setup.py egg_info
        Check the logs for full command output.'


#### Work around

**Ignore it, and keep on developing!**

These packages are not needed for development. Likely everything else will work
fine, and you won't run into any issues while developing, since the local
development set-up is using Sqlite, not Postgres, and the local development
server doesn't use `gunicorn`.

#### Solution

For GNU/Linux based systems, `psycopg2` this can often be properly solved by
simply installing the Postgres client locally on your operating system (e.g.
`sudo apt install postgres`). For Macintosh-based operating systems, the
solution might be more involved, and we'd recommend searching for Mac-specific
answers about Python3 `psycopg2` failing to compile.


### Issue: `collectstatic` while deploying to Heroku fails

If you get an error like this:

        remote:            conn.setdefault('ATOMIC_REQUESTS', False)
        remote:        AttributeError: 'NoneType' object has no attribute 'setdefault'


That might mean your Postgres database isn't yet created, and that you possibly
skipped that step:

        heroku addons:create heroku-postgresql:hobby-dev

----------------------


## Going further




### Mailgun

1. Add env variables to Heroku as such:

```
heroku config:set MAILGUN_API_KEY=(YOUR API KEY AS SPECIFIED BY MAILGUN)
heroku config:set MAILGUN_DOMAIN=(YOUR DOMAIN AS SPECFIEID BY MAILGUN)
```

2. Install anymail

```
pipenv install django-anymail
```

3. Then, add the following to your `production.py`:


        # Anymail (Mailgun)
        # ------------------------------------------------------------------------------
        # https://anymail.readthedocs.io/en/stable/installation/#installing-anymail
        INSTALLED_APPS += ['anymail']
        EMAIL_BACKEND = 'anymail.backends.mailgun.EmailBackend'
        # https://anymail.readthedocs.io/en/stable/installation/#anymail-settings-reference
        ANYMAIL = {
            'MAILGUN_API_KEY': os.environ.get('MAILGUN_API_KEY'),
            'MAILGUN_SENDER_DOMAIN': os.environ.get('MAILGUN_DOMAIN')
        }



### AWS S3

If you want to be able to upload files and not have them be wiped out each time
you launch, you'll need to set up Amazon S3 or an equivalent competing Object
Store (such as Digital Ocean's Object Store).

Setup AWS and get your keys by following this guide:

<https://devcenter.heroku.com/articles/s3>


### Integrating with React (Create React App)

- This assumes familiarity with React and Create React App (CRA).
- These instructions will work with other frontend frameworks as well that
  follow a similar development pattern as CRA, with only a few tweaks necessary
  based on the commands they expect and the files and directories their
  build-tools generate

1. Start a new React app called "frontend", by running the following command in
the same directory as `manage.py`:
```
npx create-react-app frontend
```

2. Build the frontend. The goal here is to just have the "sample app" that
comes with CRA built and residing in the `build/` directory:
```
cd frontend
npm run build
```

3. Configure Django to serve up React's compiled JS, CSS, etc as additional
static files. Put this at the end of your "base.py" settings file:
```
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, '..', 'frontend', 'build', 'static'),
]
```

4. Create a view-function in Django to serve up the frontend's "index.html" in
the build directory to "kick things off". Open up `apps/core/views.py` and add
the following code:
```python
from django.http import HttpResponse
def react_app(request):
    index_contents = open('./frontend/build/index.html').read()
    return HttpResponse(index_contents)
```

5. Create a URL route for your new view-function. Open up `apps/core/urls.py`
and add the following URL path to the end of the list, before the `]`:
```
path('app/', views.react_app),
```

6. Now, run the Django server as you normally would, and navigate to
`localhost:8000/app/` -- if you did everything correctly, you should see the
CRA sample application in your browser!


7. If you are using React Router, you will want Django to serve up React in
lieu of a 404 page, to permit ANY route to go to React Router (not just `app/`
or the one you specify). Go into the project-level urls.py, and add the
following to the very end of the file:
```
from django.urls import re_path
from app.core import views
urlpatterns += [re_path(r'.*', views.react_app)]
```

Tips:

* To keep on using CRA's test server during development so you get
  live-reloading, running both Django and node simultaneously. To do this,
  you'll have to configure CRA's proxy setting, by editing
  `frontend/package.json` to include `"proxy": "http://localhost:8000/",` 
* After changes to your front-end, be sure to run `npm run build` to regenerate
  the compiled version of your JS.
* When deploying to production, make sure that the `build/` directory gets
  included in Git (remove it from .gitignore in the root directory and the
  `frontend/` directory if it happens to be in either)

