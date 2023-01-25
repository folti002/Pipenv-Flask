from flask import *

app = Flask(__name__)

# Standard Python function that returns a function - function returned by app.route is then executed on hello_world() function 
# The following function is called, when the URL / is visited
@app.route("/") 
def hello_world():
  return "<p>Hello, World!</p>"

@app.route('/hi', methods=['GET'])
def hi():
  user_name = request.args.get("userName", "unknown")
  return render_template('main.html', user=user_name) 