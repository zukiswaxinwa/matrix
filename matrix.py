import random,time,colorama


while True:
  for num in range(20):
    matrix = random.randint(0,1)
    print(colorama.Fore.GREEN + colorama.Style.BRIGHT + str(matrix), end=" ")
