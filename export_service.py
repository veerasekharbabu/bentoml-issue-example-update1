from mypackage1.service import Service
from mypackage2.model import MySVC

service = Service()
service.pack("model", MySVC())  # MySVC could be loaded from a checkpoint instead
service.save()
