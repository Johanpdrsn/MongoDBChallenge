# MongoDBChallenge

A simple command line app the flattens a JSON object. The app expects input via ``stdin`` and takes no other arguments, and assumes that the input contains no arrays.

To run the app via the command line use ``cat test.json | ./app.py`` (execution rights needed, else ```python app.py```) to pass the content of ``test.json``to the app.


To run the test suite execute ```./test.py``` (again with the execution rights). The small test suite contains only unit tests.
