from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

def sortstr(Y):
    for i in range(1, len(Y)):
        b = Y[i]
        j = i - 1
        while (j >= 0) and (b < Y[j]):
            Y[j + 1] = Y[j]
            j -= 1
        Y[j + 1] = b
    return Y


@app.route("/")
def go():
    filename = "programm.csv"
    with open(filename, "w") as file_object:
        file_object.write("name")
        file_object.write(",")
        file_object.write("email")
        file_object.write(",")
        file_object.write("answer")
        file_object.write("\n")

    return render_template("1.html")

@app.route("/answer", methods=["POST"])
def nn():
    name = request.form["name"]
    email = request.form["email"]
    answer = request.form["message"]
    filename = "programm.csv"

    with open(filename, "a") as file_object:
        file_object.write(name)
        file_object.write(",")
        file_object.write(email)
        file_object.write(",")
        file_object.write(answer)
        file_object.write("\n")

    return render_template("1.html")

@app.route("/answer2", methods=["POST"])
def sortsting():
    string = list(map(int, request.form["string"].split()))
    string = sortstr(string)
    string = " ".join(map(str, string))
    return render_template("/flask.html", ans=string)

@app.route("/answer3", methods=["POST"])
def findsting():
    name1 = request.form["name1"]
    f = pd.read_csv("programm.csv")
    answ2 = f[f["name"] == name1].values
    answ2 = " ".join(answ2[0])
    return render_template("/put.html", ans2=answ2)

if __name__ == "__main__":
       app.run(debug=True)