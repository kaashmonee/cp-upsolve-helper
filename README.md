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

output: note, passes the first case, fails on the others
```
F
======================================================================
FAIL: test_function (cphelper.helpers.Runner.test_solution.<locals>._.test_function)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/opt/homebrew/anaconda3/lib/python3.11/site-packages/cphelper/helpers.py", line 67, in test_function
    sself.assertEqual(result, expected)
AssertionError: '0' != '4'
- 0
+ 4


----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (failures=1)
```

