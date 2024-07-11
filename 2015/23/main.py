def getValues(file_name: str) -> [int]:
    return [(i.strip().split(' ')) for i in open(file_name, 'r')]


def main() -> None:
    registers: {str: int} = {'a': 0, 'b': 0}
    instructs: [[str]] = getValues("input.txt")

    index: int = 0
    while index < len(instructs):
        print(index)
        index_increment: int = 1
        instruction: [str] = instructs[index]
        match instruction[0]:
            case "hlf":
                registers[instruction[1]] = registers.get(instruction[1]) / 2
            case "tpl":
                registers[instruction[1]] = registers.get(instruction[1]) * 3
            case "inc":
                registers[instruction[1]] += 1
            case "jmp":
                index_increment = int(instruction[1])
            case "jie":
                if registers.get(instruction[1][:1]) % 2 == 0:
                    index_increment = int(instruction[2])
            case "jio":
                if registers.get(instruction[1][:1]) == 1:
                    index_increment = int(instruction[2])

        index += index_increment
    print(registers)


main()