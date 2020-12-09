'''
Runs 50 times, creating a file with contents 
"This file was created on [STUDENT]'s computer at [TIME] in [LOCATION]"
'''

from datetime import datetime
import os

for i in range(50):
    with open("file_{}.txt".format(i), "w") as file:
        file.write("This file was created on [INSERT YOUR NAME HERE]'s computer at {} in {}".format(datetime.now(), os.getcwd()))
