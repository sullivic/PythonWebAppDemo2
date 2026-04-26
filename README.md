# Second WebAppDemo

- This showcases skills in python based web application.
- This second project demonstrates automatically driving db migration.
- It also demonstrates populating a vectordb and using that for search.
- Although these datasets are minimal, a commercial product can be derived by scaling up the data-points and query complexity.

# packages, dependencies, tools.

- ubuntu-linux (x86_64)
- PyCharm IDE (and IDEA WebStorm)
- python-3.x.y
- pip
- venv
- mariadb
- mysql-connector-python
- alembic
- sqlalchemy
- Flask
- HTML
- CSS
- Javascript
- Twitter-bootstrap
- npm
- ReactJS

- FastAPI serves both backend and frontend app (via static content)
very basic UI: text box input, button to do Ajax call, textarea to display json results (and unordered list)

- ReactJS is used.

- NOTE: the bootstrap page (menus) is not connected: we are focussing on the server-side functionality

## To run

- in this project install directory

- $ source ./.venv/bin/activate
- $ python3 ./WebAppDemoTwoFlaskApp.py

- browser home-page at the web-address http://localhost:5000/SecondPythonDemoApp.html

## Alembic commands from project installation directory

- alembic upgrade head
- alembic downgrade base
