# my_game

A small repo for testing some stuff,
here i will note some commands i used.

some usefull info : https://py-vscode.readthedocs.io/en/latest/index.html

# Python env :
* $ python -V  -> Python 3.7.0
* pip install virtualenv
* Activate the venv : source mypython/bin/activate (with git bash)
* Just enter : 'deactivate' to deactivate the venv

# pip list, pip 19.2.3
* pip install virtualenv
* pip install pytest

# dev env :
* python -m pip install pylint
* python -m pip install black

# Vscode and python
Okay, this is the first time for me, using python with vscode i mean.
I want to use venv, with that i can use specific modules / package / extension from python
and don't corrupt all my python env on my desktop.

+ ## The virtual env

venv is a python package, you can install it with pip :
```
pip install virtualenv
```

Next you can create the virtual env :
```
virtualenv myvenv
```

On windows, to activate/deactivate the env :
```
myvenv\Scripts\activate
myvenv\Scripts\deactivate
```
On unix system, to activate/deactivate the env :
```
source myvenv/bin/activate
deactivate
```
+ ## Vscode
Choose the right python interpreter in vscode
```
CTRL + SHIFT + P
```
then type 
```
python: Select Interpreter
````
And choose the one in your venv

And for finish :
```json
    "python.formatting.provider": "black",
    "editor.formatOnSave": true,
    "python.linting.pylintArgs": [
        "--extension-pkg-whitelist=pygame"
    ],
```

you can also add a .env file in your folder.
it can add some specific things in there, like adding to pythonpath some folder !
```
PYTHONPATH=./little_rpg:${PYTHONPATH}
```