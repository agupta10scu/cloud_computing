from flask import Flask,render_template,jsonify
import json
import os
from requests import request as requests

app = Flask(__name__)

@app.route('/',methods= ['GET'])
def meal_recommendation():
    api_host = os.environ.get('API_HOST')
    api_port = os.environ.get('API_PORT')
    api_endpoint = os.environ.get('API_ENDPOINT')
    url = f'http://{api_host}:{api_port}/{api_endpoint}'

    response = requests.get(url)
    recommendation = json.loads(response.text)
    return render_template('food.html')

if __name__ == "__main__":
    port = os.environ.get('CONSUMER_PORT')
    app.run(debug=True, host='0.0.0.0', port=port)
