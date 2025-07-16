# ⚽ Football Player Tracker

A simple web application built using **Flask** and **MySQL** that allows users to **track football players** and their information — add, view, and delete players dynamically.

---

## 📌 Features

- ✅ Add new football players (name, age, country, club)
- 📋 View all players in a neat HTML table
- ❌ Delete players by ID
- 🔗 Connected to a MySQL database
- 🌐 Runs on local browser via Flask

---

## 🛠️ Tech Stack

| Layer       | Tool           |
|-------------|----------------|
| Backend     | Python (Flask) |
| Database    | MySQL          |
| Frontend    | HTML (Jinja2)  |
| IDE         | PyCharm        |

---

## 🚀 How to Run the Project (for anyone)

> You can clone and run this project on any machine that supports Python and MySQL.

### 🔃 Step-by-step:

```bash
 1. Clone the repository
git clone https://github.com/mayukh-karmakar/football_tracker.git
cd football_tracker

2. Install Flask
pip install flask

3. Set up MySQL
- Create a database named `football_db`
- Import the SQL file if available (e.g., `football_db.sql`)
OR manually create tables based on your app.py logic

 4. Run the Flask application
python app.py

 5. Open browser and visit:
http://127.0.0.1:5000/
