#creating GUI
import tkinter as tk
import speedtest
from tkinter import messagebox 

st = speedtest.Speedtest()
root = tk.Tk()
root.geometry("400 x 400")
root.title ("speed test")
root.configure(bg = "black")
font = ("Verdana", 15 , "bold")

#function to check speed

def check() :
    messagebox.showinfo("confirmation",'speed test starting ...please be patient May take up to 1min ')
    d.configure(text=str(st.download()//10**6) + "Mbps")
    u.configure(text=str(st.upload()//10**6) + "Mbps")
    p.configure(text=str(int(st.results.ping)) + "Ms")
    l.configure(text="speed test completed")

#GUI design

dspeed = tk.Label(root,text = "Download speed" , bg = "black", fg = "yellow" , font = font)
dspeed.place (x=10 , y=10)
d=tk.Label( root , text = "0 Mbps" , bg = "black" , fg= "yellow" , font = font)
d.place( x = 250 , y = 10)
upspeed = tk.Label(root,text = "Upload speed" , bg = "black", fg = "yellow" , font = font)
upspeed.place (x=10 , y= 50)
u= tk.Label(root,text = "0 Mbps" , bg = "black", fg = "yellow" , font = font)
u.place( x = 250 , y = 50)
ping = tk.Label(root,text = "Ping" , bg = "black", fg = "yellow" , font = font)
ping.place (x=10 , y=90)
p = tk.Label(root,text = "0 Ms" , bg = "black", fg = "yellow" , font = font)
p.place( x=250 , y = 90)

l= tk.Label(root,text = "click here to start Speed test" , bg = "black" , fg= "yellow" , font = (15))
l.place ( x= 50 , y = 250)
b= tk.Button(root , text = " Speed test" , command = check , bg = "yellow" , fg = "black")
b.place( x=50 , y= 300 , height = 40 , width = 300)
root.mainloop()
