import numpy as np

class A:
    def __getitem__(self, item):
        print(repr(item))

if __name__ == "__main__":
    for i in range(1):
        print(i)