from appname import db

class Points(db.Model):
    __tablename__ = 'points'
    id = db.Column(db.Integer, primary_key=True)
    erodov = db.Column(db.Integer)
    newton = db.Column(db.Integer)
    tesla = db.Column(db.Integer)