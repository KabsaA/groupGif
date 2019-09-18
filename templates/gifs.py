apikey = "F9X97G66FSHO"
  lmt = 10

  r = requests.get("https://api.tenor.com/v1/trending?key=%s&limit=%s" % (apikey, lmt))

  if r.status_code == 200:
      trending_gifs = json.loads(r.content)
  else:
      trending_gifs = None

  print (trending_gifs)

  params = {
  "q": "query_term",
  "Key": "F9X97G66FSHO"
  #limit = 8
}
  # TODO: Extract the query term from url using request.args.get()
  r = requests.get('https://api.tenor.com/v1/search', params=params)

  # TODO: Use the '.json()' function to get the JSON of the returned response
  # object
  gifJson = r.json()

  # TODO: Using dictionary notation, get the 'results' field of the JSON,
  # which contains the GIFs as a list
  { "results": "link", "media": {
  "url": "url",
  "GIFs": ["media"] }
  #"tags": 8,
}
  gif_display = gifJson["url"]["Gifs"]
  return gif_display
