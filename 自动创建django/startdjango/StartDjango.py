import threading
import time
import os 

class StartDjango(threading.Thread,object):
	loc=""
	name=""
	url=""

	def __init__(self):
		super(StartDjango,self).__init__()
		self.instance=None
	def __call__(self,*args,**kwd):
		if not self.instance  is None:
			self.instance = super(StartDjango, self).__call__(*args, **kw)  
			return self.instance
		
	def creatProject(self, loc,name,appname):
		self.loc=loc
		self.name=name
		os.chdir(loc)
		path=os.path.exists(loc+"\\"+name)

		if(not path):
			os.system("django-admin.py startproject "+name)
			os.chdir(loc+"\\"+name)
			os.system("manage.py startapp "+appname)
		else:
			print("目录已经存在")
    # 默认的线程接口可以在里面写要调用的函数
	def run(self):   
		os.chdir(self.loc+"\\"+self.name)
		r=os.popen("manage.py runserver "+self.url) 

		
	# 调取默认的的线程开始方法start()
	def runser(self,url):
			self.url=url
			self.start()
			time.sleep(1)
			i=input("stop[y or n]?:")
			os.system("taskkill /F /IM  python.exe")

    #结束线程，要延时，否则线程没有创建就不能
    #结束线程。
	def  stop(self):
			time.sleep(1)
			os.system("taskkill /F /IM python.exe")

	def  comand(self,cmd):
		os.chdir(self.loc+"\\"+self.name)
		os.system("manage.py "+cmd)
			
	




	






