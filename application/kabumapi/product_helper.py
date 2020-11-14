import json

class ProductHelper():
    __instance = None

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = ProductHelper()
        return cls.__instance

    def getProductByTextJson(self, textJsonProduct):
        return json.loads(textJsonProduct)
