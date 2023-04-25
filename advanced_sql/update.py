from main import Projektas
from session import session

projektas1 = session.query(Projektas).get(1)
projektas1.price = 21000
session.delete(projektas1)
session.commit()
