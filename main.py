from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    var_1 = request.form.get("var_1", type=int)
    var_2 = request.form.get("var_2", type=int)
    operation = request.form.get("operation")
    if(operation == 'and'):
        result = var_1 & var_2
    elif(operation == 'or'):
        result = var_1 | var_2
    elif(operation == 'not_a'):
        result = ~var_1
    elif(operation == 'xor'):
        result = var_1 ^ var_2
    else:
        result = 'INVALID CHOICE'
    entry = result
    return render_template('result.html', entry=entry)

if __name__ == "__main__":
    app.run(debug=True)
