require 'yaml'
require_relative './core/o_auth'
require_relative './core/configger'

setting = YAML.load_file(File.expand_path('../settings.yml', __FILE__))
auth = O_auth.new(setting['consumer_key'], setting['consumer_secret'])

url = auth.get_url
system("start #{url}")
print('Enter pin code :')
pin = gets
token, secret = auth.get_token(pin.to_i)

client = Twitter::REST::Client.new do |conf|
  conf.consumer_key = setting['consumer_key']
  conf.consumer_secret = setting['consumer_secret']
  conf.access_token = token
  conf.access_token_secret = secret
end
uid = client.user.id

config = {
    'uid': uid,
    'consumer_key': setting['consumer_key'],
    'consumer_secret': setting['consumer_secret'],
    'access_token': token,
    'access_token_secret': secret
}

YAML.dump(config, open(File.expand_path("../data/conf/#{uid}.conf", __FILE__)))

