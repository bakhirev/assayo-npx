#!/usr/bin/env node

const fs = require('node:fs');
const { promisify, format } = require('node:util');
const { argv } = require('node:process');
const { exec } = require('node:child_process');
const path = require('node:path');

const asyncExec = promisify(exec);

const log = argv.includes('--debug')
  ? (m) => console.log(`Assayo: ${m}`)
  : () => {};

function getErrorMessage(error) {
  if (typeof error !== "object" || error === null) {
    return String(error);
  }
  if (typeof error.stack === "string") {
    return error.stack;
  }
  return format("%o", error);
}

function onFatalError(error) {
  process.exitCode = 2;
  const message = getErrorMessage(error) || 'error';
  console.error(`Assayo: ${message}`);
}

function getSaveLogCommand(fileName) {
  const raw = argv.includes('--no-file') ? '' : '--raw --numstat';
  return `git --no-pager log ${raw} --oneline --all --reverse --date=iso-strict --pretty=format:"%ad>%aN>%aE>%s" > ${fileName}`;
}

(async function main() {
  process.on("uncaughtException", onFatalError);
  process.on("unhandledRejection", onFatalError);

  const distDir = 'assayo';
  const distPath = process.cwd(); // place, when user use library

  // 1. Copy folder ./assayo from package to ./assayo in project
  const source = path.resolve(__dirname, 'assayo');
  const target = path.resolve(distPath, distDir);
  const copy = `cp -r ${source} ${target}`;
  await asyncExec(copy);
  log('directory with HTML report was be created');

  // 2. Run "git log" and save output in file ./assayo/log.txt
  log('reading git log was be started');
  const fileName =  path.resolve('./', distDir, 'log.txt');
  const command = getSaveLogCommand(fileName);
  await asyncExec(command);
  log('the file with git log was be saved');

  // 3. Replace symbols in ./assayo/log.txt
  const content = fs.readFileSync(fileName, "utf8")
    .replace(/`/gim, '')
    .replace(/\n/gim, '`);\nreport.push(`');
  fs.writeFileSync(fileName, `report.push(\`${content}\`);`);

}()).catch(onFatalError);
