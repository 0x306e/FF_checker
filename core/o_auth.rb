require 'twitter'
require 'oauth'
require 'oauth/consumer'
require 'yaml'

module FF_checker
  class O_auth
    def initialize(key, secret)
      @consumer = OAuth::Consumer.new(
          key,
          secret,
          site: 'https://api.twitter.com'
      )
    end

    def get_url
      @token = @consumer.get_request_token
      @url = @token.authorize_url
      return @url
    end

    def get_token(pin_code)
      @token.get_access_token(:oauth_verifier => pin_code)
      return @token.token, @token.secret
    end

  end
end
