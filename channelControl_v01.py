#Python ChannelControl_v1.0.py create date 2015-06-01 made by ChanSteve  
import maya.cmds as cmds

#Edit Translate Check Box Value.
def checkBoxVal(inputAttr):
	inputAttrVal = cmds.checkBox(inputAttr, query=True, v=True)
	if inputAttr == "tx":
		attrs = ['tx', 'ty', 'tz']
	elif inputAttr == "rx":
		attrs = ['rx', 'ry', 'rz']
	elif inputAttr == "sx":
		attrs = ['sx', 'sy', 'sz']
		
	if inputAttrVal == True:
		for attr in attrs:
			cmds.checkBox(attr, v=0, e=1)
	    
	if inputAttrVal == False:
		for attr in attrs:
			cmds.checkBox(attr, v=1, e=1)
        
#Operation
def operation():
	sels = cmds.ls(sl=True)
	attrs = ['tx','.ty','tz','rx','ry','rz','sx','.sy','.sz','.v']
	for sel in sels:
	    for attr in attrs:
	        chBoxValue = cmds.checkBox(attr, query=True, v=True)
	        if chBoxValue == True:
	            cmds.setAttr (sel + "." + attr, lock=False, keyable=True)
	        if chBoxValue == False:
	            cmds.setAttr (sel + "." + attr, lock=True, keyable=False)
	        
#Channel control window   
def channelControl():
    
	windowID = 'channelControlWindowID'
	
	if cmds.window( windowID, exists=True ):
		cmds.deleteUI( windowID )
    
	cmds.window(windowID,title = 'Channel Control', sizeable = 1, rtf=1, toolbox=1)

	cmds.rowColumnLayout (numberOfColumns = 5, columnWidth = [(1,50), (2,20), (3,20), (4,20), (5,35) ])

	cmds.separator( style='none' )
	cmds.text ( label='X' )
	cmds.text ( label='Y' )
	cmds.text ( label='Z' )
	cmds.separator( style='none' )

	cmds.text ( label='Translate' )
	cmds.checkBox('tx', label='', v=1)
	cmds.checkBox('ty', label='', v=1)
	cmds.checkBox('tz', label='', v=1)
	cmds.button (label='A', command="checkBoxVal('tx')")

	cmds.text ( label='Rotate' )
	cmds.checkBox('rx', label='', v=1)
	cmds.checkBox('ry', label='', v=1)
	cmds.checkBox('rz', label='', v=1)
	cmds.button (label='A', command="checkBoxVal('rx')")

	cmds.text ( label='Scale' )
	cmds.checkBox('sx', label='', v=1)
	cmds.checkBox('sy', label='', v=1)
	cmds.checkBox('sz', label='', v=1)
	cmds.button (label='A', command="checkBoxVal('sx')")

	cmds.text ( label='visibility' )
	cmds.separator( style='none' )
	cmds.separator( style='none' )
	cmds.checkBox('vis', label='', v=1)
	cmds.separator( style='none' )
	
	cmds.separator( style='none' )
	cmds.separator( style='none' )
	cmds.separator( style='none' )
	cmds.separator( style='none' )
	cmds.button (label='Apply', command='operation()')
	
	cmds.showWindow(windowID)    

channelControl()

