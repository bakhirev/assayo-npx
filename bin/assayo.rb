#!/usr/bin/env ruby

def get_save_log_command(fileName)
  raw = "--raw --numstat"
  if ARGV.include?('--no-file')
    raw = ""
  end
  return "git --no-pager log #{raw} --oneline --all --reverse --date=iso-strict --pretty=format:\"%ad>%aN>%aE>%s\" > #{fileName}"
end

def show_message(message)
  if ARGV.include?('--debug')
    puts "Assayo: #{message}"
  end
end

def create_report()
  # folder, when library was saved
  SOURCE_DIR = 'assayo'
  SOURCE_PATH = Dir.pwd

  # folder, when user run library
  DIST_DIR = 'assayo'
  DIST_PATH = Process.cwd

  # 1. Copy folder ./assayo from package to ./assayo in project
  source = File.join(SOURCE_PATH, SOURCE_DIR)
  target = File.join(DIST_PATH, DIST_DIR)
  copy_cmd = "cp -r #{source} #{target}"
  begin
    system(copy_cmd)
  rescue => e
    puts "Assayo: cant copy files: #{e.message}"
  end
  show_message("directory with HTML report was be created")

  # Run "git log" and save output in file ./assayo/log.txt
  show_message("reading git log was be started")
  fileName = File.join(Dir.pwd, DIST_DIR, 'log.txt')
  save_log_cmd = get_save_log_command(fileName)
  begin
    system(save_log_cmd)
  rescue => e
    puts "Assayo: cant create log file: #{e.message}"
  end
  show_message("the file with git log was be saved")

  # 3. Replace symbols in ./assayo/log.txt
  content = File.read(filename, 'UTF-8').gsub(/`/, '')
  content = content.gsub(/\n/, '`);\nr(f`')
  File.open(filename, 'w') { |file| file.write("r(f\`#{content}\`);") }
end

create_report()
