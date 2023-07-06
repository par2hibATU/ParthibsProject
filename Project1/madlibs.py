def greet(fx):
    def mfx(*args, **kwargs):
        print("Hi viewers, welcome to my YouTube channel.")  # using decorators
        fx(*args, **kwargs)
        print("Bless your eyes")

    return mfx

@greet
def youtuber(username, type, acquainted_knowledge, way_of_comm):
    print(f"Please subscribe to this {username} channel.This channel provides {type} type of videos which will help common "
          f"people to enrich their "
          f"knowledge in {acquainted_knowledge}. If you want more variant in videos, just {way_of_comm} us here.")


youtuber("PoliticsOfNature",  "Environmental", "environmental cognition","email" )



#######WrongCodeHere
#Learning in this fault code
"""The code is using decorators to add additional functionality to the youtuber() function.
However, there is an issue with the implementing the decorator.

The problem lies in the return mfx() line within the greet() function. When defining a decorator, we should return 
the decorated function itself, without calling it immediately. By including the parentheses (), we are actually 
executing the decorated function at the time the decorator is defined, rather than when it is called."""


"""def greet(fx):
    def mfx(*args, **kwargs):
        print("Hi viewers, welcome to my YouTube channel.")  # using decorators
        fx(*args, **kwargs)
        print("Bless your eyes")

    return mfx()

@greet
def youtuber(username):
    print(f"Please subscribe to this {username} channel.")


youtuber("2")"""
"""
def print_range(start, end):
	# Loop through the numbers from start to end
	n = start
	while n <= end:
		print(n)

print_range(1, 5)"""

"""multiplier = 1
result = multiplier*5
while result <= 50:
  print(result)
  multiplier += 1
  result = multiplier*5
print("Done")
"""


"""def is_power_of_two(number):
    # This while loop checks if the "number" can be divided by two
    # without leaving a remainder. How can you change the while loop to
    # avoid a Python ZeroDivisionError?
    while number % 2 == 0:
        number = number / 2
    # If after dividing by 2 "number" equals 1, then "number" is a power
    # of 2.
    if number == 0:
        return True
    return False


# Calls to the function
print(is_power_of_two(0))  # Should be False
print(is_power_of_two(1))  # Should be True
print(is_power_of_two(8))  # Should be True
print(is_power_of_two(9))  # Should be False"""
"""for n in range(0,18+1,2):
    print(n*2)"""
"""def countdown(start):
    x = start
    if x > 0:
        return_string = "Counting down to 0: "
        while x >= 0:  # Complete the while loop condition
            return_string += str(x)  # Add the numbers to the "return_string"
            if x > 0:
                return_string += ","
            x -= 1  # Decrement the appropriate variable
    else:
        return_string = "Cannot count down to 0"
    return return_string


print(countdown(52))"""
"""x = 1
sum = 0
while x <= 10:
    sum += x
    x += 1
print(sum)
# Should print 55"""
"""for outer_loop in range(2, 6+1):
    for inner_loop in range(outer_loop):
        if inner_loop % 2 == 0:
            print(inner_loop)"""
"""
def count_to_ten():
    x = 0
    while x <= 10:
        print(x)


count_to_ten()"""