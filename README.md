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

