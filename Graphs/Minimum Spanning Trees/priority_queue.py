from heapq import heapify, heappop, heappush
class priority_queue:
    def __init__(self):
        self.queue = []
        heapify(self.queue)

    def push(self, priority, value):
        heappush(self.queue, (priority, value))

    def pop(self):
        if self.queue:
            return heappop(self.queue)

    def __len__(self):
        return len(self.queue)

    def __str__(self):
        return str(self.queue)

    def __contains__(self, key):
        return key in self.queue