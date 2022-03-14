from flask import Flask, redirect, url_for, request, render_template, \
    make_response
import pybrake.flask


app = Flask(__name__)


app.config['PYBRAKE'] = dict(
    project_id=369254,
    project_key='b4cd81d1b6f867b8eb3c465e6c619cc3',
)
app = pybrake.flask.init_app(app)


@app.route('/')
def sayhello():
    5/0
    return 'Hello'


# app.add_url_rule('/','hello', sayhello)


@app.route('/<one>add<two>')
def add(one, two):
    return f"{one}+{two}={int(one) + int(two)}"


@app.route('/<name>')
def sayhi(name):
    return render_template('hello.html', name=name)


@app.route('/panel/<salutation>')
def saysomething(salutation):
    if salutation == 'guest':
        return redirect(url_for('sayhello'))
    else:
        return redirect(url_for('sayhi', name=salutation))


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        # password=request.form['password']
        res = make_response(redirect(url_for('sayhi', name=username)))
        res.set_cookie('username', username)
        return res
    else:
        name = request.cookies.get('username')
        if name:
            print(name,">>>>>>>>>>>")
            res = make_response(redirect(url_for('sayhi', name=name)))
            return res
        return render_template('login.html')
          # 750976123


if __name__ == '__main__':
    app.debug = True
    app.run(port=8069)
