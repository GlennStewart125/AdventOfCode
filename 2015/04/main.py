from __future__ import annotations
import hashlib

HASH = hashlib._hashlib.HASH


def main() -> None:
    key: str = "bgvyzdsv"
    find_hex(key, 5)
    find_hex(key, 6)


def find_hex(key: str, length: int) -> int:
    number: int = 0
    while True:
        hash_result: HASH = hashlib.md5(str.encode(key + str(number)))
        hexadecimal_str: str = hash_result.hexdigest()

        if hexadecimal_str[:length] == "0" * length:
            print(number)
            break

        number += 1
    return number


main()
