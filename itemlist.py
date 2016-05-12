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
        return "{}".format('hello world')

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

