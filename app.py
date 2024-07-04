from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# WeatherAPI key
WEATHER_API_KEY = '686d5a140e3d427c96985827240407'

def get_client_ip():
    # Use request headers to get the real client IP if behind a proxy
    if request.headers.getlist("X-Forwarded-For"):
        ip = request.headers.getlist("X-Forwarded-For")[0]
    else:
        ip = request.remote_addr

    # If running locally, use a known public IP address for testing
    if ip == '127.0.0.1':
        ip = '8.8.8.8'  # Google's public DNS server IP for testing

    return ip

@app.route('/api/hello', methods=['GET'])
def hello():
    visitor_name = request.args.get('visitor_name', 'Mark')
    client_ip = get_client_ip()

    # Use a service to get the location from the IP
    location_response = requests.get(f'http://ip-api.com/json/{client_ip}')
    location_data = location_response.json()

    city = location_data.get('city', 'Unknown')

    # Use weatherapi.com to get the temperature
    weather_response = requests.get(
        f'http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={city}'
    )
    weather_data = weather_response.json()

    temperature = weather_data['current']['temp_c']
    greeting = f'Hello, {visitor_name}! The temperature is {temperature} degrees Celsius in {city}.'

    return jsonify({
        'client_ip': client_ip,
        'location': city,
        'greeting': greeting
    })

if __name__ == '__main__':
    app.run(debug=True)
