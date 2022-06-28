def name_of_oldest(names, ages):  # parallel lists

    oldest_age_pos = ages.index(max(ages))

    return names[oldest_age_pos]











def main():

    names = ['Cue Nguyen', 'Hellene Clinton', 'Sarah Edison']

    ages = [50, 30, 20]

    print(name_of_oldest(names, ages))











# start the program

if __name__ == '__main__':

    main()