# Open Food Facts Category Match API exercise

## Table of contents
* [Introduction](#introduction)
* [Setup](#setup)
* [Settings](#settings)
[link text](#abcde)



## <a name="abcde">Introduction</a>
This application follows the instructions in `TASK_INSTRUCTIONS.md`. 

It uses `Spacy`, `pandas`, `flask`, `uswgi` and `nginx` to create a REST 
micro-service that takes as input a string parameter containing natural 
language in any relevant language, and returns a list of matched categories 
from Open Food Facts (see `app/data/off_categories.tsv`) 
independent of case and plurality and punctuation.

# Setup

## Docker
Make sure docker is installed on your machine,
see instructions here: https://docs.docker.com/get-docker/

## Installation
copy `match.tar.gz` file into `somedir` and extract it:

`cd somedir`

`tar xvf match.tar.gz`

## Settings

Settings can be found in `settings.py`. Notable are:

`PERSIST_MATCH_OBJECTS` - Save artifacts for future use. Defaults to `True`.

`DEBUG` - Sets level of output debug messages (e.g. timings). 
Defaults to `None`.


## Build the docker image

`docker build -t match_img .`  

**Notes:** 
- Don't forget the dot at the end :-)
- This step will take a few minutes (possibly 5 to 10 minutes depending   
on network & machine speed?) - enough time to grab a cup of tea ;-) 

## Run a docker container from the created image 
`docker run -v $PWD/app/data:/app/data --name match_container -p 8080:80 match_img`

**Notes:**
- This was tried with Linux and should be fine on mac. 
For Windows, you may need to use `%cd%` instead of `$PWD`
- Your local `app/data` directory will be mounted into the container. 
If the setting `PERSIST_MATCH_OBJECTS` is set to `True` and the relevant 
`*_PICKLE_FILE` path settings prefix is `data/`, the pickled objects will be 
saved *on your local drive* (not within the container). This allows 
reuse of calculated phrase-matching objects even if the docker image and/or 
container are removed.
- This step may take a few minutes (possibly 2, depending   
on machine speed?) when initially run as phrase-match objects need to be 
created. If `PERSIST_MATCH_OBJECTS` is `True` this step will be faster in 
future uses. 

## Usage
Once the container is up and running `localhost` should 
accept requests like the examples below.  

### Examples
Try the following in your browser:

`http://127.0.0.1:8080/?text=I+love+concentrated+apricot+juice.+I+can+also+drink+blueberry-juices+or+concentrated+Blueberry+juices`

`http://127.0.0.1:8080/?text=Who+ordered+Vergeoises?`

## Stop/start the docker container

`docker stop match_container`

`docker start match_container`

## View the log of a started container

`docker logs match_container`


## Test
Currently example tests are in:
- `app/tests/functional` 
- `app/nlp/tests/integration` 
- `app/nlp/tests/unit`

###To run all tests in the docker container

- Connect to the running container with
`docker exec -it mycontainer /bin/bash`
- Issue 
`pytest -v`

###To run all tests not within the docker container

- Create a `python 3.6` virtual environment (you may need to install 
`virtualenv`)
- Activate the virtual environment and issue:
`pytest -v`


## Possible next steps:
1. There are more than 40 languages in `app/data/off_categories.tsv`. I used 
`Spacy`'s english large pretrained statistical model to lemmatize 
english categories. It seems `Spacy` has models for about 15 languages 
(including a `Multi-language`model) and it could be used to lemmatize
 additional languages. Other packages (e.g. `NLTK` may be useful as well). 
2. The application currently tries to match both cleaned match-phrases and 
lemmatized (English) phrases. For english the lemmatized may be enough, 
depending on the quality of the lemmatization. The additional data does not 
seem to create a substantial overhead on querys. Looking further into this may 
lead to removing the English cleaned sentences?
3. Documentation (e.g. docstrings) and testing are not complete. 
4. For a more complicated application, additional dev and deployment 
requirements I would consider `poetry` and/or `conda` to manage packages.


To have paths recognised when running tests from sb_nlp (?) issued:
export PYTHONPATH="${PYTHONPATH}:/path/to/sb_nlp"


* Optimize lemmatization
* Save phrasematcher to disk. Pickle?

* I'm aware of a discrepancy:
    Input: I like lemon juice and granulated sugar on my pancakes.

    Output: [ "Lemon juice", "Granulated sugars", "Pancakes" ]

    Note that this input should not match other phrases from the phrases list
    that have the word juice or sugar in them if the rest of those
    phrases are not matched with this input.


FLASK

NOTE: the flask server is not for production, leave it on port 5000 for now.
        When insatlling a production server switch to port 8080

To run flask dev server, issue:
    export FLASK_APP=app.main
    source venv/bin/avtivate
    flask run

Example URLs:
DEV SERVER on port 5000 -
http://127.0.0.1:5000/?text=I+love+concentrated+apricot+juice.+I+can+also+drink+blueberry-juices+or+concentrated+Blueberry+juices
http://127.0.0.1:5000/?text=I+love+concentrated+apricot+juice

production port 8080 -
http://127.0.0.1:8080/?text=I+love+concentrated+apricot+juice.+I+can+also+drink+blueberry-juices+or+concentrated+Blueberry+juices

http://127.0.0.1:8080/?text=I+love+concentrated+apricot+juice
