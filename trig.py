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
        if request.method == 'POST': # маршутчик-обработчик вызывается, когда пользователь отрпавляет форму на севрер
            num_1 = request.form['num_1'] # для ввода одного из функций tan cos sin ctg
            num_2 = float(request.form['num_2']) # для ввода числа 
            num_3 = int(request.form['num_3']) # для ввода точности 
            num_4 = 'on' if request.form.get('num_4') else 'off' # для определения, в каком из размеров нужно считать (флаг)

            arg = num_2 # значение, котрое будет в строке ответа
            answer = '°' if num_4 == 'on' else 'рад' # устанавливает градусы или рад

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
