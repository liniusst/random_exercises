from main import Projektas
from session import session

projektas1 = Projektas("Naujas pr.", 20000)
session.add(projektas1)
session.commit()

projektas2 = Projektas("2 projektas", 55000)
session.add(projektas2)
session.commit()
