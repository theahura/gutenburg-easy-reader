"""Grabs a Project Gutenburg url from frontend, returns the html."""

from flask import Flask, jsonify, render_template, request
import validators

import IPython


# Flask.
app = Flask(__name__, template_folder='frontend/', static_folder='frontend/')


# Routes.
@app.route('/', methods=['GET'])
def index():
  return render_template('index.html')


@app.route('/get_url', methods=['POST'])
def get_url():
  print 'Got url.'
  print request.data
  print validators.url(request.data)
  return 'test'


def main():
  app.run(debug=True)

if __name__ == '__main__':
  main()
