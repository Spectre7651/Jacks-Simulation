import jacks
from colorama import Fore, Back, Style
import timeit
runtimestart = timeit.default_timer()
times = []
for i in range(10000): #Change the number in the range to ajust how many simulations to run
  try:  
    #print("Game no" , Fore.RED + str(i))
    #print(Style.RESET_ALL)
    times.append((jacks.jacks()*2))
  except IndexError:
    pass
runtimeend = timeit.default_timer()
    
average = ((sum(times) / len(times))/60)
maxtime = (max(times)/60)
print("Results:")
print("Average game time:",round(average,2),"mins")
print("Max game time:",round(maxtime,2),"mins")
print("Simulation took",((runtimeend - runtimestart)),"seconds")
  
f = open("results.csv", "a")
output = "\n" + str(round(average,2)) + "," + str(round(maxtime,2))
f.write(output)
f.close()
