from flask import Flask, render_template, url_for
from flask import make_response
app = Flask(__name__)

@app.route('/')
@app.route('/Home')
@app.route('/home')
def home():
	return render_template('home.html')

@app.route('/About')
@app.route('/about')
def about():
	return "<h1>An informational page about COVID-19</h1>"

@app.route('/Services')
@app.route('/services')
def service():
	return "<h1> Provided Services </h1>"

@app.route('/Updates')
@app.route('/updates')
def updates():
	return "<h1> Updates information </h1>"

@app.route('/Facts')
@app.route('/facts')
def facts():
	return "<h1> Facts about Covid-19 </h1>"


@app.route('/Links')
@app.route('/links')
def links():
	return "<h1> A set of links</h1>"

#Redirect for all routes not in the app.
#make_response simplifies the error message process.
@app.route('/<p_n>')
def other_page(p_n):
    	response = make_response('The page named %s does not exist.' \
                             % p_n, 404)
    	return response
