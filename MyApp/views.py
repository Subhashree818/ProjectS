from django.shortcuts import render
import os
import shutil

# Create your views here.

def index(request):
    if request.method == 'GET':
        return render(request, 'MyApp/index.html')
    elif request.method == 'POST':
        try:
            action = request.POST['options']
            if action == 'CreateDir':
                dirPath = request.POST['directorypath']
                dirname = request.POST['directoryname']
                print(action,dirPath,dirname)
                os.mkdir(dirPath+'/'+dirname, 0o777)
                return render(request, 'MyApp/index.html', {"message": 'Successfully created a Dir: '+dirname})
            elif action == 'DeleteDir':
                dirPath = request.POST['directorypath']
                dirname = request.POST['directoryname']
                #os.remove(dirPath+'/'+dirname)
                shutil.rmtree(dirPath+'/'+dirname)
                return render(request, 'MyApp/index.html', {"message": 'Successfully delete a Dir: '+dirname})
        except Exception as e:
            return render(request, 'MyApp/index.html', {"message": 'Unable to perform the operation as we have error saying '+ str(e)})
            
def index2(request):
    if request.method == 'GET':
        return render(request, 'MyApp/index.html')