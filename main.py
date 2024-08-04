import argparse
import logging
from mod.model import setup_logging, get_user_input, process_rectangles

if __name__ == "__main__":
    setup_logging()

    parser = argparse.ArgumentParser(description="Работа с прямоугольниками")
    parser.add_argument("--w1", type=int, help="Ширина первого прямоугольника")
    parser.add_argument("--h1", type=int, help="Высота первого прямоугольника (по умолчанию равна ширине)")
    parser.add_argument("--w2", type=int, help="Ширина второго прямоугольника")
    parser.add_argument("--h2", type=int, help="Высота второго прямоугольника (по умолчанию равна ширине)")

    try:
        args = parser.parse_args()

        if args.w1 is None or args.w2 is None:
            print("Не все аргументы командной строки указаны.")
            print(f"-----------------------------------------\nРабота с прямоугольниками:\n-----------------------------------------")
            w1, h1, w2, h2 = get_user_input()
            args.w1 = w1
            args.h1 = h1
            args.w2 = w2
            args.h2 = h2

        process_rectangles(args.w1, args.h1, args.w2, args.h2)
    except SystemExit as e:
        logging.error(f"Ошибка в аргументах командной строки: {e}")
    except ValueError as e:
        logging.error(f"Ошибка ввода от пользователя: {e}")
