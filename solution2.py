#n this kata, your job is to create a class Dictionary which you can add words to and their entries. Example:
# >>> d = Dictionary()

# >>> d.newentry('Apple', 'A fruit that grows on trees')

# >>> print(d.look('Apple'))
# A fruit that grows on trees

# >>> print(d.look('Banana'))
# Can't find entry for Banana



class Dictionary():
    dic = {}

    def newentry(self, fruit, description):
        self.dic[fruit] = description

    def look(self, fruit):
        objlist = list(self.dic.keys())
        if fruit in objlist:
            print("Yes", fruit, "is in the dictionary!")
            
        else:
            print("No", fruit, "is Not in the dictionary!")
            

z=Dictionary()
z.newentry("Cherrygum", "fruit")
print(type(z))

z.look("Banana")
print(z.dic)



