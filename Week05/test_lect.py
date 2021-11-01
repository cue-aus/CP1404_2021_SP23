my_dict = {'bill': 3, 'rich': 10}
my_copy_dict = my_dict.copy()
print(my_copy_dict)
print(my_copy_dict.items())
print(my_copy_dict.keys())
print(my_copy_dict.pop('bill'))
print(my_copy_dict)

name_to_age = {"Bill": 21, "Jane": 4, "Jack": 56}
name = input('Enter name: ')
age = int(input('Enter age: '))
name_to_age[name] = age
for key, value in name_to_age.items():
    print("{:10s}-{:10d}".format(key, value))
values = ["a", "b", "c"]
for count, value in enumerate(values):
    print(count, value)
for count, key in enumerate(name_to_age):
    print(count, key)
name_to_age = {"Bill": 17, "Jane": 34, "Jack": 56, "Sven": 13}
result = {name: age for name, age in name_to_age.items() if age < 18}
print(result)
my_subjects = {'CP1401', 'CP1404', 'MA1000'}
your_subjects = {'CP1404', 'MA1008', 'NM1010'}
print(my_subjects - your_subjects)
print(my_subjects | your_subjects)
print(my_subjects & your_subjects)
print(my_subjects ^ your_subjects)