import argparse
from .sortnote import Sortnote
from .cronmanager import *
import sys
import os

def cli():

  parser = argparse.ArgumentParser(prog='notevault', description='Brings order to a chaotic world.')
  parser.add_argument('mode', choices=['enable', 'disable', 'run', 'reset', 'status'], help='Setups cron job for this directory')
  parser.add_argument('directory', nargs="?")
  
  parser.add_argument('-d', '--dry',action='store_true', help='Dry run: Do not rename files, only print')
  parser.add_argument('-v', '--verbose',action='store_true', help='Verbose: Prints file rename descriptions')
  parser.add_argument('-Y', action='store_true', help='[internal] Use as a cron deamon')

  args = parser.parse_args()

  if args.mode == "reset":
    CronDeleteAll()
    return
  elif args.mode == "status":
    CronStatus()
    return

  if args.directory:
    executeMode(args.directory,args.mode,args.dry,args.verbose,args.Y)
  else:
    while 1:
      try:
        line = sys.stdin.readline()
      except KeyboardInterrupt:
          break
      if not line:
          break
      line = line.strip('\n')
      line = line.strip('\t')
      executeMode(line,args.mode,args.dry,args.verbose,args.Y)


def executeMode(directory, mode, dry, verbose, cron):
  # TODO check validity directory

  if mode == "disable":
    if not directory:
        parser.error("Needs directory")
    cm = CronManager(directory)
    cm.deleteCron()
    return

  if not os.path.isdir(directory):
    print("Directory '" + directory + "' does not exist.")
    return

  if mode == "enable":
    cm = CronManager(directory)
    cm.addCron()
  elif mode == "run":
    try:
      sorter = Sortnote(directory, dry, verbose)
      sorter.sortDirectory()
    except Exception,e:
      print str(e)
      if cron:
        print "Remove cronjob."
        cm = CronManager(directory)
        cm.deleteCron()
  else:
    parser.error("Unknown command")
