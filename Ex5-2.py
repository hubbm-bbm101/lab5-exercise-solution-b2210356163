 x=(str(input("Please enter a valid e-mail:")))
 
 def emailfunc():
   if '@' in x:
     if '.' in x:
            
            print (x," is a valid e-mail")
     else:
            
            print (x, " is not a valid e-mail")
   else:
     
     print (x ," is not a valid e-mail")
 emailfunc()     