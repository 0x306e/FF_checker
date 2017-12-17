require 'twitter'
require 'twitter_oauth'

module FF_checker
  client = TwitterOAuth::Client.new(
    :consumer_key => '',
    :consumer_secret => ''
  )

  request_token = client.request_token
end
