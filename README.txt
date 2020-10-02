Todo:

* Optimize lemmatization
* Save phrasematcher to disk. Pickle?

* I'm aware of a discrepancy:
    Input: I like lemon juice and granulated sugar on my pancakes.

    Output: [ "Lemon juice", "Granulated sugars", "Pancakes" ]

    Note that this input should not match other phrases from the phrases list
    that have the word juice or sugar in them if the rest of those
    phrases are not matched with this input.