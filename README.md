
# Social Network
Social-Network is a simple social networking application with features like posting photos, adding likes and comments (much like facebook).\
It's currently titled 'Instabook' (yes, that's combination of Instagram and Facebook, as I couldn't come up with some creative title), though open to suggestions!

# Technology Stack

* Bootstrap: HTML, CSS and JS Library for styling web pages
* JavaScript: Adding interactivity to web pages
* Python: Primary Programming Language
* Django: Backend Framework

# Requirements
* Python --version >= 3
* Pip3

# Installation
### Steps ###
* Clone the forked repository in your local system.\
```git clone https://github.com/<username>/Social-Network```\
```cd Social-Network```\
Make sure you are inside Social-Network directory before proceeding with following steps.

* Create a virtual environment and start it by running\
```python3 -m venv myvenv```\
```source myvenv/bin/activate```

* Run ``` pip3 install -r requirements.txt``` to install the project dependencies.

* Setup database by running commands\
```python manage.py makemigrations```\
```python manage.py migrate```

* Start the web server by running ```python manage.py runserver```\
Now, open your web browser and enter ```http://127.0.0.1:8000/``` to see the website up and running.


# References
**Resources to learn Django**:\
[https://docs.djangoproject.com/en/3.0/](https://docs.djangoproject.com/en/3.0/)\
[https://tutorial.djangogirls.org/en](https://tutorial.djangogirls.org/en)

**Bootstrap Documentation:**\
[https://getbootstrap.com/docs/4.4/getting-started/introduction/](https://getbootstrap.com/docs/4.4/getting-started/introduction/)\

**Django Crispy Forms**\
[https://django-crispy-forms.readthedocs.io/en/latest/install.html](https://django-crispy-forms.readthedocs.io/en/latest/install.html)\

**Python Imaging Library-Pillow**\
[https://pypi.org/project/Pillow/2.2.2/](https://pypi.org/project/Pillow/2.2.2/)\

Other useful links:\
[https://github.com/revsys/django-friendship](https://github.com/revsys/django-friendship)\
