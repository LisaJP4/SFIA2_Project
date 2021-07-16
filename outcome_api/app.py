from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Service 4 - use fortune and days to deliver a fate
@app.route('/getoutcome', methods=['GET', 'POST'])
def get_outcome():
    fate = request.get_json()
    if fate == {"1" : "True"}:
        return "You only got a light touch - you are back out into the field in no time."
    elif fate == {"1" : "False"}:
        return "You prayed to be spared - but your prayers were not heard. The plague makes your teeth fall out."
    elif fate == {"2": "True"}:
        return "You only got a light touch - you are back out into the field in no time."
    elif fate == {"2": "False"}:
        return "You prayed to be spared - but your prayers were not heard. The plague makes your teeth fall out."
    elif fate == {"5" : "True"}:
        return "A plague doctor makes you drink forty filthy potions. It makes you even sicker - but you are still alive by the end of the week."
    elif fate == {"5" : "False"}:
        return "A plague doctor visits you with a jar of leeches - he says there is nothing to be done but sends you a bill for his services anyway."
    elif fate == {"6" : "True"}:
        return  "A plague doctor makes you drink forty filthy potions. It makes you even sicker - but you are still alive by the end of the week."
    elif fate == {"6" : "False"}:
        return "A plague doctor visits you with a jar of leeches - he says there is nothing to be done but sends you a bill for his services anyway."
    elif fate == {"7" : "True"}:
        return "A mysterious traveller claiming they are from the future gives you a magical ~medicine~ which cures you on your deathbed!"
    else:
        return "Uh oh, call the gravedigger. You are a goner!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)

