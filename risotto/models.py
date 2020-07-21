import pandas as pd
from typing import Optional, List
from flask import current_app

from risotto import db


class Paper(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cord_id = db.Column(db.String(length=256))
    title = db.Column(db.Text)
    abstract = db.Column(db.Text)

    # TODO: join DFs
    @staticmethod
    def all() -> pd.DataFrame:
        # all_papers = current_app._artifacts.papers_artifact.to_json(orient="records")
        all_papers = current_app._artifacts.papers_artifact
        return all_papers

    @staticmethod
    def filter(
        papers: pd.DataFrame,
        topic: Optional[str],
        subtopic: Optional[str],
        search: Optional[str],
    ) -> pd.DataFrame:
        if topic is not None:
            topic_mask = papers["topic"] == int(topic)
            papers = papers[topic_mask]
        if subtopic is not None:
            subtopic_mask = papers["subtopic"] == int(subtopic)
            papers = papers[subtopic_mask]
        if search is not None and len(search) > 0:
            search_mask = (
                (papers["title"] + papers["abstract"]).str.lower().str.contains(search)
            )
            papers = papers[search_mask]
        return papers
