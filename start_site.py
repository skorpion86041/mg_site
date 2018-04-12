from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/blank')
def blank():
    return render_template('blank.html')


@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

@app.route('/product')
def product():
    return render_template('product.html')

@app.route('/store')
def store():
    return render_template('store.html')






# @app.route('/hello')
# def hello():
#     return 'Hello World'
#
#
# @app.route('/user/<username>')
# def show_user_profile(username):
#     return 'Это пользователь ' + username
#
#
# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     return 'ID этого поста : ' + str(post_id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
