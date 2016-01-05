from flask import Flask,render_template,flash,request,url_for,redirect;

from app import app;

@app.route('/')
def home():

    return '''<html>
                    <head>
                    <title>homepage</title>
                    </head>
                    <body>
						<h1>u are on the home page</h1>
					</body>
              </html>''';

@app.route('/signin')
def signin():
	return render_template('signin.html');

@app.route('/showname')
def showname():
	return render_template('showlist.html');

@app.route('/showtime/<name>')    
def myshow(name):
    return '<h2>' + name + '</h2>';

@app.route('/homepage')
def homepage():
	try:
		return render_template('index.html');
	except exception as e:
		return (str(e));
	
@app.errorhandler(404)
def error_page(e):
    render_template("404.html");

@app.errorhandler(405)
def error_method(e):
    render_template("405.html");	

@app.route('/login/',methods=['GET','POST'])
def login():
	error='';
	try:
		if request.method=="POST":
			attempted_username=request.form['username']
			attempted_password=request.form['password']
			
				#flash(attempted_username)
		
			if attempted_username=="admin" and attempted_password=="password":
				return redirect(url_for('homepage'))
			else:
				error="Invalid login"
		return render_template('login.html',error=error)	
	except Exception as e:
		flash(e)
		return render_template('login.html',error=error)
	
@app.route('/signup/')
def signup():
	return render_template('signup.html')
	

    

