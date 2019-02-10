# QGIS Lightweight Plugin Server

This is intended to be a lightweight plugin server for QGIS that can be easily
deployed to get a private QGIS plugin server in your own system.

## Quick Start

```bash
cp sample.env .env

pip install -r requirements/dev-requirements.txt

flask db upgrade

flask run
```

In QGIS open the Manage Plugins menu item. Select settings, then add a new
server: http://localhost:5000/plugins/plugins.xml

In your browser open http://localhost:5000 to check out the web interface.

## Application settings

There are several configuration options that should be a consideration when
deploying the application:

### Mail server settings

There are several stages at which the application expects to be sending email
when in production. If the mail server is unavailable the mail sending will
silently fail. If it is configured in the .env file (see `sample.env`) then
emails will be sent at the following stages:

1. When a user uploads a plugin all admins will be sent an email with the
   description of the plugin, link to the plugin page, etc.
2. When an admin approves the plugin for usage the author will be sent an email.
3. Emails will be sent as per Flask Security's standards

### Upload settings

There are two options where you can upload the plugin zipfiles:
 
1. They can either be uploaded to a local directory on the machine using
   Flask-Upload
2. They can be uploaded to an S3 bucket using the boto3 library

### Authentication requirements

- TODO: Enabling (or not) authentication requirements for plugins.xml

## Testing

- TODO: Running unit tests

## Production deployment

- TODO: Zappa
- TODO: WSGI application
