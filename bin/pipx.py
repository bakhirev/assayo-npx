#!/usr/bin/env python

import os
import sys
import shutil
from subprocess import check_output

def getSaveLogCommand(fileName):
  raw = '--raw --numstat'
  if '--no-file' in sys.argv:
    raw = ''
  return 'git --no-pager log ' + raw + ' --oneline --all --reverse --date=iso-strict --pretty=format:"%ad>%aN>%aE>%s" > ' + fileName

def runScript():
  # folder, when library was saved
  SOURCE_DIR = 'assayo'
  SOURCE_PATH = os.path.dirname(__file__)

  # folder, when user run library
  DIST_DIR = 'assayo'
  DIST_PATH = os.getcwd()

  # 1. Copy folder ./assayo from package to ./assayo in project
  source = os.path.join(SOURCE_PATH, SOURCE_DIR)
  target = os.path.join(DIST_PATH, DIST_DIR)
  shutil.copytree(source, target)
  print('directory with HTML report was be created')

  # 2. Run 'git log' and save output in file ./assayo/log.txt
  print('reading git log was be started')
  fileName = os.path.join(DIST_PATH, DIST_DIR, 'log.txt')
  command = getSaveLogCommand(fileName)
  check_output(command, shell=True)
  print('the file with git log was be saved')

  # 3. Replace symbols in ./assayo/log.txt
  with open(fileName, 'r+') as f:
      content = f.read().replace('`', '').replace('\n', '`);\nreport.push(`')
      f.seek(0)
      f.write(f'report.push(\`{content}\`);')
      f.truncate()
