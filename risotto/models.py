from collections import defaultdict
from typing import Optional, List, Tuple, DefaultDict

import pandas as pd
from flask import current_app


class Paper:
    @staticmethod
    def all() -> pd.DataFrame:
        all_papers = current_app._artifacts.papers_artifact
        return all_papers

    @staticmethod
    def filter(
        papers: pd.DataFrame, topic: str, subtopic: str, search: str,
    ) -> pd.DataFrame:
        if len(topic) > 0:
            topic_mask = papers["topic"] == int(topic)
            papers = papers[topic_mask]
        if len(subtopic) > 0:
            subtopic = subtopic.split("-")[1]
            subtopic_mask = papers["subtopic"] == int(subtopic)
            papers = papers[subtopic_mask]
        if len(search) > 0:
            search_mask = (
                (papers["title"] + papers["abstract"])
                .str.lower()
                .str.contains(search, regex=False)
            )
            papers = papers[search_mask]
        return papers

    @staticmethod
    def sort(papers: pd.DataFrame, by: str, ascending: bool) -> pd.DataFrame:
        return papers.sort_values(by=by, ascending=ascending)


class Topic:

    TOKENS_PER_TOPIC = 5

    @classmethod
    def all(
        cls,
    ) -> Tuple[List[Tuple[str, str]], DefaultDict[str, List[Tuple[str, str]]]]:
        topics_df = current_app._artifacts.topics_artifact
        topics, subtopics = cls._get_topics(topics_df)
        return topics, subtopics

    @classmethod
    def _get_topics(
        cls, topics_artifact: pd.DataFrame
    ) -> Tuple[List[Tuple[str, str]], DefaultDict[str, List[Tuple[str, str]]]]:
        """
        Args:
            - topics_artifact: a Pandas DataFrame with the tokens pesudocounts
                of the each topic and subtopic.
        Returns:
            - topics: list of tuples. Each tuple's first and second elements are
                the topic's readable name and identifier, respectively.
            - subtopics: dictionary with topic ids as key and list of tuples as
                values. Each tuple's first and second elements are
                the subtopic's readable name and identifier, respectively.
        """
        topics = []
        subtopics = defaultdict(list)
        for col_name in topics_artifact.columns:
            if "-" not in col_name:
                topics.append(
                    (cls._get_dropdown_name(topics_artifact[col_name]), str(col_name))
                )
            else:
                topic_id = str(col_name.split("-")[0])
                subtopics[topic_id].append(
                    (cls._get_dropdown_name(topics_artifact[col_name]), str(col_name))
                )
        return topics, subtopics

    @classmethod
    def _get_dropdown_name(cls, series: pd.Series) -> str:
        """
        Args:
            - series: a Pandas Series with the tokens pseudocounts of a topic
                or subtopic
        Returns:
            - str: a readable name of the topic or subtopic
        """
        prefix = f"#{series.name}"
        most_relevant = ", ".join(
            map(str, series.sort_values(ascending=False).index[: cls.TOKENS_PER_TOPIC])
        )
        return f"{prefix} ({most_relevant})"
