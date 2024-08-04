import logging
from .exceptions import NegativeValueError


class Rectangle:
    def __init__(self, width, height=None):
        self.width = width
        self.height = height if height is not None else width
        logging.info(f"Создан {str(self).lower()}")

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value < 0:
            logging.error(f"Попытка установить отрицательную ширину: {value}")
            raise NegativeValueError(f"Ширина должна быть положительной, а не {value}")
        self._width = value
        logging.info(f"Установлена ширина: {value}")

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value < 0:
            logging.error(f"Попытка установить отрицательную высоту: {value}")
            raise NegativeValueError(f"Высота должна быть положительной, а не {value}")
        self._height = value
        logging.info(f"Установлена высота: {value}")

    def perimeter(self):
        perimeter = 2 * (self.width + self.height)
        logging.info(f"Периметр {self.name_self()} = {perimeter}")
        return perimeter

    def area(self):
        area = self.width * self.height
        logging.info(f"Площадь {self.name_self()} = {area}")
        return area

    def __add__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        new_width = self.width + other.width
        new_height = self.height + other.height
        logging.info(
            f"Сложение {str(self).lower()} и {str(other).lower()}: новый прямоугольник с шириной {new_width} и высотой {new_height}")
        return Rectangle(new_width, new_height)

    def __sub__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        new_width = abs(self.width - other.width)
        new_height = abs(self.height - other.height)
        logging.info(
            f"Вычитание {str(self).lower()} и {str(other).lower()}: новый прямоугольник с шириной {new_width} и высотой {new_height}")
        return Rectangle(new_width, new_height)

    def __lt__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        result = self.area() < other.area()
        logging.info(f"Сравнение {str(self).lower()} < {str(other).lower()}: {result}")
        return result

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        result = self.area() == other.area()
        logging.info(f"Сравнение {str(self).lower()} == {str(other).lower()}: {result}")
        return result

    def __le__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        result = self.area() > other.area()
        logging.info(f"Сравнение {str(self).lower()} > {str(other).lower()}: {result}")
        return result

    def __str__(self):
        return f"Прямоугольник со сторонами {self.width} и {self.height}"

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def name_self(self):
        lst = str(self).lower().split()
        lst[0] += 'а'
        return ' '.join(lst)
