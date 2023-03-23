from ProductAnalyzer import ProductAnalyzer
from database import Database
from writeAJson import writeAJson

db = Database(database="mercado", collection="compras")
db.resetDatabase()

prod = ProductAnalyzer()
prod.db = db
prod.total()
prod.mais_vendido()
prod.mais_gastou()
prod.acima_de_um()