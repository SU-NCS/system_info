import sys
# https://github.com/workhorsy/py-cpuinfo

# Import cpuinfo.py from up one directory
sys.path.append('../cpuinfo')

if __name__ == '__main__':
	from multiprocessing import freeze_support
	from cpuinfo import get_cpu_info

	# NOTE: Make sure to call freeze_support or Pyinstaller will break
	freeze_support()
	#print(get_cpu_info())
	cpu_info = get_cpu_info()
	
	print(type(cpu_info))
	for key in cpu_info:
		print(key,":", cpu_info[key])
	# for attr, value in cpu_info.__dict__.iteritems():
	# 	print ("Attribute: " + str(attr or ""))
	# 	print ("Value: " + str(value or ""))