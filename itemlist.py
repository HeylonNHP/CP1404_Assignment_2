import item
class ItemList:
    def __init__(self, item_list_of_tuples=list([])):
        self.item_list = []
        # if list of tuples is parsed in, convert tuples to item.Item and add to ItemList
        for item_tuple in item_list_of_tuples:
            if str(item_tuple[3]).lower() == "in":
                on_hire = False
            else:
                on_hire = True
            current_item = item.Item(str(item_tuple[0]),str(item_tuple[1]),float(item_tuple[2]), on_hire)
            self.add_item(current_item)

    def __str__(self):
        returnstring = ""
        for listitem in self.item_list:
            returnstring += "{}, ".format(listitem.get_name())
        if returnstring == "":
            return "no items"
        return returnstring[0:-2]


    def __len__(self):
        return len(self.item_list)

    def __iter__(self):
        for item in self.item_list:
            yield item

    def __getitem__(self, item):
        return self.item_list[item]

    def __setitem__(self, key, value=item.Item()):
        self.item_list[key] = value

    def add_item(self, item=item.Item()):
        self.item_list.append(item)

    def get_item_by_name(self,item_name):
        for list_item in self.item_list:
            if list_item.get_name() == item_name:
                return list_item

    def set_item_by_name(self,item_name, item):
        for i in range(0,len(self.item_list)):
            if self.item_list[i].get_name() == item_name:
                self.item_list[i] = item
