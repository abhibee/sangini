from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
    return "Hello World!"


@app.route('/<name>')
def hello_name(name):
    return "Hello {}! How are you?.".format(name)


if __name__ == '__main__':
    app.run()
