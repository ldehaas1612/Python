def ticker(filename):
    tickers = {}
    f = open(filename, "r")
    lines = f.readlines()
    f.close()
    for line in lines:
        fullLine = line.split(":")
        tickers[fullLine[0]] = fullLine[1][:-1]
    return tickers

def convert(dictionary,search):
    for key, value in dictionary.items():
        if key == search:
            return "Ticker symbol: "+value
        elif value == search:
            return "Company name: "+key
    return "Not found.."

tickers = ticker("tickers.txt")
print(convert(tickers,input("Geef de ticker van het bedrijf: ")))
print(convert(tickers,input("Geef de bedrijfsnaam: ")))