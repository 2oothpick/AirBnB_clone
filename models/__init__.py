#!/usr/bin/python3
"""
create a unique FileStorage instance for your application.
"""


from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
