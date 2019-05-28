## Running the application

Just run these commands in the project directory to create the virtual environment folder

```
pip install virtualenv
virtualenv venv
```

Once you have the venv folder, run these commands to install the packages:

```
call venv\scripts\activate.bat
pip install -r requirements.txt
```

You're ready to go and run the app:

```
call venv\scripts\activate.bat
python manage.py runserver
```