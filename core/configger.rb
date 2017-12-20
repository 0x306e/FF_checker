require 'yaml'

module FF_checker
  class Configger
    def initialize(uid)
      @file = File.expand_path('./data/' + uid + '.yml', __FILE__)
    end

    def load
      return YAML.load_file(@file)
    end
  end
end