# app.app_context() is a context manager provided by Flask that creates an application
# context for your Flask application. This context allows you to access the Flask application 
# and its configuration, as well as the objects and variables that are attached to it.
# When you use app.app_context(), you can run code within the context of your Flask application,
# even if it's outside of a request context. This is useful in cases where you need to perform 
# operations that are related to your application, such as creating database tables or initializing 
# an object with configuration from your application,
# but you don't have access to a request context.

from flask import Flask, request
from flask_cors import CORS
from models import db, Activity

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db.init_app(app)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/create_activity', methods=['POST'])
def create_activity():
    if request.method=='POST':
        data = request.json
        new_activity = Activity(data)   
        try:
            db.session.add(new_activity)
             #print(new_activity) 
            db.session.commit()
            #Activity.query.all() 
            return new_activity.to_dict()
        except:
            return "Error"    
    else:
        return "Error"
if __name__ == '__main__':
    with app.app_context():
        # code that needs access to the application context goes here
        db.create_all()
    app.run(debug=True)

# In this example, the db.create_all() method is called within the context of the Flask application, 
# which allows it to access the db object that was created using Flask-SQLAlchemy and 
# the configuration for the application.