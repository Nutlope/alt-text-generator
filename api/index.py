import os

import replicate
from flask import Flask, request

app = Flask(__name__)

os.environ.get("REPLICATE_API_TOKEN")

@app.route('/')
def home():
  # Get imageUrl query param
  args = request.args
  imageUrl = args.to_dict().get('imageUrl')

  # Run ML Model with imageUrl
  model = replicate.models.get("salesforce/blip")
  version = model.versions.get("2e1dddc8621f72155f24cf2e0adbde548458d3cab9f00c0139eea840d0ac4746")

  # Get the alt text result and return it
  output = version.predict(image=imageUrl)
  return output
