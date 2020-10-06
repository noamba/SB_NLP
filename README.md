# OFF (Open Food Facts) Category Match API exercise

## Table of contents
* [Introduction](#introduction)
* [Requirements](#requirements)
* [Installation and setup](#installation-and-setup)
* [Usage](#Usage)
* [Additional docker commands and testing](#additional-docker-commands-and-testing)
* [Possible next steps](#possible-next-steps)

## Introduction
This application follows the instructions in `TASK_INSTRUCTIONS.md`. 

It uses `Spacy`, `pandas`, `flask`, `uswgi`, `nginx` and `docker` to create a REST 
micro-service that takes as input a string parameter containing natural 
language in any relevant language, and returns a list of matched categories 
from Open Food Facts (see `app/data/off_categories.tsv`) 
independent of case, plurality and punctuation.

The phrase-matching object is created (or loaded from disk) at application
startup. This takes a while, but, it allows for the more important 
*quick responses* from the API 
endpoint when searching for matching categories in a phrase.

## Requirements
Recommended: 16 GB RAM (though 8 should probably be enough).

## Installation and setup

### Docker
Make sure docker is installed on your machine,
to install see instructions here: https://docs.docker.com/get-docker/

### Files
copy `match.tar.gz` file into `somedir` and then:

`cd somedir`

`tar xvf match.tar.gz`

`rm match.tar.gz`  # this is recommended to minimize the context given to docker

### Settings

Settings can be found in `settings.py`. You don't need to change anything.
Notable settings are:

`PERSIST_MATCH_OBJECTS` - Save artifacts for future use. Defaults to `True`.

`DEBUG` - Sets level of debug messages sent to output. Defaults to `None`.


### Build the docker image

`docker build -t match_img .`  

#### Notes 
- Don't forget the dot at the end :-)
- This step will take a few minutes (possibly 5 to 10 minutes depending   
on network & machine speed?) - enough time to grab a cup of tea ;-) 

## Usage

### Run a docker container from the created image 
`docker run --name match_container -p 8080:80 match_img`

#### Notes
- This was tried with Linux and should be fine on Mac. 
For Windows, you may need to use `%cd%` instead of `$PWD`
- If the setting `PERSIST_MATCH_OBJECTS` is set to `True` pickled objects will be 
saved within your container. This allows reuse of calculated phrase-matching 
objects when the docker container is restarted.
- This step may take a few minutes (depending on machine speed). The interface 
will be ready when the message ">>> Match application is ready <<<" is displayed 
in the container log (and output).
- If `PERSIST_MATCH_OBJECTS` is `True` this step will be faster in 
future uses.

### Using the interface
Once the container is up and running `localhost` should 
accept requests like the examples below.  

### Examples
Try the following in your browser:

`http://127.0.0.1:8080/?text=I+love+concentrated+apricot+juice.+I+can+also+drink+blueberry-juices+or+concentrated+Blueberry+juices`

`http://127.0.0.1:8080/?text=Who+ordered+Vergeoises?`


## Additional docker commands and testing

### Stop/restart the docker container

`docker stop match_container`

`docker start match_container`

### View the log of a started container

`docker logs match_container`

### Tests
Currently example tests are in:
- `app/tests/functional` 
- `app/nlp/tests/integration` 
- `app/nlp/tests/unit`

#### To run all tests in the docker container
- Connect to the running container with
`docker exec -it match_container /bin/bash`
- Issue: `pytest -v`

#### To run tests in a dev environment
- Create a `python 3.6` virtual environment (you may need to install 
`virtualenv`)
- issue: `export FLASK_APP=main`
- Activate the virtual environment and cd to `app` dir: `cd app`
- issue: `pytest -v`

#### To run the app in a dev environment

Follow instructions in 
[To run tests in a dev environment](#to-run-tests-in-a-dev-environment). 
Then, activated in the `app` dir, issue: `python main.py`

**NOTE: The Flask server runs on port 5000**


## Possible next steps
1. NLP nay be improved. For example: There are more than 40 
languages in the `off_categories.tsv` file. I used 
`Spacy`'s large English model to lemmatize all categories. It seems `Spacy` 
has models for about 15 languages (including a `Multi-language` model) - 
those could be used to lemmatize specific languages better. 
Other packages (e.g. `NLTK`) may be useful for this as well. 
2. Add tests: For example, I did not test all units (functions).
3. Persist data in a production level DB (perhaps Postgres/Redis/Mongo?) 
instead of a file.
4. Add type annotation to allow static type checking with mypy. 
5. For a more complicated application and/or additional dev and deployment 
requirements I would consider `poetry` and/or `conda` to manage packages.

