import json
from Classes import Product, Listing, Result, ProdDecoder, ListDecoder, Encoder

productFile = 'products.txt'
listingFile = 'listings.txt'
resultsFile = 'results.txt'

products = []
listings = []
results = []

print('Reading Listings File...')
list = open(listingFile)
for line in list:
  listings.append(json.loads(line, object_hook = ListDecoder))
list.close()

print('Reading Products File...')
prod = open(productFile)
for line in prod:
  product = json.loads(line, object_hook = ProdDecoder)
  result = Result(product.Name)
  results.append(result)
  for list in listings:
    if product.Model in list.Title:
      result.AddListing(list)
prod.close()

print('Writing Results File...')
resFile = open(resultsFile, 'w+')
#json.dump(results, resFile, cls = Encoder)
for res in results:
  resFile.write(json.dumps(res.Encode(), cls = Encoder) + '\n')

resFile.close()
print('Done!')
