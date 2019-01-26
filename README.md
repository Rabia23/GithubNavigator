# GithubNavigator

Prerequisite:
Make sure you have Python installed in your system :)

Getting Started

Step 1: Install, Create and Activate Virtual Environment

- Install virtual env using command:
    pip install virtualenv
Note: If you already have virtual env in your system then skip this step.
- Go to project folder e.g cd Desktop/task-github
- Create the virtual env by following command:
    virtualenv githubnavigator_venv<name of the environment>
- Activate the virtual env:
    source githubnavigator_venv/bin/activate


Step 2: Install Project Dependencies

- cd githubnavigator and run the following command:
    pip install -r requirements.txt
Note: You can see your installed dependencies by running command: pip freeze


Step 3: Start the Application

./manage.py runserver
open a browser and do GET request to e.g. http://localhost:8000/navigator?search_term=arrow

