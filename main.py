from flask import Flask, render_template, request
import requests
from googletrans import Translator


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    news = None
    quotable = None
    if request.method == 'POST':
        city = request.form['city']
        weather = get_weather(city)
        news = get_news()
        quotable = get_quotable()
    return render_template("index.html", weather=weather, news=news, quotable=quotable)

def translate_text(text, dest_language='ru'):
    translator = Translator()
    translated_text = translator.translate(text, dest=dest_language)
    return translated_text.text
def get_quotable():
    # api_key = "bca1c0489a6a8bebf9a512c7411aa5c7"
    url = "https://api.quotable.io/random"
    response = requests.get(url)
    return response.json()

def get_weather(city):
    api_key = "bca1c0489a6a8bebf9a512c7411aa5c7"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()

def get_news():
    api_key = "38452c6909914325ab3e398367664f67"
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
    response = requests.get(url)
    return response.json().get('articles', [])

if __name__ == '__main__':
   app.run(debug=True)