from kivy.app import App
from kivy.lang import Builder
from HeylonWhiteA1 import load_items
from HeylonWhiteA1 import save_items
import item
import itemlist

ITEMS_FILE = "items.csv"

class ItemsForHire(App):

    def __init__(self, **kwargs):
        super(ItemsForHire, self).__init__(**kwargs)
        #Load items
        item_list_of_tuples = load_items(ITEMS_FILE)
        self.item_list = itemlist.ItemList(item_list_of_tuples)

    def build(self):
        self.title = "Items for hire"
        self.root = Builder.load_file('app.kv')
        return self.root

    def on_stop(self):
        print("Bye")





ItemsForHire().run()