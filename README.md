#COMP3278-Project - group 33
COMMANDS:

Convert ui to .py:
pyuic5 -o homepage.py homepage.ui
pyuic5 -o login.py login.ui

resource browser:
pyrcc5 resource.qrc -o resource_rc.py


import database: source facerecognition.sql

changing data in database for testing: manually change in facerecognition.sql


