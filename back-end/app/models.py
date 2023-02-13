from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    learning_objectives = db.Column(db.String(500))
    description = db.Column(db.Text)
    target_left = db.Column(db.Integer)
    target_right = db.Column(db.Integer)
    periodicity = db.Column(db.Integer)
    duration = db.Column(db.Integer)
    presence = db.Column(db.String(100))
    sub_grouping = db.Column(db.String(100))
    teacher_role = db.Column(db.String(100))
    evaluation = db.Column(db.Text)
    material_description = db.Column(db.Text)
    img_url = db.Column(db.Text)

    def __init__(self, data):
        self.title = data['title']     
        if 'learning_objectives' in data:
            self.learning_objectives = data['learning_objectives']
        if 'description' in data:
            self.description = data['description']
        if 'target_left' in data:
            self.target_left = data['target_left']
        if 'target_right' in data:
            self.target_right = data['target_right']
        if 'periodicity' in data:
            self.periodicity = data['periodicity']
        if 'duration' in data:
            self.duration = data['duration']
        if 'presence' in data:
            self.presence = data['presence']
        if 'sub_grouping' in data:
            self.sub_grouping = data['sub_grouping']
        if 'teacher_role' in data:
            self.teacher_role = data['teacher_role']
        if 'evaluation' in data:
            self.evaluation = data['evaluation']
        if 'material_description' in data:
            self.material_description = data['material_description']
        if 'img_url' in data:
            self.img_url = data['img_url']


    def to_dict(self):
        activity = {}
        activity['title'] = self.title
        activity['learning_objectives'] = self.learning_objectives 
        activity['description'] = self.description 
        activity['target_left'] = self.target_left 
        activity['target_right'] = self.target_right
        activity['periodicity'] = self.periodicity 
        activity['duration'] = self.duration
        activity['presence'] = self.presence
        activity['sub_grouping'] = self.sub_grouping
        activity['teacher_role'] = self.teacher_role
        activity['evaluation'] = self.evaluation 
        activity['material_description'] = self.material_description 
        activity['img_url'] = self.img_url
        return activity


    
