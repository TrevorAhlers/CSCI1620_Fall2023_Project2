from steel_conversion_logic import *

def main():
    """
    Application window
    """
    application = QApplication([])
    window = Logic()
    window.setGeometry(700,300,250,250)
    window.setFixedSize(window.size())
    window.show()
    application.exec()

if __name__ == '__main__':
    main()