from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty

from HeylonWhiteA1 import load_items
from HeylonWhiteA1 import save_items
import item
import itemlist

ITEMS_FILE = "items.csv"

class ItemsForHire(App):

    status_text = StringProperty()

    def __init__(self, **kwargs):
        super(ItemsForHire, self).__init__(**kwargs)
        self.status_text = "Choose an action from the left menu, then select items on the right"
        #Load items
        item_list_of_tuples = load_items(ITEMS_FILE)
        self.item_list = itemlist.ItemList(item_list_of_tuples)

    def build(self):
        self.title = "Items for hire"
        self.root = Builder.load_file('app.kv')
        return self.root

    def set_menu_togglebuttons(self, my_name):
        """
        Sets every other menu toggle button back to the default state
        :param my_name: name of the menu toggle button to keep 'down'
        """
        togglebutton_dict = {"list_items": self.root.ids.list_items, "hire_items": self.root.ids.hire_items,
                             "return_items": self.root.ids.return_items, "add_items": self.root.ids.add_items}
        for menu_togglebutton in togglebutton_dict.keys():
            if my_name != menu_togglebutton:
                togglebutton_dict[menu_togglebutton].state = "normal"
            elif my_name == menu_togglebutton:
                togglebutton_dict[menu_togglebutton].state = "down"

    def handle_list_items(self):
        self.root.ids.item_grid.clear_widgets()
        self.set_menu_togglebuttons("list_items")
        for listitem in self.item_list:
            if listitem.get_hired_out_status() == False:
                colour = (0,0,1,1)
            else:
                colour = (1,0,0,1)
            temp_button = Button(text=listitem.get_name(), background_color=colour)
            temp_button.bind(on_release=self.handle_list_item_click)
            self.root.ids.item_grid.add_widget(temp_button)

    def handle_list_item_click(self, button_instance):
        selected_item = self.item_list.get_item_by_name(button_instance.text)
        description = selected_item.get_description()
        cost = selected_item.get_cost()
        is_hired_out = selected_item.get_hired_out_status()
        if is_hired_out == True:
            is_hired_out = "out"
        else:
            is_hired_out = "in"
        self.status_text = "{} ({}), ${:.2f} is {}".format(button_instance.text, description, cost, is_hired_out)

    def on_stop(self):
        print("Bye")





ItemsForHire().run()