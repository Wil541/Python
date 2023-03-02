max_caracter = 140

T = input("Digite o seu TWEET: ")

quantidade_tweet = len(T)

if quantidade_tweet <= max_caracter:
    print("TWEET")
else:
    print("MUTE")