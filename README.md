# GithubNavigator

## Prerequisite:
Make sure you have Python installed in your system :)

## Getting Started

**Step 1:** Install, Create and Activate Virtual Environment

- Install virtual env using command:
```
pip install virtualenv
```
Note: If you already have virtual env in your system then skip this step.
- Clone the project using command:
```
git clone https://github.com/Rabia23/GithubNavigator.git
```
- Go to project folder e.g cd GithubNavigator
- Create the virtual env by following command:
```
virtualenv <name of the environment> e.g virtualenv githubnavigator_venv
```
- Activate the virtual env:
```
source githubnavigator_venv/bin/activate
```

**Step 2:** Install Project Dependencies

- Install requirements:
```
pip install -r requirements.txt
```
Note: You can see your installed dependencies by running command: ```pip freeze```


**Step 3:** Start the Application

```
./manage.py runserver
```
open a browser and do GET request to e.g. http://localhost:8000/navigator?search_term=arrow

