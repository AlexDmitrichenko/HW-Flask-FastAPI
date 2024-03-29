from flask import Flask, render_template, request

app = Flask(__name__)


@app.get('/')
def index():
    return render_template('form_task7_HW.html')


@app.post('/')
def index_post():
    number = request.form.get('number')

    if number.isdigit():
        result = f'{number}² = {int(number) ** 2}'
        color = 'success'
    elif number.replace('.', '').isdigit():
        result = f'{number}² = {round(float(number) ** 2, 5)}'
        color = 'success'
    else:
        result = 'неправильное число'
        color = 'danger'

    return render_template('form_task7_HW.html', result=result, color=color)


if __name__ == '__main__':
    app.run(debug=True)