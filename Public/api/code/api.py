from random import random
from flask import Flask
import os
import random

app = Flask(__name__)

meals = [{'Name':'Veg Biryani','price':'$23.00'},
        {'Name':'Chicken pasta','price':'$12.59'},
        {'Name':'Kadhai Paneer','price':'$15.99'},
        {'Name':'Chole bature','price':'$7.99'},
        {'Name':'Allo chaat','price':'$0.00'},
        {'Name':'Garlic bread','price':'$12.00'},
        {'Name':'Latte','price':'$4.99'},
        {'Name':'Sandwich','price':'$8.59'},
        {'Name':'Rajma chaval','price':'$19.00'},
        {'Name':'Chole chaval','price':'$10.99'},
        {'Name':'Yellow lentils','price':'$11.00'},
        {'Name':'south indian combo','price':'$12.78'},
        {'Name':'curd','price':'$2.00'},
        {'Name':'lemonade','price':'$10.00'},
        {'Name':'brownie','price':'$2.50'}]

os.environ["API_ENDPOINT"]='meal'

api_endpoint = os.environ.get("API_ENDPOINT")
@app.route('/'+api_endpoint)
def get_reco():
    random_choice = random.randint(0,14)
    return meals[random_choice]

if __name__ == '__main__':
    port = os.environ.get('API_PORT',5000)
    app.run(host='0.0.0.0',port=port)
 