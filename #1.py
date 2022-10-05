coin = ['Bitcoin', 'Ether', 'Ripple', 'Litecoin']
code = ['BTC', 'ETH', 'XRP', 'LTC']


def main(coin, code):
    dictionary = {}
    dictionary = dict(zip(coin, code))
    return dictionary

print(main(coin, code))

