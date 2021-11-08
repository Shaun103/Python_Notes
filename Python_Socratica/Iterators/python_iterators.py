def main() -> None:

    # list = ['Cx32', 'GSOF', 'Emily', 'Franz', 'Rex']

    # for element in list: 
    #     print(element)


#     for element in ('Cx32', 'GSOF', 'Emily', 'Franz', 'Rex'):
#         print(element)

#     for letter in 'Socratica':
#         print(letter)

# # print binary
#     for byte in b'Binary':
#         print(byte)

# Error # integers are not integer 
# #    for digit in 63725846375:
# #        print(digit)
    # a = 5462756565
    # digits = [int(d) for d in str(a)] # converting into strings
    # print(a)

# ________________ ________________#
# finding out if something is iterable

    # usernames = ('Cx32', 'GSOF', 'Emily', 'Franz', 'Rex')

    # looper1 = usernames.__iter__()
    # print(type(looper1))
    
    # print(looper1.__next__())
    # print(looper1.__next__())
    # print(looper1.__next__())
# ________________ #


#     users = ['Cx32', 'GSOF', 'Emily', 'Franz', 'Rex']

#     for user in users:
#         print(user)

#     looper = iter(users)
#     while True:
#             try:
#                 user = next(looper)
#                 print(user)
#             except StopIteration:
#                 break
# # ________________ #

    class Portfolio:
        def __init__(self):
            self.holdings = {} # key = ticker, value = number of shares
        
        def buy(self, ticker, shares):
            self.holdings[ticker] = self.holdings.get(ticker, 0) + shares
        
        def sell(self, ticker, shares):
            self.holdings[ticker] = self.holdings.get(ticker, 0) - shares

        def __iter__(self):
            return iter(self.holdings.items())
    
    p = Portfolio()

    p.buy('Alpha', 15)
    p.buy('BETA', 23)
    p.buy('GAMMA', 9)
    p.buy('GAMMA', 20)

    for (ticker, shares) in p:
        print(ticker, shares)
    
    print('\n')
# ________________ #


    import itertools 

    ranks = list(range(2, 11)) + ['J', 'Q', 'K', 'A']
    ranks = [str(rank) for rank in ranks]

    # print(ranks)

    suits = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
    deck = [card for card in itertools.product(ranks, suits)]

    for (index, card) in enumerate(deck):
        print(1 + index, card)

    hands = [hand for hand in itertools.combinations(deck, 5)]

    print('\n')
    print(f'The number of 5-card poker hands is {len(hands)}.')

if __name__ == "__main__":
    main() 