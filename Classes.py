import json
from json import JSONEncoder
from collections import OrderedDict

class Product:
  def __init__(self, name, mfg, model, date):
    self.Name = name
    self.Mfg = mfg
    self.Model = model
    self.Date = date

class Listing:
  def __init__(self, title, mfg, currency, price):
    self.Title = title
    self.Mfg = mfg
    self.Currency = currency
    self.Price = price

  def Encode(self):
    return OrderedDict([("title", self.Title), ("manufacturer", self.Mfg), 
      ("currency", self.Currency), ("price", self.Price)])

def ProdDecoder(obj):
  product = Product(obj['product_name'], obj['manufacturer'], obj['model'], 
    obj['announced-date'])
  if obj.get('family'):
    product.Family = obj['family']
  return product

def ListDecoder(obj):
  listing = Listing(obj['title'], obj['manufacturer'], obj['currency'], 
    obj['price'])
  return listing 

class Result:
  def __init__(self, name):
    self.Name = name
    self.Listings = []

  def AddListing(self, listing):
    self.Listings.append(listing)
  
  def Encode(self):
    return OrderedDict([("product_name", self.Name), 
      ("listings", self.Listings)])

class Encoder(JSONEncoder):
  def default(self, obj):
    if hasattr(obj, 'Encode'):
      return obj.Encode()
    else:
      return JSONEncoder.default(self, obj)
