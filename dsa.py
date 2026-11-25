# Second Largest Number
numbers = [10, 25, 5, 40, 15, 30] 
def second_largest(args):
   first_largest = args[0]
   second_largest = 0
   for number in args:
       if number >= first_largest:
        second_largest = first_largest  # 10
        first_largest = number
        print(f"first number ", first_largest)
       else:
        # first_largest >= second_largest
        print(f"second" , second_largest)
        
second_largest([10, 25, 5, 40, 15, 30])