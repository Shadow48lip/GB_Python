import sys

class Parent:
    def __init__(self):
        self.children = []

    def add(self, ch):
        self.children.append(ch)
        ch.parent = self

class Child:
    def __init__(self):
        self.parent = None


p = Parent()

p.add(Child())


print(sys.getrefcount(p))

print(sys.getrefcount(p.children[0]))
