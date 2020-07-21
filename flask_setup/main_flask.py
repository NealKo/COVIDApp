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
	return render_template('about.html', title='About')

@app.route('/Services')
@app.route('/services')
def service():
	return render_template('services.html', title='Services')

@app.route('/Updates')
@app.route('/updates')
def updates():
	return render_template('updates.html', title='Updates')

@app.route('/Facts')
@app.route('/facts')
def facts():
	return render_template('facts.html', title='Facts')


@app.route('/Links')
@app.route('/links')
def links():
	return render_template('links.html', title="Links")

#Redirect for all routes not in the app.
#make_response simplifies the error message process.
@app.route('/<p_n>')
def other_page(p_n):
    	response = make_response('The page named %s does not exist.' \
                             % p_n, 404)
    	return response
