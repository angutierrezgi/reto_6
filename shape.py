import math

class Point():
    definition: str = "Entidad geometrica abstracta que representa una ubicación en un espacio."
    def __init__(self, x: float=0, y: float=0):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x
    @x.setter
    def x(self, new_x):
        self._x = new_x

    @property
    def y(self):
        return self._y
    @y.setter
    def y(self, new_y):
        self._y = new_y
    
    def reset(self):
        self.x = 0
        self.y = 0
    def compute_distance(self, point: "Point")-> float:
        distance = ((self.x - point.x)**2+(self.y - point.y)**2)**(0.5)
        return distance
    def __repr__(self):
        return f"({self.x},{self.y})"
    
class Line():
    def __init__(self, start_point: Point, end_point: Point):
        self._start: Point = start_point
        self._end: Point = end_point
        self._length: float = start_point.compute_distance(end_point)
        self._slope: float = self.compute_slope()

    @property
    def start(self):
        return self._start
    @property
    def y(self):
        return self._y
    
    def compute_length(self) -> float:
        return self._length
    def compute_slope(self) -> float:
        slope: float = None
        if self._end.x - self._start.x == 0:
            slope = None
            return slope
        else:
            slope = (self._end.y - self._start.y) / (self._end.x - self._start.x)
            return round(slope, 3)
    def compute_horizontal_cross(self) -> bool:
        x_intersect: bool = False
        if self._start.y >= 0 and self._end.y <= 0:
            x_intersect = True
        elif self._start.y <= 0 and self._end.y >= 0:
            x_intersect = True
        return x_intersect
    def compute_vertical_cross(self) -> bool:
        y_intersect: bool = False
        if self._start.x >= 0 and self._end.x <= 0:
            y_intersect = True
        elif self._start.x <= 0 and self._end.x >= 0:
            y_intersect = True
        return y_intersect
    def discretize_line(self, n : int) -> list:
        i: int = 0
        points: list = []
        while(i < n):
            aux_x = self._start.x + ((i / (n - 1)) * (self._end.x - self._start.x))
            aux_y = self._start.y + ((i / (n - 1)) * (self._end.y - self._start.y))
            points.append(Point(round(aux_x, 3),round(aux_y, 3)))
            i += 1
        return points
    def __str__(self):
        result: list = [
            f"Start: {self._start}",
            f"End: {self._end}",
            f"Length: {self.compute_length()}",
            f"Slope: {self.compute_slope()}",
            f"Cross x-axis: {self.compute_horizontal_cross()}",
            f"Cross y-axis: {self.compute_vertical_cross()}"
        ]
        return "\n".join(result)

class Shape():
    def __init__(self, vertices: list, edges: list):
        self._vertices: list = vertices
        self._edges: list = edges
        self._inner_angles: list = self.compute_inner_angles()
        self.is_regular: bool = False
    def compute_inner_angles(self) -> list:
        angles: list = []
        n_verts = len(self._vertices)
        for i in range(n_verts):
            prev_vert = self._vertices[i - 1]
            midl_vert = self._vertices[i]
            next_vert = self._vertices[(i + 1) % n_verts]

            v = [prev_vert.x - midl_vert.x, prev_vert.y - midl_vert.y]
            u = [next_vert.x - midl_vert.x, next_vert.y - midl_vert.y]

            dot_prod = v[0] * u[0] + v[1] * u[1]
            norm_v = ((v[0] * v[0]) + (v[1] * v[1])) ** 0.5
            norm_u = ((u[0] * u[0]) + (u[1] * u[1])) ** 0.5

            cos_angle = dot_prod / (norm_u * norm_v)
            cos_angle = max(-1.0, min(1.0, cos_angle))
            angle_rad = math.acos(cos_angle)
            angle_deg = math.degrees(angle_rad)

            angles.append(round(angle_deg, 3))
        return angles
    def compute_area():
        raise NotImplementedError("Must be implemented in subclass!!")
    def compute_perimeter():
        raise NotImplementedError("Must be implemented in subclass!!")

class Rectangle(Shape):
    def __init__(self, vertices: list, edges: list):
        super().__init__(vertices, edges)
        self.width: float = self._edges[0].compute_length()
        self.height: float = self._edges[1].compute_length()
        if self.width == self.height:
            self.is_regular: bool = True
        else:
            self.is_regular: bool = False
    def compute_area(self) -> float:
        return self.width * self.height
    def compute_perimeter(self) -> float:
        return 2*self.width + 2*self.height
    def __str__(self):
        result: list = [
            f"Vertices: {self._vertices}",
            f"Inner Angles: {self._inner_angles}",
            f"Width: {self.width}",
            f"Height: {self.height}",
            f"Regular Shape: {self.is_regular}",
            f"Area: {self.compute_area()}",
            f"Perimeter: {self.compute_perimeter()}"
        ]
        return "\n".join(result)  
      
