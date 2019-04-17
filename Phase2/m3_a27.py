class Open_File:
   def openf(self,file_loc):
        try:
            file = open(file_loc,"r+")
            print(file.read())
            file.write("Hello")
            
        except Exception as e:
            print(e)
        
        finally:
            file.close()
 
c = Open_File()
loc = input("Enter file location: ")
c.openf(loc)
