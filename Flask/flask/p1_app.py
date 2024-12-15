from flask import Flask,render_template

'''Creating a instance of the flask class'''

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to this flask workshop.\njust need to save changes"

@app.route("/index")
def index():
    return "this is the new index page"

@app.route('/success/<int:score>')
def success(score):
    res=''
    if score>=50:
        res='PASS'
    else:
        res="Fail"
    return render_template('result.html', results=res)

@app.route('/newres/<int:score>')
def newres(score):
    res=''
    if score>=50:
        res='PASS'
    else:
        res="Fail"
    exp={'marks':score,'Staus':res}
    return render_template('result1.html', results2=exp)

@app.route('/condition/<int:score>')
def condition(score):
    
    return render_template('result2.html', results3=score)

if __name__=="__main__":
    app.run(debug=True)