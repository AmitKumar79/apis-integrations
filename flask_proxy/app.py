from flask import Flask, request, jsonify
import os, requests
from urllib.parse import urlencode

app = Flask(__name__)
GOOGLE_MAPS_KEY = os.environ.get("GOOGLE_MAPS_API_KEY", "REPLACE_WITH_KEY")

@app.route('/maps/geocode')
def geocode():
    address = request.args.get('address')
    if not address:
        return jsonify({'error': 'address query required'}), 400
    params = {'address': address, 'key': GOOGLE_MAPS_KEY}
    url = 'https://maps.googleapis.com/maps/api/geocode/json?' + urlencode(params)
    return jsonify(requests.get(url).json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
