import random
import time
import sys
class color:
     BOLD = '\33[1m'
     END = '\33[0m'
     RED = '\33[91m'
     BLUE = '\33[95m'
     YELLOW = '\33[92m'
     CYAN = '\33[99m'
#60 beats per second
tempo=60.0/float(sys.argv[1])

Chords=['E', 'A', 'D', 'C']
while True:
  time.sleep(tempo)
  c=random.choice(Chords) 
  if Chords.index(c) == 0:
    print color.BOLD + color.RED + c + color.END
  elif Chords.index(c) == 1:
    print color.BOLD + color.BLUE + c +color.END
  elif Chords.index(c) == 2:
    print color.BOLD + color.CYAN + c + color.END
  else:
    print color.BOLD + color.YELLOW + c + color.END

  
