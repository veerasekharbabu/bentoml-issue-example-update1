from mypackage.service import Service
from mypackage1.model import MySVC

service = Service()
service.pack("model", MySVC())  # MySVC could be loaded from a checkpoint instead
service.save()