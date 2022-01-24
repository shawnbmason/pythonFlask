from flask import Flask

app = Flask(__name__)

@app.route('/orders/<username>/<int:order_id>')
def orders(user_name, order_id):
    return f'<p>Fetching order #{order_id} for {user_name}.</p>'

@app.route('/')
@app.route('/home')
def home():
    return '<h1>Hello, World!</h1>'

@app.route('/reporter/<int:reporter_id>')
def reporter(reporter_id):
    return '''
    <h2>Reporter {reporter_id} Bio</h2>
    <a href="/">Return to home page</a>
    '''
    
    
# First flask app
from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
  return '<h1>Hello, World!</h1>'


@app.route('/reporter/<int:reporter_id>')
def reporter(reporter_id):
  return f'''
  <h2>Reporter {reporter_id} Bio</h2>
  <a href="/">Return to home page</a>
  '''
@app.route('/article/<article_name>')
def article(article_name):
  return f'''
  <h2>{article_name.replace('-', ' ').title()}</h2>
  <a href='/'>Return back to home page</a>
  '''



from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  return '''
  <h1>Adopt a Pet!</h1>
  <p>Browse through the links below to find your furry friend:</p>
  <ul>
    <li><a href='animals/dogs'>Dogs</a></li>
    <li><a href='animals/cats'>Cats</a></li>
    <li><a href='animals/rabbits'>Rabbits</a></li>
  </ul>
  '''


@app.route('/animals/<pet_type>')
def animals(pet_type):
    html = f'<h1>List of pets {pet_type}</h1>'
    return html
   