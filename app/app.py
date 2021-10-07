from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    request_type_str = request.method
    if request_type_str == 'GET':
        return render_template('index.html', href2='')
    else:
        num_A = request.form['A']
        num_B = request.form['B']
        final_result = int(num_A) + int(num_B)
        return render_template('index.html', href2='A = '+str(num_A)+', B= '+str(num_B)+', A + B = '+str(final_result))
