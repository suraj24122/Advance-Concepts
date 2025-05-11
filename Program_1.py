# getters and setters

class student:
    def __init__(self):
        self._name = ""

    def get_name(self):
        return self._name
    
    def set_name(self, name):
        self._name = name

#object
s1 = student()
s1.set_name("Suraj")
print(s1.get_name())