import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QTextBrowser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re
from PySide6.QtGui import QIcon

from ui_form import Ui_MainWinodw

# для обновления .ui файла
# pyside6-uic form.ui -o ui_mainwindow.py

# id для тестов
#"0000-0001-7000-956X"
#"0000-0001-5987-3357"


class MainWinodw(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowIcon(QIcon("ID.png"))
        self.ui = Ui_MainWinodw()
        self.ui.setupUi(self)
        self.ui.textBrowser.setOpenExternalLinks(True)

        self.ui.lineEdit.setPlaceholderText("Enter ORCID id here")
        self.ui.pushButton.clicked.connect(self.the_button_was_clicked)


    def the_button_was_clicked(self):
        self.ui.textBrowser.clear()
        name = self.ui.lineEdit.text()
        if not re.match(r"....-....-....-....", name):
            self.ui.textBrowser.append("The ID does not match the pattern")
            return

        options = Options()
        options.add_argument("--headless")
        driver = webdriver.Firefox(options = options)
        driver.get("https://orcid.org/" + name)

        try:
            author_name = driver.find_element(By.CLASS_NAME, "orc-font-heading")
        except:
            self.ui.textBrowser.append("A problem occured during the search\nplease check your input data")
            return

        try:
            article_name = driver.find_elements(By.CLASS_NAME, "work-title")
        except:
            self.ui.textBrowser.append(author_name.text + "\n")
            self.ui.textBrowser.append("only the name was found")
            return

        try:
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

        except:
            for i in range(len(article_name)):
                self.ui.textBrowser.append("- " + article_name[i].text + "\n")
            return

        self.ui.textBrowser.append(author_name.text + "\n")
        for i in range(len(article_name)):
            self.ui.textBrowser.append("- " + article_name[i].text + " (" + "<a href=\'" + links[i] + "\'>Link</a>" + ")\n")

        driver.quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWinodw()
    widget.setFixedSize(428, 600)
    widget.show()
    sys.exit(app.exec())
