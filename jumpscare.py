import time,sys,random
#function I use to write text letter by letter
def sprint(str,ptime=1,ctime=.3,ltime=.05,end='\n'): # the basic sprint function; prints letter by letter
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        if letter == "." or letter == "!" or letter == "?":
            time.sleep(ptime)
        elif letter == ",":
            time.sleep(ctime)
        else:
            time.sleep(ltime)
    sys.stdout.write(end)
    sys.stdout.flush()
    return ''
sprint('What do you want the maximum number of minutes to be jumpscared to be?',end='')
minutes = input()
while True:
    try: 
        minutes = int(minutes)
    except:
        minutes = input("That's not a valid number!")
    else:
        break
seconds = random.randrange(0,60*minutes)
if minutes == 1:
    sprint('You will be jumpscared any second in the next minute starting...')
else:
    sprint('You will be jumpscared any second in the next {num_of_min} minutes, starting...'.format(num_of_min=minutes))
print('Now!')
start_time = time.time()
num = 0
while time.time() < start_time + seconds:
  time.sleep(1)
  num += 1
  print(num)
time.sleep(.5)
print('Boo!')
time.sleep(1)
sprint('Were you scared?')
