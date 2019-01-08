from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def homepage():
    return "This is a homepage."




if __name__ == '__main__':
    app.run(port='80')
