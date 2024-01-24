#define a function for lists
def merge_list(list1, list2):
    result_list = []
#create for loop
    #for loop first list
    for num in list1:
        #check if number is odd
        if num % 2 != 0:
            #store odd number to result list
            result_list.append(num)
            
    #for loop second list
    for num in list2:
        #check if number is even
        if num % 2 == 0:
            #store even number to result list
            result_list.append(num)
#add given lists then print once checked
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
print("result list:", merge_list(list1, list2))