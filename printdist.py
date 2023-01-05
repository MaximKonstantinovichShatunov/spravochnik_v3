def print_str(data):
    for v in data:
        print(v)
        
    
def print_list(data):
    for i in data:
        if i != '':
            for j in i.split(', '):
                print(j)
        print()

            