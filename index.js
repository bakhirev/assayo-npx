#!/usr/bin/env node

const fs = require('node:fs');
const { promisify, format } = require('node:util');
const { argv } = require('node:process');
const { exec } = require('node:child_process');

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
  const distPath = process.cwd();

  const source = `${__dirname}\\build`;
  const build = `${distPath}\\${distDir}`;
  const copy = `cp -r ${source} ${build}`;
  await asyncExec(copy);
  log('directory with HTML report was be created');

  log('reading git log was be started');
  const fileName = `./${distDir}/log.txt`;
  const command = getSaveLogCommand(fileName);
  await asyncExec(command);
  log('the file with git log was be saved');

  const content = fs.readFileSync(fileName, "utf8")
    .replace(/`/gim, '')
    .replace(/\n/gim, '`);\nreport.push(`');
  fs.writeFileSync(fileName, `report.push(\`${content}\`);`);

}()).catch(onFatalError);
