from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home_9.html')


@app.route('/jeans/')
def clothes():
    return render_template('jeans_9.html')


@app.route('/jacket/')
def jacket():
    return render_template('jacket_9.html')


@app.route('/shoes/')
def shoes():
    return render_template('shoes_9.html')


if __name__ == '__main__':
    app.run()