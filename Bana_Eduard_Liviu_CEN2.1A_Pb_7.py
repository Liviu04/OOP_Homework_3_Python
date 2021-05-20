

#we use this"person_list"to help us with the next operations between persons
person_list = []
class Family_tree():

    def __init__(self):
        #we use a list of lists to add all members of a person's family
        self.family_tree = {"sibling": [], "parent": [], "grandparent": [], "children": []  ,"ancestor": [], 'spouse':[],"uncle":[],"brother-in-law":[]}

class Person:

    def __init__(self, name,name_of_family,gender):
        self.name = name
        self.name_of_family=name_of_family
        self.gender=gender
        self.family_tree = Family_tree().family_tree
        #person_list.append(self)
    #the above functions are used to create the kinship relations between persons
    def add_parents(self, parent_one, parent_two):
        self.family_tree['parent'].append(parent_one)
        if parent_one not in parent_two.family_tree['spouse']:
            parent_two.family_tree['spouse'].append(parent_one)
        self.family_tree['parent'].append(parent_two)
        if parent_two not in parent_one.family_tree['spouse']:
            parent_one.family_tree['spouse'].append(parent_two)
        if self not in parent_one.family_tree['children']:
            parent_one.add_children(self)
        if self not in parent_two.family_tree['children']:
            parent_two.add_children(self)

        for child in self.family_tree['children']:
            if parent_one not in child.family_tree['grandparent']:
               child.family_tree['grandparent'].append(parent_one)
            if parent_two not in child.family_tree['grandparent']:
               child.family_tree['grandparent'].append(parent_two)

        for grandparent in parent_one.family_tree['parent']:
                self.family_tree['grandparent'].append(grandparent)  
        for grandparent in parent_two.family_tree['parent']:
                self.family_tree['grandparent'].append(grandparent)


        # Adds the parents as ancestors of the Person 
        if parent_one not in self.family_tree['ancestor']:
            self.family_tree['ancestor'].append(parent_one)
        for ancestor in parent_one.family_tree['ancestor']:
            if ancestor not in self.family_tree['ancestor']:
                self.family_tree['ancestor'].append(ancestor)

        if parent_two not in self.family_tree['ancestor']:
            self.family_tree['ancestor'].append(parent_two)
        for ancestor in parent_two.family_tree['ancestor']:
            if ancestor not in self.family_tree['ancestor']:
                self.family_tree['ancestor'].append(ancestor)


    def add_children(self, child):
        self.family_tree['children'].append(child)
        if self not in child.family_tree['parent']:
             child.add_parents(self,self.family_tree['spouse'][-1])

        if len(self.family_tree['children'])!=1:
           for child_1 in self.family_tree['children']:
              for child_2 in self.family_tree['children']:
                if child_1.name != child_2.name and child_2 not in child_1.family_tree['sibling']:
                    child_1.family_tree['sibling'].append(child_2)

        if self.family_tree['sibling'] != None:
            for child_1 in self.family_tree['children']:
                for uncle in self.family_tree['sibling']:
                    if uncle not in child_1.family_tree['uncle']:
                        child_1.family_tree['uncle'].append(uncle)

        if self.family_tree['brother-in-law'] != None:
            for child_1 in self.family_tree['children']:
                for uncle in self.family_tree['brother-in-law']:
                    if uncle not in child_1.family_tree['uncle']:
                        child_1.family_tree['uncle'].append(uncle)
 
       

    def add_spouse(self, spouse):
        if self.gender == 'M':
            spouse.name_of_family=self.name_of_family
        else:
            self.name_of_family=spouse.name_of_family

        if spouse not in self.family_tree['spouse']:
            self.family_tree['spouse'].append(spouse)
            for sibling in spouse.family_tree['sibling']:
                self.family_tree['brother-in-law'].append(sibling)
                sibling.family_tree['brother-in-law'].append(self)
        if self not in spouse.family_tree['spouse']:
            spouse.family_tree['spouse'].append(self)
            for sibling in self.family_tree['sibling']:
                spouse.family_tree['brother-in-law'].append(sibling)
                sibling.family_tree['brother-in-law'].append(spouse)

    def get_divorce(self,spouse):
        if self.family_tree["spouse"][-1]==spouse:
            if self.gender=='F':
                self.name_of_family=self.family_tree['parent'][-1].name_of_family
            else:
                spouse.name_of_family=spouse.family_tree['parent'][-1].name_of_family
            spouse.family_tree["spouse"].clear()
            self.family_tree["spouse"].clear()
            self.family_tree["brother-in-law"].clear()
            spouse.family_tree["brother-in-law"].clear()
            
        else:
            print("They are not in a relation")
            


    

                
            

