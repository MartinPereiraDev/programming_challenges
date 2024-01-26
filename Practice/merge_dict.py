"""
Merge dictionary  with update() 
"""
dict_colors = {1:'Blue', 2:'Red'}
dict_colors2 =  {3:'White', 4:'Green'}

dict_colors.update(dict_colors2)

print("dictionary merge with update : ",dict_colors)

dict_colors_merge = {**dict_colors, **dict_colors2}

print("dictionary merge with ** : ", dict_colors_merge)
