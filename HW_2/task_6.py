from flask import Flask, render_template, request

app = Flask(__name__)


@app.get('/')
def index():
    return render_template('form_task6_HW.html')


@app.post('/')
def index_post():
    name = request.form.get('name')
    age = request.form.get('age')

    if age.isdigit() and 0 < int(age) <= 120:
        result = f'возраст {age}'
        color = 'success'
    else:
        result = 'неправильный возраст'
        color = 'danger'

    return render_template(
        'form_task6_HW.html', name=name, result=result, color=color
    )


if __name__ == '__main__':
    app.run(debug=True)