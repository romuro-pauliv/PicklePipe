# +--------------------------------------------------------------------------------------------------------------------|
# |                                                                                         app/i_queue/pickle_queue.py|
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
import pickle
from uuid           import uuid4
from datetime       import datetime
from pathlib        import Path

from manager.directories    import DirManager
from config.vars            import ConfigPath, ConfigQueue

from typing import Any
# |--------------------------------------------------------------------------------------------------------------------|


class QueuePickle(DirManager):
    def __init__(self) -> None:
        self.binqueue_dir_create()
    
    @staticmethod
    def put(object: Any) -> None:
        now     : list[str] = str(datetime.now().timestamp()).split(".")
        filename: str = f"{now[0]}_{now[1]}|{str(uuid4())}{ConfigQueue.EXTENSION}"
        
        with open (Path(ConfigPath.BINQUEUE, filename), "wb") as f:
            pickle.dump(object, f)
    
    