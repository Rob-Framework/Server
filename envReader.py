data = []

def read():
    path = '.env'
    file = open(path, 'r')
    
    lines = file.readlines()
    for line in lines:
        d = line.strip().split('=', 1)
        if len(d) == 2:
            data.append({ 'key': d[0], 'value': d[1] })

    file.close()

def getValue(key):
    for x in data:
        if x['key'] == key:
            return x['value']
    
    return ''

def getBool(key):
    value = getValue(key)
    value = value.lower().strip()
    if value == 'true':
        return True
    elif value == 'false':
        return False