import time

class Lights:

    __color = ('red', 'yellow', 'green')

    def running(self):
        print(Lights.__color[0])
        time.sleep(7)
        print(Lights.__color[1])
        time.sleep(2)
        print(Lights.__color[2])
        time.sleep(5)

a = Lights()
print(a.running())
