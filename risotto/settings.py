import os

SQLALCHEMY_DATABASE_URI = "sqlite:///db.sqlite"
SQLALCHEMY_TRACK_MODIFICATIONS = False

ARTIFACTS_PATH = os.environ.get("ARTIFACTS_PATH", "./artifacts/artifacts.hdf")


def freeze():
    return {k: v for k, v in globals().items() if k.isupper()}
