import pandas as pd


def load_artifacts(app):
    artifacts_path = app.config["ARTIFACTS_PATH"]

    class _RisottoArtifacts:
        def __init__(self):
            self._bare_papers_artifact: pd.DataFrame = pd.read_hdf(
                artifacts_path, key="papers"
            ).fillna("N/A")
            self._papers_topics_artifact: pd.DataFrame = pd.read_hdf(
                artifacts_path, key="papers_topics"
            )
            self.papers_artifact: pd.DataFrame = self._bare_papers_artifact.join(
                self._papers_topics_artifact
            )
            self.topics_artifact: pd.DataFrame = pd.read_hdf(
                artifacts_path, key="topics"
            )

    app._artifacts = _RisottoArtifacts()
