Steps to setup the project :

1) fork the repository  for your use. 

2) make sure pip (python module) is installed globally (http://www.pip-installer.org/en/latest/installing.html#installing-globally)
    
3) Install virtualenv (python module, see https://pypi.python.org/pypi/virtualenv) - 
	$> pip install virtualenv

4) install the project repository
	$> cd path/to/some_folder
	
	$> git clone <forked_path> 
    
5) install the project dependencies
	$> cd path/to/some_other_folder/ 
	
	$> virtualenv mysite_env 
	
	$> source mysite_env/bin/activate 
	
	(mysite_env)$> cd path/to/cloned_project 
	
	(mysite_env)$> pip install -r requirements.txt 
    
6) To start the local webserver, this should start the application on 8000 port
	(mysite_env)$> manage.py runserver
    
7) Goto localhost:8000, to see the application
    
	go to admin (username = admin / password = admin):
	http://127.0.0.1:8000/admin/
    
	to see list of problems
	http://127.0.0.1:8000/problems/
    
	from here click the problem to see its details. There is just one problem right now.