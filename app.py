from flask import Flask, jsonify, request
# In-memory storage for contacts
contacts = {}
app = Flask(__name__)

@app.route('/api/contacts/<int:id>', methods=['GET'])
def get_contact(id):
    # Retrieve a contact by ID
    contact = contacts.get(id)
    if contact:
        return jsonify(contact), 200
    else:
        return jsonify({"error": "Contact not found"}), 404

@app.route('/api/contacts/<int:id>', methods=['PUT'])
def update_contact(id):
    # Update a contact by ID
    data = request.get_json()
    if id in contacts:
        contacts[id].update(data)
        return jsonify({"success": True, "error": None}), 200
    else:
        return jsonify({"success": False, "error": "Contact not found"}), 404

@app.route('/api/contacts/<int:id>', methods=['DELETE'])
def delete_contact(id):
    # Delete a contact by ID
    if id in contacts:
        del contacts[id]
        return jsonify({"success": True, "error": None}), 200
    else:
        return jsonify({"success": False, "error": "Contact not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
