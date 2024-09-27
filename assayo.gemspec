# coding: utf-8
lib = File.expand_path('./assayo', __FILE__)
$LOAD_PATH.unshift(lib) unless $LOAD_PATH.include?(lib)

Gem::Specification.new do |s|
  s.name        = "assayo"
  s.version     = "0.0.1"
  s.summary     = "Assayo"
  s.description = "Visualization and analysis of git commit statistics. Team Lead performance tool."
  s.authors     = ["Aleksei Bakhirev"]
  s.email       = "alexey-bakhirev@yandex.ru"
  #s.files       = ["bin/assayo.rb"]
  s.files       = `git ls-files`.split($/).reject{|x| x.start_with?("assayo")}
  s.require_paths = ["assayo"]
  s.executables << "assayo"
  s.homepage    = "https://github.com/bakhirev/assayo"
  s.license     = "MIT"
end
