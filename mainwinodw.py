import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QTextBrowser, QFileDialog
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import re
from PySide6.QtGui import QIcon

from ui_form import Ui_MainWinodw

# для обновления .ui файла
# pyside6-uic form.ui -o ui_mainwindow.py

# id для тестов
#"0000-0001-7000-956X"
#"0000-0001-5987-3357"

mainText = ""

class MainWinodw(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowIcon(QIcon("pics/ID.png"))
        self.ui = Ui_MainWinodw()
        self.ui.setupUi(self)
        self.ui.textBrowser.setOpenExternalLinks(True)
        self.ui.lineEdit.setPlaceholderText("Enter ORCID id here")

        self.ui.pushButtonEnter.clicked.connect(self.the_Enterbutton_was_clicked)
        self.ui.pushButtonSave.clicked.connect(self.the_Savebutton_was_clicked)


    def the_Enterbutton_was_clicked(self):
        global mainText
        mainText = ""

        self.ui.textBrowser.clear()
        name = self.ui.lineEdit.text()

        if not re.match(r"....-....-....-....", name):
            self.ui.textBrowser.append("The ID does not match the pattern")
            mainText += "The ID does not match the pattern"
            return

        options = Options()
        options.add_argument("--headless")
        driver = webdriver.Firefox(options = options)
        driver.get("https://orcid.org/" + name)

        try:
            author_name = driver.find_element(By.CLASS_NAME, "orc-font-heading")

        except NoSuchElementException:
            self.ui.textBrowser.append("A problem occured during the search\nplease check your input data")
            mainText += "A problem occured during the search\nplease check your input data"
            return

        article_name = driver.find_elements(By.CLASS_NAME, "work-title")

        if len(article_name) == 0:
            self.ui.textBrowser.append(author_name.text)
            self.ui.textBrowser.append("\nOnly the name was found")
            mainText += (author_name.text + "\nOnly the name was found")
            return


        wait = WebDriverWait(driver, 10)

        xpath = "//*[@class='underline ng-star-inserted']"
        buttons = driver.find_elements(By.XPATH, xpath)
        wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))

        for bt in buttons:
            driver.execute_script("arguments[0].click();", bt)
            wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))

        time.sleep(1)

        elements = driver.find_elements(By.XPATH, xpath)
        unfiltered_links = [elem.get_attribute('href') for elem in elements]
        before_removed = list(filter(lambda item: item is not None, unfiltered_links))
        links = [a for a in before_removed if ('doi' in a or 'scopus' in a or 'publons' in a)]

        if len(links) == 0:
            self.ui.textBrowser.append(author_name.text + "\n")
            for i in range(len(article_name)):
                self.ui.textBrowser.append("- " + article_name[i].text + "\n")
                mainText += ("- " + article_name[i].text + "\n")
            return

        self.ui.textBrowser.append(author_name.text + "\n")
        mainText += (author_name.text + "\n")

        for i in range(len(article_name)):
            self.ui.textBrowser.append("- " + article_name[i].text + " (" + "<a href=\'" + links[i] + "\'>Link</a>" + ")\n")
            mainText += ("- " + article_name[i].text + " (" + links[i] + ")\n")

        driver.quit()

    def the_Savebutton_was_clicked(self):
        global mainText

        if mainText  == "":
            return

        else:
            fileName = QFileDialog.getSaveFileName(self, 'Title', '', filter="Text files (*.txt)")
            if fileName[0] != "":
                with open (fileName[0], 'w+') as f:
                    f.write(mainText)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWinodw()
    widget.setFixedSize(428, 600)
    widget.show()
    sys.exit(app.exec())
