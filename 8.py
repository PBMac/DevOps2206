boom = list(range(1,101))
for i in boom:
    if i % 7 != 0 and "7" not in str(i):
        print(i)
    else:
        print("BOOM")