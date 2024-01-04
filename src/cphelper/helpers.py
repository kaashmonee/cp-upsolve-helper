import uthelper.helpers as uthelper

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
        lines = input_str.strip().splitlines()
        test_cases = []
        cur_line_num = 1
        while cur_line_num < len(lines):
            test_case: list = []
            for inp_type in self.input_types:
                cur_line: str = lines[cur_line_num]
                if inp_type == SEQ:
                    ints_str = cur_line.strip().split()
                    ints = list(map(lambda s: int(s), ints_str))
                    test_case.append(ints)  # type: ignore
                elif inp_type == INP:
                    test_case.append(int(cur_line))
                elif inp_type == STRNG:
                    stripped: str = cur_line.strip()
                    test_case.append(stripped)  # type: ignore
                elif inp_type == MULF:
                    mulf_result = list(map(float, cur_line.strip().split()))
                    test_case = mulf_result
                elif inp_type == MUL:
                    mul_result = list(map(int, cur_line.strip().split()))
                    test_case = mul_result

                cur_line_num += 1

            test_cases.append(test_case)

        return test_cases

    def test_solution(self, soln, expected_outputs):
        self.expected_outputs = expected_outputs.strip().splitlines()
        if len(self.expected_outputs) != len(self.test_cases):
            raise Exception(
                f"expected number of outputs: {len(expected_outputs)} does not match number of test cases: {len(self.test_cases)}")

        import unittest

        @uthelper.run
        class _(unittest.TestCase):
            def test_function(sself):
                for i in range(len(self.expected_outputs)):
                    test_case = self.test_cases[i]
                    result = str(soln(*test_case))
                    expected = self.expected_outputs[i]
                    sself.assertEqual(result, expected)


def main():
    """
    r = Runner(...) 
    def solution(arg1, arg2, arg3): pass # implementation omitted
    expected_outputs = [...]
    r.test_solution(solution, expected_outputs)
    """
    pass


if __name__ == "__main__":
    main()
