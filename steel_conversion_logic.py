from PyQt6.QtWidgets import *
from gui import *


class Logic(QMainWindow, Ui_MainWindow):

    
    flange_thickness = {
        
        "B" : "3/16",
        "C" : "7/32",
        "D" : "1/4",
        "E" : "5/16",
        "F" : "3/8",
        "H" : "1/2",
        "I" : "5/8",
        "J" : "3/4",
        "K" : "7/8",
        "L" : "1"
        
                    }
    
    web_thickness = {
        
       "WL" : "1/8",
       "WA" : "5/32",
       "WB" : "3/16",
       "WC" : "7/32",
       "WD" : "1/4",
       "WE" : "5/16",
       "WF" : "3/8",
       "WH" : "1/2",
       "WI" : "5/8",
       "WJ" : "3/4"
        
                    }
    
    material_thickness = {
        
        "4" : "14",
        "2" : "12"
                         }
    
    
    
    def __init__(self) -> None:
        """
        initializes the application
        """
        super().__init__()
        self.setupUi(self)
        

    
    def convertted(self) -> None:
        """
        After checking a radio button and entering the part number
        checks which member is needed to be converted and outputs all
        Part data.
        """
        #Primary
        try:
            if self.radioButton1.isChecked():
                
                part_num = self.part.text()
                
                x = list(part_num)
                
                #Primary
                if x[0] !="W":
                    raise IndexError
                    
                if (x[1].isdigit() == False) or (x[2].isdigit() == False): 
                    raise IndexError
                else:
                    beam_depth = x[1] + x[2]
                
                if (x[3].isdigit() == False):
                    raise IndexError
                else:
                    flange_width = x[3]
                    
                if x[4] != "0":
                    raise IndexError
                
                
                flange_thick = x[5]
                if Logic.flange_thickness.get(flange_thick) == None:
                    raise IndexError
                web_thick = x[6] + x[7]
                if Logic.web_thickness.get(web_thick) == None:
                    raise IndexError


                self.result.setText(f" Build-Up Member\n Beam Depth: {beam_depth}\"\n Flange Width: {flange_width}\"\n Flange_Thickness: {Logic.flange_thickness.get(flange_thick)}\"\n Web Thickness: {Logic.web_thickness.get(web_thick)}\"")
        
            #Secondary
            elif self.radioButton2.isChecked():
                part_num = self.part.text()
                
                x = list(part_num)
                
                if (x[0].isdigit() == False) or (x[1].isdigit() == False): 
                    raise IndexError
                else:                
                    member_depth = x[0] +x[1]
                    
                if x[2] !="X":
                    raise IndexError
                
                if (x[3].isdigit() == False) or (x[4].isdigit() == False):
                    raise IndexError
                else:
                    if x[4] == '5':
                        flange_width = x[3] + " 1/2"
                    else:
                        flange_width = x[3]
                        
                if (x[5] == "Z") or (x[5] == "C"):
                    member_type = x[5] +"ee"
                else:
                    raise IndexError
                
                if (x[6].isdigit() == False) or (x[7].isdigit() == False):
                    raise IndexError
                else:
                    material_thickness = x[6] + x[7]
                
                
                self.result.setText(f" Secondary Member\n Member Depth: {member_depth}\"\n Flange Width: {flange_width}\"\n Member Type: {member_type}\n Member Thickness: {material_thickness} Guage")
                
            # Eave Strut
            elif self.radioButton3.isChecked():
                part_num = self.part.text()
                
                x = list(part_num)
                
                if (x[0].isdigit() == False) or (x[1].isdigit() == False):
                    raise IndexError
                else:
                    nominal_depth = x[0] + x[1]
                    
                    
                material_thickness = x[2]
                if Logic.material_thickness.get(material_thickness) == None:
                    raise IndexError
                
                if (x[3] != "D") or (x[4] != "U"):
                    raise IndexError

                if (x[5].isdigit() == False) or (x[6].isdigit() == False):
                    raise IndexError
                else:
                    roof_pitch = x[5] + x[6]
                    
                if x[7] != 's':
                    raise IndexError
                
                self.result.setText(f" Eave Strut\n Nominal Depth: {nominal_depth}\"\n Material Thickness: {Logic.material_thickness.get(material_thickness)} Guage\n Roof Pitch: {roof_pitch}")
            
            else:
                self.result.setText("No operation selected")
        except IndexError:
            self.result.setText('Enter Correct Part Number')
        except TypeError:
            self.result.setText('Values must be positive')            
        
    def clearred(self) -> None:
        """
        Clears the conversion menu and resets the application
        """
      
        for radioButton in [self.radioButton1, self.radioButton2, self.radioButton3]:
            radioButton.setAutoExclusive(False)
            radioButton.setChecked(False)
            radioButton.setAutoExclusive(True)
        self.part.setText("")
        self.result.setText("")
  
        
    