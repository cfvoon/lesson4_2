from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    request_type_str = request.method
    if request_type_str == 'GET':
        return render_template('index.html', href2='')
    else:
        value_bread = 2
        value_cake = 3
        value_coffee = 2
        value_tea = 1
        num_bread = request.form['bread']
        num_cake = request.form['cake']
        num_coffee = request.form['coffee']
        num_tea = request.form['tea']
        total_bread = int(num_bread)*value_bread
        total_cake = int(num_cake)*value_cake
        total_coffee = int(num_coffee)*value_coffee
        total_tea = int(num_tea)*value_tea
        
        final_result = total_bread + total_cake + total_coffee + total_tea
        return render_template('index.html', href2='Bread = '+str(num_bread)+', Cake= '+str(num_cake)+', Coffee='+str(num_coffee)+', Tea='+str(num_tea)+',  Total = '+str(final_result))
