from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/api/products', methods=['GET'])
def get_products():
    url = "https://s3.amazonaws.com/open-to-cors/assignment.json"

    try:
        response = requests.get(url)
        response.raise_for_status()

        # Parse the JSON data
        products_data = response.json()

        return jsonify(products_data)
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
