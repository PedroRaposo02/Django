# Django Tutorial

This README provides instructions on how to install this Django tutorial project, set up the required dependencies using `requirements.txt`, and provides an overview of the project structure.

## Installation

1. Clone the repository to your local machine.
2. Navigate to the project directory: `tutorial/`.
3. Create a virtual environment: `python -m venv env`.
4. Activate the virtual environment:
  - On Windows: `.\env\Scripts\activate`
  - On macOS/Linux: `source env/bin/activate`
5. Install the project dependencies: `pip install -r requirements.txt`.
6. Run the project with docker: `docker-compose up`.

- `polls` app: This app is a part of the tutorial project and serves as an example for building a simple polling application.
- `manage.py`: This file is used to interact with various Django commands.
- `tutorial` directory: This directory contains the project settings and configuration files.

To run the project, follow these steps:

1. Open a terminal or command prompt.
2. Navigate to the project directory: `tutorial/`.
3. Activate the virtual environment:
  - On Windows: `.\env\Scripts\activate`
  - On macOS/Linux: `source env/bin/activate`
4. Run the Django development server: `python manage.py runserver`.
5. Open your web browser and visit `http://localhost:8000/` to access the project.

To run the project with docker, follow these steps:

1. Open a terminal or command prompt.
2. Run the following command:
  docker compose up --build -d --force-recreate
3. Open your web browser and visit `http://localhost:8000/` to access the project.
4. To restart the container from 0 before the previous command run this command:
  docker compose down -v