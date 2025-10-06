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

'''
From flask import Flask
- This imports the flask class from the Flask library

app=Flask(__name__)
- This creates your web application.
__name__ tells flask where your app's main file is.

@app.route('/')
-This line tells flask what URL should trigger a specific function.
here ('/') means the homepage.

def home(): return "Hello Flask"
- when someone visits your homepage, flask runs this function and shows that text

@app.route('/about')
- This sets up another route for /about

if__name__=='__main__':
-This means: only run the app is this file is executed directly(not imported)

app.run(debug=true)
-This starts a devlopment web serve and shows helpful error message if something goes wrong.
'''