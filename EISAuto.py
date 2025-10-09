from pywinauto import Application, keyboard
import time

def EISAuto():
    #Preliminary code with be written to use Notepad
    app = Application().start("notepad.exe")
    time.sleep(0.2)

    dlg = app.UntitledNotepad

    edit = dlg.Edit
    edit.type_keys("Hello! This is the Notepad Explorer Test V1", with_spaces=True)

    dlg.type_keys("%F")
    time.sleep(0.2)
    dlg.type_keys("A")
    #Sequence should end with Save As dialog open on screen



