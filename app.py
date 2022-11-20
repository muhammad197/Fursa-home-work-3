import redis , requests
from flask import Flask,render_template

app = Flask(__name__)
datab = redis.Redis(host='redis', port=6379)

#BTC price
def bprice():
    api = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=ILS"
    res = (requests.get(api)).json()
    BTC_in_ILS = res["ILS"]
    return str(BTC_in_ILS)+" new israeli shekel"

#avg price last 10 min
def rateavg():
    api = "https://min-api.cryptocompare.com/data/v2/histominute?fsym=BTC&tsym=ILS&limit=10"
    res = (requests.get(api)).json()
    rates =[]   
    for i in range(10):
        rate = res['Data']["Data"][i]['close']
        rates.append(rate)
    
    average = sum(rates) / 10
    return str(average)+" new israeli shekel"

@app.route('/')
def hello():
    return render_template('index.html',first_text=bprice(),second_text=rateavg())