from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def go():
    filename = 'programm.csv'
    with open(filename, 'w') as file_object:
        file_object.write('name')
        file_object.write(',')
        file_object.write('email')
        file_object.write(',')
        file_object.write('answer')
        file_object.write("\n")

    return render_template('1.html')

@app.route('/answer', methods=['POST'])
def nn():
    name = request.form['name']
    email = request.form['email']
    answer = request.form['message']
    filename = 'programm.csv'

    with open(filename, 'a') as file_object:
        file_object.write(name)
        file_object.write(',')
        file_object.write(email)
        file_object.write(',')
        file_object.write(answer)
        file_object.write("\n")

    return render_template('1.html')

if __name__ == '__main__':
       app.run(debug=True)