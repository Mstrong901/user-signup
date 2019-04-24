from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

username = []
password = []
password2 = []
email = []

@app.route("/register", methods=['POST', 'GET'])
def submit_form():
    have_error = False
    username = cgi.escape(request.form['username'])
    password = cgi.escape(request.form['password'])
    password2 = cgi.escape(request.form['password2'])
    email = cgi.escape(request.form['email'])

    parameters = dict(username=username, email=email)

    if " " in username:
        parameters['username_error'] = "Username Error"
        have_error = True

    if (len(username) < 3) or (len(username) > 20):
        parameters['username_error'] = "Username Error"
        have_error = True

    if " " in password:
        parameters['password_error'] = "Password Error"
        have_error = True
    
    if (len(password) < 3) or (len(password) > 20):
        parameters['password_error'] = "Password Error"
        have_error = True

    if password != password2:
        parameters['passwordverify_error'] = "Passwords must match"
        have_error = True
 

    if email.find('@') > 1:
        parameters['email_error'] = "Invalid Email"
        have_error = True

    if email.find('.') == -1 and len(email) > 0:
        parameters['email_error2'] = "Invalid Email."
        have_error = True

    if have_error:
        return render_template ('edit.html', title= "Signup", **parameters)
    else:
        return render_template('add-confirmation.html', username=username)

@app.route("/")
def index():

    encoded_error = request.args.get("error")
    return render_template('edit.html', error=encoded_error and cgi.escape(encoded_error, quote=True))

app.run()
