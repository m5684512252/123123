money = int(input("金额: "))

if money >= 500:
    money = money * 0.8
    print(money)
elif money >= 300:  # 走到这里，暗含 money < 500
    money = money * 0.9
    print(money)
elif money >= 100:  # 走到这里，暗含 money < 300
    money = money * 0.95
    print(money)
else:               # 走到这里，暗含 money < 100
    print(money)