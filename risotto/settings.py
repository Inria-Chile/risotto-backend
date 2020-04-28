import os

SQLALCHEMY_DATABASE_URI = "sqlite:///example.sqlite"
SQLALCHEMY_TRACK_MODIFICATIONS = False


def freeze():
    return {k: v for k, v in globals().items() if k.isupper()}
