
from crontab import CronTab
import os

class CronManager(object):
  
  def __init__(self):
    self.cron = CronTab(user=True)

  def addCron(self):
    self.deleteCron()
    job = self.cron.new(command='notevault run')
    job.set_comment(self.id())
    job.every().hour()
    self.cron.write()

  def deleteCron(self):
    toDelete = [job for job in self.cron if (self.id() in job.comment)]
    for job in toDelete:
      self.cron.remove(job)
    self.cron.write()

  def id(self):
    return "-notevault-"


