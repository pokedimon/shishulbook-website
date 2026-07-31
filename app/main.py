import secrets
from flask import Flask, url_for, render_template

app = Flask(__name__)
app.config['SERVER_NAME'] = 'localhost:8080'
app.config['SECRET_KEY'] = secrets.token_urlsafe(32)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(port=8080, debug=True)
    