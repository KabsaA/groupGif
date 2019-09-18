from flask import Flask, render_template, request
import requests
import json


app = Flask(__name__)

@app.route('/')
def index():

#Extract the query term from url using request.args.get()
    query = request.args.get('search')

#Make 'params' dictionary containing:
    # a) the query term, 'q'
    # b) your API key, 'key'
    # c) how many GIFs to return, 'limit'
    params = {'q': query,
        'key': 'F9X97G66FSHO',
        'limit': '8'}

    r = requests.get("https://api.tenor.com/v1/search", params=params)
     # TODO: Use the '.json()' function to get the JSON of the returned response
    gifJson = r.json()
    gifDisplay = gifJson['results'] # Getting results attribute from the json object

    title =  'Search for Gifs!'
    return render_template("index.html",title = title,query = query,gifDisplay = gifDisplay)
    # Two lines above are showing the gifs and title and rendering the index file

if __name__ == '__main__':
    app.run(debug=True)
