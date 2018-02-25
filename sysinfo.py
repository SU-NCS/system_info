# https://docs.python.org/3/using/windows.html
import platform

from multiprocessing import cpuinfo
import freeze_support()

machine = platform.machine()
#'x86'
version = platform.version()
#'5.1.2600'
platform = platform.platform()
#'Windows-XP-5.1.2600-SP2'
#system = platform.system()
#uname = platform.uname()
#('Windows', 'name', 'XP', '5.1.2600', 'x86', 'x86 Family 6 Model 15 Stepping 6, GenuineIntel')
#system = platform.system()
#'Windows'
#processor = platform.processor()
#'x86 Family 6 Model 15 Stepping 6, GenuineIntel'

print ("machine chip      :", machine)
print ("windows version   :", platform)



# NOTE: Needed for Pyinstaller
info = cpuinfo.get_cpu_info()
print(info)
