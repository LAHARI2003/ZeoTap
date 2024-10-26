# backend/tests.py
import unittest
from ast import create_rule, evaluate_rule

class TestRuleEngine(unittest.TestCase):
    def test_create_rule(self):
        rule = "age > 30 AND department = 'Sales'"
        ast = create_rule(rule)
        self.assertIsNotNone(ast)

    def test_evaluate_rule(self):
        rule = "age > 30"
        ast = create_rule(rule)
        data = {"age": 35}
        result = evaluate_rule(ast, data)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
