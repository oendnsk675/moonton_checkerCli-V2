import re
def hapus(data, name_file):
    items = open(name_file, "r").read()
    replace = re.sub(data, "", items)
    open(name_file, "w").write(replace)
    
def clear_resource(name_file):
    user_data = [user for user in open(name_file, "r").readlines()]
    open(name_file, "w").write("")
    for s in user_data:
        if s == "\n":
            pass
        else:
            open(name_file, "a").write(s)
            
