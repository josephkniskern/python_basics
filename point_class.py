class Point:
    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 2)
second_point = Point(1, 2)
point.draw()
print(point == second_point)
combined_points = point + second_point
print(combined_points.x, combined_points.y)
