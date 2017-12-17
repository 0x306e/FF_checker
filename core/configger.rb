require 'yaml'
module FF_checker
  class Configger
    def initialize(file)
      @file = File.expand_path('../data/' + file, __FILE__)
    end

    def load
      return YAML.load(@file)
    end
  end
end