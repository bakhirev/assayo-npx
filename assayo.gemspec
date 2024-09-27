# coding: utf-8
Gem::Specification.new do |s|
  s.name        = "assayo"
  s.version     = "0.0.2"
  s.summary     = "Assayo"
  s.description = "Visualization and analysis of git commit statistics. Team Lead performance tool."
  s.authors     = ["Aleksei Bakhirev"]
  s.email       = "alexey-bakhirev@yandex.ru"
  s.files       = Dir["{assayo}/**/*"] + ["bin/assayo.rb", "README.md"]
  s.require_paths = ["assayo"]
  s.executables << "assayo"
  s.homepage    = "https://github.com/bakhirev/assayo"
  s.license     = "MIT"
  s.metadata    = {
    "homepage_uri" => "https://github.com/bakhirev/assayo",
	"source_code_uri" => "https://github.com/bakhirev/assayo"
  }
end
