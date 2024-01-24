# keywords
# for parameter use the key[data]
def get_product(**product):
    print(product["id"], product["name"], product["desc"], product["color"])

    if product["name"] == "xxphone":
        print("Product :", product["name"], "in stock")
    else:
        print("Product :", product["name"], "does not exist")    
    
    

# define product 
get_product(id="203",
            name="iphone", 
            desc="It's an iPhone",
            color="black" 
            )