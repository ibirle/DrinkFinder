Try it Out: BeerMaid.me
Intro:
This project is a website designed to help find alcoholic beverages. I worked on this project as part of Hack Umass, a weekend hackathon. I worked with two other people and my job was background api handling and web hosting while others worked on the html and css. 

Skills Exhibited:
-Python
-Flask
-Linux Systems
-API Handeling

How It Works:
The website is controlled using the flask module for Python. Flask handles the incoming calls and routes each to an html file. When a drink needs to be found python sends api request to the various databases and then parses the json files received. A drink is chosen given he criteria and it is presented to the user. The Phython file is hosted on a remote server through Digital Ocean. The server uses a combination of nginx and gunicorn to properly manage the Flask app.