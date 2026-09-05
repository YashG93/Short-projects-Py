from flask import Flask,request,render_template
from operation import Add_amt,Add_exp,Total_bal

app=Flask(__name__)

@app.route("/",methods=["POST","GET"])
def expense():
    result=None
    exception=None

    if request.method=="POST":
        command=request.form["command"]
        amount=request.form["amount"]

        try:
            if command=="add_amount":
                amount=float(amount)
                result=Add_amt(amount)

            elif command=="add_exp":
                amount=float(amount)
                result=Add_exp(amount)

            elif command=="total_bal":
                result=Total_bal()

            else:
                result="Invalid"

        except Exception:
            exception=("Enter Correct value:")

    return render_template("index.html",result=result,exception=exception)
app.run(debug=True)