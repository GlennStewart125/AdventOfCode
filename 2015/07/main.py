from typing import TextIO

calc: {str: [str]} = {}
signals: {str: int} = {}


def main() -> None:
    file: TextIO
    with open("input.txt", "r") as file:
        line: str
        for line in file:
            (operation, wire_id) = line.split('->')
            calc[wire_id.strip()] = operation.strip().split()

    wire: str
    for wire in calc.keys():
        calculate_signal(wire)

    result_a: int = signals['a']
    print("a: {}".format(result_a))

    signals.clear()
    signals['b'] = result_a
    for wire in calc.keys():
        calculate_signal(wire)
    print("a: {}".format(signals['a']))


def calculate_signal(wire: str) -> int:
    try:
        return int(wire)
    except ValueError:
        pass

    inputs: [str] = calc[wire]
    if wire not in signals.keys():
        if len(inputs) == 1:
            signals[wire] = calculate_signal(inputs[0])
        else:
            operation: str = inputs[-2]
            match operation:
                case "AND":
                    signals[wire] = calculate_signal(inputs[-1]) & calculate_signal(inputs[-3])
                case "OR":
                    signals[wire] = calculate_signal(inputs[-1]) | calculate_signal(inputs[-3])
                case "LSHIFT":
                    signals[wire] = calculate_signal(inputs[-3]) << calculate_signal(inputs[-1])
                case "RSHIFT":
                    signals[wire] = calculate_signal(inputs[-3]) >> calculate_signal(inputs[-1])
                case "NOT":
                    signals[wire] = ~ calculate_signal(inputs[-1]) & 0xffff

    return signals[wire]


main()
