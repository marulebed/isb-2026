"""
CLI-интерфейс приложения.

Позволяет:
- вычислять HMAC;
- проверять подлинность сообщения.
"""

import argparse

from crypto_engine import build_hmac, check_hmac
from settings import DEFAULT_SECRET


def start_cli() -> None:
    """
    Запускает интерфейс командной строки.
    """

    parser = argparse.ArgumentParser(
        description="Проверка подлинности сообщений через HMAC"
    )

    parser.add_argument(
        "--action",
        choices=["generate", "validate"],
        default="generate",
        help="Режим работы программы",
    )

    parser.add_argument("--message", type=str, help="Текст сообщения")

    parser.add_argument(
        "--key", type=str, default=DEFAULT_SECRET, help="Секретный ключ"
    )

    parser.add_argument("--signature", type=str, help="HMAC для проверки")

    arguments = parser.parse_args()

    try:
        if arguments.action == "generate":
            if not arguments.message:
                print("Ошибка: сообщение отсутствует")
                return

            result = build_hmac(arguments.message, arguments.key)

            print(f"Сообщение: {arguments.message}")
            print(f"HMAC: {result}")

        else:
            if not arguments.message or not arguments.signature:
                print("Ошибка: недостаточно параметров")
                return

            valid = check_hmac(arguments.message, arguments.key, arguments.signature)

            if valid:
                print("Подлинность подтверждена")
            else:
                print("Обнаружено изменение данных")

    except Exception as error:
        print(f"Ошибка: {error}")
