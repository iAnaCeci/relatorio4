from database import Database
from writeAJson import writeAJson


class ProductAnalyzer:
    db = None
    def __int__(self):
        db = Database(database="mercado", collection="compras")

        pass
    def total(self):

        result = self.db.collection.aggregate([

            {"$unwind": "$produtos"},
            {"$group": {"_id": "$cliente_id",
                        "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},

        ])
        writeAJson(result, 'Total')


    def mais_vendido(self):
        result = self.db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.descricao", "total": {"$sum": "$produtos.quantidade"}}},
            {"$sort": {"total": -1}},

        ])
        writeAJson(result, 'Mais Vendido')

    def mais_gastou(self):
        result = self.db.collection.aggregate([
                {"$unwind": "$produtos"},
                {"$group": {"_id": {"cliente": "$cliente_id", "data": "$data_compra"}, "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
                {"$sort": {"_id.data": 1, "total": -1}},
                {"$group": {"_id": "$_id.data", "cliente": {"$first": "$_id.cliente"}, "total": {"$first": "$total"}}},
                {"$limit": 1}

            ])

        writeAJson(result, 'Mais Gastou')


    def acima_de_um(self):
        result = self.db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.descricao", "quantidade": {"$sum": "$produtos.quantidade"} }},
            {"$match":{"quantidade":{"$gt":1}}}
            # {"$sort": {"maior": -1}},

        ])
        writeAJson(result, 'Acima de um')



