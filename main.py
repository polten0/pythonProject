import os
import random

isAlive = True
difficult = 1
operations = ['+', '-', '*']

def Calculate(int1, int2, operation):
    match operation:
        case '+':
            return int1 + int2
        case '-':
            return int1 - int2
        case '*':
            return int1 * int2

while isAlive:
    rndInt1 = random.randint(1, 10)
    rndInt2 = random.randint(1, 10)
    rndOp = random.choice(operations)

    print(rndInt1, rndOp, rndInt2)
    playerAnswer = input()
    if int(playerAnswer) == Calculate(rndInt1, rndInt2, rndOp):
        print('Правильно\n')
        difficult += 1
    else:
        print('Неправильно, ответ:', Calculate(rndInt1, rndInt2, rndOp))
        isAlive = False