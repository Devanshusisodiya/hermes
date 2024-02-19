from hermes.storage import Storage
from hermes.layer import TransactionLayer

# initialising an agents storage 
storage = Storage()

# initialising a communication layer
layer = TransactionLayer(storage=storage)