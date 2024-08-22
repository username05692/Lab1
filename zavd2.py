start = 10
final=50
days=1
run=start
while run<final:
  run += run*0.10
  days+=1
print(f"Спортсмен подолає 50 км за {days} днів.")
