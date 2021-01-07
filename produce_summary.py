
# defining fuction to do formatting
def melon_report(file):
    """formats text file"""

    # for each line of text, strip the right spaces and split the string into a list based on the | separator
    for line in the_file:
        line = line.rstrip()
        words = line.split('|')

        # sets variables melon, count, list equal to correct references in list words
        melon = words[0]
        count = words[1]
        amount = words[2]

        # prints formatted text then closes file
        print(f"Delivered {count} {melon}s for total of ${amount}")
    the_file.close()

# prints the day as a heading, sets the_file equal to the corresponding txt file, then calls melon_report
print("Day 1")
the_file = open("um-deliveries-20140519.txt")
melon_report(the_file)

print("Day 2")
the_file = open("um-deliveries-20140520.txt")
melon_report(the_file)

print("Day 3")
the_file = open("um-deliveries-20140521.txt")
melon_report(the_file)
