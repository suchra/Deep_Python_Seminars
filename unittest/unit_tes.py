import unittest
from unittest.mock import patch
from io import StringIO

def atm_operation(current_balance, transactions, exceeded_wealth_tax, user_input):
    with patch("builtins.input", side_effect=user_input), patch("sys.stdout", new_callable=StringIO) as mock_output:
        exec(open("your_atm_code.py").read())
    return current_balance, transactions, exceeded_wealth_tax, mock_output.getvalue()

class TestATM(unittest.TestCase):
    def test_deposit_valid_amount(self):
        current_balance, transactions, exceeded_wealth_tax, output = atm_operation(0, 0, False, ["1", "100"])
        self.assertEqual(current_balance, 100)
        self.assertEqual(transactions, 1)
        self.assertEqual(exceeded_wealth_tax, False)
        self.assertIn("Текущая сумма денег: 100", output)

    def test_deposit_invalid_amount(self):
        current_balance, transactions, exceeded_wealth_tax, output = atm_operation(0, 0, False, ["1", "75"])
        self.assertEqual(current_balance, 0)
        self.assertEqual(transactions, 0)
        self.assertEqual(exceeded_wealth_tax, False)
        self.assertIn("Сумма для пополнения должна быть кратна 50!", output)

    def test_withdraw_valid_amount(self):
        current_balance, transactions, exceeded_wealth_tax, output = atm_operation(100, 0, False, ["2", "60"])
        self.assertEqual(current_balance, 40)
        self.assertEqual(transactions, 1)
        self.assertEqual(exceeded_wealth_tax, False)
        self.assertIn("Текущая сумма денег: 40", output)

    def test_withdraw_invalid_amount(self):
        current_balance, transactions, exceeded_wealth_tax, output = atm_operation(100, 0, False, ["2", "45"])
        self.assertEqual(current_balance, 100)
        self.assertEqual(transactions, 0)
        self.assertEqual(exceeded_wealth_tax, False)
        self.assertIn("Сумма для снятия должна быть кратна 50!", output)

    def test_exit(self):
        current_balance, transactions, exceeded_wealth_tax, output = atm_operation(100, 0, False, ["3"])
        self.assertEqual(current_balance, 100)
        self.assertEqual(transactions, 0)
        self.assertEqual(exceeded_wealth_tax, False)
        self.assertIn("Работа с банкоматом завершена.", output)

if __name__ == "__main__":
    unittest.main()