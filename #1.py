def main():
    coin = ['Bitcoin', 'Ether', 'Ripple', 'Litecoin']
    code = ['BTC', 'ETH', 'XRP', 'LTC']
    dictionary = {}
    dictionary = dict(zip(coin, code))
    return dictionary

print(main())

