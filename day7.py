from lib import open_file
import re

rules = open_file("7/input")
rules_dict = {}

for rule in rules:
    bags, contain = rule.split("contain")
    contain_list = [bag.replace("bags", "").replace("bag", "").replace(".", "").strip() for bag in contain.split(", ")]
    value = []
    for bag in contain_list:
        nb, name = 0, ""
        try:
            info = bag.split(" ")
            nb = int(info[0])
            name = " ".join(info[1:])
        except:
            nb, name = 0, bag.split(" ")[0]
        value.append((nb, name))
    rules_dict[bags.replace("bags", "").strip()] = value

char_regex = re.compile("[a-z]+")

def bag_contain_gold(bag_contain):
    for bag in bag_contain:
        _,name = bag
        if name == "shiny gold":
            return True
        if name in rules_dict.keys():
            if bag_contain_gold(rules_dict[name]):
                return True
    return False

def find_shiny_gold_bag():
    shiny_gold = 0
    for bag in rules_dict.keys():
        if bag_contain_gold(rules_dict[bag]):
            shiny_gold += 1
    return shiny_gold

int_regex = re.compile("[0-9]+")

def bag_count(bag_contain):
    res = 0
    for bag in bag_contain:
        nb, name = bag
        if name in rules_dict.keys():
            nb += nb * bag_count(rules_dict[name])
            res += nb
    return res

def find_shiny_gold_nb_bag():
    return bag_count(rules_dict["shiny gold"])

print("### PART 1")
print(find_shiny_gold_bag())
print("### PART 2")
print(find_shiny_gold_nb_bag())
