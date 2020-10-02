import sys
import os

def main():
    option = sys.argv[1]
    option_stripped = option.replace(' ', '')

    if option_stripped == "-i":
        my_list = sys.argv[2].split('.')
        if len(my_list) == 0 or len(my_list) > 3:
            print ("Error in input name")
            return
        elif len(my_list) == 1:
            full_name = os.path.join("http://",  "www." + my_list[0] + ".edu")
        elif len(my_list) == 2:
            full_name = os.path.join("http://", "www." + my_list[0] + '.' + my_list[1])
        else:
            full_name = os.path.join("http://", my_list[0] + '.' + my_list[1] +'.' + my_list[2])

        print ("The full name of " + sys.argv[2] + " is " + full_name)
    else:
        print ("main.py -i input_name")

if __name__ == '__main__':
    main()