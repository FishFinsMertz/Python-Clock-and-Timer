import time
#Clock
start = time.time()

now = time.gmtime()
now = time.asctime(now)
print (now)

time.sleep(3)

stop = time.time()

print(stop-start)

#Timer in seconds
countdown_timer = int(input("Enter the countdown time in seconds"))

for a in range (countdown_timer, 0, -1):
  seconds = a % 60
  minutes = int(a / 60) % 60
  hours = int(a / 3600)
  print(f"{hours:02}:{minutes:02}:{seconds:02}")
  time.sleep(1)
print("Countdown completed")

