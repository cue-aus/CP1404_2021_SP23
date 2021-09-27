valid_input = False
while not valid_input:
    try:
        age = int(input("Age: "))
        valid_input = True
    except ValueError:  # or just  except:
        print("Invalid (not an integer)")
if age % 2:
    print("{} is odd".format(age))
else:
    print("{} is even".format(age))

