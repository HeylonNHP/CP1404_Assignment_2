from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.properties import StringProperty

from HeylonWhiteA1 import load_items
from HeylonWhiteA1 import save_items
import item
import itemlist

ITEMS_FILE = "items.csv"
ITEM_IN_COLOUR = (0,0,1,1)
ITEM_OUT_COLOUR = (1,0,0,1)

class ItemsForHire(App):

    status_text = StringProperty()

    def __init__(self, **kwargs):
        super(ItemsForHire, self).__init__(**kwargs)

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

# HIRING ITEMS
    def handle_hire_items(self):
        self.root.ids.item_grid.clear_widgets()
        self.set_menu_togglebuttons("hire_items")
        self.root.ids.confirm_items.unbind()
        self.root.ids.confirm_items.bind(on_release=self.handle_confirm_hire)

        for listitem in self.item_list:
            if listitem.get_hired_out_status() == False:
                colour = ITEM_IN_COLOUR
                temp_button = ToggleButton(text=listitem.get_name(), background_color=colour)
                temp_button.bind(on_release=self.handle_hire_item_click)
            else:
                colour = ITEM_OUT_COLOUR
                temp_button = Button(text=listitem.get_name(), background_color=colour)
                temp_button.bind(on_release=self.handle_hire_item_click)

            self.root.ids.item_grid.add_widget(temp_button)

    def handle_hire_item_click(self, button_instance):
        temp_item_list = itemlist.ItemList()
        total_cost = 0.0
        for childitem in self.root.ids.item_grid.children:
            if childitem.state == "down":
                selected_item = self.item_list.get_item_by_name(childitem.text)
                temp_item_list.add_item(selected_item)
                total_cost += selected_item.get_cost()
        self.status_text = "Hiring: {} for ${:.2f}".format(temp_item_list,total_cost)

    def handle_confirm_hire(self,button_instance):
        for childitem in self.root.ids.item_grid.children:
            if childitem.state == "down":
                current_item = self.item_list.get_item_by_name(childitem.text)
                current_item.set_hired_out_status(True)
                self.item_list.set_item_by_name(childitem.text, current_item)
        self.handle_list_items()

# LISTING ITEMS

    def handle_list_items(self):
        """
        Handles events associated with clicking the list items menu toggle button
        """
        self.status_text = "Choose an action from the left menu, then select items on the right"
        self.root.ids.item_grid.clear_widgets()
        self.set_menu_togglebuttons("list_items")

        for listitem in self.item_list:
            if listitem.get_hired_out_status() == False:
                colour = ITEM_IN_COLOUR
            else:
                colour = ITEM_OUT_COLOUR

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