class Square(Rectangle):
    def __init__(self, vertices: list, edges: list):
        super().__init__(vertices, edges)
        # Here for the Square class, it checks if both side lenghts are the same
        # and if they're not, it raises a ValueError between the sides and
        # prevents the square object from being built
        if not (self._edges[0].compute_length() == self._edges[1].compute_length()):
            raise ValueError("Not a Square")
        self.side_length: float = self._edges[0].compute_length()
        self.is_regular: bool = True
    def compute_area(self) -> float:
        return self.side_length ** 2
    def compute_perimeter(self) -> float:
        return 4 * self.side_length
    def __str__(self):
        result: list = [
            f"Vertices: {self._vertices}",
            f"Inner Angles: {self._inner_angles}",
            f"Side Length: {self.side_length}",
            f"Regular Shape: {self.is_regular}",
            f"Area: {self.compute_area()}",
            f"Perimeter: {self.compute_perimeter()}"
        ]
        return "\n".join(result)  
    
class Triangle(Shape):
    def __init__(self, vertices: list, edges: list):
        super().__init__(vertices, edges)
        self._a: float = self._edges[0].compute_length()
        self._b: float = self._edges[1].compute_length()
        self._c: float = self._edges[2].compute_length()
        if math.isclose(self._a, self._b) and math.isclose(self._b, self._c):
            self.is_regular: bool = True
        else:
            self.is_regular: bool = False
    def compute_perimeter(self):
        perimeter: float = self._a + self._b + self._c
        return round(perimeter, 3)
    def compute_area(self) -> float:
        s: float = self.compute_perimeter() / 2
        area : float = (s * (s - self._a) * (s - self._b) * (s - self._c)) ** 0.5
        return round(area, 3)
    def __str__(self):
        result: list = [
            f"Vertices: {self._vertices}",
            f"Inner Angles: {self._inner_angles}",
            f"Regular Shape: {self.is_regular}",
            f"Area: {self.compute_area()}",
            f"Perimeter: {self.compute_perimeter()}"
        ]
        return "\n".join(result)  
    
class Isosceles(Triangle):
    def __init__(self, vertices: list, edges: list):
        super().__init__(vertices, edges)
        # Similarly to the Square class, it checks if any two sides are the same
        # length, and if they're not it prevents the Isosceles triangle to instance
        if not (math.isclose(self._a, self._b) or math.isclose(self._b, self._c) or math.isclose(self._a, self._c)):
            raise ValueError("Not an Isosceles triangle!!")
    def compute_perimeter(self):
        return super().compute_perimeter()
    def compute_area(self):
        return super().compute_area()
    def __str__(self):
        return super().__str__()
    
class Equilateral(Triangle):
    def __init__(self, vertices: list, edges: list):
        super().__init__(vertices, edges)
        self.is_regular: bool = True
        # Here it's more rigorous and checks if every side is the same length,
        # when it doesn't ocurr, then it doesn't create an instance of class Equilateral
        if not (math.isclose(self._a, self._b) and math.isclose(self._b, self._c)):
            raise ValueError("Not an Equilateral triangle!!")
    def compute_perimeter(self):
        return super().compute_perimeter()
    def compute_area(self):
        return super().compute_area()
    def __str__(self):
        return super().__str__()
    
class Scalene(Triangle):
    def __init__(self, vertices: list, edges: list):
        super().__init__(vertices, edges)
        # Here it checks that every side length is different from each other
        # and once again, if not, it prevents the instance of Scalene
        if math.isclose(self._a, self._b) or math.isclose(self._b, self._c) or math.isclose(self._a, self._c):
            raise ValueError("Not an Scalene triangle!!")
    def compute_perimeter(self):
        return super().compute_perimeter()
    def compute_area(self):
        return super().compute_area()
    def __str__(self):
        return super().__str__()
    
class TriRectangle(Triangle):
    def __init__(self, vertices:list, edges: list):
        super().__init__(vertices, edges)
        # Here it instead checks if any angle on its list is  90 degrees,
        # and whether it isn't, it does not instance TriRectangle
        if not any(math.isclose(angle, 90.0) for angle in self._inner_angles):
            raise ValueError("Not a Right Triangle!!")
    def compute_perimeter(self):
        return super().compute_perimeter()
    def compute_area(self):
        return super().compute_area()
    def __str__(self):
        return super().__str__()
