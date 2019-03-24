# PlaceQuest

This application was created for the Hack Mental Health 2019 Conference in San Francisco. PlaceQuest is a user-friendly, time-saving, collaborative, hospital discharge planning platform for social workers.

## Tech Stack
Backend: Python, Flask
Frontend: JavaScript, JQuery, HTML, CSS, Bootstrap
Tools: PostgrSQL
APIs: Goolge Maps API

## Set-Up
After cloning the repo, do the following in the top level directory:

```
virtualenv env
source env/bin/activate
pip3 install -r requirements.txt

cd src
createdb placequestdb
python3 seed.py
```

To start the app:
```
python3 server.py
```

To shut-down app:
```
[Ctrl+c]
dropdb placequestdb
```
