# List 
#     store collection of data 
#     its mutable 
#     its contain dulpicate value 
#     its can be acess by indexing
# its like array in javascript

data = ["anand", "raja", "anand"]
# print(data)


# tuple is similar to a List, but you cannot modify its elements after creation.
# - Allows duplicate values.
# - Maintains insertion order.
# - Does not allow modification.
# - Supports indexing.
# can not be modfifeid

data = ("anand", "raja" ,"tuple")
# print(data)


# A Dictionary stores data in key: value pairs.
# - Stores data as key-value pairs.
# - Maintains insertion order.
# - You can add, update, and delete values.
# - Keys must be unique.
    # its object in Javascrit
    
obj ={
    id:1,
    "name":"anand",
    "age": "33",
    "course": ["javascript", "Ai","python"]
}

# print(obj)


# A Set stores unique values.
# - Does not allow duplicates.
# - Does not support indexing.
# - Is mutable.
# - Does not guarantee insertion orde
#  same doesnt allow the dulipcate 

numbers = {10, 20, 30, 10, 20}
# print(numbers)

numbers = [10, 25, 5, 40, 15]

def largestNumber(args):
 largest= args[0]
 for number in args:
    if number > largest:
        largest = number
        # print(largest)
largestNumber([10, 25, 5, 40, 15])


# Given a list of integers, count how many numbers are even.
numbers = [10, 15, 20, 25, 30, 35, 40]
def count_Number(args):
    count =0
    for number in args:
        if number % 2== 0 :
            count = count + 1
    print(count)
count_Number([10, 15, 20, 25, 30, 35, 40])