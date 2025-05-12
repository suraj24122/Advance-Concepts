def show_snacks(**kwargs):
    for item, quantity in kwargs.items():
        print(f"I have {quantity} {item}")

show_snacks(cookie=2, juice=1, candy=5)
