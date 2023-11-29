import requests

r = requests.get(f"https://itunes.apple.com/search?term={input('Please enter a search term:')}&entity=album").json()

print(f"The search returned {r.get('resultCount')} results.")

for i in range(r.get('resultCount')):
    print(f"Artist: {r.get('results')[i].get('artistName')} - Album: {r.get('results')[i].get('collectionName')} - Track Count: {r.get('results')[i].get('trackCount')}")