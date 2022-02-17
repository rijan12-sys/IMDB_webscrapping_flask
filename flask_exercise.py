from flask import Flask, render_template, redirect, request
from pip._vendor import requests
from bs4 import BeautifulSoup



app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('flip.html' )
@app.route('/display', methods = ['POST']) 
def display():
    count = request.form['moviesNum']
    html_text = requests.get("https://www.imdb.com/search/title/?title_type=feature&sort=num_votes,desc&count=" + count).content
    soup = BeautifulSoup(html_text, 'html.parser')
    list = soup.find_all('div', class_="lister-item mode-advanced")
    for movies in list:
        movie_name = ("Name: " + movies.h3.a.text)
        ratings = ("Ratings: " + movies.strong.text)
        genre =("Genre: " + (movies.find("span", class_="genre").text))
    return render_template('test.html', movies = list) 


if __name__=='__main__':
    app.run(debug=True)