myroot=''  
def setXml(root,tree):  
    global myroot  
    global mytree  
    myroot=root  
    mytree=tree  
# Function to list all xml elements      
def readContact():  
    global myroot  
    for contact in myroot.findall('contact'):  
        contactId=contact.attrib['id']  
        name=contact.find('name').text  
        address=contact.find('address').text  
        phone=contact.find('phone').text  
        print("  Name =",name,"\n"," Address =",address,"\n",  
        " Phone =",phone,"\n"," Id =",contactId)  
        print("----------------------------")  
    input("Press any key to continue...")      
# Function to return next element id          
def getId():  
    global myroot  
    temp = 0  
    for contact in myroot.findall('contact'):  
        id= int(contact.attrib['id'])  
        if id>temp:  
            temp=id  
    return temp+1       
# Function to create a new element         
def newContact(ET):  
    global myroot  
    global mytree  
    print("Create a record")  
    name=input("Name:")  
    address=input("Address:")  
    phone=input("Phone:")          
    nextId=getId()  
    newrecord = ET.SubElement(myroot, "contact",id=str(nextId))  
    ET.SubElement(newrecord, "name", name="name").text = name  
    ET.SubElement(newrecord, "address", name="address").text = address  
    ET.SubElement(newrecord, "phone", name="phone").text = phone  
    mytree.write("contact.xml")    
    print("Contact created...")  
# Function to delete a element          
def deleteContact():  
    global myroot  
    global mytree  
    deleteRecord=int(input("Enter the id of the contact you want to delete: "))  
    #loop through all id's  
    for contact in myroot.findall('contact'):  
        delid= int(contact.attrib['id'])  
        if delid == deleteRecord:  
            myroot.remove(contact)              
            mytree.write("contact.xml")  
            print("Contact deleted...")      
# Function to update a element  
def updateContact():  
    global myroot  
    global mytree  
    updateRecord=int(input("Enter the id of contact you want to update: "))  
    for contact in myroot.findall('contact'):  
        upid= int(contact.attrib['id'])  
        if upid == updateRecord:  
            #first we will select all current values  
            name = contact.find('name').text  
            address = contact.find('address').text  
            phone = contact.find('phone').text  
           #update..the or input means if input is empty keep old value  
            name = input("Please enter name:") or name  
            contact.find('name').text= name  
            address = input("Please enter address:") or address  
            contact.find('address').text= address  
            phone = input("Please enter phone:") or phone  
            contact.find('phone').text= phone  
            mytree.write("contact.xml")  
            print("Contact updated...")