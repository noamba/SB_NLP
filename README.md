# Category Match API exercise

## Table of contents
* [Introduction](#introduction)
* [Requirements](#requirements)
* [Installation and setup](#installation-and-setup)
* [Usage](#Usage)
* [Additional docker commands and testing](#additional-docker-commands-and-testing)
* [Possible next steps](#possible-next-steps)

## Introduction
This application follows the instructions in the provided 
`TASK_INSTRUCTIONS.png` image. It uses `Python`, 
`Spacy`, `Pandas`, `Flask`, `uSWGI`, `Nginx` and `Docker` to create a REST 
micro-service that takes as input a string parameter containing natural 
language in any language, and returns a list of matching categories 
independent of case, plurality and punctuation (see details and examples
in TASK_INSTRUCTIONS.png).

The phrase-matching object is created (or loaded from disk) at application
startup. This takes a while, but, it allows for the more important 
*snappy response* from the API 
endpoint when searching for categories in a phrase.

## Requirements
Recommended: 16 GB RAM (though 8 should probably be enough).

## Installation and setup

### Docker Installation
Make sure docker is installed on your machine,
to install see instructions here: https://docs.docker.com/get-docker/

### Run from the docker image on dockerhub

This is the simplest option to run the application: Only one command 
is required for the API be available. It could be a good idea if you 
have a fast internet connection as the pulled image weighs a few GB. If you 
choose this deployment, issue:

`docker run --name match_container -p 8080:80 noamba/matches:latest`   

#### Notes
- The interface will be ready when the message 
">>> Match application is ready <<<" is displayed 
in the container log (and output).  


### Build the docker image locally and run it
Alternatively, you can build the image locally. This will reduce the amount 
of data pulled from dockerhub. After building the image you will need to `run` 
it with the instructions below. 

To choose this method issue:

`docker build -t match_img .`  

#### Notes 
- Consider changing settings (see below) before building the image
- Don't forget the dot at the end of the `build` command :-)
- This step will take a few minutes (depending   
on network & machine speed?) - enough time to grab a cup of tea ;-) 


When completed, run a docker container from the created image, issue:

`docker run --name match_container -p 8080:80 match_img`


#### Notes
- If the setting `PERSIST_MATCH_OBJECTS` is set to `True` pickled objects will be 
saved within your container. This allows reuse of calculated phrase-matching 
objects when the docker container is restarted. 
- To save the pickled objects on your file system, you could mount a directory 
with the `--volume` option of `docker run` and set the file paths in 
`settings.py` accordingly.
- This step may take a few minutes as well (depending on machine speed). 
The interface will be ready when the message 
">>> Match application is ready <<<" is displayed 
in the container log (and output).
- If `PERSIST_MATCH_OBJECTS` is `True` this step will be faster in 
future uses.


### Settings

Settings can be found in `app/settings.py`. If you want to change them 
best to do so before building the image, or, with the local settings file 
mounted into the container. 

Notable settings are:

`PERSIST_MATCH_OBJECTS` - Save artifacts for future use. Defaults to `True`.

`DEBUG` - Sets level of debug messages sent to output. Defaults to `None`.


## API Usage

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

Issue: `docker exec -it match_container /bin/bash -c "pytest -v"`

#### To run tests in a dev environment
- Create a `python 3.6` virtual environment (you may need to install 
`virtualenv`)
- issue: `export FLASK_APP=main`
- Activate the virtual environment and cd to the `app` dir: `cd app`
- Issue: `pytest -v`

#### To run the app in a dev environment

Follow instructions in 
[To run tests in a dev environment](#to-run-tests-in-a-dev-environment). 
Then, activated in the `app` dir, issue: `python main.py`

**NOTE: The Flask server runs on port 5000**


## Possible next steps
- NLP nay be improved. For example: There are more than 40 
languages in the `off_categories.tsv` file. I used 
`Spacy`'s large English model to lemmatize all categories. It seems `Spacy` 
has models for about 15 languages (including a `Multi-language` model) - 
those could be used to lemmatize specific languages better. 
Other packages (e.g. `NLTK`) may be useful for this as well. 
- Add tests: For example, I did not test all units (functions).
- Persist data in a production level DB (perhaps Postgres/Redis/Mongo?) 
instead of a file.
- Add type annotation to allow static type checking with mypy. 
- Optimize speed and memory footprint of the initial match-phrase objects 
creation.
- Deploy to AWS.
- For a more complicated application and/or additional dev and deployment 
requirements I would consider `poetry` and/or `conda` to manage packages.

