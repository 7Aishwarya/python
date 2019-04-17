class Store:
    _item_count = 100
 
    @classmethod
    def addItem(cls, count):
        cls._item_count += count
    @classmethod
    def issueItem(cls, count):
        cls._item_count -= count
        
    @staticmethod
    def getItemCount():
        return Store._item_count
 
counter1 = Store()
counter1.addItem(2)
counter1.issueItem(1)
print(counter1.getItemCount())
