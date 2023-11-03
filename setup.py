transactions = []

def record_transaction():
    transaction_type = input("Loại giao dịch (Thu/Chi): ").strip().lower()
    if transaction_type not in ['thu', 'chi']:
        print("Loại giao dịch không hợp lệ.")
        return

    amount = float(input("Số tiền: "))
    description = input("Mô tả: ")
    
    transactions.append({
        'type': transaction_type,
        'amount': amount,
        'description': description
    })
    
    print(f"Giao dịch {transaction_type}: {amount} VND đã được ghi lại.")

def calculate_balance():
    total_income = sum(transaction['amount'] for transaction in transactions if transaction['type'] == 'thu')
    total_expense = sum(transaction['amount'] for transaction in transactions if transaction['type'] == 'chi')
    balance = total_income - total_expense
    return total_income, total_expense, balance

def main():
    while True:
        print("\nChương trình quản lý thu chi")
        print("1. Ghi giao dịch")
        print("2. Xem tổng thu chi")
        print("3. Kết thúc")
        
        choice = input("Chọn tùy chọn (1/2/3): ")
        
        if choice == "1":
            record_transaction()
        elif choice == "2":
            total_income, total_expense, balance = calculate_balance()
            print(f"Tổng số tiền thu: {total_income} VND")
            print(f"Tổng số tiền chi: {total_expense} VND")
            print(f"Số dư: {balance} VND")
        elif choice == "3":
            break
        else:
            print("Tùy chọn không hợp lệ. Vui lòng chọn lại.")

if __name__ == "__main__":
    main()