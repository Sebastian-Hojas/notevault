import argparse
from .sortnote import Sortnote
from .cronmanager import *
from .configmanager import ConfigManager
import sys
import os

def cli():

  parser = argparse.ArgumentParser(prog='notevault', description='Brings order to a chaotic world.')
  parser.add_argument('mode', choices=['enable', 'disable', 'run', 'reset', 'status'], help='Setups cron job for this directory')
  parser.add_argument('directory', nargs="?")
  
  parser.add_argument('-d', '--dry',action='store_true', help='Dry run: Do not rename files, only print', default=False)
  parser.add_argument('-v', '--verbose',action='store_true', help='Verbose: Prints file rename descriptions', default=False)
  parser.add_argument('-c', '--config', action='store_true', help='Path to user config file', default=os.path.join(os.path.expanduser("~"), ".notevault.config"))

  args = parser.parse_args()

  if args.mode == "reset" or args.mode == "status" or args.mode == "reset":
    executeMode(args.mode,None,args.config,args.dry,args.verbose,parser)
  else:
    executeModeWithPipe(args,parser)

def executeMode(mode,directory,config,dry,verbose,parser):
  if mode == "reset":
    CronManager().deleteCron()
    ConfigManager(config,dry,verbose).disableAll()
    # delete config file?
    return
  elif mode == "status":
    # TODO check if cron is set
    ConfigManager(config,dry,verbose).status()
    return
  elif mode == "enable":
    try:
      directoryExists(directory,True)
      ConfigManager(config,dry,verbose).enable(directory)
      CronManager().addCron()
    except Exception as e:
      parser.error("Warning: " + str(e))
    
  elif mode == "disable":
    ConfigManager(config,dry,verbose).disable(directory)
  elif mode == "run":
    try:
      sorter = Sortnote(directory, dry, verbose)
      sorter.sortDirectory()
    except Exception,e:
      print str(e)
  else:
    parser.error("Unknown command")

def executeModeWithPipe(args,parser):
  # single directory passed
  if args.directory:
    assertDirectoryExists(args.directory,parser,True)
    executeMode(args.mode,args.directory,args.config, args.dry,args.verbose,parser)
  # retrieve directories from pipe
  elif not sys.stdin.isatty():
    if args.verbose:
      print("Reading from pipe.")
 
    while 1:
      try:
        line = sys.stdin.readline()
      except KeyboardInterrupt:
          break
      if not line:
          break
      line = line.strip('\n')
      line = line.strip('\t')
      executeMode(args.mode,line,args.config, args.dry,args.verbose,parser)
  # retrieve directories from config
  else:
    if args.verbose:
      print("Reading from config.")
    cm = ConfigManager(args.config,args.dry,args.verbose)
    for folder in cm.enabledFolders():
      executeMode(args.mode,folder,args.config, args.dry,args.verbose,parser)


def assertDirectoryExists(directory, parser, checkFS=False):
  try:
    directoryExists(directory,checkFS)
  except Exception as e:
    parser.error(Str(e))

def directoryExists(directory,checkFS=False):
  if not directory:
    raise Exception("Needs directory")
  elif checkFS and not os.path.isdir(directory):
    raise Exception("Directory '" + directory + "' does not exist")
