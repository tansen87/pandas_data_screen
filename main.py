import os
import sys
import datetime

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QColor, QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog

from ui_main import Ui_MainWindow

global file_name, file_out, targets, col_name, sep_char


class MyMainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.start_x = None
        self.start_y = None
        self.anim = None
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint)  # 设置窗口标志：隐藏窗口边框
        self.lineEdit.setAttribute(QtCore.Qt.WA_MacShowFocusRect, 0)
        self.btn()
        self.display()
        self.progress_bar()
        self.log = RecordLog

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            super(MyMainForm, self).mousePressEvent(event)
            self.start_x = event.x()
            self.start_y = event.y()

    def mouseReleaseEvent(self, event):
        self.start_x = None
        self.start_y = None

    def mouseMoveEvent(self, event):
        try:
            super(MyMainForm, self).mouseMoveEvent(event)
            dis_x = event.x() - self.start_x
            dis_y = event.y() - self.start_y
            self.move(self.x() + dis_x, self.y() + dis_y)
        except:
            pass

    def effect_shadow_style(self, widget):
        effect_shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        effect_shadow.setOffset(12, 12)  # 偏移
        effect_shadow.setBlurRadius(128)  # 阴影半径
        effect_shadow.setColor(QColor(155, 230, 237, 150))  # 阴影颜色
        widget.setGraphicsEffect(effect_shadow)

    def btn(self):
        # connect function
        self.btn_close.clicked.connect(self.btn_close_func)
        self.btn_enlarge.clicked.connect(self.btn_enlarge_func)
        self.btn_contract.clicked.connect(self.showMinimized)
        self.btn_select.clicked.connect(self.openfile)
        self.btn_save_path.clicked.connect(self.save_path)
        self.btn_cond1.clicked.connect(self.open_target)
        self.btn_col1.clicked.connect(self.open_col)
        self.btn_run.clicked.connect(self.handle_df)
        self.btn_about.clicked.connect(self.about)
        self.btn_merge_data.clicked.connect(self.merge_data)

        # set icon
        self.btn_select.setIcon(QIcon('./static/img/excel.png'))
        self.btn_save_path.setIcon(QIcon('./static/img/folder.png'))
        self.btn_cond1.setIcon(QIcon('./static/img/cond.png'))
        self.btn_col1.setIcon(QIcon('./static/img/col.png'))
        self.btn_run.setIcon(QIcon('./static/img/run-line.png'))
        self.btn_about.setIcon(QIcon('./static/img/about.png'))
        self.btn_merge_data.setIcon(QIcon('./static/img/merge.png'))

    def merge_data(self):
        self.thread_merge = MergeDataThread()
        self.thread_merge.signal_trans.connect(self.update_text)
        self.thread_merge.moveToThread(self.thread_merge)
        self.thread_merge.start()

    def display(self):
        self.lineEdit.setPlaceholderText("待筛选的列")
        self.lineEdit_sep.setPlaceholderText("文件分割符号")

    def btn_close_func(self):
        window.close()

    def btn_enlarge_func(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def progress_bar(self):
        self.progressBar.setRange(0, 99)
        self.progressBar.hide()

    def callback(self, i):
        self.progressBar.show()
        self.progressBar.setValue(i)

    def callback_done(self, i):
        self.is_done = i
        if self.is_done == 1:
            self.progressBar.show()
            self.progressBar.setValue(99)
            self.progressBar.setFormat("screening completed")

    def openfile(self):
        global file_name
        file = QFileDialog.getOpenFileName(self, "Select file", "*.csv;*.xlsx;*.xls;*.CSV;*.XLSX;*.XLS")[0]
        file_ = 'open file name: ' + os.path.basename(file)
        self.textBrowser.setText(file_)
        self.log.write_log(file_)
        file_name = file

    def save_path(self):
        global file_out
        output = QFileDialog.getExistingDirectory(self, "Select the file save path", "./")
        output_ = 'file path: ' + output
        self.textBrowser.setText(output_)
        self.log.write_log(output_)
        file_out = output

    def open_target(self):
        global targets
        target = QFileDialog.getOpenFileName(self, "Select txt file", "*.txt")[0]
        target_ = 'screening conditions: ' + os.path.basename(target)
        self.textBrowser.setText(target_)
        self.log.write_log(target_)
        file_target = target
        with open(file_target, 'r', encoding='utf-8') as fp:
            lines = fp.readlines()
        targets = [line.strip('\n') for line in lines]

    def open_col(self):
        global col_name, sep_char
        col = self.lineEdit.text()
        sep = self.lineEdit_sep.text()
        col_name = col
        sep_char = sep
        if sep == "":
            if col == "":
                col_ = f"Error: '待筛选的列'不能为空"
            else:
                col_ = f"待筛选的列: {col}"
        else:
            col_ = f"待筛选的列: {col}\n分割符号: {sep}"
        self.textBrowser.setText(col_)
        self.log.write_log(col_)

    def handle_df(self):
        self.progressBar.setValue(0)
        self.is_done = 0
        self.thread_hand = HandleThread()
        self.thread_hand.signal_trans.connect(self.update_text)
        self.thread_hand.progressBarValue.connect(self.callback)
        self.thread_hand.signal_done.connect(self.callback_done)
        self.thread_hand.moveToThread(self.thread_hand)
        self.thread_hand.start()

    def update_text(self, text):
        self.textBrowser.append(text)

    def about(self):
        self.textBrowser.setText("NameError: name 'file_name' is not defined -> 未打开文件\n"
                                 "NameError: name 'sep_char' is not defined -> 未点击🔍按钮\n"
                                 "NameError: name 'targets' is not defined -> 未选择筛选条件\n"
                                 "NameError: name 'file_out' is not defined -> 未选择文件路径")


class HandleThread(QThread):
    signal_trans = pyqtSignal(str)
    progressBarValue = pyqtSignal(int)
    signal_done = pyqtSignal(int)

    def __init__(self):
        super(HandleThread, self).__init__()
        self.log = RecordLog

    def write(self, text):
        self.signal_trans.emit(str(text))

    def run(self):
        self.write('-------------------开始运行-------------------')
        import pandas as pd
        try:
            file = os.path.splitext(file_name)
            if file[1].lower() == ".xlsx" or file[1].lower() == ".xls":
                df = pd.read_excel(file_name, dtype=object)
            if file[1].lower() == '.csv':
                if sep_char == "":
                    df = pd.read_csv(file_name, dtype=object)
                else:
                    df = pd.read_csv(file_name, dtype=object, sep=sep_char)
            ls_col = [df.columns[col] for col in range(len(df.columns))]
            read_tips = f"{os.path.basename(file_name)} read successfully"
            self.write(read_tips)
            self.log.write_log(read_tips)
            data_fr = pd.DataFrame(df, columns=ls_col)
            for i in range(len(targets)):
                cd = {
                    col_name: targets[i]
                }
                new_df = self.df_screen(data_fr, cd)
                try:
                    new_df.to_excel(f"{file_out}/{str(targets[i])}.xlsx", encoding='gbk', index=False)
                    out = f"{str(i + 1)} {str(targets[i])}.xlsx is saved."
                    self.write(out)
                    self.log.write_log(out)
                    self.progressBarValue.emit(int(i / len(targets) * 100))
                except:
                    new_df.to_csv(f"{file_out}/{str(targets[i])}.csv", encoding="utf-8", index=False)
                    out = f"{str(i + 1)} {str(targets[i])}.csv is saved."
                    self.write(out)
                    self.log.write_log(out)
                    self.progressBarValue.emit(int(i / len(targets) * 100))
                else:
                    pass
            self.signal_done.emit(1)

        except NameError as e:
            err = f"NameError: {e}"
            self.write(err)
            self.log.write_log(err)
        except ModuleNotFoundError as e:
            err = f"ModuleNotFoundError: {e}"
            self.write(err)
            self.log.write_log(err)
        except Exception as e:
            err = f"Error: {e}"
            self.write(err)
            self.log.write_log(err)
        else:
            com_tips = f"{len(targets)} files split"
            self.write(com_tips)
        self.write('-------------------运行结束-------------------')

    def df_screen(self, data, cd_data):
        df_cy = data.copy()
        idx_z = [True for i in df_cy.index]
        orcom = lambda a, b: [any([a[i], b[i]]) for i in range(len(a))]  # 列表a与列表b 或 比较
        addcom = lambda a, b: [all([a[i], b[i]]) for i in range(len(a))]  # 列表a与列表b 与 比较
        for z in cd_data:
            if isinstance(cd_data[z], list):
                for index, c in enumerate(cd_data[z]):
                    if index != 0:
                        idx_c = orcom(idx_c, list(df_cy[z] == c))
                    else:
                        idx_c = list(df_cy[z] == c)
            else:
                idx_c = list(df_cy[z] == cd_data[z])
            idx_z = addcom(idx_z, idx_c)
        return df_cy.loc[idx_z, :]


class MergeDataThread(QThread):
    signal_trans = pyqtSignal(str)

    def __init__(self):
        super(MergeDataThread, self).__init__()
        self.log = RecordLog

    def write(self, text):
        self.signal_trans.emit(str(text))

    def run(self):
        import pandas as pd
        try:
            lst_file = list()
            init_path = f"{file_out}/"
            files = os.listdir(init_path)
            for file in range(len(files)):
                read_file = f"{init_path}{files[file]}"
                try:
                    df = pd.read_excel(read_file, dtype=object)
                except:
                    df = pd.read_csv(read_file, dtype=object)
                lst_file.append(df)
                read_tips = f"{file+1} {os.path.basename(read_file)} read successfully"
                self.write(read_tips)
                self.log.write_log(read_tips)
            all_file = pd.concat(lst_file, axis=0, ignore_index=True)
            now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            try:
                all_file.to_excel(f"{init_path}{now}_merged.xlsx", index=False, encoding="gbk")
                com_tips = f"file save path: {init_path}, Merge File Name: '{now}_merged.xlsx'."
                self.write(com_tips)
                self.log.write_log(com_tips)
            except:
                all_file.to_csv(f"{init_path}{now}_merged.csv", index=False, encoding="utf-8")
                com_tips = f"file save path: {init_path}, Merge File Name: '{now}_merged.csv'."
                self.write(com_tips)
                self.log.write_log(com_tips)
            else:
                pass
        except Exception as e:
            err = f"Error: {e}"
            self.write(err)
            self.log.write_log(err)
        else:
            pass


class RecordLog:
    def __init__(self):
        super(RecordLog, self).__init__()

    def write_log(logs) -> None:
        with open("log.txt", "a+", encoding="utf-8") as fp:
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            re_logs = f"{now} -> {str(logs)}\n"
            fp.write(re_logs)
        return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainForm()
    window.show()
    sys.exit(app.exec())
