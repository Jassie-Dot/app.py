from flask import Flask  # Import the Flask class

# Create an instance of Flask
app = Flask(__name__)

# This is the route for the homepage "/"
@app.route('/')
def home():
    return "Hello Flask"  # Text shown on the main page

# This is the route for the About page "/about"
@app.route('/about')
def about():
    return "This is About Page"  # Text shown on the About page

# Run the app
if __name__ == '__main__':
    app.run(debug=True)

