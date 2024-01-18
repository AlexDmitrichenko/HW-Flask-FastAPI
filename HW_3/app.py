from flask import Flask, render_template, redirect, url_for
from flask_wtf import CSRFProtect
from hashlib import sha256
from HW_3.models import db, User
from HW_3.forms import SingUpForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '3aa6d8a359ff3cf7f0eac295629748935cb45a059e392cc9f2a8e8fe9ac04c9f'
csrf = CSRFProtect(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///date.db'
db.init_app(app)


@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('Create database - Ok')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = SingUpForm()
    if form.validate_on_submit():
        user = User(firstname=form.firstname.data,
                    surname=form.surname.data,
                    email=form.email.data,
                    password=sha256(form.password.data.encode(encoding='utf-8')).hexdigest())
        db.session.add(user)
        db.session.commit()
        print(f'Adding user {form.firstname.data} {form.surname.data}!')
        return redirect(url_for('index'))

    return render_template('signin.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
