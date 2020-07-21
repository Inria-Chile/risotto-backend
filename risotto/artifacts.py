from dataclasses import dataclass

import pandas as pd


def load_artifacts(app):
    artifacts_path = app.config["ARTIFACTS_PATH"]

    @dataclass
    class _RisottoArtifacts:
        papers_artifact: pd.DataFrame = pd.read_hdf(artifacts_path, key="papers")
        papers_topics_artifact: pd.DataFrame = pd.read_hdf(
            artifacts_path, key="papers_topics"
        )
        topics_artifact: pd.DataFrame = pd.read_hdf(artifacts_path, key="topics")

    app._artifacts = _RisottoArtifacts()
