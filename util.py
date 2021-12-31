
# Get value if exists from dic
def get_value(dict, key):
    if key in dict:
        return dict[key]
    else:
        return None

def flatten(t):
    return [item for sublist in t for item in sublist]
