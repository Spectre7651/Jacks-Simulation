import jacks_source
import timeit
runtumestart = timeit.default_timer()
times = []
for i in range(10):
    try:
        startTime = timeit.default_timer()
        jacks_source.jacks()
        endTime = timeit.default_timer()
        times.append((endTime - startTime))
    except IndexError:
        pass
runtimeend = timeit.default_timer()
print("Average game time",((sum(times) / len(times))/60))
print("Max game time",(max(times)/60))
print("Sim time" ((runtimestart - runtimeend)/60))
