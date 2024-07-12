# +--------------------------------------------------------------------------------------------------------------------|
# |                                                                                          app/manager/directories.py|
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
import os
import shutil
from pathlib import Path

from config.vars import ConfigPath
# |--------------------------------------------------------------------------------------------------------------------|


class DirManager(object):
    def __init__(self) -> None:
        pass    
        
    def binqueue_dir_create(self) -> None:
        if str(ConfigPath.BINQUEUE).split("/")[-1] not in os.listdir(ConfigPath.QUEUE):
            os.mkdir(ConfigPath.BINQUEUE)
    
    def binqueue_dir_delete(self) -> None:
        try:
            shutil.rmtree(ConfigPath.BINQUEUE)
        except OSError as e:
            print(f"Error: {e.filename} - {e.strerror}")