class Robot:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hello, my name is {self.name}.")


tom = Robot("Tom")
jerry = Robot("Jerry")


tom.introduce()
jerry.introduce()
