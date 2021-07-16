from flask import Flask, Response, request, jsonify
import random

app = Flask(__name__)

# Service 2 - generate a number between 1 and 7(inclusive)
@app.route('/getday', methods=['GET'])
def get_day():
    time = random.randint(1, 7)
    return str(time)
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)