# Web App for Predicting Russian Troll Tweets

This [web app]() is a companion to my project using machine learning to [classify tweets from Russian troll accounts].

It's built using `flask` and deployed to `heroku`.

## Set-Up Instructions

#### 1. Set the `FLASK_APP` environment variable, and run flask

```bash
$ export FLASK_APP=app.py
$ export FLASK_ENV=development
$ flask run
```

#### 2. Create a new heroku app

```bash
$ heroku create russian-trolls-detector
```

#### 3. Make modifications to the app, add and commit changes, and push to `heroku` remote

```bash
$ git add .
$ git commit -m "a commit message"
$ git push heroku master 
```