class Operations():

     

    def list_relation(self, person_name, relation):
    #determine for a person: the list of persons with a specified degree of kinship (with the current person)
        sorted_relations = []
        for person in person_list:
            if person_name == person.name:
                for family_member in person.family_tree[relation]:
                    #print(person.family_tree[relation])
                    sorted_relations.append(family_member.name +" "+ family_member.name_of_family)
        
        for member in sorted(sorted_relations):
            if member != person_name:
                print(member)
                

    def is_relation(self, person_name_one, person_name_two, relation):
        #  Checks to see if person_one has RELATION with person_two
        #  All the above attributes are strings
        #  Returns true or false
        
        for person in person_list:
            if person_name_one == person.name:
                for person_2 in person_list:
                    if person_name_two == person_2.name:
                        if person_2 in person.family_tree[relation]:
                            print("Yes")
                            
                            return
                        else:
                            print("No")
                            
                            return
        
        print("No")

    def closest_relation(self, person_two, person_one):
        #determine for two people if there is a degree of kinship between them and what is that (spouse, parent, sibling, grandparent,
        #his child, uncle, brother-in-law).
        if person_two in person_one.family_tree["spouse"]:
            print("spouse")
            
            return
        if person_two in person_one.family_tree["parent"]:
            print("parent")
           
            return
        if person_two in person_one.family_tree["sibling"]:
            print("sibling")
            
            return
        if person_two in person_one.family_tree["brother-in-law"]:
            print("brother-in-law")
            
            return
        if person_two in person_one.family_tree["uncle"]:
            print("uncle")
          
            return

        if person_two in person_one.family_tree["children"]:
            print("child")
            return
        if person_two in person_one.family_tree["grandparent"]:
            print("grandparent")
            return
        if person_two in person_one.family_tree["ancestor"]:
            print("ancestor")
            return
        else:
            print("Unrelated")
            return

def retrieve_person(person_name,name_of_family,gender):
    #we use this function to create a person and to add his name in a "person_list"
    for person in person_list:
        if person.name == person_name:
            return person

    x = Person(person_name,name_of_family,gender)
    person_list.append(x)
    return x


op = Operations()
person_1=retrieve_person("Mihai","Popescu",'M')
person_2=retrieve_person("Ionela","Iliuta",'F')
person_1.add_spouse(person_2)
person_3=retrieve_person("George","Anghel",'M')
person_4=retrieve_person("Maria","Barbu",'F')
person_4.add_spouse(person_3)

person_5=retrieve_person("Daniel","Popescu",'M')
person_1.add_children(person_5)
person_6=retrieve_person("Bogdan","Popescu",'M')
person_1.add_children(person_6)
person_7=retrieve_person("Roberta","Popescu",'F')
person_1.add_children(person_7)
person_8=retrieve_person("Denisa","Anghel",'F')
person_3.add_children(person_8)
person_9=retrieve_person("Sergiu","Anghel",'M')
person_3.add_children(person_9)

person_6.add_spouse(person_8)
person_10=retrieve_person("Stefan","Popescu",'M')
person_6.add_children(person_10)
print(person_3.name,person_3.name_of_family,"'s children are:")
op.list_relation(person_3.name,"children")
print("The relation between",person_6.name,person_6.name_of_family,"and",person_9.name,person_9.name_of_family,"is:")
op.closest_relation(person_6,person_9)
print(person_10.name,person_10.name_of_family,"'s grandparents are:")
op.list_relation(person_10.name,"grandparent")
print(person_10.name,person_10.name_of_family,"'s uncles are:")
op.list_relation(person_10.name,"uncle")
print("The relation between",person_5.name,person_5.name_of_family,"and",person_6.name,person_6.name_of_family,"is:")
op.closest_relation(person_5,person_6)
print(person_8.name,person_8.name_of_family,"'s siblings are:")
#the family name of person_8 is different from that of his sibling because person_8 has a spouse and is a woman
#she got her husband's name 
op.list_relation(person_8.name,"sibling")

print ("the relation between",person_6.name,person_6.name_of_family,"and",person_8.name,person_8.name_of_family,"is:")
op.closest_relation(person_1,person_2)
print(person_6.name,person_6.name_of_family,"'s brothers-in-law are:")
op.list_relation(person_6.name,"brother-in-law")
print(person_8.name,person_8.name_of_family,"'s brothers-in-law are:")
op.list_relation(person_8.name,"brother-in-law")
person_6.get_divorce(person_8)
print ("the relation between",person_6.name,person_6.name_of_family,"and",person_8.name,person_8.name_of_family,"after divorce is:")
op.closest_relation(person_6,person_8)
print(person_6.name,person_6.name_of_family,"'s brothers-in-law are:")
op.list_relation(person_6.name,"brother-in-law")
print(person_8.name,person_8.name_of_family,"'s brothers-in-law are:")
op.list_relation(person_8.name,"brother-in-law")

print("the",person_10.name,person_10.name_of_family,"parents are:")
op.list_relation(person_10.name,"parent")