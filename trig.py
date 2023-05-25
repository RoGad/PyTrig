from flask import Flask, render_template, request
from math import cos, sin, tan, pi

app = Flask(__name__)
def trig():
    @app.route('/')
    @app.route('/index')
    def index():
        return render_template("index.html")

    @app.route('/', methods=['POST', 'GET'])
    def form():
        if request.method == 'POST':
            num_1 = request.form['num_1']
            num_2 = float(request.form['num_2'])
            num_3 = int(request.form['num_3'])
            num_4 = 'on' if request.form.get('num_4') else 'off'

            arg = num_2
            answer = '°' if num_4 == 'on' else 'рад'

            try:
                if num_1 == 'cos':
                    func_name = 'cos'
                    result = round(cos(num_2), num_3)
                elif num_1 == 'sin':
                    func_name = 'sin'
                    result = round(sin(num_2), num_3)
                elif num_1 == 'tan':
                    func_name = 'tan'
                    result = round(tan(num_2), num_3)
                elif num_1 == 'ctg':
                    func_name = 'ctg'
                    result = round(1 / tan(num_2), num_3)
                else:
                    func_name = 'такой функции нет'
                    result = 'решения нет'
            except ZeroDivisionError:
                result = 'нет решения'

            ans = f'{func_name}({arg} {answer}) = {result}'
            return render_template('index.html', ans=ans)
    app.run()
