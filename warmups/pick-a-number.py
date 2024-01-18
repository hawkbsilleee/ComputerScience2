
# """Given two integers low and high, print the
#     number of guesses required to find number."""
def pick_a_number(low, high, number):

    count = 1
    guess = (low+high)//2
    while guess != number:
        guess = (low + high) // 2
        count += 1
        if guess > number:
            high = guess
        else:
            low = guess

    return count

print(pick_a_number(0,100,5))
      