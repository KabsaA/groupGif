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
        'key': 'DT7VKCNIRM18',
        'limit': '8'}

    r = requests.get("https://api.tenor.com/v1/search", params=params)
    gifJson = r.json()
    title =  'Search for Gifs!'
    gifDisplay = gifJson['results']


    return render_template("index.html",title = title,query = query,gifDisplay = gifDisplay)

if __name__ == '__main__':
    app.run(debug=True)
