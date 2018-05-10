import arcpy
import pythonaddins

class ExplosionButtonClass(object):
    """Implementation for addin_addin.explosionbutton (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pythonaddins.MessageBox("pre-script test","window1")
        object = pythonaddins.GPToolDialog("m:/Documents/Programming2/Prac1/Models.tbx", "ExplosionScript")
        pythonaddins.MessageBox("post-script test","windonw2")
