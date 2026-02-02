# Passing multiple arguments

# Chicken
# items : kebabs, fried, crispy, Tandoori, Mandi
# based on the requirement -> we can pass the single or multiple arguments

def chicken(*items):
    print(items)

Rahul = chicken("Kebabs")
Aman = chicken("fried", "crispy")
Mani = chicken("fried", "crispy", "Tandoori")
Reddy = chicken("poluv", "Egg", "Mutton", "Keema", "Biryani")
