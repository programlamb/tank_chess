import sys

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow


TANKS_DESCRIPTION = {'1': [5, (1, 0, 0), 1, 3, 2], '2': [4, (2, 1, 0), 2, 3, 2], '3': [3, (3, 2, 1), 3, 3, 2]}
TRANSFORM_ROTATE = {'1': [(0, 1), ''], '2': [(1, 1), ''], '3': [(1, 0), ''], '4': [(1, -1), ''], '5': [(0, -1), ''],
                    '6': [(-1, -1), ''], '7': [(-1, 0), ''], '8': [(-1, 1), '']}


class TankChess(QMainWindow):
    def __init__(self):
        super(TankChess, self).__init__()
        uic.loadUi('des.ui', self)

        self.now = self.rules  # выбрана стандартная кнопка
        self.turn = 'w'  # ход игрока white
        self.action_points = 0

        self.rules.clicked.connect(self.rule)
        self.tanks.clicked.connect(self.info)  # реакции на нажатие кнопок
        self.fire.clicked.connect(self.canon_fire)
        [i.clicked.connect(self.choice) for i in self.squares.buttons()]

    def keyPressEvent(self, event):  # реакции на нажатие кнопок клавиатуры
        if event.key() == Qt.Key_Left or event.key() == Qt.Key_A:
            self.rotate('left')
        if event.key() == Qt.Key_Right or event.key() == Qt.Key_D:
            self.rotate('right')

        if event.key() == Qt.Key_Up or event.key() == Qt.Key_W:
            self.riding_up()
        if event.key() == Qt.Key_Down or event.key() == Qt.Key_S:
            self.riding_back()

    def choice(self):
        if self.now == self.rules and self.sender().text() != '' and self.sender().text()[0] == self.turn:
            # если выбрана стандартная кнопка, и если нажата не пустая клетка и это танк игрока,
            self.now = self.sender()  # то сохраняем название кнопки и выделяем её цветом
            self.now.setStyleSheet('background-color: rgb(228, 230, 78)')

            self.action_points = TANKS_DESCRIPTION[self.sender().text()[1]][0]
        elif self.now != self.rules and self.action_points == TANKS_DESCRIPTION[self.now.text()[1]][0]:
            # если танк ничего не делал в ходу,
            self.now.setStyleSheet('')  # то очищаем выбор
            self.now = self.rules
            if self.sender().text() != '' and self.sender().text()[0] == self.turn:  # если нажата не пустая клетка,
                self.now = self.sender()  # и это танк игрока, то сохраняем название кнопки и выделяем её цветом
                self.now.setStyleSheet('background-color: rgb(228, 230, 78)')
                self.action_points = TANKS_DESCRIPTION[self.sender().text()[1]][0]

    def rule(self):
        pass

    def info(self):
        pass

    def rotate(self, direction):
        if self.action_points != 0 and self.now:  # если танк выбран, и у него есть очки действия
            if direction == 'left':  # если нажата кнопка поворот на право
                if int(self.now.text()[2]) - 1 == 0:
                    self.now.setText(self.now.text()[:2] + '8')
                else:
                    self.now.setText(self.now.text()[:2] + str(int(self.now.text()[2]) - 1))
                self.action_points -= 1
            elif direction == 'right':  # если нажата кнопка поворот на лево
                if int(self.now.text()[2]) + 1 == 9:
                    self.now.setText(self.now.text()[:2] + '1')
                else:
                    self.now.setText(self.now.text()[:2] + str(int(self.now.text()[2]) + 1))
                self.action_points -= 1

    def riding_back(self):
        pass

    def riding_up(self):
        if int(self.now.text()[2]) + TRANSFORM_ROTATE[self.now.text()[2]][0][0] == range(1, 16) and\
            int(self.now.text()[2]) + TRANSFORM_ROTATE[self.now.text()[2]][0][1] == range(1, 16):
            

    def canon_fire(self):
        pass


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TankChess()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
