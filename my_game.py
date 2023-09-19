import numpy as np

def game_core_v3(number: int = 1) -> int:
  predict = 30
  count = 1
  if predict < number:
    predict += 65
    count += 1
    if predict < number:
      predict += 10
      count += 1
    else:
      predict -= 7
  elif predict > number:
    predict -= 13
    count += 1
    if predict> number:
      predict-= 8
      count+=1
    else:
      predict -=1
  while predict < number:
        predict += 1
        count += 1
  while predict > number:
        predict -= number
        count += 1
  return count
print(f'Количество попыток: {game_core_v3()}') 


