class Client
  def initialize(data)
    @consumer_key = data.consumer_key
    @consumer_secret = data.consumer_secret
    @access_token = data.access_token
    @access_token_secret = data.access_token_secret
  end
end
