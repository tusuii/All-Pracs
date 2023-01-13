import xml.etree.ElementTree as ET   
import sys  
#importing module we created as myfun  
import mymodules as myfun  
try:
    while True:
        mytree = ET.parse('contact.xml') 
        myroot = mytree.getroot()  
        choice=int(input('What you want to do..?\n 1.List\n 2.Insert \n 3.Update \n 4.Delete \n'))  
        myfun.setXml(myroot,mytree)  
        #using python conditional statement..calls function according to choice  
        myfun.newContact(ET) if choice ==2 else ""  
        myfun.updateContact() if choice ==3 else ""     
        myfun.deleteContact() if choice ==4 else ""  
        myfun.readContact() if choice ==1 else ""     
except OSError as err:  
    print("OS error: {0}".format(err))  
except:  
    print("Unexpected error:", sys.exc_info()[0])  
    raise  