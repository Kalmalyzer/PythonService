 
import win32serviceutil
import win32service
import win32event
import os
import sys
import time
from threading import Thread
import httpserver

class ServiceLauncher(win32serviceutil.ServiceFramework):
	_svc_name_ = 'PythonService'
	_svc_display_name_ ="Python based win32 service"
	_svc_description_ = ""
	def __init__(self, args):
		win32serviceutil.ServiceFramework.__init__(self, args)
		self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)

	def SvcStop(self):
		self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
		win32event.SetEvent(self.hWaitStop)

	def SvcDoRun(self):
		thread = Thread(target = httpserver.run_httpserver)
		thread.daemon = True
		thread.start()
		while (1):
		    rc = win32event.WaitForSingleObject(self.hWaitStop, 1000)
		    if rc==win32event.WAIT_OBJECT_0:
			# Stop event
			break


if __name__ == '__main__':
	win32serviceutil.HandleCommandLine(ServiceLauncher)
