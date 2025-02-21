from flask import Flask, render_template, request
import requests
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)  

API_KEY = "d6189249502c4d9eb5e1bad9d3408116"
BASE_URL = "https://newsapi.org/v2/everything"

def get_news(query):
  
    """
    Fetch news articles based on the query.

    :param query: Search keyword for news
    :return: List of articles
    """
    params = {
        "q": f"{query} India",
        "sortBy": "publishedAt",
        "language": "en",
        "apiKey": API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code != 200:
        return []
    # print(f"Fetching news for {query}: {response.status_code}")  # Debug print
    # print(response.json())  # Print full response
    return response.json().get("articles", [])

@app.route("/")
def home():
    """
    Home route to fetch general news.

    ---
    parameters:
      - name: q
        in: query
        type: string
        required: false
        default: "tesla"
        description: Search keyword for fetching news articles
    responses:
      200:
        description: A list of news articles
        schema:
          type: array
          items:
            properties:
              title:
                type: string
                description: Title of the news article
              description:
                type: string
                description: Short description of the news article
              url:
                type: string
                description: URL to the full article
              urlToImage:
                type: string
                description: URL of the news image
    """
    query = request.args.get("q", "tesla")
    articles = get_news(query)
    if not articles:  # Check if articles list is empty
        message = "No articles found. Try a different search query."
    else:
        message = None
    return render_template("index.html", articles=articles, active_page="home", message=message, query=query)

@app.route("/search", methods=["GET"])
def search():
    query = request.args.get("q")
    if query:
        articles = get_news(query)
        if articles:
            return render_template("index.html", articles=articles)
        else:
            return render_template("index.html", articles=None)
    return render_template("index.html", articles=None)
  
@app.route("/business")
def business():
    """
    Fetch business news.

    ---
    responses:
      200:
        description: A list of business-related news articles
    """
    articles = get_news("business")
    return render_template("index.html", articles=articles, active_page="business")

@app.route("/technology")
def technology():
    """
    Fetch technology news.

    ---
    responses:
      200:
        description: A list of technology-related news articles
    """
    articles = get_news("technology")
    return render_template("index.html", articles=articles, active_page="technology")

@app.route("/sports")
def sports():
    """
    Fetch sports news.

    ---
    responses:
      200:
        description: A list of sports-related news articles
    """
    articles = get_news("sports")
    return render_template("index.html", articles=articles, active_page="sports")

@app.route("/politics")
def politics():
    """
    Fetch politics news.

    ---
    responses:
      200:
        description: A list of politics-related news articles
    """
    articles = get_news("politics")
    return render_template("index.html", articles=articles, active_page="politics")

@app.route("/entertainment")
def entertainment():
    """
    Fetch entertainment news.

    ---
    responses:
      200:
        description: A list of entertainment-related news articles
    """
    articles = get_news("entertainment")
    return render_template("index.html", articles=articles, active_page="entertainment")

@app.route("/world")
def world():
    """
    Fetch world news.

    ---
    responses:
      200:
        description: A list of world-related news articles
    """
    articles = get_news("world")
    return render_template("index.html", articles=articles, active_page="world")

if __name__ == "__main__":
    app.run(debug=True)
