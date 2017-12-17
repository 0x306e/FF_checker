require 'twitter'
require 'twitter_oauth'
require 'yaml'

module FF_checker
  class O_auth
    key = YAML.load_file('./settings.yml')

    client = TwitterOAuth::Client.new(
        :consumer_key => key['consumer_key'],
        :consumer_secret => key['consumer_secret']
    )

    request_token = client.request_token
  end
end
