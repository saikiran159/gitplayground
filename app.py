from flask import Flask
from flask import make_response,jsonify

app = Flask(__name__)

@app.route('/get',methods=["GET"])
def get_request():
    return make_response(jsonify({"name":"saikiran","age":26}),200)

if __name__ == "__main__":
    app.run()