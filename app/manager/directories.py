# +--------------------------------------------------------------------------------------------------------------------|
# |                                                                                          app/manager/directories.py|
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
import os
import shutil
from pathlib import Path

from app.config.vars import ConfigPath
# |--------------------------------------------------------------------------------------------------------------------|


class DirManager(object):
    @staticmethod
    def binqueue_dir_create() -> None:
        if str(ConfigPath.BINQUEUE).split("/")[-1] not in os.listdir(ConfigPath.QUEUE):
            os.mkdir(ConfigPath.BINQUEUE)
    
    @staticmethod
    def binqueue_dir_delete() -> None:
        try:
            shutil.rmtree(ConfigPath.BINQUEUE)
        except OSError as e:
            print(f"Error: {e.filename} - {e.strerror}")