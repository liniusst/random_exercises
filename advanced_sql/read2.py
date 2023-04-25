from main import Projektas
from session import session

search = session.query(Projektas).filter(Projektas.name.ilike("2%"))
search2 = session.query(Projektas).filter(Projektas.price > 1000)
search3 = session.query(Projektas).filter(
    Projektas.price > 1000, Projektas.name.ilike("2%")
)

# print(search)
# print([i for i in search])
# print([i for i in search2])
# print([i for i in search3])
price_sum = 0
for i in search2:
    price_sum += i.price

print(price_sum)
