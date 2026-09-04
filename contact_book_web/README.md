# Contact Book — Web App (Task 4)

A contact book web application: add, search, update, and delete contacts through a browser interface, backed by a Flask API and a JSON data file.

## Technologies Used

- **Backend:** Python 3, [Flask](https://flask.palletsprojects.com/)
- **Frontend:** HTML5, CSS3 (custom, no framework), vanilla JavaScript (`fetch` API)
- **Storage:** `contacts.json` — a flat JSON file on disk, read/written by the Flask backend
- **Fonts:** Lora (headings), Inter (body/UI) via Google Fonts

## Features

- **Add Contact** — name, phone (validated, min. 7 digits), optional email (format-validated), with duplicate-name protection.
- **View All Contacts** — displayed as a grid of index-style cards, sorted alphabetically.
- **Search Contact** — live, debounced search by name (partial, case-insensitive) as you type.
- **Update Contact** — edit any contact's details in place.
- **Delete Contact** — remove a contact with a confirmation step.
- **Persistent Storage** — every change is written straight to `contacts.json`, so data survives server restarts.
- **No page reloads** — the frontend is a single page that talks to the backend via a small JSON API, so all actions happen instantly in place.

## Project Structure

```
contact_book_web/
├── app.py                 # Flask backend (routes + JSON API + validation)
├── requirements.txt        # Python dependencies
├── contacts.json           # Auto-generated data file (created on first use)
├── templates/
│   └── index.html          # Single-page frontend markup
├── static/
│   ├── style.css           # Styling (index-card / rolodex visual design)
│   └── script.js            # Frontend logic (fetch calls, rendering, modals)
└── README.md
```

## API Overview

| Method | Route                    | Description                       |
|--------|---------------------------|------------------------------------|
| GET    | `/`                        | Renders the web page               |
| GET    | `/api/contacts?q=<name>`   | List contacts, optional name filter|
| POST   | `/api/contacts`            | Add a new contact                  |
| PUT    | `/api/contacts/<id>`       | Update an existing contact         |
| DELETE | `/api/contacts/<id>`       | Delete a contact                   |

## Setup Instructions

### Prerequisites
- Python 3.7 or later

### Steps

1. **Clone the repository**
   ```bash
   git clone <GITHUB_REPO_LINK>
   cd <repo-folder>/contact_book_web
   ```

2. **(Recommended) Create a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate      # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**
   ```bash
   python3 app.py
   ```

5. **Open it in your browser**
   Visit **http://127.0.0.1:5000/**

6. **Data file**
   `contacts.json` is created automatically in the project folder the first time you add a contact, and stores all records, e.g.:
   ```json
   [
       {
           "id": "4d5e303f-4422-44d8-b9c4-3bc4942ca769",
           "name": "Alice Smith",
           "phone": "9876543210",
           "email": "alice@example.com"
       }
   ]
   ```

## GitHub Repository Link

[https://github.com/harshikadarda/CodeOrbit-Intenship](https://github.com/harshikadarda/CodeOrbit-Intenship)

