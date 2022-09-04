import os


class Paths:
    def get_project_root(self):
        return os.path.abspath(os.curdir)
