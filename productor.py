from app.i_queue.pickle_queue import QueuePickle
import multiprocessing as mp
import numpy as np

def f() -> None:
    a: list[float] = []
    for i in range(np.random.randint(1000, 2000)):
        a.append(i**i)
    QueuePickle.put(a)


MAX_CPU: int = mp.cpu_count() - 1
process: list[mp.Process] = []


n: int = 0
while True:
    if len(process) < MAX_CPU:
        process.append(mp.Process(target=f))
        process[-1].start()
        n += 1
    
    process2delete: list[int] = []
            
    try:
        for h, i in enumerate(process):
            if not i.is_alive():
                process2delete.append(h)
                i.close()
    except ValueError:
        pass
    
    for i in process2delete:
        process.pop(i)
          
    if n == 100:
        break
      
for i in process:
    i.join()
    i.close()