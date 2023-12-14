"""
(Stopwatch) Design a class named StopWatch. The class contains:
■ The private data fields startTime and endTime with get methods.
■ A constructor that initializes startTime with the current time.
■ A method named start() that resets the startTime to the current time.
■ A method named stop() that sets the endTime to the current time.
■ A method named getElapsedTime() that returns the elapsed time for the
stop watch in milliseconds.
Draw the UML diagram for the class, and then implement the class. Write a test
program that measures the execution time of adding numbers from 1 to
1,000,000.
"""
import time
class Stopwatch:
    def __init__(self):
        self.__startTime = time.time()
        self.__endTime = 0
    # Getters
    def getStartTime(self):
        # RETURN IN READABLE FORMAT
        return time.ctime(self.__startTime)
    def getEndTime(self):
        return time.ctime(self.__endTime)
    # methods
    def start(self):
        self.__startTime = time.time()

    def stop(self):
        self.__endTime = time.time()

    def getElapsedTime(self):
        return int((self.__endTime - self.__startTime) * 1000)

# test
sw = Stopwatch()
print(sw.getStartTime())
sw.start()
for i in range(1000000):
    pass
sw.stop()
print(sw.getElapsedTime(),"ms")