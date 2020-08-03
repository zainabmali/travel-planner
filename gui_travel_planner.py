
import sys
from pyqtgraph.Qt import QtCore, QtGui
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QComboBox, QLineEdit, QLabel, QTextEdit, QPushButton, QSizePolicy


import travel_planner


class Window(QtGui.QMainWindow):
  def __init__(self):
    
    self.travel_planner = travel_planner.TravelPlanner()


    super(Window, self).__init__()

    main_layout = QtGui.QGridLayout()
    self.setWindowTitle("Travel Planner")

    # Add config layout
    configLayout = QtGui.QGridLayout()
   
    self.country_label = QLabel()
    self.country_label.setText("Country")
    self.country_box = QLineEdit()

    configLayout.addWidget(self.country_label, 0, 0, 1, 1)
    configLayout.addWidget(self.country_box, 0, 1, 1, 1)
    
    self.configGroupBox = QtGui.QGroupBox()
    self.configGroupBox.setStyleSheet("font-size: 15px;")
    self.configGroupBox.setSizePolicy(QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Fixed))
    self.configGroupBox.setLayout(configLayout)

    # Add device angle layout
    axisLayout = QtGui.QGridLayout()
    self.selection_label = QLabel()
    self.selection_label.setMaximumWidth(114)
    self.selection_label.setText("Action type")
    self.selection_box = QComboBox()
    self.selection_box.addItems(['', 'All country information', 'capital', 'region', 'currencies', 'languages', 'population', 'borders', 'timezones'])
    self.selection_box.currentIndexChanged.connect(self.selectHorizontalBoxChange)
    
    axisLayout.addWidget(self.selection_label, 0, 0)
    axisLayout.addWidget(self.selection_box, 0, 1)
    
    self.axisGroupBox = QtGui.QGroupBox()
    self.axisGroupBox.setStyleSheet("font-size: 15px;")
    self.axisGroupBox.setSizePolicy(QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Fixed))
    self.axisGroupBox.setLayout(axisLayout)

    runLayout = QtGui.QGridLayout()
    self.runButton = QPushButton()
    self.runButton.setText("Submit")
    self.runButton.clicked.connect(self.runScript)

    self.logTextBox = QTextEdit()
    self.logTextBox.setMinimumHeight(300)
    self.logTextBox.setReadOnly(True)
    runLayout.addWidget(self.logTextBox, 0, 0, 3, 1)
    runLayout.addWidget(self.runButton, 0, 1)
    self.runGroupBox = QtGui.QGroupBox()
    self.runGroupBox.setStyleSheet("font-size: 15px;")
    self.runGroupBox.setLayout(runLayout)

    # Setup main layout
    main_layout.addWidget(self.configGroupBox, 0, 0)
    main_layout.addWidget(self.axisGroupBox, 1, 0)
    main_layout.addWidget(self.runGroupBox, 2, 0)
    
    # main_layout.addWidget(self.uploadGroupBox, 3, 0)
    central_widget = QWidget()
    central_widget.setLayout(main_layout)

    self.setCentralWidget(central_widget)
    self.resize(QDesktopWidget().availableGeometry(self).size() * 0.4)  # Set display window to 40% of desktop.


  def selectHorizontalBoxChange(self, i):
    self.dropdown_horizontal_map = {0: 'Please select an option.',
                                    1: 'All country information',
                                    2: 'capital',
                                    3: 'region',
                                    4: 'currencies',
                                    5: 'languages',
                                    6: 'population',
                                    7: 'borders',
                                    8: 'timezones'
                                    }
    self.horizontal_selection = self.dropdown_horizontal_map[i]
    print(self.dropdown_horizontal_map[i])
    return

  def stop_button_press(self):
    print('stop button pressed')
    return

  def runScript(self):
    self.logTextBox.append("Processing\n")
    self.runButton.setEnabled(False)


    country = self.country_box

    if self.horizontal_selection == 'All country information':
      country_info = self.travel_planner.get_country_info(country.text())
      for key, value in country_info.items():
        self.logTextBox.append(key)
        self.logTextBox.append(str(value))
        self.logTextBox.append('\n')




    # first_name = self.first_name_box.text()
    # last_name = self.last_name_box.text()
    # phone_number = self.phone_number_box.text()
    # if self.horizontal_selection == 'New contact':
    #   self.contact_book.new_contact(first_name, last_name, phone_number)
    #   self.logTextBox.append("\nSuccessfully added contact: \n" + first_name + ' '+ last_name + ' ' + phone_number)
    # elif self.horizontal_selection == 'Update contact':
    #   self.contact_book.update_contact(first_n=first_name, last_n=last_name, phone=phone_number)
    #   self.logTextBox.append("\nSuccessfully updated contact: \n" + first_name + ' '+ last_name + ' ' + phone_number)
    # elif self.horizontal_selection == 'Delete contact':
    #   self.contact_book.delete_contact(first_name, last_name, phone_number)
    #   self.logTextBox.append("\nSuccessfully deleted contact: \n" + first_name + ' '+ last_name + ' ' + phone_number)
    # else:
    #   listed_contacts = self.contact_book.list_contacts()
    #   self.logTextBox.append("Contacts:")
    #   for contact in listed_contacts:
    #     self.logTextBox.append(contact[0])
    #     self.logTextBox.append(contact[1])
    #     self.logTextBox.append(contact[2])
    #     self.logTextBox.append("\n")
    #     print(contact[0], contact[1], contact[2])
      
    
    self.runButton.setEnabled(True)
    

if __name__ == '__main__':

  app = QtGui.QApplication(sys.argv)
  mainWindow = Window()
  mainWindow.show()
  sys.exit(app.exec_())