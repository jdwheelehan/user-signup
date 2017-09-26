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

    if not is_integer(hours):
        hours_error = 'Not a valid integer'
        hours = ''
    else:
        hours = int(hours)
        if hours > 23 or hours <0:
            hours_error = 'Hour value out of range (0-23)'
            hours = ''

    if not is_integer(minutes):
        minutes_error = 'Not a valid integer'
        minutes = ''
    else:
        minutes = int(minutes)
        if minutes > 59 or minutes < 0:
            minutes_error = 'Minutes value out of range (0-59)'
            minutes = ''

    if not user_error and not pass_error and not vpass_error and not email_error:
        
        return redirect('/welcome')
    else:
        template = jinja_env.get_template('form.html')
        return template.render(user_error=user_error,
            pass_error=pass_error, vpass_error=vpass_error, email_error=email_error, user=username,
            email=email)



@app.route('/welcome')
def valid_time():
    name = request.args.get('user')
    return '<h1>Welcome {0}!!!</h1>'.format(name)
app.run()