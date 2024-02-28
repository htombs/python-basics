my_list = [13, 2, 11, 18, 3, 12, 0, 7, 9, 99, 44, 76]

for num in sorted(my_list): # the "for num" is basically assigning each of the numbers in my_list as "num" and tells the function to cyle though each unit when the "print(num)" is called
    if (num % 2 == 1): # the % sign is asking if, after num has been devided by 2, is there 1 left over? If so, it returns TRUE so is shown when the "print(num) is called"
        print(num)

# you could also find the even numbers by asking is 0 is left over after num has been devided by 2