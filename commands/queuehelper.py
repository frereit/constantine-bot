class QueueHelper:
    def __init__(self):
        self.queue = []  # We want the queue to be shared by all QueueHelper Objects
        self.nowplaying = None

    def __len__(self):
        return len(self.queue)

    def append(self , item):
        self.queue.append(item)

    def pop(self , index):
        return self.queue.pop(index)
