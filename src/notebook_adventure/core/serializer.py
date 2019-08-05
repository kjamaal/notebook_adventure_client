'''serializer / de-serializer module

'''
import pickle

def serialize(data):
  return pickle.loads(data)

def de_serialize(string):
  return pickle.dumps(string)
