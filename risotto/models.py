import pandas as pd
from flask import current_app

from risotto import db


class Paper(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cord_id = db.Column(db.String(length=256))
    title = db.Column(db.Text)
    abstract = db.Column(db.Text)

    @staticmethod
    def all() -> pd.DataFrame:
        # all_papers = current_app._artifacts.papers_artifact.to_json(orient="records")
        all_papers = current_app._artifacts.papers_artifact
        return all_papers
