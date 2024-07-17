# +--------------------------------------------------------------------------------------------------------------------|
# |                                                                                                     app/__main__.py|
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|

# |--------------------------------------------------------------------------------------------------------------------|

from i_queue.pickle_queue import QueuePickle

q: QueuePickle = QueuePickle()
for i in range(10):
    q.put([i])


import os
from config.vars import ConfigPath
import pickle
from pathlib import Path

filename_list: list[str] = os.listdir(ConfigPath.BINQUEUE)

timestamp_list: list[float] = []
id_list: list[str] = []

for i in filename_list:
    _timestamp, _id = i.split("|")
    timestamp_list.append(float(_timestamp.replace("_", ".")))
    id_list.append(_id.split(".")[0])

def get() -> None:
    min_index: int = timestamp_list.index(min(timestamp_list))
    to_read: str = filename_list[min_index] 
    filename_list.remove(to_read)
    timestamp_list.pop(min_index)
    id_list.pop(min_index)
    
    with open(Path(ConfigPath.BINQUEUE, to_read), "rb") as f:
        print(pickle.load(f))
    

for i in range(10):
    get()