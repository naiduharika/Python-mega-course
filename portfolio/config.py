import os
from dotenv import load_dotenv


class ConfigGetter(dict):
    def __getattr__(self, attr):
        try:
            return self[attr]
        except KeyError as ke:
            raise AttributeError(f"Config has no '{ke.args[0]}'")

    def __setattr__(self, attr, value):
        self[attr] = value


class Config(ConfigGetter):
    project_folder = os.path.abspath(".")
    load_dotenv(os.path.join(project_folder, '.env'))

    def __init__(self):
        super().__init__({})
        self.host = os.getenv("EMAIL_HOST")
        self.port = os.getenv("PORT")
        self.username = os.getenv("USERNAME")
        self.password = os.getenv("PASSWORD")
