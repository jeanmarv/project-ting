class Queue:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        return self._data.append(value)

    def dequeue(self):
        return self._data.pop(0)

    def search(self, index):
        if index < 0 or index > self.__len__():
            raise IndexError
        return self._data[index]
