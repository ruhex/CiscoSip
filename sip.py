import urllib.request
from tkinter import *
from re import I, compile, findall
import xml.etree.ElementTree as etree

tree = etree.parse("C:\Temp\config.xml")
root = tree.getroot()
phoneslist = []
ip_str = ('http://' + root[1].text + '/pdir.htm').replace("\n","")
print(ip_str)
req = urllib.request.Request(ip_str)
with urllib.request.urlopen(req) as response:
	the_page = response.read()
st = "".join(map(chr, the_page))
massiv = compile(r'name="([^"]*)" value="([^"]*)"', I).findall(st)
massiv2 = {}
pattern = re.compile('(n=[\d]+).*(p=[\d\.])')



for phone in massiv:
	
	
	
	name = compile(r'n=([^]*);p=([^]*)', I).findall(phone[1])
	phn = compile(r'p=([^]*); p=([^]*)', I).findall(phone[1])
	
	phoneslist.append(name + phn)
	
	
	

for el in root:
	massiv.append(el.text)
	
def phoneAdd(name, number):
	phoneslist.append({name:number})

def phonesRefr():
		for i in phoneslist:
			phones.insert(END, i)
		print(phoneslist)
		

def XmlSave(ip):
	massiv[1] = ip
	root[1].text = ip.replace("\n","")
	etree.ElementTree(root).write("C:\Temp\config.xml")
	
def test():
    lb["text"] = massiv[1]

def InfoGUI():
	mGuiInfo = Tk()
	mGuiInfo.title('Info')
	Label(mGuiInfo, text="Version: ").grid(row=0, column=0)
	Label(mGuiInfo, text = massiv[0]).grid(row=0, column=1)	
	
def SettingGUI():
	mGuiSet=Tk()
	mGuiSet.title('Setting')	
	Label(mGuiSet, text='Ip phone:').grid(row=0)	
	textip=Text(mGuiSet,height=1,width=40)
	textip.grid(row=0, column=1)
	textip.insert(1.0,massiv[1])
	buttonSave=Button(mGuiSet,text='save',font='arial 8', command=lambda:XmlSave(textip.get('1.0', END))).grid(row=0,column=3)


mGui=Tk()
mGui.title('Cisco sip config')

#Menu
menu = Menu(mGui, tearoff = 0)
menu.add_command(label="Настройка", command=SettingGUI)
menu.add_command(label="О программе", command=InfoGUI)
mGui.config(menu=menu)
phones=Listbox(mGui,height=10,width=100,selectmode=SINGLE)
for i in phoneslist:
	phones.insert(END, i)
phones.grid(sticky='nwe', columnspan=2)
Label(mGui, text='Name:').grid(row=1, column=0)
Label(mGui, text='Phone:').grid(row=2, column=0)
textName = Text(mGui,height=1)
textPhone = Text(mGui,height=1)
textName.grid(row=1, column=1)
textPhone.grid(row=2, column=1)
buttonAdd=Button(mGui,text='Add',font='arial 8', command=lambda:phoneAdd(
						textName.get('1.0', END), textPhone.get('1.0', END))).grid(sticky='nwe',row=3,column=0)
buttonCommit=Button(mGui,text='Commit',font='arial 8', command=phonesRefr).grid(sticky='nwe',row=3,column=1)




mGui.mainloop()