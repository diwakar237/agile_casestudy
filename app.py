from flask import Flask, request, jsonify

app = Flask(__name__)
inventory = {}

@app.route('/add', methods=['POST'])
def add_medicine():
    data = request.json or {}
    name = data.get('name')
    quantity = data.get('quantity', 0)
    if not name:
        return jsonify({"error": "Medicine name is required"}), 400
    inventory[name] = inventory.get(name, 0) + int(quantity)
    return jsonify({"message": f"Added {quantity} of {name} successfully!"}), 201

# v2 feature: Update Quantity
@app.route('/update', methods=['PUT'])
def update_medicine():
    data = request.json or {}
    name = data.get('name')
    quantity = data.get('quantity')
    if name not in inventory:
        return jsonify({"error": "Medicine not found"}), 404
    inventory[name] = int(quantity)
    return jsonify({"message": f"Updated {name} quantity to {quantity}."}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
