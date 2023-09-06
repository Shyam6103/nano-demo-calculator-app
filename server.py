from flask import Flask,jsonify,request

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    
    return "helo world!"

@app.route("/calculator/add", methods=['POST'])
def add():
    num=request.json
    a=num["first"]
    b=num["second"]
    return jsonify({ 'result': a+b }  ),200

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    num=request.json
    a=num["first"]
    b=num["second"]
    return jsonify({ 'result': a-b }  ),200


if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
