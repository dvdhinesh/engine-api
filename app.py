from flask import Flask
import os
import random

app = Flask(__name__)

@app.route("/")
def hello_engine():
    return "<p>Hello, Engine!</p>"

@app.route('/metrics')
def metrics():
    metrics = ""
    metrics += 'view_total{product="%s"} %s\n' % (random.randrange(1,10), random.randrange(2000, 50000,50))
    return metrics    

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)