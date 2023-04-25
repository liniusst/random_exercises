from main import Projektas
from session import session

# project1 = session.query(Projektas).all()

# for project in project1:
#     print(project.name)
# print(project1.name)

project = session.query(Projektas).filter_by(name="2 projektas").first()
print(project)
