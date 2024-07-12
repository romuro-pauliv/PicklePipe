# +--------------------------------------------------------------------------------------------------------------------|
# |                                                                                         app/i_queue/pickle_queue.py|
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
import pickle
from uuid import uuid4

from manager.directories import DirManager
from config.vars import ConfigPath, ConfigQueue

from typing import Any
# |--------------------------------------------------------------------------------------------------------------------|


class QueuePickle(DirManager):
    def __init__(self) -> None:
        self.binqueue_dir_create()
    
    @staticmethod
    def put(object: Any) -> None:
        filename: str = f"{str(uuid4())}{ConfigQueue.EXTENSION}"
        with open (f"{ConfigPath.BINQUEUE}{filename}", "wb") as f:
            pickle.dump(object, f)
            