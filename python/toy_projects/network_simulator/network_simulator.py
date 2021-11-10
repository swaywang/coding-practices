#simple network simulator
from collections import deque


class NetworkUtil():
    def __init__(self):
        pass

    @staticmethod
    def connect_routers(router1, router2):
        router1.add_neighbor(router2)
        router2.add_neighbor(router1)

class Router():
    def __init__(self, name):
        self._name = name
        self._queue = deque()
        self._neighbors = list()

    def receive(self):
        if not self._queue:
            return None

        name, received_msg = self.get_msg_from_queue()
        print(f"{self.name} reveive msg:{received_msg} from {name}")

    def send(self, msg):
        for neighbor in self.neighbors:
            neighbor.push_msg_into_queue(self, msg)

    @property
    def neighbors(self):
        return self._neighbors

    @property
    def name(self):
        return self._name

    def push_msg_into_queue(self, sender, msg):
        self._queue.append((sender.name, msg))

    def get_msg_from_queue(self):
        if not self._queue:
            return None

        return self._queue.popleft()

    def add_neighbor(self, neighbor):
        self._neighbors.append(neighbor)

    def print_neighbors(self):
        for neighbor in self.neighbors:
            print(neighbor)

    def __repr__(self):
        return f"Router {self.name}"


def main():
    routers = [
        Router("r1"),
        Router("r2"),
        Router("r3"),
    ]

    for router in routers:
        print(router)
    NetworkUtil.connect_routers(routers[0], routers[1])
    NetworkUtil.connect_routers(routers[0], routers[2])
    print(f"r1 neighbors:")
    routers[0].print_neighbors()
    routers[0].send("hello")
    for router in routers[0].neighbors:
        router.receive()

if __name__ == "__main__":
    main()
