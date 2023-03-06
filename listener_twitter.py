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
token = 'AAAAAAAAAAAAAAAAAAAAAHP7dAEAAAAAbSQi9jIHuQn9j6GhP021K0h%2F4uM%3DJkvdY7ik2ZdodLe7x5djVqjhDGiym6lj1r67MDV0YVAqg1RmFe'
keyword = 'futebol'

class GetTweets(tweepy.streamming.StreamListener):
    def on_tweet(self, tweet):
        print(tweet.text)
        print('='*50)
        connection.send(tweet.text.encode('utf-8', 'ignore'))

    def on_error(self, tweet_code):
        if tweet_code == 420:
            return False
        

printer = GetTweets(token)
printer.add_rule(tweepy.StreamRule(keyword))
printer.filter()

connection.close()