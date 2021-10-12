def name_of_oldest(names, ages):
    oldest_pos = ages.index(max(ages))
    return names[oldest_pos]


names = ["Cue Nguyen", "Hellene Clinton", "Sarah Edison"]
ages = [40, 55, 20]

print(name_of_oldest(names, ages))
