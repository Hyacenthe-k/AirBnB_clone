#!/usr/bin/python3
"""Initializes the models package with a unique FileStorage instance."""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
