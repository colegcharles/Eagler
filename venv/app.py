from flask import Flask, escape, request, render_template, url_for, session

app = Flask(__name__)

app.secret_key = "abc"  

users = {
    'cole': 'password',
    'sofia': 'password',
    'tom': 'password'
}
@app.route('/login', methods=['GET','POST'])
def hello():
    if request.method == 'POST':
        if request.form['psw'] == users[request.form['uname']]:
            session['userName'] = request.form['uname']
            return render_template('home.html')
        print(request.form['uname'])
    name = render_template('login.html')
    return name

if __name__ == '__main__':
    app.run(debug=True)