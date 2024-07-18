# +--------------------------------------------------------------------------------------------------------------------|
# |                                                                                         app/i_queue/pickle_queue.py|
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
import pickle
import os

from uuid           import uuid4
from datetime       import datetime
from pathlib        import Path

from app.manager.directories    import DirManager
from app.config.vars            import ConfigPath, ConfigQueue

from typing import Any
# |--------------------------------------------------------------------------------------------------------------------|

class QueueController(object):
    def __init__(self) -> None:
        self.filename_list  : list[str]     = []
        self.timestamp_list : list[float]   = []
        self.filename2remove: list[str]     = []
    
    def _update_filename_list(self) -> None:
        self.filename_list: list[str] = os.listdir(ConfigPath.BINQUEUE)
        for i in self.filename2remove:
            self.filename_list.remove(i)
        
    def _create_timestamp_list(self) -> None:
        self.timestamp_list: list[float] = []
        for i in self.filename_list:
            _timestamp, _ = i.split("|")
            self.timestamp_list.append(float(_timestamp.replace("_", ".")))
    
    def _update_queue_files(self) -> None:
        self._update_filename_list()
        self._create_timestamp_list()
    
    def _remove_from_instance(self, index: int) -> None:
        self.filename2remove.append(self.filename_list[index])
        self.filename_list.pop(index)
        self.timestamp_list.pop(index)
    
    def _get_first_filename(self) -> str:
        try:
            min_index: int = self.timestamp_list.index(min(self.timestamp_list))
        except ValueError:
            return "empty queue"
        
        file2read: str = self.filename_list[min_index]
        self._remove_from_instance(min_index)
        
        return file2read


class QueuePickle(DirManager, QueueController):
    def __init__(self) -> None:
        self.binqueue_dir_create()
        super().__init__()
    
    @staticmethod
    def put(object: Any) -> None:
        now     : list[str] = str(datetime.now().timestamp()).split(".")
        filename: str = f"{now[0]}_{now[1]}|{str(uuid4())}{ConfigQueue.EXTENSION}"
        
        with open(Path(ConfigPath.BINQUEUE, filename), "wb") as f:
            pickle.dump(object, f)
    
    def init_read_queue(self) -> None:
        self._update_queue_files()
    
    def get(self) -> Any:
        file: str = self._get_first_filename()
        if file == "empty queue":
            return file
        
        if os.path.getsize(Path(ConfigPath.BINQUEUE, file)) > 0:
            with open(Path(ConfigPath.BINQUEUE, file), "rb") as f:
                unpickler = pickle.Unpickler(f)
                a: Any = unpickler.load()
            return a

        return [0]
    
    def get_and_update(self) -> Any:
        self._update_queue_files()
        return self.get()

    def clear(self) -> None:
        for i in self.filename2remove:
            os.remove(Path(ConfigPath.BINQUEUE, i))
        self.filename2remove: list[str] = []
    
    def end_queue(self) -> None:
        self.clear()
        filenames: list[str] = os.listdir(ConfigPath.BINQUEUE)
        for i in filenames:
            os.remove(Path(ConfigPath.BINQUEUE, i))
        
        self.filename_list: list[str]       = []
        self.timestamp_list: list[float]    = []
        self.filename2remove: list[str]     = []