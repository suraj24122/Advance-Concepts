try:
    print(10 / 0)
except:
    print("Error happened!")
finally:
    print("Always runs!")


try:
    x = "hello"
    print(int(x))
except:
    print("Conversion failed.")
finally:
    print("Done trying!")
