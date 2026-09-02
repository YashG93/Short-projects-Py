
from flask import Flask,render_template,request
from operation import add,sub,mult,div

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def calculator():
    result=None
    exception=None
    if request.method=="POST":
        expression=request.form["expression"]

        try:
            if "+" in expression:
                a,b=expression.split("+")
                a=float(a)
                b=float(b)
                result=(add(a,b))

            elif "-" in expression:
                a,b=expression.split("-")
                a=float(a)
                b=float(b)
                result=(sub(a,b))

            elif "x" in expression:
                a,b=expression.split("x")
                a=float(a)
                b=float(b)
                result=(mult(a,b))

            elif "%" in expression:
                a,b=expression.split("%")
                a=float(a)
                b=float(b)
                result=(div(a,b))

            else:
                result="Invalid "

        except Exception:
            exception=("Enter correct Expression:")
            
    return render_template("index.html",result=result,exception=exception)

app.run(debug=True)