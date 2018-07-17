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

@app.route('/consoles')
def consoles():
    return render_template('consoles.html')

@app.route('/accessories')
def accessories():
    return render_template('accessories.html')

@app.route('/courier')
def courier():
    return render_template('courier.html')

@app.route('/pickup')
def pickup():
    return render_template('pickup.html')

@app.route('/data')
def data():
    return render_template('data.html')


@app.route('/location')
def location():
    return render_template('location.html')

@app.route('/games')
def games():
    return render_template('games.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/departure')
def departure():
    return render_template('departure.html')


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
