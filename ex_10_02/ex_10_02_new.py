""" 10.2 Write a program to read through the mbox-short.txt and figure
out the distribution by hour of the day for each of the messages.
You can pull the hour out from the 'From ' line by finding the time
and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the
counts, sorted by hour as shown below. """

fname = input("Enter file name: ")                 # prompts user for file name
# guardian/conditional statement to avoid absurd filenames
if len(fname) < 1:                                 # if absurd filename taken as input
    fname = "mbox-short.txt"                       # considers filename as "mbox-short.txt"
else:                                              # else if proper filename taken as input
    try:                                           # tries to open the file
        fhand = open(fname)                        # opens the file chosen by user
    except FileNotFoundError:                      # catches exception if no such file is found
        print('File', fname, 'is not found')       # displays error message
        quit()                                     # quits the program

hour_dict = dict()                                 # creates an empty dictionary to store the hour value and its count
tuple_list = list()                                # creates an empty list to store sorted (key, value) tuples
for line in fhand:                                 # hovering through the lines in the file handler
    if line.startswith('From '):                   # if line starts with 'From ' element
        line = line.split()                        # splits the line into a list of words
        time = line[5]                             # the fifth element of word-list represents the time
        time_list = time.split(':')                # splits the time into hour, minute and second & stores in a list
        hour_list = list(time_list[:1])            # slices out the hour-head out of the time-list & stores in hour-list
        for hour in hour_list:                     # hovering through the hour values in hour-list
            hour_dict[hour] = hour_dict.get(hour, 0) + 1
# increments the count of an 'hour' value if it is already present in the dict()
# else if the 'hour' value absent in the dict(), add it to the dict()
# '0' is the default count if no such 'hour' value is present in the dict()

for key, value in sorted(hour_dict.items()):       # hovering through (key, value) pair sorted tuple of (hour, count)
    new_tuple = (int(key), value)                  # converts (str)key to (int)key & stores it in a new tuple with count
    tuple_list.append(new_tuple)                   # adds each new tuples to the tuple-list as sorted (key, value) pair
    print(key, value)                              # displays the hour distribution in a sorted way
