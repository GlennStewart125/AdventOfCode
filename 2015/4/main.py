from __future__ import annotations
from hashlib import md5


def main() -> None:
    key: str = "bgvyzdsv"
    findHex(key, 5)
    findHex(key, 6)


def findHex(key: str, length: int) -> int:
    number: int = 0
    while True:
        hash_result = md5(str.encode(key + str(number)))
        hexadecimal_str: str = hash_result.hexdigest()

        if hexadecimal_str[:length] == "0" * length:
            print(number)
            break

        number += 1
    return number


main()
