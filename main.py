from flask import Flask, request, redirect
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader
(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/validate-info")
def index():
    template = jinja_env.get_template('form.html')
    return template.render()

@app.route('/validate-info', methods=['POST'])
def validate_info():
    username = request.form['user']
    password = request.form['pass']
    vpassword = request.form['passv']
    email = request.form['email']
    user_error = ''
    pass_error = ''
    vpass_error = ''
    email_error = ''

    if username == '':
        user_error = 'Please enter a username.'
        
    if len(username) < 3 or len(username) > 20 or ' ' in username:
            user_error = 'Username invalid'
    
    if password == '':
        pass_error = 'Please enter a password.'

    if len(password) < 3 or len(password) > 20 or ' ' in password:
            pass_error = 'Password invalid.'

    if vpassword == '':
        vpass_error = 'Please verify the password.'

    if vpassword != password:
        vpass_error = "Passwords do not match."

    if len(email) >= 1 and len(email) < 3 or len(email) > 20 or ' ' in email or '@' not in email:
        email_error = "Enter valid email please."
    
    if not user_error and not pass_error and not vpass_error and not email_error:
      
        return redirect('/welcome')
    else:
        template = jinja_env.get_template('form.html')
        return template.render(user_error=user_error,
            pass_error=pass_error, vpass_error=vpass_error, 
            email_error=email_error, user=username,
            email=email)



@app.route('/welcome')
def valid_signin():
    name = request.args.get('user')
    
    return '<h1>Welcome {0}!!!</h1>'.format(name)
app.run()