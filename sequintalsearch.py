import random

def sequintial_search (number_list, target_value):
    for index in range (len (number_list)):
        if target_value == number_list[index]:
            return index
        
    return -1

def main ():
    #create list
    number_list = random.sample(range(1,101),100)
    number_list.sort()


    found_index =sequintial_search (number_list, 77)

    print (found_index)


main()
