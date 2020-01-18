import json

class keys(object):
    def __init__(self, raw_string):
        # Get the string and convert to a dict using JSON
        if raw_string != '':
            self.keysd = json.loads(raw_string)
        # If string is empty, dict is empty too
        else:
            self.keysd = {}
    
    def add(self, secret, title='None'):
        for k, i in self.keysd.items():
            if i == title:
                raise Exception('Title already in use, please choose a diferent one')
        self.keysd.update({title:secret})
    
    def __str__(self):
        # Convert the  dict to string using JSON
        return json.dumps(self.keysd)
    
    def remove(self, arg):
        for title, secret  in self.keysd.items():
            if title == arg:
                # 'False' is for the method .pop() don't raise any error
                self.keysd.pop(title, False)
                return True
        return False
    
    def get(self, title):
        # Search by title
        for k,i in self.keysd.items():
            if i == title:
                return {k:self.keysd[k]}
        return False
