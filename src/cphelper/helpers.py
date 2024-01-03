
SEQ = "seq"
MUL = "mul"
INP = "inp"
STRNG = "strng"
MULF = "mulf"

_inp_type = {SEQ, MUL, INP, STRNG, MULF}


class Runner:
    def __init__(self, inp_str: str, input_types: list[str]):
        for t in input_types:
            if t not in _inp_type:
                raise Exception(f"{t} not in valid input types: {_inp_type}")

        self.input_types = input_types
        self.test_cases = self._read_input(inp_str)

    def _read_input(self, input_str: str):
        lines = input_str.splitlines()
        self.test_cases = []
        cur_line_num = 1
        test_case = []
        while cur_line_num < len(lines):
            for inp_type in self.input_types:
                cur_line = lines[cur_line_num]
                if inp_type == SEQ:
                    ints_str = cur_line.strip().split()
                    ints = list(map(lambda s: int(s), ints_str))
                    test_case.append(ints)
                elif inp_type == INP:
                    test_case.append(int(cur_line))
                elif inp_type == STRNG:
                    test_case.append(cur_line.strip())
                elif inp_type == MULF:
                    mulf_result = list(map(float, cur_line.strip().split()))
                    test_case.append(mulf_result)
                elif inp_type == MUL:
                    mul_result = map(int, cur_line.strip().split())
                    test_case.append(mul_result)

                cur_line += 1

    def test_solution(self, soln, expected_outputs):
        if len(expected_outputs) != len(self.test_cases):
            raise Exception(
                "expected number of outputs does not match number of test cases")

        for i in range(len(expected_outputs)):
            test_case = self.test_cases[i]
            result = soln(*test_case)
            print(result)


def main():
    Runner("something", [SEQ])


if __name__ == "__main__":
    main()
