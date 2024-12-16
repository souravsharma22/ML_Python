from flask import Flask, render_template,request,redirect,url_for

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


@app.route('/submit', methods=['GET','POST'])
def submit():
    total_score = 0
    if request.method=='POST':
        science = float(request.form['science'])
        math = float(request.form['maths'])
        c = float(request.form['c'])
        dataScience = float(request.form['dataScience'])
        total_score= (science+math+c+dataScience)/4
    else:
        return render_template('getresult.html')
    return redirect(url_for('success', score = total_score))


if __name__=="__main__":
    app.run(debug=True)