from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('home_8.html')


@app.route('/about/')
def about():
    return render_template('about_8.html')


@app.route('/contact/')
def contact():
    return render_template('contact_8.html')


if __name__ == '__main__':
    app.run()