from flask import Flask  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following

def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/dojo')
def success():
    return 'Dojo!'

@app.route('/say/<string:name>')
def say(name):
    return f'Hello, {name.title()}'

@app.route('/repeat/<int:num>/<string:str>')
def repeat(num, str):
    output = ''
    i = 0
    while i < num:
        output += f'<p>{str}</p>'
        i += 1
    return output

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(host='localhost', port=5001, debug=True)    # Run the app in debug mode.

# Need to change the port for mac to port 5001 due to AirPlay occupies port 5000



# Notice how we are accessing the app object and running the route 
# method, passing in a string that is the route that we want to add to 
# our application. You must do this for every route that you want to 
# add to our application.
