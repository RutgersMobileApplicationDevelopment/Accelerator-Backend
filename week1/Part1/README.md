
# Hack Night 1: Intro To Flask

Welcome to RUMAD Hack Nights! Tonight we are going to build a simple web backend API giving a quick introduction to flask.

## What is Flask?
Flask Is a simple but powerful web microframework for **python**. Flask is easy to install so we can get our web api up and running in minutes. 

## Setting Up Flask

 - ## Mac
	 1. Install pip package manager so we can install the flask packages in your terminal run: ``` sudo easy_install pip ``` 
	 2. Install Flask using pip run:  ``` pip install Flask ```
	 3. You're all done Proceed to the "Hello Flask" section
- ## Debian Linux Distros
	1. Run in your terminal ``` sudo apt-get install python-pip ```
	2. Do steps 2 & 3 in the Mac section 
- ## Windows
	1. Install python 
	2. Do each step in the mac section from command prompt

## "Hello Flask"
Now that we have flask installed it is time to start making something awesome
If you have not already download the week 1 folder.

- To make sure your Flask install is working properly in your command line navigate inside the week1 folder and run the command: ``` FLASK_APP=HelloWorld.py flask run```
- Navigate to the given URL (http://127.0.0.1:5000/) in your browser, If you see Hello Flask you installed everything correctly
- If it does not work ask and someone will be able to help you
- In the next section we will take a deep dive into HelloWorld.py to help you understand how it works.

## Understanding HelloWorld.py

### What is a server? How does it work?
![Image of server](https://ruslanspivak.com/lsbaws-part1/LSBAWS_HTTP_request_response.png)

As the image shows, you send a request to a server to get a response from the server. The request is you pressing ENTER after typing in a URL, The server is located at that URL. The website you see is the response from the server. Now, we're making our own server with our own URL and our own responses. 

### What is Flask?
We encourage you to read more about Flask and its features(just google it!). But overall, Flask is just a framework. that lets us make a server ourselves. It'll be more clear in the next section.

### Our app
We will go line by line to give a general understanding of our hello flask application. 

- First we import Flask and instantiate the flask app.
```python
from flask import Flask
app = Flask(__name__)
```
- Then we tell the app that the following function will be responsible for returning the "/" route.
```python
@app.route("/")
```

What does this mean? It's just how github.com/RutgersMobileApplicationDevelopment shows you something different from github.com/mongo. The URL is *routed* differently based on what the text after the / looks like. So different URLs run different code and show different results. How does it do that? See below.

- Then we define the function that returns the body of the web request, this can return HTML or some other encoding to pass information to a user or another program. Essentially, for this particular route, we are running the following function.
```python
def hello():
	return "Hello Flask"
```

- Then we define another route.
```python
@app.route("/one")
def func():
	return 1
```
This is a new route. If you go to http://127.0.0.1:5000/one in your browser, you should now see 1. This is the basic way servers respond to different user needs: by defining multiple routes.

## Simple User Input
The simpilest way for your server to collect data from a user is a GET request. A get request is a method for passing data to the server by encoding the data into the URL by adding a followed by a parameter name like ```?bar=``` then the value we want to pass into the parameter: ```?bar=foo```. To test this out check out UserInput.py.

Like Before run ``` FLASK_APP=UserInput.py flask run``` and go to the Uppercase route and pass something into the "word" parameter like so ```/Uppercase?word=python``` and see how the server responds.

To add multiple parameters you should use "&" after a parameter and write a new parameter like:
```
/example?Foo=Hello&Bar=World
``` 
Where we pass both of the parameters Foo and Bar

## Understanding UserInput.py
Opening up UserInput.py you will find a very similar format to HelloWorld.py the parts of the code we are most concerned with are these 2 lines:
```python
from flask import request
...
word = request.args.get('word')
```
To handle get requests we must first import flask's request variable. Then in our route function we can access any get arguments through the ```request.args.get``` function like seen in the second line.

## What Next?
For the rest of the night or during the week you should create an api with 2 routes:
 1. /tax to calculate sales tax of a bill (use a fixed 7% sales tax)
 2. /tip to calculate calculate the tip for a bill where you can enter a tip percentage and a bill total
 
 hint: You need to figure out how to convert the string inputs from ```get()``` to a number.
