"""
Contact Book — Flask Web App
-----------------------------
Backend server exposing a small JSON API for managing contacts, plus a
single-page frontend (templates/index.html + static/script.js) that talks
to it. Contacts are persisted to contacts.json on disk.

Routes:
    GET    /                      -> renders the web page
    GET    /api/contacts          -> list all contacts (optional ?q=search)
    POST   /api/contacts          -> add a new contact
    PUT    /api/contacts/<id>     -> update an existing contact
    DELETE /api/contacts/<id>     -> delete a contact
"""

import json
import os
import re
import uuid

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

DATA_FILE = os.path.join(os.path.dirname(__file__), "contacts.json")


# ---------------------------------------------------------------------------
# Data persistence helpers
# ---------------------------------------------------------------------------
def load_contacts():
    """Load the contact list from the JSON file on disk."""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except (json.JSONDecodeError, IOError):
        return []


def save_contacts(contacts):
    """Persist the contact list to the JSON file on disk."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(contacts, f, indent=4)


# ---------------------------------------------------------------------------
# Validation helpers
# ---------------------------------------------------------------------------
def is_valid_email(email):
    if not email:
        return True  # optional field
    return re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email) is not None


def is_valid_phone(phone):
    if not phone:
        return False
    cleaned = re.sub(r"[\s\-\+\(\)]", "", phone)
    return cleaned.isdigit() and len(cleaned) >= 7


# ---------------------------------------------------------------------------
# Page route
# ---------------------------------------------------------------------------
@app.route("/")
def index():
    return render_template("index.html")


# ---------------------------------------------------------------------------
# API routes
# ---------------------------------------------------------------------------
@app.route("/api/contacts", methods=["GET"])
def get_contacts():
    """Return all contacts, optionally filtered by a case-insensitive
    partial match on the name (query param 'q')."""
    contacts = load_contacts()
    query = request.args.get("q", "").strip().lower()

    if query:
        contacts = [c for c in contacts if query in c["name"].lower()]

    contacts = sorted(contacts, key=lambda c: c["name"].lower())
    return jsonify(contacts)


@app.route("/api/contacts", methods=["POST"])
def add_contact():
    """Create a new contact from JSON body: {name, phone, email}."""
    data = request.get_json(silent=True) or {}
    name = (data.get("name") or "").strip()
    phone = (data.get("phone") or "").strip()
    email = (data.get("email") or "").strip()

    if not name:
        return jsonify({"error": "Name is required."}), 400
    if not is_valid_phone(phone):
        return jsonify({"error": "Phone must contain at least 7 digits."}), 400
    if not is_valid_email(email):
        return jsonify({"error": "Email format is invalid."}), 400

    contacts = load_contacts()

    if any(c["name"].lower() == name.lower() for c in contacts):
        return jsonify({"error": f"A contact named '{name}' already exists."}), 409

    new_contact = {
        "id": str(uuid.uuid4()),
        "name": name,
        "phone": phone,
        "email": email,
    }
    contacts.append(new_contact)
    save_contacts(contacts)
    return jsonify(new_contact), 201


@app.route("/api/contacts/<contact_id>", methods=["PUT"])
def update_contact(contact_id):
    """Update an existing contact's phone/email/name by id."""
    data = request.get_json(silent=True) or {}
    contacts = load_contacts()

    contact = next((c for c in contacts if c["id"] == contact_id), None)
    if not contact:
        return jsonify({"error": "Contact not found."}), 404

    name = (data.get("name") or contact["name"]).strip()
    phone = (data.get("phone") or contact["phone"]).strip()
    email = data.get("email", contact["email"]).strip()

    if not name:
        return jsonify({"error": "Name is required."}), 400
    if not is_valid_phone(phone):
        return jsonify({"error": "Phone must contain at least 7 digits."}), 400
    if not is_valid_email(email):
        return jsonify({"error": "Email format is invalid."}), 400

    # Prevent renaming into a duplicate of another existing contact
    if any(c["id"] != contact_id and c["name"].lower() == name.lower() for c in contacts):
        return jsonify({"error": f"A contact named '{name}' already exists."}), 409

    contact["name"] = name
    contact["phone"] = phone
    contact["email"] = email
    save_contacts(contacts)
    return jsonify(contact)


@app.route("/api/contacts/<contact_id>", methods=["DELETE"])
def delete_contact(contact_id):
    """Delete a contact by id."""
    contacts = load_contacts()
    remaining = [c for c in contacts if c["id"] != contact_id]

    if len(remaining) == len(contacts):
        return jsonify({"error": "Contact not found."}), 404

    save_contacts(remaining)
    return jsonify({"message": "Deleted."})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
