import arcpy
import pythonaddins


class ExplosionButtonClass(object):
    """Implementation for addin_addin.explosionbutton (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        if arcpy.Exists("m:/Documents/Programming2/Prac1/TEST.shp"):
            arcpy.Delete_management("m:/Documents/Programming2/Prac1/TEST.shp")
        pythonaddins.MessageBox("Deleting Test File","Clean Up")
        
        object = pythonaddins.GPToolDialog("m:/Documents/Programming2/Prac1/Models.tbx", "ExplosionScript")
 
        combobox.items = ["Test Box"]

class BonjourBoxClass(object):
    """Implementation for addin_addin.combobox (ComboBox)"""
    def __init__(self):
        self.editable = True
        self.enabled = True
        self.dropdownWidth = 'WWWWWW'
        self.width = 'WWWWWW'
    def onSelChange(self, selection):
        pythonaddins.MessageBox("Hello World","Test Box")
    def onEditChange(self, text):
        pass
    def onFocus(self, focused):
        pass
    def onEnter(self):
        pass
    def refresh(self):
        pass