def count_ips(filename):
    #create an empty dictionary 
    file_list=[]
    #open the file in read-only ('r')
    #use with-statement to automatically close the file/release memory after operation
    with open(filename, 'r') as file: 
        myIps_list = [line.strip().split('- -')[0] for line in file]
        myIps_set = set(myIps_list) #gives unique values
        my_dict = {i:myIps_list.count(i) for i in myIps_list} # counts number of ip calls per ip adress and assigns count-value to ip-address key

        return my_dict

# only run the code inside the if statement when the program is run directly by the Python interpreter. 
# #The code inside the if statement is not executed when the file's code is imported as a module.
if __name__ == '__main__' : 
   print(count_ips('logfile.txt'))
