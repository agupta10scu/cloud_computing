from flask import Flask,render_template,jsonify
import json
import os
import requests
import sys

app = Flask(__name__)

@app.route('/',methods= ['GET'])
def meal_recommendation():
    api_host = os.environ.get('API_HOST')
    api_port = os.environ.get('API_PORT')
    api_endpoint = os.environ.get('API_ENDPOINT')
    url = f'http://{api_host}:{api_port}/{api_endpoint}'
    res = ''
    while res == '':
        try:
            res = requests.get(url, verify=False, timeout=3)
            break          
        except:
            url = url.replace('localhost', '192.168.240.1')

    recommendation = json.loads(res.text)
    print(recommendation)
    return render_template('food.html', reco = recommendation)

if __name__ == "__main__":
    port = os.environ.get('CONSUMER_PORT',80)
    app.run(debug='True', host='0.0.0.0', port=port)
