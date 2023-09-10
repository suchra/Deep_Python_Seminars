def atm_transaction(current_balance, transactions, exceeded_wealth_tax, choice, amount=None):
    if choice == "1":
        if amount % 50 == 0:
            current_balance += amount
            transactions += 1
            if transactions % 3 == 0:
                deposit_interest = current_balance * 0.03
                current_balance += deposit_interest
        else:
            print("Сумма для пополнения должна быть кратна 50!")
    elif choice == "2":
        if amount % 50 == 0:
            if exceeded_wealth_tax:
                current_balance -= current_balance * 0.1
            withdrawal_fee = min(max(30, amount * 0.015), 600)
            if current_balance >= amount + withdrawal_fee:
                current_balance -= amount + withdrawal_fee
                transactions += 1
                if transactions % 3 == 0:
                    deposit_interest = current_balance * 0.03
                    current_balance += deposit_interest
            else:
                print("Недостаточно средств для снятия!")
        else:
            print("Сумма для снятия должна быть кратна 50!")
    elif choice == "3":
        print("Работа с банкоматом завершена.")

    if current_balance >= 5000000:
        exceeded_wealth_tax = True

    return current_balance, transactions, exceeded_wealth_tax