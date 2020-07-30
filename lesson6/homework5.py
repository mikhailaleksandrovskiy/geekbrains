class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        return f"Запуск отрисовки {self.title}"

class Pen(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f"Запуск отрисовки {self.title} ручкой"

class Pencil(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f"Запуск отрисовки {self.title} карандашом"

class Handle(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f"Запуск отрисовки {self.title} маркером"


a = Stationery('TEST')
b = Pen('TEST')
c = Pencil('TEST')
d = Handle('TEST')
print(a.draw())
print(b.draw())
print(c.draw())
print(d.draw())
