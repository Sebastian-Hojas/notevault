
from crontab import CronTab
import os

def id():
  return "sortnote: "

def CronDeleteAll():
  cron = CronTab(user=True)
  toDelete = [job for job in cron if isSortNoteJob(job)]
  for job in toDelete:
    cron.remove(job)
  cron.write()

def CronStatus():
  cron = CronTab(user=True)
  activeJobs = [job.comment.replace(id(), '') for job in cron if isSortNoteJob(job)]
  if len(activeJobs) == 0:
    print "No active jobs."
  else:
    print "Active jobs:"
  
  for job in activeJobs:
    print job

def isSortNoteJob(job): 
  return id() in job.comment

class CronManager(object):
  
  def __init__(self, directory):
    self.cron = CronTab(user=True)
    self.directory = os.path.abspath(directory)

  def addCron(self):
    self.deleteCron()
    job = self.cron.new(command='sortnote -Y ' + self.directory)
    job.set_comment(self.id())
    job.every().hour()
    self.cron.write()

  def deleteCron(self):
    toDelete = [job for job in self.cron if (self.directory in job.comment)]
    for job in toDelete:
      self.cron.remove(job)
    self.cron.write()

  def id(self):
    return id() + self.directory


