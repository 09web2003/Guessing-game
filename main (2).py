
import random
target__value=random.randint(1,11)
guess_value=int(input("Enter Your Guess Value :"))
while guess_value !=target__value:
      print("Guess is wrong")
      guess_value=int(input("Enter Your Guess Value :"))
print("Well Done!")      