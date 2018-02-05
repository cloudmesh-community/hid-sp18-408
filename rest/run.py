import os
from eve import Eve
import platform
import psutil

app = Eve()


@app.route('/details')
def details():
	architecture =platform.processor()
	details=platform.uname()
	operating_system =platform.system()
	
	a = []
	a.append("OS:"+operating_system)
	a.append("Processor:"+architecture)
	a.append("Laptop:"+details[1])
	return "<br />".join(a)


@app.route('/ram')
def ram():
	ram = "RAM"+ " "+str(psutil.virtual_memory())
	return ram


@app.route('/disk')
def disk():
	disk = str(psutil.disk_usage('/'))
	return "Disk Usage:" + disk

if __name__ == '__main__':
    app.run()