from flask import Flask

'''Creating a instance of the flask class'''

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to this flask workshop.\njust need to save changes"

@app.route("/index")
def index():
    return "this is the new index page"

if __name__=="__main__":
    app.run(debug=True)