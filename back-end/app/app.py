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
from models import db, Activity, Activity_competence, Competence

app = Flask(__name__)
CORS(app)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost/activities'
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

@app.route('/create_emosocio_competence', methods=['POST'])
def create_emosocio_competence():
    if request.method=="POST":
        data = request.json
        print(data)
        try:
          activity=(Activity.query.filter_by(activity_title=data["activity_title"])).first().to_dict()
          id = activity["id"]
          print(id)
          new_emosocio_competency = Activity_competence(emosocio_competency_title=data["emosocio_competency_title"], activity_id=id)
          try:
            db.session.add(new_emosocio_competency)
            db.session.commit() 
            return new_emosocio_competency.to_dict()
          except:
            return "Error"  
        except:
            return "Error"         
    else:
        return "Error"

@app.route('/create_competence', methods=['POST'])
def create_competence():
        if request.method=="POST":
            data = request.json
            new_competence = Competence(code=data['code'])
            try:
                db.session.add(new_competence)
                db.session.commit() 
                return {"code": new_competence.code}
            except:
                return "Error" 
        else:
            return "Error"

@app.route('/get_activities', methods=['GET'])
def get_activities():
    if request.method=="GET":
        try:
            activities = Activity.query.all() 
            activities_dict = []
            for activity in activities:
                act_to_dict = activity.to_dict()
                emoSocio_competencies=Activity_competence.query.filter(Activity_competence.activity_id==act_to_dict["id"]).all()
                act_to_dict['emosocio_competences'] = [x.to_dict()["emosocio_competency_title"] for x in emoSocio_competencies]
                activities_dict.append(act_to_dict)
            return activities_dict
        except:
            return "Error"    
    else:
        return "Error"

@app.route('/get_activity', methods=['GET'])
def get_activity():
    if request.method=="GET":
        id = request.args.get('activity_id')
        activity=(Activity.query.filter_by(id=id)).first().to_dict()
        emoSocio_competencies=Activity_competence.query.filter(Activity_competence.activity_id==id).all()
        activity['emosocio_competences'] =  [x.to_dict()["emosocio_competency_title"] for x in emoSocio_competencies]  
        return activity 
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