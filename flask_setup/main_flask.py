from flask import Flask, render_template
from flask import make_response
import pandas as pd

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

# This is for only testing display of tables
@app.route('/table')
@app.route('/Table')
def displayTables():
	df = pd.DataFrame({'State': ['California', 'Florida', 'Texas'],
					   'Total cases': [375363, 333201, 317730]  ,
					   'Total Deaths': [7595, 4895, 3865]})
	return render_template('table.html',  tables=[df.to_html(classes='data', header="true")])

@app.route('/ctable')
def displayCTable():
	pass
	#df = DataFetcher.get_countries()
	#df.to_html(header="true", table_id="table")

#Redirect for all routes not in the app.
#make_response simplifies the error message process.
@app.route('/<p_n>')
def other_page(p_n):
    	response = make_response('The page named %s does not exist.' \
                             % p_n, 404)
    	return response
