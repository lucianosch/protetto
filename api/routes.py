# from protetto import app
from flask import Flask,render_template, session, redirect, url_for, flash, request

app = Flask(__name__)

app.config['SECRET_KEY'] = b'Fr@s3_S3GR3t@_H2O_C6H12O6'
elenco = [{"username": "Tizio", "password": "Tizio"},
          {"username": "Caio", "password": "Caio"},
          {"username": "Sempronio", "password": "Sempronio"}]

nomi = []
for user in elenco:
    nomi.append(user['username'])


@app.route('/', methods=('GET', 'POST'))
@app.route('/home', methods=('GET', 'POST'))
def home():
    if request.args:
        return render_template('welcome.html', utente=request.args['utente'])
    else:
        return render_template('home.html')


'''
@app.route('/home/<utente>', methods=('GET', 'POST'))
def welcome(utente):
    return render_template('welcome.html', utente=utente)



@app.route('/benvenuto', methods=('GET', 'POST'))
def benvenuto():
    if request.method == 'POST':
        utente = request.json['utente']
        return render_template('welcome.html', utente=utente)
    return redirect(url_for('home'))
'''


@app.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        d = {'username': username, 'password': password}
        if not username:
            flash('Username is required!')
        elif not password:
            flash('Password is required!')
        elif elenco.count(d) == 0:
            flash('Login incorrect!')
        else:
            session['connesso'] = True
            # return redirect(url_for('index'))
            return redirect('/index')
    return render_template('login.html')


@app.route('/registrati', methods=('GET', 'POST'))
def registrati():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        pass2 = request.form['password2']
        d = {'username': username, 'password': password}
        if not username:
            flash('Username is required!')
        elif not password or not pass2:
            flash('Password is required!')
        elif password != pass2:
            flash('Le password non corrispondono')
        elif nomi.count(username) > 0:
            flash('Nome utente già presente!')
        else:
            elenco.append(d)
            nomi.append(d['username'])
            # txt = "Complimenti {user}, ti sei registrato!"
            # flash(txt.format(user=username))
            return redirect(url_for('home', utente=username))
            # return redirect(url_for('webhook'), code=307)
            # render_template('welcome.html', utente=username)

    return render_template('registrazione.html')


@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method =='POST':
        return 'Hello'
    if 'connesso' not in session:
        return redirect(url_for('home'))
    return render_template('index.html')


@app.route('/page/<num>')
def page(num):
    if 'connesso' not in session:
        return redirect(url_for('index'))
    return render_template('page.html', num=num)


@app.route('/logout')
def logout():
    session.clear()
    # session.pop('connesso')
    return redirect(url_for('index'))


'''
@app.route('/login/<username>')
def login(username):
    if elenco.count(username) == 1:
        session['username'] = username
        return 'Logged in as ' + username
    else:
        return 'You are not authorized'


@app.route('/controlla/<username>')
def controlla(username):
    if 'username' in session and session['username'] == username:
        return 'You are logged in'
    else:
        return 'Not logged in'


@app.route('/')
@app.route('/home')
def index():
    return render_template('home.html')


@app.route('/page/<num>')
def page(num):
    return render_template('page.html', num=num)
'''
# app.run()
