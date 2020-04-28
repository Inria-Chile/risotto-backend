from risotto import db


class Paper(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cord_id = db.Column(db.String(length=256))
    title = db.Column(db.Text)
    abstract = db.Column(db.Text)
