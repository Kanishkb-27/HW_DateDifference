from flask import Flask,render_template,request
from datetime import date

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calculate",methods=["POST"])
def calculate():
    d1=int(request.form.get("d1"))
    m1=int(request.form.get("m1"))
    y1=int(request.form.get("y1"))
    d2=int(request.form.get("d2"))
    m2=int(request.form.get("m2"))
    y2=int(request.form.get("y2"))
    date1=date(y1,m1,d1)
    date2=date(y2,m2,d2)
    difference=date2-date1
    return render_template("index.html",difference=difference.days)
if __name__=="__main__":
    app.run(debug=True)