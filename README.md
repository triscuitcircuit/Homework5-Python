# Homework5-Python
Moonwake github workflow practice

[![Python application status badge](https://github.com/triscuitcircuit/Homework5-Python/actions/workflows/python-app.yml/badge.svg)](https://github.com/triscuitcircuit/Homework5-Python/actions/workflows/python-app.yml)

[![Publish package to Test PyPI](https://github.com/triscuitcircuit/Homework5-Python/actions/workflows/publish-app.yml/badge.svg)](https://github.com/triscuitcircuit/Homework5-Python/actions/workflows/publish-app.yml)

## Description
This repository is used to practice CI/CD workflows by using GitHub actions to lint, style check, and test code before commiting to the repository. The project implements GitHub actions to lint and style check commits with Flake8 and Black, and test commits using Pytest. The status of the testing can be seen on the badge at the top of this page.

## DevOps workflow
An image demonstrating the DevOps workflow we implemented can be seen below.

![Devops image](https://github.com/triscuitcircuit/Homework5-Python/blob/8ee4eea64f3ba6083126ef1916aa11772d7e971a/DEVOPS%20Workflow.png)

The pre-commit file checks style, credentials, large files, and lints before commited to the repository. Testing is then run using GitHub actions and PyTest. Upon completion, post-commit hooks run on GitHub actions and the package is published to Test PyPI.

The file Work flow Events in the repository shows the events and
runners that are used. The image J1 shows the Jobs for all of the
events.