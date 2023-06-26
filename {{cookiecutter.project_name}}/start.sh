#!/bin/bash
# Use this script to start the application with hot reload during local
# development.
APP_ENV=dev uvicorn main:app --port 44777 --reload --log-level info
