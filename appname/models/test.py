from appname import db

class test(db.Model):
    __tablename__ = 'test'    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)