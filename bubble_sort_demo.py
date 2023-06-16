import random

def bubble_sort(data_list):
    number_of_items = len(data_list)
    for i in range (number_of_items):
        #loop
        for j in range (number_of_items - 1):
            #compare
            if (data_list[j+1] > data_list[j]) :
                #swap
                temp = data_list[j]
                data_list[j] = data_list[j+1]
                data_list[j+1] = temp
    
    return data_list

    
    #loop through the list to visit each item

    #loop through list to compare items to adjacent items
    #compare adjacent items
    #if right is less than left then swap position


def main():
    #create a list of integers
    integer_list= random.sample(range(0,1000), 100)
    #call bubble sort
    sorted_list = bubble_sort(integer_list)

    print (sorted_list)

main ()
