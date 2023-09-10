import pytest
from my_atm_code import atm_transaction

@pytest.fixture
def initial_state():
    return 0, 0, False

def test_deposit_valid_amount(initial_state):
    current_balance, transactions, exceeded_wealth_tax = initial_state
    current_balance, transactions, exceeded_wealth_tax = atm_transaction(current_balance, transactions, exceeded_wealth_tax, "1", 100)
    assert current_balance == 100
    assert transactions == 1
    assert exceeded_wealth_tax is False

def test_deposit_invalid_amount(initial_state):
    current_balance, transactions, exceeded_wealth_tax = initial_state
    current_balance, transactions, exceeded_wealth_tax = atm_transaction(current_balance, transactions, exceeded_wealth_tax, "1", 75)
    assert current_balance == 0
    assert transactions == 0
    assert exceeded_wealth_tax is False

def test_withdraw_valid_amount(initial_state):
    current_balance, transactions, exceeded_wealth_tax = initial_state
    current_balance, transactions, exceeded_wealth_tax = atm_transaction(current_balance, transactions, exceeded_wealth_tax, "2", 100)
    assert current_balance == -105
    assert transactions == 1
    assert exceeded_wealth_tax is False

# По аналогии добавьте другие тесты для остальных функций вашего банкомата

if __name__ == "__main__":
    pytest.main()