from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# ─────────────────────────────────────
# Get a new database connection
# ─────────────────────────────────────
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Iammayukh@123",
        database="football_db"
    )

# ─────────────────────────────────────
# Add a player
# ─────────────────────────────────────
def add_player_to_db(name, age, country, club, position):
    db = get_db_connection()
    cursor = db.cursor()
    try:
        cursor.execute(
            "INSERT INTO players (name, age, country, club, position) VALUES (%s, %s, %s, %s, %s)",
            (name, age, country, club, position)
        )
        db.commit()
    finally:
        cursor.close()
        db.close()

# ─────────────────────────────────────
# Delete a player
# ─────────────────────────────────────
def delete_player_from_db(player_id):
    db = get_db_connection()
    cursor = db.cursor()
    try:
        cursor.execute("DELETE FROM players WHERE id = %s", (player_id,))
        db.commit()
    finally:
        cursor.close()
        db.close()

# ─────────────────────────────────────
# Get players (with optional filtering)
# ─────────────────────────────────────
def get_players_from_db(country=None, club=None):
    db = get_db_connection()
    cursor = db.cursor()
    try:
        query = "SELECT * FROM players"
        values = []

        if country:
            query += " WHERE country = %s"
            values.append(country)

        if club:
            if country:
                query += " AND club = %s"
            else:
                query += " WHERE club = %s"
            values.append(club)

        cursor.execute(query, values)
        players = cursor.fetchall()
        return players
    finally:
        cursor.close()
        db.close()

# ─────────────────────────────────────
# Get all unique countries
# ─────────────────────────────────────
def get_all_countries():
    db = get_db_connection()
    cursor = db.cursor()
    try:
        cursor.execute("SELECT DISTINCT country FROM players")
        countries = [row[0] for row in cursor.fetchall()]
        return countries
    finally:
        cursor.close()
        db.close()

# ─────────────────────────────────────
# Get all unique clubs
# ─────────────────────────────────────
def get_all_clubs():
    db = get_db_connection()
    cursor = db.cursor()
    try:
        cursor.execute("SELECT DISTINCT club FROM players")
        clubs = [row[0] for row in cursor.fetchall()]
        return clubs
    finally:
        cursor.close()
        db.close()

# ─────────────────────────────────────
# Routes
# ─────────────────────────────────────
@app.route('/')
def index():
    country = request.args.get('country')
    club = request.args.get('club')

    players = get_players_from_db(country, club)
    countries = get_all_countries()
    clubs = get_all_clubs()

    return render_template("index.html", players=players, countries=countries, clubs=clubs)

@app.route('/add', methods=['POST'])
def add_player():
    name = request.form['name']
    age = request.form['age']
    country = request.form['country']
    club = request.form['club']
    position = request.form['position']
    add_player_to_db(name, age, country, club, position)
    return redirect('/')

@app.route('/delete/<int:player_id>')
def delete_player(player_id):
    delete_player_from_db(player_id)
    return redirect('/')

# ─────────────────────────────────────
# Run the app
# ─────────────────────────────────────
if __name__ == '__main__':
    app.run(debug=True)
