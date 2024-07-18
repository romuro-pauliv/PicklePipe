from app.i_queue.pickle_queue import QueuePickle

q: QueuePickle = QueuePickle()
q.end_queue()

while True:
    a = q.get_and_update()
    if a != "empty queue":
        print(len(a))