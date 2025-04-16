from app import setup
from app.database.SqliteConnection import SqliteConnection

app = setup()
db = SqliteConnection()

if __name__ == "__main__":
    app.run(debug=True)