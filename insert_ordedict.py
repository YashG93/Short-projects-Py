from collections import OrderedDict

order_dict=OrderedDict([('b',2),('c',3),('d',4)])

new_item=OrderedDict([('a',1)])

new_item.update(order_dict)

print(new_item)