def check_installed(pkg):
    try:
        __import__(pkg)
        return(True)
    except ModuleNotFoundError:
        return(False)

#install package
def install(package):
    import subprocess,sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

#creating a shortcut to this file on the desktop, if it doesn't exist
if not check_installed('winshell'):
    install('winshell')
    install('pypiwin32')
import winshell,os

from win32com.client import Dispatch

desktop = winshell.desktop()
path=os.path.join(desktop, "GéoQuiz.lnk")
target=os.path.join(os.path.dirname(os.path.abspath(__file__)), "main_fix.py")
wDir = desktop
icon=os.path.join(os.path.dirname(os.path.abspath(__file__)), "geoquiz.ico")
shell=Dispatch('WScript.shell')

shortcut=shell.CreateShortCut(path)
shortcut.Targetpath=target
shortcut.WorkingDirectory=wDir
shortcut.IconLocation=icon
shortcut.save()
