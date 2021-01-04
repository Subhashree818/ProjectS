from django.shortcuts import render
import os
import shutil
import threading
# Create your views here.
def createDir(dirpathname, dirname):
    print(dirpathname, dirname)
    os.mkdir(dirpathname+'/'+dirname, 0o777)
    print(dirpathname, dirname)
    return 'Successfully created a Dir: '+dirname

def deleteDir(dirpathname, dirname):
    print(dirpathname, dirname)
    shutil.rmtree(dirpathname+'/'+dirname)
    return 'Successfully delete a Dir: ' + dirname


def index(request):
    if request.method == 'GET':
        return render(request, 'MyApp/index.html')
    elif request.method == 'POST':
        try:
            action = request.POST['options']
            print("Action : ", action)
            if action == 'CreateDir':
                dirPath = request.POST['directorypath']
                dirname = request.POST['directoryname']
                print(dirPath, dirname, "inside index func creatae dir")
                t1 = threading.Thread(target=createDir(dirPath ,dirname))
                print(action,dirPath,dirname)
                #os.mkdir(dirPath+'/'+dirname, 0o777)
                return render(request, 'MyApp/index.html', {"message": 'Successfully created a Dir: '+dirname})
                #t1 = threading.Thread(target=createDir(dirPath,dirname)) 
            elif action == 'DeleteDir':
                dirPath = request.POST['directorypath']
                dirname = request.POST['directoryname']
                #os.remove(dirPath+'/'+dirname)
                #shutil.rmtree(dirPath+'/'+dirname)
                t2 = threading.Thread(target=deleteDir(dirPath, dirname))
                return render(request, 'MyApp/index.html', {"message": 'Successfully delete a Dir: '+dirname})
        except Exception as e:
            return render(request, 'MyApp/index.html', {"message": 'Unable to perform the operation as we have error saying '+ str(e)})
            
def index2(request):
    if request.method == 'GET':
        return render(request, 'MyApp/index.html')