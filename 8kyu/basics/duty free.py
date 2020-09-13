def duty_free(price, discount, holiday_cost):
    savings = ((price * 100) * discount) / 10000
    print(savings)
    return int(holiday_cost // savings)


print(duty_free(12, 50, 1000))  # , 166)
print(duty_free(17, 10, 500))  # , 294)
