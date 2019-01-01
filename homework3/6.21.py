def sqrt(n):
    lastGuess=10
    nextGuess=1
    while lastGuess-nextGuess>0.00001:
        t=nextGuess
        nextGuess=(lastGuess+n/lastGuess)/2
        lastGuess=t
    return nextGuess
