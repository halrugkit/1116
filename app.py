from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/join')
def join():
    return render_template('join.html')

@app.route('/mypage')
def mypage():
    return render_template('mypage.html')

@app.route('/memberModify')
def memberModify():
    return render_template('mypageModify.html')

@app.route('/doolReg')
def doolReg():
    return render_template('mypageDoolReg.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)