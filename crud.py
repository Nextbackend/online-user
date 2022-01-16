import time


class ListOperation():
    def __init__(self):
        self.list = []
        self.start = time.time()

    def add(self, id):
        self.list.append(id)

    def clear2(self):
        while True:
            print(len(self.list))
            user_set=set(self.list)
            print(len(user_set))
            self.list.clear()
            self.start = time.time()
            print("---list cleared---")

            time.sleep(5)


# l = ListOperation()
# l.add('1')
# print(l.list)
# l.clear()
# l.add('1222')
# print(l.list)
