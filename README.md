# Simple data processing coding assignment for Python Software Engineer role

# The task

Create a REST micro-service that takes as input a string parameter containing natural language in any relevant language, and returns a list of matched phrases from a dictionary list independent of case and plurality and punctuation.

The test dictionary is co-located with this readme - it is called off_categories.tsv. The second column, called 'category' is the column to look for (it is the categories from Open Food Facts) . The category names may be plural or singular (OFF is a crowdsourced categorisation, so is not entirely consistent), but the matches should be found either way. Some categories are in non-English language, signified by an ISO language code and colon which needs to be removed for matches to be possible.

## Example input and output (logical):

Input: ```I like lemon juice and granulated sugar on my pancakes.```

Output: ```[ "Lemon juice", "Granulated sugars", "Pancakes" ]```

Note that this input should not match other phrases from the phrases list that have the word `juice` or `sugar` in them if the rest of those phrases are not matched with this input.

## Interface

The micro-service should listen on port 8080, and should accept the input as a querystring parameter called `text`

## Requirements

* Use appropriate production-capable frameworks
* Use appropriate dependency-management and build tools
* The project's structure and organization should follow best practices
* Don't reimplement the wheel, reuse
* Prefer immutable design if possible
* Performance matters. Consider your chosen algorithm, its throughput, scalability, memory-usage
* If the framework you use is single-threaded by default, you may want to provide a multi-threaded version also
* Test your code, and your API. No need to test every permutation, but demonstrate you know the types of things to test for.
* Even though this is a simplified requirement as appropriate to being an exercise, your code should be production capable
* Show your working, if you've used any interesting libraries or approaches during development let us know and explain why in the readme. 
