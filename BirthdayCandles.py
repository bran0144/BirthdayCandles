candles = [4, 4, 1, 3]

def birthdayCakeCandles(candles):
    # max_dict = {}
    # for i in candles:
    #     max_dict[i] = max_dict.get(i, 0) + 1
    # max_count = max_dict.values()
    # max_value = max(max_count)
    # print(max_value)

    print(candles.count(max(candles)))

birthdayCakeCandles(candles)