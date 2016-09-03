import argparse
from sortnote import Sortnote
from cronmanager import *

def cli():

  parser = argparse.ArgumentParser(prog='sortnote', description='Brings order to a chaotic world.')
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

  if not args.directory:
    parser.error("Needs directory")
  elif args.mode == "disable":
    if not args.directory:
        parser.error("Needs directory")
    cm = CronManager(args.directory)
    cm.deleteCron()
  elif args.mode == "enable":
    cm = CronManager(args.directory)
    cm.addCron()
  elif args.mode == "run":
    try:
      sorter = Sortnote(args.directory, args.dry, args.verbose)
      sorter.sortDirectory()
    except Exception,e:
      print str(e)
      if args.Y:
        print "Remove cronjob."
        cm = CronManager(args.directory)
        cm.deleteCron()
  else:
    parser.error("Unknown command")
