Todo:
    have only lemma on english? currently keeping both cleaned match phrase and lemmatized
    Lemmatized only english, could do other languages with spacy, nltk or other nlp packeges that have the language?
    documentation
    docker
    poetry/conda?


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

NOTE: the flask server is not for production, leave it on port 500 for now.
        When insatlling a production server switch to port 8080

To run flask dev server, issue:
    export FLASK_APP=web.py
    source venv/bin/avtivate
    flask run

Example URLs:
http://127.0.0.1:5000/?text=I+love+concentrated+apricot+juice.+I+can+also+drink+blueberry-juices+or+concentrated+Blueberry+juices

http://127.0.0.1:5000/?text=I+love+concentrated+apricot+juice
