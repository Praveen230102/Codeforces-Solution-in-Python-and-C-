s = input()
upper_ = 0
lower_ = 0
for i in s:
    if i.upper() == i:
        upper_ += 1
    else:
        lower_ += 1
if upper_ > lower_:
    print(s.upper())
elif lower_ > upper_:
    print(s.lower())
elif upper_ == lower_:
    print(s.lower())
