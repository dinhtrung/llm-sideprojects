import unittest

from src.finance_flow.graph import classify_intent


class InputRouterAgentTestCase(unittest.IsolatedAsyncioTestCase):
    def test_something(self):
        intent = classify_intent("Analyze my spending")
        self.assertEqual("analyze_spending", intent)  # add assertion here


if __name__ == '__main__':
    unittest.main()
