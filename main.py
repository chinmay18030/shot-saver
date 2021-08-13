from tkinter import *
import tkinter
import pyautogui
import PIL.Image, PIL.ImageTk
import cv2
import numpy as np
import time
import os
import keyboard
import datetime
import os 
import keyboard
from PIL import ImageTk
import win32clipboard as clip
import win32con
from io import BytesIO
from PIL import ImageGrab



if os.path.exists("screenshots"):
    pass 
else:
    os.mkdir("screenshots")

lst = os.listdir("screenshots")

for i in lst:
    os.remove("screenshots/"+i)
x = datetime.datetime.now()


a = 0
def screenshot():
    global a
    ss = pyautogui.screenshot()
    ss = np.array(ss)
    cv_img = cv2.cvtColor(ss,cv2.COLOR_BGR2RGB)
    cv_img = cv2.resize(cv_img,(650,380))
    a+=1
    cv2.imwrite("screenshots/image"+str(a)+".png", cv_img)
    # cv2.imshow("Recent shot saved", cv_img)
    # cv2.waitKey(0)
    
    
    


while True:
    if keyboard.is_pressed("shift + a"):
        time.sleep(0.1)
        screenshot()
    if keyboard.is_pressed("shift + d"):
        break



root = tkinter.Tk()
root.title("Screenshot saver")


img_no = 0
image_list = []
for i in os.listdir("screenshots"): 
	image = cv2.imread("screenshots/"+i)
	image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
	photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(image))
	image_list.append(photo)
# print(image_list)
import PIL.Image

my_label = Label(image=image_list[0])
my_label.grid(row=0, column=0, columnspan=3)

def forward(image_number):
	global my_label
	global button_forward
	global button_back
	global img_no

	
	my_label = Label(image=image_list[image_number-1])
	my_label.grid_forget()
	button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
	button_back = Button(root, text="<<", command=lambda: back(image_number-1))
	
	if image_number == 5:
		button_forward = Button(root, text=">>", state=DISABLED)

	my_label.grid(row=0, column=0, columnspan=3)
	button_back.grid(row=1, column=0)
	button_forward.grid(row=1, column=2)
	img_no+=1
	

def back(image_number):
	global my_label
	global button_forward
	global button_back
	global img_no

	my_label.grid_forget()
	my_label = Label(image=image_list[image_number-1])
	button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
	button_back = Button(root, text="<<", command=lambda: back(image_number-1))

	if image_number == 1:
		button_back = Button(root, text="<<", state=DISABLED)

	my_label.grid(row=0, column=0, columnspan=3)
	button_back.grid(row=1, column=0)
	button_forward.grid(row=1, column=2)
	img_no-=1
	
def copy():
	global img_no
	img_list = os.listdir("screenshots")
	file_path = "screenshots/"+img_list[img_no]
	image = PIL.Image.open(file_path)
	output = BytesIO()
	image.convert('RGB').save(output, 'BMP')
	data = output.getvalue()[14:]
	output.close()
	clip.OpenClipboard()
	clip.EmptyClipboard()
	clip.SetClipboardData(win32con.CF_DIB, data)
	clip.CloseClipboard()



button_back = Button(root, text="<<", command=back, state=DISABLED,)
button_exit = Button(root, text="Copy", command=copy)
button_forward = Button(root, text=">>", command=lambda: forward(2))


button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)




root.mainloop()
