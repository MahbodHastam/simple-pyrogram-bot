def createFile(path, data):
  file = open(path, 'w')
  file.write(data)
  file.close()

def openFile(path):
  return open(path, 'r').readline()

def getStatus():
  return openFile('./settings/status.txt')

def setStatus(arg):
  createFile('./settings/status.txt', arg)