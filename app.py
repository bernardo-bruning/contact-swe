from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
# Define the Contact model
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f'<Contact {self.name}>'
contacts = {}

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
