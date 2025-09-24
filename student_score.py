from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def student_score():
    return render_template("student_score.html")
    

@app.route("/result", methods=["POST", "GET"])
def result():
    if request.method == "POST":
        result = request.form
        return render_template("result_page.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)

