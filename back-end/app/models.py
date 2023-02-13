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
    presence = db.Column(db.String(100), nullable=False)
    sub_grouping = db.Column(db.String(100), nullable=False)
    teacher_role = db.Column(db.String(100), nullable=False)
    evaluation = db.Column(db.Text)
    material_description = db.Column(db.Text)
    img_url = db.Column(db.Text)

    def __repr__(self):
        return self.title
