from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def welcome():
	return render_template('homepage.html')

@app.route('/aboutme')

def aboutme():
	return "Welcome to About Me!"

@app.route('/resume')
def resume():
	return "Welcome to Resume!"


if __name__ =="__main__":

	app.run(debug=True)