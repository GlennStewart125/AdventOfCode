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
        calculateSignal(wire)

    result_a: int = signals['a']
    print("a: {}".format(result_a))

    signals.clear()
    signals['b'] = result_a
    for wire in calc.keys():
        calculateSignal(wire)
    print("a: {}".format(signals['a']))


def calculateSignal(wire: str) -> int:
    try:
        return int(wire)
    except ValueError:
        pass

    inputs: [str] = calc[wire]
    if wire not in signals.keys():
        if len(inputs) == 1:
            signals[wire] = calculateSignal(inputs[0])
        else:
            operation: str = inputs[-2]
            match operation:
                case "AND":
                    signals[wire] = calculateSignal(inputs[-1]) & calculateSignal(inputs[-3])
                case "OR":
                    signals[wire] = calculateSignal(inputs[-1]) | calculateSignal(inputs[-3])
                case "LSHIFT":
                    signals[wire] = calculateSignal(inputs[-3]) << calculateSignal(inputs[-1])
                case "RSHIFT":
                    signals[wire] = calculateSignal(inputs[-3]) >> calculateSignal(inputs[-1])
                case "NOT":
                    signals[wire] = ~ calculateSignal(inputs[-1]) & 0xffff

    return signals[wire]


main()
