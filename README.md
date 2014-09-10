base-django
===========

Simple django app to learn nginx/gunicorn/postgresql configuration

The app uses:

* Python 2.7 
* Django 1.7
* psycopg2 2.5.4 (postgresql connector) [Windows download page](http://www.stickpeople.com/projects/python/win-psycopg/ "psycopg2-windows")

If you are on Windows, make sure you download the compiled packages for your architecture as well as verifying the Python version it is for.

Example:

* psycopg2 v2.5.4, you have 64bit Windows and we are using Python 2.7... make sure to download the file named: psycopg2-2.5.4.win-amd64-py2.7-pg9.3.5-release.exe

could run SQLite for local development but the production server runs PostgreSQL 9.3.  There is no south based migration in this app.

To use local_settings.py create this in the same directory as settings.py and put your local settings in it.  You will need to add the following to the bottom of settings.py

    try:
        from local_settings import *
    except ImportError:
        pass


This project already has this setup and the gitignore file is making sure these local settings stay on your machine as it will most likely have the secret keys etc.

Using newtestapp.service in conjunction with systemd:

    systemctl enable newtestapp.service
    systemctl start newtestapp.service

Check status with:

    systemctl status newtestapp.service


