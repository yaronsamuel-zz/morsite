import os
import ftplib
import subprocess
import sys
import datetime
import time

# things to do before the cript would run:
# install git
# install all django-packages
# config %HOME% - setx HOME %USERPROFILE%
# create _netrc in C:\users\username :
# machine github.com
# login yaronsamuel 
# password blabla
# config path environment var to include git and chrome

CHROMEPATH = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
SITE_URL = '127.0.0.1:8000'

# connection config
FTP_PASSWORD = '12qw34er'
FTP_USER = 'morsite@asafsamuel.com'
FTP_HOST = r'ftp.ordercakeinhaifa.com'
FTP_PORT = '21'


#file modification config
LOCAL_ROOT = r'c:\morsite'

FILES_TO_SYNC = [
'morsite.db' , 
'media'      ,

]
##########################



def getRecursiveDirList(path):
    retList = []
    for dirname , dirs , files in os.walk(path):
        tmpFiles = [os.path.join(dirname , fil) for fil in files]
        retList.extend(tmpFiles)
        
    return retList


def getFileList(filesToSync):
    retList = []
    
    for path in filesToSync:
        fullpath = os.path.join(LOCAL_ROOT , path)
        if os.path.isdir(fullpath):
            retList.extend(getRecursiveDirList(fullpath))
        elif os.path.isfile(fullpath):
            retList.append(fullpath)
    
    return retList
    

def downloadFile(path , failSilent = True):
    login = ftplib.FTP(FTP_HOST , FTP_USER , FTP_PASSWORD)
        
    relPath = os.path.relpath(path , LOCAL_ROOT)
    relPath = relPath.replace('\\' , '/')
    cmd = 'RETR %s' % (relPath , )

    fHandle =  open(path , 'wb')
    try:
        login.retrbinary(cmd, fHandle.write)
        print '%s downloaded!' % (path , )
    except:
        print '%s  does not exist'% (path , )
        if not failSilent:
            raise Exception("FTP exception - %s  does not exist" % (path , ) )
        
    fHandle.close()



def getDBPath(FILES_TO_SYNC):
    for fil in FILES_TO_SYNC:
        if fil.lower().endswith('.db'):
            return fil
            
def uploadFiles(fileList):
    login = ftplib.FTP(FTP_HOST , FTP_USER , FTP_PASSWORD)

    for fil in fileList:
        relPath = os.path.relpath(fil , LOCAL_ROOT)
        relPath = relPath.replace('\\' , '/')
        cmd = 'STOR %s' % (relPath , )
        login.storbinary(cmd , open(fil , 'rb'))
        print '%s uploaded!' % (fil , )

def runProcess(argv):
    sub_p = subprocess.Popen(argv)
    while sub_p.poll() is None:
        time.sleep(0.5)
        
def gitBackup(root):
    os.chdir(root)
    runProcess(['git' , 'add' ,'--all'])
    commitMessage = datetime.datetime.now().strftime('%y_%m_%d %H_%M')
    commitMessage = '"Uploader - %s"' % (commitMessage , )
    runProcess(['git' , 'commit', '-a' ,'-m' , commitMessage])
    runProcess(['git' , 'push'])
        
def runserver(root):
    manageScript = os.path.join(root , 'manage.py')
    os.chdir(root)
    subprocess.Popen(['python' , manageScript , 'runserver'])
    print 'local website is running...'
    
def runchrome():
    subprocess.Popen([CHROMEPATH , SITE_URL] )

def getRelDirsFromFiles(fileList):
    
    dirSet = set()
    for fil in fileList:
        dirname =  os.path.dirname(fil)
        if dirname == LOCAL_ROOT:
            continue
            
        dirname = os.path.relpath(dirname , LOCAL_ROOT)
        dirname = dirname.replace('\\' , '/')
        
        dirSet.add(dirname )
        
    return list(dirSet)


def getOnlyNewFiles(fileList):

    dirs = getRelDirsFromFiles(fileList)
    
    ftp = ftplib.FTP(FTP_HOST , FTP_USER , FTP_PASSWORD)
    
    retfFileList = [] 
    ftpFilelist = [] #to store all files in the frp server
    
    for dir in dirs:
        ftp.cwd('~/%s'%dir)
        tmpList = []
        ftp.retrlines('LIST',tmpList.append)
        for line in  tmpList:
            basename = line.split(' ')[-1]
            path = os.path.join(dir , basename).replace('\\' ,'/')
            ftpFilelist.append(path)
        


        
    for fil in fileList:
        relPath = os.path.relpath(fil , LOCAL_ROOT)
        relPath = relPath.replace('\\' , '/')
        if relPath not in ftpFilelist:
            retfFileList.append(fil)
        else:
            print relPath
    
    return retfFileList
    
def main():
    fileList = getFileList(FILES_TO_SYNC)
    dbPath = getDBPath(fileList)
    if '-n' not in sys.argv:
        downloadFile(dbPath , failSilent = False)
    
    runserver(LOCAL_ROOT)
    runchrome()
    
    input = ''
    while input!='x':
        print 'enter x to upload files to server'
        input = raw_input()
        
    gitBackup(LOCAL_ROOT)
    
    filesToUpload = getOnlyNewFiles(fileList)
    filesToUpload.append(dbPath)
    uploadFiles(filesToUpload)
    
    print 'upload is finished'
    print 'Press any key to exit'
    raw_input()
    
    
if __name__ == '__main__':
    
    
#TODO
# change to morsite