from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/report',methods=['POST'])
def report():
    username = request.form.get('username')
    password = request.form.get('password')
    upper,lower,hasNum,length = check_constraints(password)
    return render_template('report.html', upper=upper, lower=lower,hasNum=hasNum,length=length)

def check_constraints(str):
    upper = any(c.isupper() for c in str)
    lower = any(c.islower() for c in str)
    hasNum = str[-1].isdigit()
    length = len(str)>=8
    return upper,lower,hasNum,length
    
if __name__ == '__main__':
    app.run(debug=True)