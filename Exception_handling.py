try:
    num=0
    x=23/num
    print(x)
except ZeroDivisionError as e:
    print(f"error {e}")
except Exception as e:
    print(f"error : {e}")
else:
    print("No error")
finally:
    print("No matter what happens I will go printing myself")