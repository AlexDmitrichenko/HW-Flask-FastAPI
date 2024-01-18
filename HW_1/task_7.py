from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def news():
    news_list = [
        {
            'title': 'Заголовок новости 1',
            'description': 'Описание новости 1',
            'date': '2023-11-01'
        },
        {
            'title': 'Заголовок новости 2',
            'description': 'Описание новости 2',
            'date': '2023-12-02'
        }
    ]

    return render_template('news_7.html', news=news_list)


if __name__ == '__main__':
    app.run()