# mailgun-send-email
A demonstration of sending email using MailGun (https://www.mailgun.com/) and Python programming language.

## How do I run the program ?
* Ensure that you have created MailGun account and setup it properly.
* Ensure that you have installed Python 2.7 & Git in your local machine.
* Install `requests` python library: `sudo pip install -U requests`
* Clone this repository into your machine, by running this command: `git clone https://github.com/WendySanarwanto/mailgun-send-email.git`
* Go to cloned source code's directory using `cd` command.
* Open the `mailgun-demo.py`, fill in the blank strings marked with `TODO` comments then save the changes. 
* Run this command to run the program: `python mailgun-demo.py`

## How do I run the unit test ?
* Install `pytest` library: `sudo pip install -U pytest`
* Install `pytest-mock` library: `sudo pip install -U pytest-mock`
* Run this command to run the unit test: `pytest`

## How do I get code coverage report after I run the unit test ?
* Install `pytest-cov` library: `sudo pip install -U pytest-cov`
* Run this command to run the unit test and also getting code coverage report: `pytest --cov-report term --cov-report html:cov_html  --cov=EmailClients EmailClients/`.
* The HTML coverage report document can be found in `cov_html` directory.