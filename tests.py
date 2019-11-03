from cron_parser_optimised import *

# Test 1

ls = "1 1 1 1 1 /usr/bin/find".split(" ")

output = "minute        " + "1\n" + "hour          " + "1\n" + "day of month  " + "1\n" + "month         " + "1\n" + "day of week   " + "1\n" + "command       " + ls[5]

assert outputFormatter(ls) == output ," Should be \n" +  outputFormatter(ls)

print("Test 1/4 passed")




# Test 2

ls = "1 1,3-5 1 1 1 /usr/bin/find".split(" ")

output = "minute        " + "1\n" + "hour          " + "1 3 4 5 \n" + "day of month  " + "1\n" + "month         " + "1\n" + "day of week   " + "1\n" + "command       " + ls[5]

assert outputFormatter(ls) == output ," Should be \n" +  outputFormatter(ls)

print("Test 2/4 passed")




# Test 3

ls = "4-17 1,2,20-23 5,7,23-29 */3 2 /usr/bin/find".split(" ")

output = "minute        " + "4 5 6 7 8 9 10 11 12 13 14 15 16 17 \n" + "hour          " + "1 2 20 21 22 23 \n" + "day of month  " + "5 7 23 24 25 26 27 28 29 \n" + "month         " + "0 3 6 9 \n" + "day of week   " + "2\n" + "command       " + ls[5]

assert outputFormatter(ls) == output ," Should be \n" +  outputFormatter(ls)

print("Test 3/4 passed")


# Test 4

ls = "* * * * * /usr/bin/find".split(" ")

output = "minute        " + "0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 \n" + "hour          " + "0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 \n" + "day of month  " + "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 \n" + "month         " + "1 2 3 4 5 6 7 8 9 10 11 12 \n" + "day of week   " + "0 1 2 3 4 5 6 7 \n" + "command       " + ls[5]

assert outputFormatter(ls) == output ," Should be \n" +  outputFormatter(ls)

print("Test 4/4 passed")




print("Tests passed successfully")