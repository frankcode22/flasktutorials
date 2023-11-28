from flask import Flask

app=Flask(__name__)


@app.route('/')
def home():
    return 'Welcome home'
    # return render_template('index.html')

@app.route('/about')
def about():
    return ('This is all about us')


if __name__ == '__main__':
    app.run(debug=True)