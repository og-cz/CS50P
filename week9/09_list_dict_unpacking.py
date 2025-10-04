def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


# list
coins = [100, 50, 25]
print(total(*coins), "knuts")  # this will unpack it, whatever is in coins

# dictionaries
coins = {"galleons": 100, "sickles": 50, "knuts": 25}
print(
    total(**coins), "knuts"
)  # what this do is passing three values like galleons:100 is galleons=100
