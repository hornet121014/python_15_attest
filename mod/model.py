import logging
from mod.rectangle import Rectangle
from mod.exceptions import NegativeValueError, MissingWidthError


def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[logging.FileHandler("rectangle.log", mode='w', encoding='UTF-8')]
    )


def get_user_input():
    try:
        w1 = int(input("Введите ширину первого прямоугольника: "))
        h1 = input("Введите высоту первого прямоугольника (или оставьте пустым для использования ширины): ")
        h1 = int(h1) if h1 else w1
        print('-----------------------------------------')
        w2 = int(input("Введите ширину второго прямоугольника: "))
        h2 = input("Введите высоту второго прямоугольника (или оставьте пустым для использования ширины): ")
        h2 = int(h2) if h2 else w2
        print('-----------------------------------------')

        return w1, h1, w2, h2
    except ValueError:
        logging.error("Некорректный ввод. Пожалуйста, введите числовые значения.")
        raise


def process_rectangles(w1, h1, w2, h2):
    try:
        rect1 = Rectangle(w1, h1)
        rect2 = Rectangle(w2, h2)

        print(f"Создан {str(rect1).lower()}")
        print(f"Периметр = {rect1.perimeter()}")
        print(f"Площадь  = {rect1.area()}")
        print('-----------------------------------------')

        print(f"Создан {str(rect2).lower()}")
        print(f"Периметр = {rect2.perimeter()}")
        print(f"Площадь  = {rect2.area()}")
        print('-----------------------------------------')

        print(f"Сравнение {str(rect1).lower()} и {str(rect2).lower()}:\n"
              f"    {str(rect1).lower()} <  {str(rect2).lower()} → {rect1 < rect2}\n"
              f"    {str(rect1).lower()} == {str(rect2).lower()} → {rect1 == rect2}\n"
              f"    {str(rect1).lower()} > {str(rect2).lower()} → {rect1 > rect2}")
        print('-----------------------------------------')

        print(f"Сложение {str(rect1).lower()} + {str(rect2).lower()}:")
        rect3 = rect1 + rect2
        print(f"Создан {str(rect3).lower()}")
        print(f"Периметр = {rect3.perimeter()}")
        print(f"Площадь  = {rect3.area()}")
        print('-----------------------------------------')

        print(f"Вычитание {str(rect1).lower()} - {str(rect2).lower()}:")
        rect4 = rect1 - rect2
        print(f"Создан {str(rect4).lower()}")
        print(f"Периметр = {rect4.perimeter()}")
        print(f"Площадь  = {rect4.area()}")
        print('-----------------------------------------')

    except (NegativeValueError, MissingWidthError) as e:
        logging.error(f"Ошибка: {e}")
