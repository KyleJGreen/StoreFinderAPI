# StoreFinderAPI
an API for searching inventory data to see what locations of a store carry the item

This API currently contains only one route, located in the app/api/items.py file, along with five classes in the app/models.py file. The route is a GET function that takes the id for an item and returns both the item information and information on store locations carrying the item. Future implementations will include the ability to search items given a name, once an algorithm has been implemented for matching items with similar names. Users with permissions will also be able to submit items via a POST function once permissions have been fully implemented and another algorithm has been written for adding new items to the database.

The database for this implementation is an sqlite file located at ~/data-dev.sqlite.

To run the code (in a Linux environment,) please follow these steps:

1  In a terminal, cd into the directory you want the repository in and clone the repo\s\s
$ git clone https://github.com/KyleJGreen/StoreFinderAPI.git

2-  cd into the cloned repository and activate the virtual environment
$ cd StoreFinderAPI/
$ . venv/bin/activate

3  set environment variable for app
(venv) $ export FLASK_APP=flask_app.py

4  run the application
(venv) $ flask run

5  open up a new terminal and cd into the directory of the repo, then activate the virtual environment again
$ . venv/bin/activate

6  call the API with item id's 0-7
(venv) $ http --json http://<your ip address>:5000/api/v1/items/<0-7>
