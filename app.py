from flask import Flask, redirect, render_template, request, session, url_for
from datetime import timedelta
from pages.assignment4.assignment4 import assignment4

app = Flask(__name__)
app.register_blueprint(assignment4)

app.secret_key = '123'
app.config['SESSION_PERMANENT'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=20)


@app.route('/')
@app.route('/home_page')
def home():
    return render_template('home_page.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/Assignment_31')
def site_to_visit():
    sites = {'tel aviv': 70, 'beer sheva': 55, 'jaffa': 30, 'jerusalem': 85, 'natanya': 40}
    return render_template('Assignment_31.html',
                           tours_site_price=sites)


users = {1: {'name': 'Amir', 'email': 'amir@gmail.com'},
         2: {'name': 'Ron', 'email': 'ron@gmail.com'},
         3: {'name': 'Roy', 'email': 'roy@gmail.com'},
         4: {'name': 'Naor', 'email': 'naor@gmail.com'},
         5: {'name': 'Orel', 'email': 'orel@gmail.com'}}


@app.route('/Assignment_32', methods=['GET', 'POST'])
def Assignment_32():
    if request.method == 'POST':
        user_name_reg = request.form['uname_reg'].capitalize()
        email_reg = request.form['email_reg']
        for user in users:
            if user_name_reg == users[user]["name"]:
                if email_reg == users[user]["email"]:
                    session['username'] = user_name_reg
                    session['logedin'] = True
                    return render_template('Assignment_32.html', massage_exist="User already exist, you signed in")
                else:
                    return render_template('Assignment_32.html', massage_error="Wrong email")
        users.update({list(users.keys())[-1] + 1: {"name": user_name_reg, "email": email_reg}})
        session['username'] = user_name_reg
        session['logedin'] = True
        return redirect('/home_page')
    elif 'uname' in request.args:
        user_name = request.args['uname'].capitalize()
        for user in users:
            if users[user]["name"] == user_name:
                return render_template('Assignment_32.html', name=users[user]["name"], email=users[user]['email'])
            if user_name == "":
                return render_template('Assignment_32.html', users=users)
        return render_template('Assignment_32.html', massage_exist="User not found")
    else:
        return render_template('Assignment_32.html')


@app.route('/log_out')
def log_out():
    session['logedin'] = False
    session.clear()
    return redirect(url_for('Assignment_32'))


if __name__ == '__main__':
    app.run(debug=False)


