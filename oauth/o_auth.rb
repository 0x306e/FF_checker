require 'twitter'
require 'twitter_oauth'

module OAuth
  client = TwitterOAuth::Client.new(
    :consumer_key => '',
    :consumer_secret => ''
  )

  request_token = client.request_token
end
