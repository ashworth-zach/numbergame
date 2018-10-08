from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key='secret'
@app.route('/')
def index():
    if 'number' not in session:
        session['number']=random.randrange(0,100)
        print(session['number'])
    return render_template('index.html',playagain='none')
@app.route('/submit', methods=['POST'])
def submit():
    guess=request.form['guess']
    session['guess']=guess
    if 'guess' in session ==False:
        session['guess']=int(guess)
    if int(guess)>100:
        return redirect('/')
    if int(guess)==session['number']:
        return render_template('index.html',status='success', hotorcold='SUCCESS', playagain='visible')
    if int(guess)<session['number']:
        return render_template('index.html',status='danger', hotorcold='TOO LOW',playagain='none')
    if int(guess)>session['number']:
        return render_template('index.html',status='danger', hotorcold='TOO HIGH', playagain='none')
    print(session['number'])
    return redirect('/')
@app.route('/restart', methods=['GET'])
def restartgame():
    session.clear()
    session['number']=random.randrange(0,100)
    print(session['number'])
    return render_template('index.html', playagain='none')
if __name__=="__main__":
    app.run(debug=True)