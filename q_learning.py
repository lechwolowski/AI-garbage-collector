# import tensorflow as tf
# print(tf.version)


class Q_Learning:
    def __init__(self, gc):
        super().__init__()
        self.gc = gc

    def mixed(self): return self.gc.mixed
    def paper(self): return self.gc.paper
    def glass(self): return self.gc.glass
    def plastic(self): return self.gc.plastic


a = 5


def b(): return a


print(b())
a = 6
print(b())
