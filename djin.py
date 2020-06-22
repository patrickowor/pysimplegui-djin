import tkinter # optional only use this if the program return a call back error 
import PySimpleGUI as sg
import wolframalpha 
import os


app_id = 'enter your App ID here'
client = wolframalpha.Client(app_id)

#the gui 
layout = [[sg.T('              DJIN     ',font=("Helvetica",30,"bold"),background_color='white',text_color='red')],
         [sg.T('                                           your online genie',background_color='white',text_color='green')],      
		 [sg.Image('ai.gif')],	 
		  [sg.Multiline(default_text='ask anything ...',key='__search__', size=(50,1)),],
		  [sg.T("                                      ",background_color='white'),sg.Submit(), sg.Exit()],
		  [sg.T("                                    ", background_color='white', text_color='green', key='status')],
		  [sg.T("                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       ",background_color='white', text_color='black', key ='result')]]
		  

#the main window
window = sg.Window('DJIN your online genie', layout,resizable=True, size=(1000,1700), background_color='white')
# looping the window to keep it from exiting itself
while True:
	event, values = window.Read()
	if event is None or event == 'Exit':
		break
	elif  'ask anything ...' in values['__search__']:
	    sg.Popup("sorry you didn't type anything ")
	else:
	    question =  values['__search__']
	    try:
                #getting my results and displaying it
	        res = client.query(question)
	        window['status'].update('loading...          ')
	        answer = next(res.results).text
	        __answer = answer.replace('. ', '.\n')
	        window['status'].update('answer:         ')
	        window['result'].update(__answer)
	    except:
	        sg.Popup("sorry no internet connection ")
	    
window.Close()
