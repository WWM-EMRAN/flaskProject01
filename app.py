from flask import Flask, render_template, url_for

app = Flask(__name__)


# @app.route('/')
# def hello_world():  # put application's code here
#     return 'Hello World!'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emran_cv_printable')
def emran_cv_printable():
    return render_template('emran_cv_printable.html')


if __name__ == '__main__':
    app.run()
