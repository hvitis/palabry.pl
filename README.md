# Palabry.pl

## Game rules

- You have to guess the Wordle in six goes or less.
- Every word you enter must be in the word list. ...
- A correct letter turns green.
- A correct letter in the wrong place turns yellow.
- An incorrect letter turns gray.
- Letters can be used more than once.

## Running the code

Out of the box, Django will serve the application entry point (`index.html` + bundled assets) at `/` ,
data at `/api/`, and static files at `/static/`. Django admin panel is also available at `/admin/` and can be extended as needed.

### Template Structure

| Location       | Content                                                 |
| -------------- | ------------------------------------------------------- |
| `/backend`     | Django Project & Backend Config                         |
| `/backend/api` | Django App (`/api`)                                     |
| `/frontend`    | Vue 3 TypeScript App                                    |
| `/dist/`       | Bundled Assets Output (generated at `yarn` in the root) |

## Prerequisites

Before getting started you should have the following installed and running:

- [Node.js](https://nodejs.org/en/)
- [Yarn](https://yarnpkg.com/en/docs/install)
- [Python 3](https://wiki.python.org/moin/BeginnersGuide) + [virtual environment](https://docs.python.org/3/library/venv.html)

## Setup

```bash
$ git clone https://github.com/ksaaskil/django-vue3-template
$ cd django-vue3-template
```

Install dependencies:

```bash
$ yarn install
$ pip install -r requirements.txt
$ python manage.py migrate  # Prepare local Django database
```

## Running Development Servers

Start the Django backend:

```bash
$ python manage.py runserver
```

Start the frontend:

```bash
$ cd frontend
$ yarn serve
```

The Vue application will be served from [`localhost:8080`](http://localhost:8080/) and the Django API
and static files will be served from [`localhost:8000`](http://localhost:8000/).

The dual dev server setup allows you to take advantage of
webpack's development server with hot module replacement.
Proxy config in [`frontend/vue.config.js`](/frontend/vue.config.js) is used to route the requests
back to django's API on port 8000.

If you would rather run a single dev server, you can run Django's
development server only on `:8000`, but you have to build the Vue app first (`yarn`)
and the page will not reload on changes.

```bash
$ yarn  # Builds a dist/ folder at the root of the repository
$ python manage.py runserver
```

## Deploy

- Set `ALLOWED_HOSTS` on [`backend.settings.prod`](/backend/settings/prod.py)

## Static Assets

See `settings.dev` and [`vue.config.js`](/frontend/vue.config.js) for notes on static assets strategy.

This template implements the approach suggested by Whitenoise Django.
For more details see [WhiteNoise Documentation](http://whitenoise.evans.io/en/stable/django.html)

It uses Django Whitenoise to serve all static files and Vue bundled files at `/static/`.
While it might seem inefficient, the issue is immediately solved by adding a CDN
with Cloudfront or similar.
Use [`vue.config.js`](/vue.config.js) > `baseUrl` option to set point all your assets to the CDN,
and then set your CDN's origin back to your domains `/static` url.

Whitenoise will serve static files to your CDN once, but then those assets are cached
and served directly by the CDN.

This allows for an extremely simple setup without the need for a separate static server.

[Cloudfront Setup Wiki](https://github.com/gtalarico/django-vue-template/wiki/Setup-CDN-on-Cloud-Front)
