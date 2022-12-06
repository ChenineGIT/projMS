from time import sleep
from PyQt5.QtCore import QThread
from main_ import Main
from check_ import Checked
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtGui, QtWidgets

class Func:
    def __init__(self, ui):
        self.ui = ui
        self.list_module = list()



    def save_settings(self):
        print("saved settings")
        if self.ui.checkBox.isChecked():
            # Module
            self.ui.widget_49.setStyleSheet("background-color:rgb(2, 2, 2);")
            self.ui.widget_57.setStyleSheet("border:1px solid #fff; border-radius:5px;")
            self.ui.l1.setStyleSheet("color:rgb(255, 255, 255); border:none;")
            self.ui.l2.setStyleSheet("color:rgb(255, 255, 255); border:none;")
            self.ui.l3.setStyleSheet("color:rgb(255, 255, 255); border:none;")
            # Salle
            self.ui.widget_40.setStyleSheet("background-color:rgb(2, 2, 2);")
            self.ui.widget_41.setStyleSheet("border:1px solid #fff; border-radius:5px;")
            self.ui.ll1.setStyleSheet("color:rgb(255, 255, 255); border:none;")
            self.ui.ll2.setStyleSheet("color:rgb(255, 255, 255); border:none;")
            self.ui.ll3.setStyleSheet("color:rgb(255, 255, 255); border:none;")
            self.ui.ll4.setStyleSheet("color:rgb(255, 255, 255); border:none;")


            # Group
            self.ui.widget_45.setStyleSheet("background-color:rgb(2, 2, 2);")
            self.ui.widget_48.setStyleSheet("border:1px solid #fff; border-radius:5px;")
            self.ui.e1.setStyleSheet("color:rgb(255, 255, 255); border:none;")
            self.ui.e2.setStyleSheet("color:rgb(255, 255, 255); border:none;")
            self.ui.e3.setStyleSheet("color:rgb(255, 255, 255); border:none;")
            self.ui.e4.setStyleSheet("color:rgb(255, 255, 255); border:none;")

            # Professor
            self.ui.widget_50.setStyleSheet("background-color:rgb(2, 2, 2);")
            self.ui.widget_53.setStyleSheet("border:1px solid #fff; border-radius:5px;")
            self.ui.lll1.setStyleSheet("color:rgb(255, 255, 255); border:none;")
            self.ui.lll2.setStyleSheet("color:rgb(255, 255, 255); border:none;")
            self.ui.lll3.setStyleSheet("color:rgb(255, 255, 255); border:none;")
            self.ui.lll4.setStyleSheet("color:rgb(255, 255, 255); border:none;")

            # Settings
            self.ui.widget_59.setStyleSheet("background-color:rgb(2, 2, 2);")
            self.ui.c1.setStyleSheet("color:rgb(255, 255, 255); border:none;")
            self.ui.c2.setStyleSheet("color:rgb(255, 255, 255); border:none;")
            self.ui.c3.setStyleSheet("color:rgb(255, 255, 255); border:none;")
            self.ui.checkBox.setStyleSheet("background-color:rgb(2, 2, 2);")

        else:
            # Module
            self.ui.widget_49.setStyleSheet("background-color:rgb(255, 255, 255);")
            self.ui.l1.setStyleSheet("color:rgb(0, 0, 0);")
            self.ui.l2.setStyleSheet("color:rgb(0, 0, 0);")
            self.ui.l3.setStyleSheet("color:rgb(0, 0, 0);")

            # Salle
            self.ui.widget_40.setStyleSheet("background-color:rgb(255, 255, 255);")
            self.ui.widget_41.setStyleSheet("border:none;")
            self.ui.ll1.setStyleSheet("color:rgb(0, 0, 0); border:none;")
            self.ui.ll2.setStyleSheet("color:rgb(0, 0, 0); border:none;")
            self.ui.ll3.setStyleSheet("color:rgb(0, 0, 0); border:none;")
            self.ui.ll4.setStyleSheet("color:rgb(0, 0, 0); border:none;")

            # Professor
            self.ui.widget_50.setStyleSheet("background-color:rgb(255, 255, 255);")
            self.ui.widget_53.setStyleSheet("border:none;")
            self.ui.lll1.setStyleSheet("color:rgb(0, 0, 0); border:none;")
            self.ui.lll2.setStyleSheet("color:rgb(0, 0, 0); border:none;")
            self.ui.lll3.setStyleSheet("color:rgb(0, 0, 0); border:none;")
            self.ui.lll4.setStyleSheet("color:rgb(0, 0, 0); border:none;")

            self.ui.widget_45.setStyleSheet("background-color:rgb(255, 255, 255);")
            self.ui.widget_48.setStyleSheet("border:none;")
            self.ui.e1.setStyleSheet("color:rgb(0, 0, 0); border:none;")
            self.ui.e2.setStyleSheet("color:rgb(0, 0, 0); border:none;")
            self.ui.e3.setStyleSheet("color:rgb(0, 0, 0); border:none;")
            self.ui.e4.setStyleSheet("color:rgb(0, 0, 0); border:none;")

            self.ui.widget_59.setStyleSheet("background-color:rgb(255, 255, 255);")
            self.ui.c1.setStyleSheet("color:rgb(0, 0, 0); border:none;")
            self.ui.c2.setStyleSheet("color:rgb(0, 0, 0); border:none;")
            self.ui.c3.setStyleSheet("color:rgb(0, 0, 0); border:none;")
            self.ui.checkBox.setStyleSheet("background-color:rgb(255, 255, 255);")

    # def show_modules(self):
    #     from check_ import Checked
    #     ch = Checked()
    #     self.ui.verticalLayout_11.addWidget(ch)
    #     self.ui.scrollArea.setStyleSheet("border:1px solid #000; border-radius:5px;")

    def connect_db(self):
        import mysql.connector as con
        try:
            mydb = con.connect(
                host="127.0.0.1",
                user="root",
                password="1234",
                database="timetable"
            )
            cur = mydb.cursor()
            return mydb, cur

        except:
            msg_err = QMessageBox()
            msg_err.setText("Error Connect!")
            msg_err.setInformativeText("the connection to database failed!")
            msg_err.exec_()


    """==================================================="""
    """========= functions profs ========================="""
    def setID(self):
        db, cur = self.connect_db()
        sql = "select id_prof from prof"
        cur.execute(sql)
        ids = cur.fetchall()
        if ids == []:
            return 1
        db.close()
        return ids[-1][0] + 1

    def check(self, n, p):
        db, cur = self.connect_db()
        sql = f"select id_prof from prof where name_prof='{n}' and prenom_prof='{p}'"
        cur.execute(sql)
        ids = cur.fetchall()
        db.close()
        return ids

    def add_prof(self):
        """ func add profs """
        name = self.ui.lineEdit_21.text()
        prname = self.ui.lineEdit.text()

        if name == "" or prname == "":
            self.ui.status.setText("Enter all Info Prof")
        else:
            if self.check(name, prname) == []:
                id_prof = self.setID()
                db, cur = self.connect_db()

                sql = f"INSERT INTO prof VALUES({id_prof}, '{name}', '{prname}')"
                cur.execute(sql)
                db.commit()
                db.close()
                self.show_profs()
                self.ui.status.setText("Prof added")
            else:
                self.ui.status.setText("Prof has been added befor")



    def show_profs(self):
        try:
            mydb, cur = self.connect_db()
            sql = "select * from prof"
            cur.execute(sql)
            profs = cur.fetchall()
            self.ui.table_profs.insertRow(0)
            row = 0
            col = 0
            self.ui.table_profs.setRowCount(len(profs))
            for r in profs:
                for c in r:
                    self.ui.table_profs.setItem(row, col, QtWidgets.QTableWidgetItem("\t"+str(c)))
                    col += 1

            mydb.close()
        except:
            self.ui.status.setText("failed.")

    def delete_prof(self):
        id = self.search_prof()
        if id != None:
            mydb, cur = self.connect_db()
            sql = f"delete from prof where id_prof={id}"
            cur.execute(sql)
            mydb.commit()
            mydb.close()
            self.ui.status.setText("prof deleted.")
            self.ui.lineEdit_21.setText("")
            self.ui.lineEdit.setText("")
            self.ui.lineEdit_22.setText("")
            self.show_profs()

    def search_prof(self):
        """ func search of prof """
        name_prof = self.ui.lineEdit_22.text()
        try:
            mydb, cur = self.connect_db()
            id_prof = None
            sql = "select * from prof"
            cur.execute(sql)
            profs = cur.fetchall()
            for prof in profs:
                if prof[1] == name_prof:
                    self.ui.lineEdit_21.setText(name_prof)
                    self.ui.lineEdit.setText(prof[2])
                    id_prof = prof[0]
                    self.ui.status.setText("")
                    mydb.close()


            if id_prof == None: self.ui.status.setText("prof not found.")
            return id_prof
        except:
            self.ui.status.setText("failed.")

    """============================================"""

    def show_modules(self):
        for i in range(self.ui.verticalLayout_11.count()):
            item = self.ui.verticalLayout_11.itemAt(i).widget().deleteLater()
        l = ['res', 'sec', 'bda', 'ms']
        for ll in l:
            ch = Checked(ll)

            self.ui.verticalLayout_11.addWidget(ch)
            self.ui.scrollArea.setStyleSheet("border:1px solid #000; border-radius:5px;")
            ch.setStyleSheet("border:none;")
            self.list_module.append(ch)

    """======================================================="""
    """========== functons classes ==========================="""
    def setIdClass(self):
        db, cur = self.connect_db()
        sql = "select id_class from class"

        cur.execute(sql)
        ids = cur.fetchall()
        if ids == []:
            return 1
        print(ids)
        db.close()
        return ids[-1][0] + 1

    def checkClass(self, n):
        db, cur = self.connect_db()
        sql = f"select id_class from class where name='{n}'"
        cur.execute(sql)
        ids = cur.fetchall()
        db.close()
        return ids

    def add_class(self):
        """ func add profs """
        name = self.ui.lineEdit_14.text()
        capacity = self.ui.spinBox_5.text()
        print(self.checkClass(name), self.setIdClass())
        if name == "" or capacity == 0:
            self.ui.status_.setText("Enter all Info Class")
        else:
            if self.checkClass(name) == []:
                id_class = self.setIdClass()
                db, cur = self.connect_db()
                sql = f"INSERT INTO class VALUES({id_class}, '{name}', {capacity})"
                cur.execute(sql)
                db.commit()
                db.close()
                self.show_classes()
                self.ui.status_.setText("Class added")
            else:
                self.ui.status_.setText("Class has been added befor")


    def delete_class(self):
        id = self.search_class()
        if id != None:
            mydb, cur = self.connect_db()
            sql = f"delete from class where id_class={id}"
            cur.execute(sql)
            mydb.commit()
            mydb.close()
            self.ui.status_.setText("class deleted.")
            self.ui.lineEdit_14.setText("")
            self.ui.spinBox_5.setValue(0)
            self.ui.lineEdit_16.setText("")
            self.show_classes()


    def show_classes(self):
        """ func show all class to find in database """
        try:
            mydb, cur = self.connect_db()
            sql = "select * from class"
            cur.execute(sql)
            classes = cur.fetchall()
            self.ui.tableWidget.insertRow(0)
            row = 0
            col = 0
            self.ui.tableWidget.setRowCount(len(classes))
            for r in classes:
                for c in r:
                    self.ui.tableWidget.setItem(row, col, QtWidgets.QTableWidgetItem("\t" + str(c)))
                    col += 1

            mydb.close()
        except:
            self.ui.status_.setText("failed.")

    def search_class(self):
        """ func search of class """
        name_class = self.ui.lineEdit_16.text()
        try:
            mydb, cur = self.connect_db()
            id_class = None
            sql = "select * from class"
            cur.execute(sql)
            classes = cur.fetchall()
            for _class in classes:
                if _class[1] == name_class:
                    self.ui.lineEdit_14.setText(name_class)
                    self.ui.spinBox_5.setValue(_class[2])
                    id_class = _class[0]
                    self.ui.status_.setText("")
                    break
            if id_class == None: self.ui.status_.setText("class not found.")
            mydb.close()
            return id_class
        except:
            self.ui.status_.setText("failed.")

    """==================================================="""
    """========= functions groups ========================="""

    def setIdGroup(self):
        db, cur = self.connect_db()
        sql = "select id_groub from groub"
        cur.execute(sql)
        ids = cur.fetchall()
        if ids == []:
            return 1
        db.close()
        return ids[-1][0] + 1

    def check_Group(self, name, number):
        db, cur = self.connect_db()
        sql = f"select id_groub from groub where name_groub='{name}' and nomber_groub={number}"
        cur.execute(sql)
        ids = cur.fetchall()
        db.close()
        return ids

    def add_group(self):
        """ func add groups """
        name = self.ui.lineEdit_17.text()
        number = self.ui.spinBox_6.value()

        if name == "" or number == 0:
            self.ui.statue__.setText("Enter all Info Group")
        else:
            if self.check_Group(name, number) == []:
                id_groub = self.setIdGroup()
                db, cur = self.connect_db()

                sql = f"INSERT INTO groub VALUES({id_groub}, '{name}', {number})"
                cur.execute(sql)
                db.commit()
                db.close()
                self.show_group()
                self.ui.statue__.setText("Group added")
            else:
                self.ui.statue__.setText("Group has been added befor")

    def show_group(self):
        try:
            mydb, cur = self.connect_db()
            sql = "select * from groub"
            cur.execute(sql)
            groups = cur.fetchall()
            self.ui.table_group.insertRow(0)
            row = 0
            col = 0
            self.ui.table_group.setRowCount(len(groups))
            for r in groups:
                for c in r:
                    self.ui.table_group.setItem(row, col, QtWidgets.QTableWidgetItem("\t" + str(c)))
                    col += 1

            mydb.close()
        except:
            self.ui.statue__.setText("failed.")

    def delete_group(self):
        id = self.search_group()
        if id != None:
            mydb, cur = self.connect_db()
            sql = f"delete from groub where id_groub={id}"
            cur.execute(sql)
            mydb.commit()
            mydb.close()
            self.ui.statue__.setText("group deleted.")
            self.ui.lineEdit_17.setText("")
            self.ui.spinBox_6.setValue(0)
            self.ui.lineEdit_19.setText("")
            self.show_group()

    def search_group(self):
        """ func search of prof """
        name_group = self.ui.lineEdit_19.text()
        try:
            mydb, cur = self.connect_db()
            id_groub = None
            sql = "select * from groub"
            cur.execute(sql)
            groups = cur.fetchall()
            for group in groups:
                if group[1] == name_group:
                    self.ui.lineEdit_17.setText(name_group)
                    self.ui.spinBox_6.setValue(group[2])
                    id_groub = group[0]
                    self.ui.statue__.setText("")
                    mydb.close()

            if id_groub == None: self.ui.statue__.setText("group not found.")
            return id_groub
        except:
            self.ui.statue__.setText("failed.")


    """==================================================="""
    """========= functions Module ========================="""

    def setIdModule(self):
        db, cur = self.connect_db()
        sql = "select ID_Matiere from matiere"
        cur.execute(sql)
        ids = cur.fetchall()
        if ids == []:
            return 1
        db.close()
        return ids[-1][0] + 1

    def check_Module(self, name, type_Matiere):
        db, cur = self.connect_db()
        sql = f"select ID_Matiere from matiere where Name_Matiere='{name}' and type_Matiere='{type_Matiere}'"
        cur.execute(sql)
        ids = cur.fetchall()
        db.close()
        return ids
    '''============================================'''
    # added into table etudie
    # id_prof	id_groub	id_class	name_matiere	type_matiere	temps_etude	journee_etude
    def table_etudie(self, id_prof, id_groub, id_class, name_matiere, type_matiere, temps_etude, journee_etude):
        pass
    '''============================================'''
    # table ensenign
    def enseignematiere(self, name_prof, id_module):
        db, cur = self.connect_db()
        # get id prof
        sql1 = f"select id_prof form prof where name_prof = '{name_prof}'"
        cur.execute(sql1)
        id_prof = cur.fetchall()[0][0]
        # add to enseignematiere
        sql2 = f"insert into enseignematiere values({id_prof}, {id_module})"
        cur.execute(sql)
        db.commit()
        db.close()

    def etudematiere(self, name_group, id_module ):
        db, cur = self.connect_db()
        # get id matiare
        sql1 = f"select id_groub from groub where name_groub='{name_group}'"
        cur.execute(sql1)
        id_group = cur.fetchall()[0][0]
        # add to etudematiere
        sql = f"insert into etudematiere values({id_group}, {id_module})"
        cur.execute(sql)
        db.commit()
        db.close()

    """============================================"""

    """============================================"""
    def add_Module(self):
        """ func add groups """
        name = self.ui.lineEdit_20.text()
        type_Matiere = self.ui.comboBox_2.currentText()
        name_prof = self.ui.comboBox_3.currentText()
        name_group = self.ui.comboBox_4.currentText()

        if name == "" or type_Matiere == "" or name_prof == "" or name_group == "":
            self.ui.status_module.setText("Enter all Info Module")
        else:
            if self.check_Module(name, type_Matiere) == []:
                ID_Matiere = self.setIdModule()
                db, cur = self.connect_db()

                sql = f"INSERT INTO matiere VALUES({ID_Matiere}, '{name}', '{type_Matiere}')"
                cur.execute(sql)
                # etudematiere and enseignematiere
                self.etudematiere(name_group, ID_Matiere)
                self.enseignematiere(name_prof, ID_Matiere)

                db.commit()
                db.close()
                self.show_Module()
                self.ui.status_module.setText("Module added")
            else:
                self.ui.status_module.setText("Module has been added befor")

    def show_Module(self):
        try:
            mydb, cur = self.connect_db()
            # sql = "select .*, name_groub, name_prof from matiere, groub, prof,  " \
            #       "where etudematiere.id_Matiere=matiere"
            # etudematiere and enseignematiere
            cur.execute(sql)
            modules = cur.fetchall()
            print(modules)
            # self.ui.table_module.insertRow(0)
            # row = 0
            # col = 0
            # self.ui.table_module.setRowCount(len(modules))
            # for r in modules:
            #     for c in r:
            #         self.ui.table_module.setItem(row, col, QtWidgets.QTableWidgetItem("\t" + str(c)))
            #         col += 1
            #
            # mydb.close()
        except:
            self.ui.status_module.setText("failed.")

    def delete_module(self):
        id = self.search_Module()
        if id != None:
            mydb, cur = self.connect_db()
            sql = f"delete from matiere where ID_Matiere={id}"
            cur.execute(sql)
            mydb.commit()
            mydb.close()
            self.ui.status_module.setText("module deleted.")
            self.ui.lineEdit_20.setText("")
            self.ui.comboBox_2.setCurrentText(0)
            self.ui.comboBox_3.setCurrentText(0)
            self.ui.comboBox_4.setCurrentText(0)
            self.show_Module()

    def search_Module(self):
        """ func search of prof """
        name_Module = self.ui.lineEdit_24.text()
        try:
            mydb, cur = self.connect_db()
            ID_Matiere = None
            sql = "select * from matiere"

            cur.execute(sql)
            modules = cur.fetchall()
            for module in modules:
                if module[1] == name_Module:
                    self.ui.lineEdit_20.setText(name_Module)
                    self.ui.comboBox_2.setCurrentText(module[2])
                    self.ui.comboBox_3.setCurrentText(module[2]) # prof
                    self.ui.comboBox_4.setCurrentText(module[2]) # group
                    ID_Matiere = module[0]
                    self.ui.status_module.setText("")
                    mydb.close()

            if ID_Matiere == None: self.ui.status_module.setText("module not found.")
            return ID_Matiere
        except:
            self.ui.status_module.setText("failed.")

    def getProfs_Groups(self):
        db, cur = self.connect_db()
        sql_prof = "select name_prof from prof"
        sql_group = "select name_groub from groub"

        list_prof = list()
        list_group = list()
        cur.execute(sql_prof)
        profs = cur.fetchall()
        for prof in profs:
            for name in prof:
                list_prof.append(name)
        cur.execute(sql_group)
        groups = cur.fetchall()
        for group in groups:
            for name in group:
                list_group.append(name)
        self.combobox(list_group, list_prof)

        db.close()


    def combobox(self, list_group, list_prof):
        list_group, list_prof = self.getProfs_Groups()
        for c in list_prof:
            self.ui.comboBox_3.addItem(c)
        for c in list_group:
            self.ui.comboBox_4.addItem(c)



