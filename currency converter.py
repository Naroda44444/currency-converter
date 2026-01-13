RATES = {
    "EUR": 0.025,
    "USD": 0.027
}

print("вітаємо у конвертері валют!💰💰💰")

try:

    uah_amount_str = input("Введіть суму в гривнях (🪙UAH): ")
    uah_amount = float(uah_amount_str)

    if uah_amount < 0:

        raise ValueError("Сума не може бути від'ємною❌❌❌.")
    
    currency = input("Введіть валюту для конвертації (🪙🪙🪙   EUR або USD): ").upper()

    rate = RATES[currency]
    converted_amount = uah_amount * rate


    print(f"{uah_amount} гривень - це **{converted_amount:.2f} {currency}**💵💵💵.")
except ValueError as e:
    print(f"Помилка введення: {e}😡😡😡.")
except KeyError:
    print("Помилка: Невідома валюта. Будь ласка, виберіть EUR або USD😡😡😡.")