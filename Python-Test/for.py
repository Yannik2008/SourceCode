# Dies ist ein Test
import time
zahlen = []
x= 0
while x <= 1:
    for zahl in range(1, 350, 10):
        zahlen.append(zahl)
        print(zahlen)
        time.sleep(0.01)
    zahlen.clear()    
    print(f"\n\n{x}\n\n")
    x += 1
    
  #  time.sleep(1)
    