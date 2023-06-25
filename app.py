from flask import Flask, render_template
import recommend as rec

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/recommend')
def recommend():
    return render_template('recommend.html')

@app.route('/recommend/')
@app.route('/recommend/<input>')
def input(input=''):
    inputTratado = str(input.replace('_', ' '))
    recommendedBooks = rec.recomendar(inputTratado)
    return render_template('recommend.html', result = recommendedBooks, search = inputTratado)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

app.run(debug=True)