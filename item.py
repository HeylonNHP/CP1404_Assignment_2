class Item:
    def __init__(self, name="", description="", cost=0.00, on_hire=False):
        self.name = name
        self.description = description
        self.cost = cost
        self.on_hire = on_hire

    def __str__(self):
        return "{}".format(self.name)

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost

    def get_hired_out_status(self):
        return self.on_hire

    def set_hired_out_status(self, on_hire=False):
        self.on_hire = on_hire
