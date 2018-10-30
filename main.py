from flask import Flask, render_template, request, redirect
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

def ver_email(email):
    if email != '':
        atsign = 0
        period = 0
        for char in email:
            if char == '@':
                atsign += 1
            elif char == '.':
                period += 1
        if ((20 < len(email) or len(email) < 3) or (atsign != 1) or (period != 1) or (" " in email)):
            return False
        else:
            return True
    else:
        return True

@app.route('/index', methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']
    ver_pass = request.form['ver_pass']
    email = request.form['email']
    Error = False
    error = {
        'user' : "",
        'pass':"",
        'match':"",
        'email':""
    }

    if (username == "" or " " in username or 3 > len(username) or len(username) > 20):
        error['user'] = "That's not a valid username"
        Error = True
        pass
    else:
        pass

    if (password == "" or " " in password or 20 < len(password) or len(password) < 3):
        error['pass'] = "That's not a valid password"
        Error = True
        pass
    else:
        pass

    if (ver_pass != password or ver_pass == ""):
        error['match'] = "Passwords don't match"
        Error = True
        pass
    else:
        pass 

    if (ver_email(email) != True):
        error['email'] = "That's not a valid email"
        Error = True
        pass
    else:
        pass

    if (Error):
        return render_template('/index.html', username=username, error=error)
    else:
        return render_template('/welcome.html', username=username, email=email)
@app.route('/')
def index():
    compound_error = request.args.get('error')
    return render_template('index.html', error=compound_error and cgi.escape(compound_error, quote=True))

app.run()