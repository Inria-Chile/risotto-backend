#!/usr/bin/env bash

# Run gunicorn prodcution server
gunicorn -b :$PORT "risotto:create_app()"