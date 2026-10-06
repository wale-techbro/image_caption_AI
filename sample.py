from flask import Flask

app = Flask(__name__)

books_data = {
    1: "Python for Beginners",
    2: "Learning Flask",
    3: "ML with Python"
}

@app.route("/")
def hello():
    return "Hello, Femi"
@app.route("/author")

def author():
    return "Author: Femi Kehinde"

@app.route("/books/<int:books_id>")
def view_book(books_id):
    if books_id in books_data:
        return f"Book {books_id}: {books_data[books_id]}"
    else:
        return ("Book not found")

if __name__ == "__main__":
    app.run(debug=True)