#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from subprocess import check_output

def showMessage(message):
  if '--debug' in sys.argv:
    print('Assayo: ' + message)

def getSaveLogCommand(fileName):
  raw = '--raw --numstat'
  if '--no-file' in sys.argv:
    raw = ''
  return 'git --no-pager log ' + raw + ' --oneline --all --reverse --date=iso-strict --pretty=format:"%ad>%aN>%aE>%s" > ' + fileName

def createHtmlReport():
  # folder, when library was saved
  SOURCE_DIR = '../assayo'
  SOURCE_PATH = os.path.dirname(__file__)

  # folder, when user run library
  DIST_DIR = 'assayo'
  DIST_PATH = os.getcwd()

  # 1. Copy folder ./assayo from package to ./assayo in project
  source = os.path.join(SOURCE_PATH, SOURCE_DIR)
  target = os.path.join(DIST_PATH, DIST_DIR)
  command = 'cp -r ' + source + ' ' + target
  check_output(command, shell=True)
  showMessage('directory with HTML report was be created')

  # 2. Run 'git log' and save output in file ./assayo/log.txt
  showMessage('reading git log was be started')
  fileName = os.path.join(DIST_PATH, DIST_DIR, 'log.txt')
  command = getSaveLogCommand(fileName)
  check_output(command, shell=True)
  showMessage('the file with git log was be saved')

  # 3. Replace symbols in ./assayo/log.txt
  with open(fileName, 'r+') as f:
      content = f.read().replace('`', '').replace('$', '')
      f.seek(0)
      f.write('R(f`' + content + '`);')
      f.truncate()

def main():
  createHtmlReport()

if __name__ == "__main__":
    main()
