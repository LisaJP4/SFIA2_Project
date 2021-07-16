from flask import Flask, render_template, jsonify, Response
import requests

app = Flask(__name__)

# Create the home/welcome route

# this must query the API for a number of days and a fortune to get an outcome based on these 
@app.route('/')
def home():
    days = requests.get('http://plague_days:5001/getday')
    fortune = requests.get('http://plague_fortune:5003/getfortune')
    outcome = requests.post('http://plague_outcome:5002/getoutcome', json={days.text : fortune.text})
    if fortune.text == "True":
        luck = "Lucky"
    else:
        luck = "Unlucky"
    return render_template('plague.html', days=days.text, fortune=luck, outcome=outcome.text)
    

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)



    # for_outcome = {days.text : fortune.text}