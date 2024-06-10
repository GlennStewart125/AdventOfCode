from hashlib import md5


def main():
    key: str = "bgvyzdsv"
    findHex(key, 5)
    findHex(key, 6)


def findHex(key: str, length: int):
    number: int = 0
    while True:
        hash_result = md5(str.encode(key + str(number)))
        hexadecimal_str: str = hash_result.hexdigest()

        if hexadecimal_str[:length] == "0" * length:
            print(number)
            break

        number += 1


if __name__ == "__main__":
    main()
