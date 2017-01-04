
import os
import os.path, time, sys
import re
from sys import platform

class Sortnote:
  def __init__(self, directory, dryrun, verbose):
    self.dir = directory
    self.dryrun = dryrun
    self.verbose = verbose
    self.filematch = re.compile(r"^\d{4}_\d{2}_\d{2}_")
    os.chdir(self.dir)

  def sortDirectory(self):
    files = [f for f in os.listdir(".") if os.path.isfile(f) and not self._isTagged(f) and not f.startswith(".")]
    for file in files:
      self._renameFile(file)

  def _isTagged(self, file):
    return self.filematch.match(file)

  def _renameFile(self,file):
    date_string = ''
  
    if platform == "darwin" and file.startswith('Screen Shot '):
      # extra handling
      year = file[12:16]
      month = file[17:19]
      day = file[20:22]
      date_string = year + '_' + month + '_' + day

    else:
      mtime = time.localtime(os.path.getmtime(file))
      date_string = time.strftime('%Y_%m_%d', mtime)

    newFileName = date_string + '_' + file

    if not self.dryrun:
      os.rename(file, newFileName)
    if self.verbose or self.dryrun:
      print "%45s --> %s" % (file, newFileName)
    
    return


