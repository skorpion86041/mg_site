from flask import Flask
from flask import render_template
from flask import request

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

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/delivery')
def delivery():
    return render_template('delivery.html')

@app.route('/exchange')
def exchange():
    return render_template('exchange.html')

@app.route('/repairs')
def repairs():
    return render_template('repairs.html')

@app.route('/shares')
def shares():
    return render_template('shares.html')

@app.route('/training')
def training():
    return render_template('training.html')

@app.route('/training2')
def training2():
    return render_template('training2.html')

@app.route('/consoles')
def consoles():
    return render_template('consoles.html')

@app.route('/accessories')
def accessories():
    return render_template('accessories.html')

@app.route('/games')
def games():
    return render_template('games.html')



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
