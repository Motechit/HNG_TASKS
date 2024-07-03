from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api/<user_ip>")

def api(user_ip):
    user_data = {
        "client_ip": "127.0.0.1", 
        "location": "New York",
        "greeting": "Hello Mark!, the temperature is 11 degrees Celcius in New York"
    }

    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra
    return jsonify(user_data), 200
# def home():
#     return "Hello there, Please review my Stage 1 Task. Thank you!"

if __name__ == "__main__":
    app.run(debug=True)