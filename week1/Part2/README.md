
# Week 2
## Today's Topics
- Using Postman to send requests
- Different kinds of HTTP methods
- Putting data in the body


### Postman
1) https://www.getpostman.com/. Download it and open it up. 
2) Run the `methods.py` flask app we have given, like we did last week.
3) Go to Postman. In the URL field, put in 127.0.0.1:5000/hello.
4) To the left of the URL, make sure it says "GET", otherwise click on the dropdown and select "GET". 
5) Press send. 
6) You should see a messaging saying "You have sent a GET request."
7) Now, change the "GET" to a "POST" and press send. You should see "You have sent a POST request."

This is the general idea of different kinds of HTTP methods. You can have one route, `/hello`, and have it do different things based on what kind of request you send it. See the next section for more details.


### Different kinds of HTTP methods
When you put a URL in the browser, your browser implicitly sends a GET request. This is what we did last week. When you typed in "127.0.0.1:5000/one" in your browser, it sent a GET request to that URL. A GET request is used when you're trying to retrieve, or "get", data from a server. There are several types of requests you can use using the HTTP protocol, and GET is simply one of them. Now, look at the file we have provided, `methods.py`.

Last wee, we wrote our code in `HelloWorld.py` like this:
```
@app.route("/")
def hello():
    return "Hello Flask"
```

But now, in `methods.py`, we have:
```
@app.route("/hello", methods=['GET', 'POST'])
def hello():
    return "Hello Flask"
```

This means we're listening for both GET requests and POST requests on our route `/hello`. Last week, we were only listening for GET requests, implicitly. 

Read this (https://www.tutorialspoint.com/http/http_methods.htm) description of some common HTTP methods(GET, POST, PUT, DELETE) and their use cases, and try to do your own research on how this works. As usual, ask us if you have any questions,but try to figure it out yourself first!

**Exercise:**
1) Write a new route that listens for POST requests only, call it `/add`. Have it take two numbers as user input(remember from last week!) and return the sum of the two numbers. 
2) Modify the `/add` route to also listen for GET requests. Have it return a random number when called. You'll have to look up how get random numbers in Python. 

Note - you should never separate this kind of functionality(exercise 2) based on the method that was used. This is only for your understanding and practice!


### Sending complex data
Up till now, we have sent only small pieces of data in the URL using our parameters, like `/tax&amount=12` or something like that. Many times, we want to send large amounts of complex data that would just clutter our URL. 

First, for those of you don't know about JSON, we need to go through that first. JSON is just a way of structuring data. Read this link(https://www.makeuseof.com/tag/json-laymans-overview/) and do more of your own research to get comfortable with JSON.

Now, consider a case where you have to send more than just a few things in your request. Let's say you're trying to create an app to store user information and you have to send the username, their address (which has 4 parts: street, town, state, and zip), their phone number, their hobbies (which could be a long list), and much more. You clearly can't send all of those in the URL. 

The way to do this is to use the **body** of the request. You can send a lot of complex data in the body of the request in a JSON format. 

Make sure `methods.py` is running again, and in Postman, type in 127.0.0.1:5000/complex as youre URL and change the method to POST. Now, navigate to the tab labelled "Body". This is where you put data in the body. Click on the "raw" radio button. Paste the following into there:
```
{
	"username": "sponegebob",
	"age": 19,
	"hobbies": ["swimming", "reading", "skiing"],
	"address": {
 		"street": "124 Conch Street",
        	"town": "Bikini Bottom",
        	"state": "NJ",
        	"zip": "08901"
    	}
}
```

Then, to the right next to "form-data x-www-form-urlencoded raw binary", click on the dropdown that right now says "Text" and click "JSON(application/json)". Click send. You should see some output. Yay! You just sent a POST request with some data.

Feel free to change this up, play around with the route, and experiment with things to see how it works. 

**Exercise:**
Write a route that listens to POST requests and takes the following parameters:
```
{
	"name": <user's name>,
	"waiter": <name of the waiter>,
	"tip": <percent tip that they want to give>,
	"total": <total amount on receipt>,
	"items": [ an array of items that were ordered ]
}
and it returns a string saying "<user's name> ordered <each>, <item>, <in>, <the>, <list> from <waiter> and is paying <total with tip included>. "
```
