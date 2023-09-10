def atm_simulator():
    """
    Пример использования банкомата:

    >>> current_balance = 0
    >>> transactions = 0
    >>> exceeded_wealth_tax = False

    >>> def input_mock(prompt):
    ...     # Эмуляция ввода пользователя для тестирования
    ...     print(prompt, end=' ')
    ...     return input()

    >>> def test_atm_operations():
    ...     nonlocal current_balance, transactions, exceeded_wealth_tax
    ...     current_balance = 0
    ...     transactions = 0
    ...     exceeded_wealth_tax = False

    ...     # Тестируем пополнение счета
    ...     test_input = input_mock("1\\n100\\n")
    ...     if test_input == "1":
    ...         deposit_amount = int(input_mock("Введите сумму для пополнения (должна быть кратна 50): "))
    ...         if deposit_amount % 50 == 0:
    ...             current_balance += deposit_amount
    ...             transactions += 1
    ...             if transactions % 3 == 0:
    ...                 deposit_interest = current_balance * 0.03
    ...                 current_balance += deposit_interest

    ...     current_balance  # Проверка текущего баланса после пополнения
    ...     # Ожидаемый результат: 100

    ...     # Тестируем снятие средств
    ...     test_input = input_mock("2\\n60\\n")
    ...     if test_input == "2":
    ...         withdrawal_amount = int(input_mock("Введите сумму для снятия (должна быть кратна 50): "))
    ...         if withdrawal_amount % 50 == 0:
    ...             if exceeded_wealth_tax:
    ...                 current_balance -= current_balance * 0.1
    ...             withdrawal_fee = min(max(30, withdrawal_amount * 0.015), 600)
    ...             if current_balance >= withdrawal_amount + withdrawal_fee:
    ...                 current_balance -= withdrawal_amount + withdrawal_fee
    ...                 transactions += 1
    ...                 if transactions % 3 == 0:
    ...                     deposit_interest = current_balance * 0.03
    ...                     current_balance += deposit_interest

    ...     current_balance  # Проверка текущего баланса после снятия
    ...     # Ожидаемый результат: 40

    >>> test_atm_operations()
    """
    pass

# Запустить тесты
if __name__ == "__main__":
    import doctest
    doctest.testmod()