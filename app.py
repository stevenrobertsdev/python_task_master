from flask import Flask, render_template, url_for

# references this file - app.py
app = Flask(__name__)


# setup index route
@app.route('/')
def index():
    # render_template knows to look in the templates folder
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)

