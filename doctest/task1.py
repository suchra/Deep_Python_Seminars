current_balance = 0
transactions = 0
exceeded_wealth_tax = False

while True:
    print("Текущая сумма денег:", current_balance)
    print("Выберите действие:")
    print("1. Пополнить")
    print("2. Снять")
    print("3. Выйти")
    choice = input()

    if choice == "1":
        deposit_amount = int(input("Введите сумму для пополнения (должна быть кратна 50): "))
        if deposit_amount % 50 == 0:
            current_balance += deposit_amount
            transactions += 1
            if transactions % 3 == 0:
                deposit_interest = current_balance * 0.03
                current_balance += deposit_interest
        else:
            print("Сумма для пополнения должна быть кратна 50!")
    elif choice == "2":
        withdrawal_amount = int(input("Введите сумму для снятия (должна быть кратна 50): "))
        if withdrawal_amount % 50 == 0:
            if exceeded_wealth_tax:
                current_balance -= current_balance * 0.1
            withdrawal_fee = min(max(30, withdrawal_amount * 0.015), 600)
            if current_balance >= withdrawal_amount + withdrawal_fee:
                current_balance -= withdrawal_amount + withdrawal_fee
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
        break
    else:
        print("Некорректный выбор действия. Пожалуйста, выберите снова.")

    if current_balance >= 5000000:
        exceeded_wealth_tax = True
    else:
        exceeded_wealth_tax = False