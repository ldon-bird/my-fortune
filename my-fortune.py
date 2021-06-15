import random

fortune_file = open("./fortune.txt")
fortune_lines= fortune_file.readlines()

# Count the lines of the fortune file ##
#line_counter = 0
#for fortune_line in fortune_file:
#	line_counter += 1

line_counter = len(fortune_lines)
#print(line_counter)

print(fortune_lines[random.randint(0, line_counter-1)], end = '')

fortune_file.close()

#import linecache
#print(linecache.getline('this_is_file.txt',7))

