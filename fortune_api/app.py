from flask import Flask, Response, request, jsonify
import random

app = Flask(__name__)

# Service 3 - generate the fortune ether Good or Bad
@app.route('/getfortune', methods=['GET'])
def get_fortune():
    fortune = random.choice([True, False])
    return str(fortune)
   
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003, debug=True)