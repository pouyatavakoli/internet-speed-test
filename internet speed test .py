#testing internet speed using python 
# make sure to read the readme.md file and follow instructions
  
import speedtest   

# making options for different functions 
st = speedtest.Speedtest() 
  
option = int(input('''What speed do you want to test:   
  
1) Download Speed   
  
2) Upload Speed   
  
3) Ping  
  
Your Choice: ''')) 
  
# what should each option do 
if option == 1:   
  
    print(st.download())   
  
elif option == 2:  
  
    print(st.upload())   
  
elif option == 3:   
  
    servernames =[]   
  
    st.get_servers(servernames)   
  
    print(st.results.ping)   
# if user enters wrong option 
else: 
  
    print("Please enter the correct choice !")