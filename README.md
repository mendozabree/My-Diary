# My-Diary

[![Build Status](https://travis-ci.com/mendozabree/My-Diary.svg?branch=develop)](https://travis-ci.com/mendozabree/My-Diary)
[![Maintainability](https://api.codeclimate.com/v1/badges/b244783690700c7ae422/maintainability)](https://codeclimate.com/github/mendozabree/My-Diary/maintainability)
[![Coverage Status](https://coveralls.io/repos/github/mendozabree/My-Diary/badge.svg)](https://coveralls.io/github/mendozabree/My-Diary)

This is a web application where one can write down their thoughts , feelings. Day to Day activities, it's a personal diary.

## Getting Started
This is the software that you need to get started with.

### Prerequisites

* Python 3.6 to 3.7
* pip
* Flask 1.0.2

  
  [Here](https://www.python.org/getit/) is how to get python up and running
  
  [Here](https://pip.pypa.io/en/stable/installing/) is how to get pip up and running
  

## Setting Up for Development
These are instructions for setting up MyDiary app in a development enivornment.

* Make a directory on your computer and a virtual environment
  ```
  $ mkdir myDiary
  $ cd ~/myDiary
  ```

* Prepare the virtual environment
    ```
    $ py -m venv myDiaryvenv
    $ myDiaryvenv/Scripts/activate
    ```

* Clone the project repo
  ```
  $ git clone https://github.com/mendozabree/My-Diary.git
  ```
  

* Install necessary requirements
  ```
  $ pip install -r myDiary/requirements.txt
  ```

* Run development server
  ```
  $ python run.py
  ```
  
This site should now be running at http://localhost:5000 

These are the endpoints to test

| METHOD       | Endpoint           | Description  |
| ------------- |:-------------:| -----|
| GET      | /api/v1/entries | Get all entries
| GET      | /api/v1/entries/id      | Get specific entry using an id |
| POST | /api/v1/entries      | Create a new entry |
| PUT      | /api/v1/entries/id      | Modify a specific entry using an id |

## Running the tests with covergae
* Install nosetests and coverage
  ```
  $ pip install nose coverage
  ```

* Running the tests
  ```
  $ nosetests -v --with-coverage --cover-package=api
  ```

## Deployment sites
The user interfaces are hosted at https://mendozabree.github.io/My-Diary/UI/index.html

The api is hosted on heroku at https://mydiary-api-heroku.herokuapp.com/

