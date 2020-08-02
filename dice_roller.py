import random



def main():
  
  dice_rolls = 2
  dice_sum = 0
  
  for i in range(0,dice_rolls):
    roll = random.randint(1,6)
    dice_sum += roll
    
    if roll == 1:
            print('You reolled a {roll}! Critical Fail')
        elif roll == 6:
            print('You reolled a {roll}! Critical Sucess!')
        else:
            print(f'You rolled a {roll}')
    print(f'Your have rolled a total of {dice_sum}')

if __name__== "__main__":
  main()
