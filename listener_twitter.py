import socket
import tweepy

# Twitter API credentials
HOST = 'localhost'
PORT = 9009

s = socket.socket()
s.bind((HOST, PORT))
print(f"Aguardando conexão na porta: {PORT}")
s.listen(5)

connection, address = s.accept()
print(f"Recebendo solicitação de {address}")

# Using Tokens
token = 'YOUR_TOKEN'
keyword = 'YOUR_KEYWORD'

class GetTweets(tweepy.streamming.StreamListener):
    def on_tweet(self, tweet):
        print(tweet.text)
        print('='*50)
        connection.send(tweet.text.encode('latin1', 'ignore'))

    def on_error(self, tweet_code):
        if tweet_code == 420:
            return False
        

printer = GetTweets(token)
printer.add_rule(tweepy.StreamRule(keyword))
printer.filter()

connection.close()