#!/usr/bin/env bash

# Run gunicorn prodcution server
gunicorn "risotto:create_app()"