from pywinauto import Application, keyboard
import time
import EISAuto

def main():
    #Run files and operate full system
    EISAuto.EISAuto()
    print("The sequence has been completed.")
    time.sleep(1)
    print("You should now see the SaveAs dialog")

main()
