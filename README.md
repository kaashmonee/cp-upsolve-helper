# cp-upsolve-helper

## Usage
```bash
pip install .
```

```python
import uthelper.helpers as helper
import unittest

@helper.run
class TestClass(unittest.TestCase):
    def test_example(self):
        self.assertEqual(True, True)

class TestClassDoesntRun(unittest.TestCase):
    def test_example_doesnt_run(self):
        self.assertEqual(True, False)
```

### defining custom solution function and testing

```python
import cphelper.helpers as cphelper

inp_str = """
8
2 3
1 2
3 11
1 5
5 10
4 6
3 9
250000000 500000000
"""

expected_output = """
6
4
33
25
20
12
27
1000000000
"""

r = cphelper.Runner(inp_str, [cphelper.MUL])


def solution(a, b):
    if a == 2 and b == 3:
        return 6
    return 0

r.test_solution(solution, expected_output)

```

