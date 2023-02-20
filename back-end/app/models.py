from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    activity_title = db.Column(db.String(100), nullable=False)
    learning_objectives = db.Column(db.String(500))
    didactic_strategies = db.relationship('Didactic_strategies', backref='didact_activity')
    description = db.Column(db.Text)
    target_age_group_left = db.Column(db.Integer)
    target_age_group_right = db.Column(db.Integer)
    periodicity = db.Column(db.Integer)
    duration = db.Column(db.Integer)
    presence = db.Column(db.String(100))
    emoSocio_competencies = db.relationship('EmoSocio_Competencies', backref='emosoc_compet_activity')
    sub_grouping = db.Column(db.String(100))
    teacher_role = db.Column(db.String(100))
    evaluation = db.Column(db.Text)
    adapted_to_special_needs = db.relationship('Adapted_to_special_needs', backref='sp_needs_activity')
    publications = db.relationship('Publications', backref='publication_activity')
    material_description = db.Column(db.Text)
    languages = db.relationship('Languages', backref='lang_activity')
    img_url = db.Column(db.Text)

    def __init__(self, data):
        self.title = data['activity_title']     
        if 'learning_objectives' in data:
            self.learning_objectives = data['learning_objectives']
        if 'description' in data:
            self.description = data['description']
        if 'target_age_left' in data:
            self.target_age_left = data['target_age_left']
        if 'target_age_right' in data:
            self.target_age_right = data['target_age_right']
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
        activity['activity_title'] = self.activity_title
        activity['learning_objectives'] = self.learning_objectives 
        activity['description'] = self.description 
        activity['target_age_left'] = self.target_age_left 
        activity['target_age_right'] = self.target_age_right
        activity['periodicity'] = self.periodicity 
        activity['duration'] = self.duration
        activity['presence'] = self.presence
        activity['sub_grouping'] = self.sub_grouping
        activity['teacher_role'] = self.teacher_role
        activity['evaluation'] = self.evaluation 
        activity['material_description'] = self.material_description 
        activity['img_url'] = self.img_url
        return activity

class Didactic_strategies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    didactic_strategy_title = db.Column(db.String(100), nullable=False)
    activity_id = db.Column(db.Integer, db.ForeignKey('activity.id'))

class EmoSocio_competencies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    emosocio_competency_title = db.Column(db.String(100), nullable=False)
    activity_id = db.Column(db.Integer, db.ForeignKey('activity.id'))    

class adapted_to_special_needs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    special_need_title = db.Column(db.String(100), nullable=False)
    activity_id = db.Column(db.Integer, db.ForeignKey('activity.id'))

class Publications(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    publication_title = db.Column(db.String(100), nullable=False)
    activity_id = db.Column(db.Integer, db.ForeignKey('activity.id'))

class Language(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    language_title = db.Column(db.String(100), nullable=False)
    activity_id = db.Column(db.Integer, db.ForeignKey('activity.id'))