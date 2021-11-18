import sys

from PyQt5 import uic
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow


TANKS_DESCRIPTION = {'1': [5, (1, 0, 0), 1, 3, 2], '2': [4, (2, 1, 0), 2, 3, 2], '3': [3, (3, 2, 1), 3, 3, 2],
                     '4': [5, (1, 0, 0), 1, 3, 2]}
TRANSFORM_ROTATE = {'1': [(0, 1), ''], '2': [(1, 1), ''], '3': [(1, 0), ''], '4': [(1, -1), ''], '5': [(0, -1), ''],
                    '6': [(-1, -1), ''], '7': [(-1, 0), ''], '8': [(-1, 1), '']}


class TankChess(QMainWindow):
    def __init__(self):
        super(TankChess, self).__init__()
        uic.loadUi('des.ui', self)
        self.board = {'0101': self.pb_a1, '0102': self.pb_a2, '0103': self.pb_a3, '0104': self.pb_a4,
                      '0105': self.pb_a5, '0106': self.pb_a6, '0107': self.pb_a7, '0108': self.pb_a8,
                      '0109': self.pb_a9, '0110': self.pb_a10, '0111': self.pb_a11, '0112': self.pb_a12,
                      '0113': self.pb_a13, '0114': self.pb_a14, '0115': self.pb_a15, '0116': self.pb_a16,
                      '0201': self.pb_b1, '0202': self.pb_b2, '0203': self.pb_b3, '0204': self.pb_b4,
                      '0205': self.pb_b5, '0206': self.pb_b6, '0207': self.pb_b7, '0208': self.pb_b8,
                      '0209': self.pb_b9, '0210': self.pb_b10, '0211': self.pb_b11, '0212': self.pb_b12,
                      '0213': self.pb_b13, '0214': self.pb_b14, '0215': self.pb_b15, '0216': self.pb_b16,
                      '0301': self.pb_c1, '0302': self.pb_c2, '0303': self.pb_c3, '0304': self.pb_c4,
                      '0305': self.pb_c5, '0306': self.pb_c6, '0307': self.pb_c7, '0308': self.pb_c8,
                      '0309': self.pb_c9, '0310': self.pb_c10, '0311': self.pb_c11, '0312': self.pb_c12,
                      '0313': self.pb_c13, '0314': self.pb_c14, '0315': self.pb_c15, '0316': self.pb_c16,
                      '0401': self.pb_d1, '0402': self.pb_d2, '0403': self.pb_d3, '0404': self.pb_d4,
                      '0405': self.pb_d5, '0406': self.pb_d6, '0407': self.pb_d7, '0408': self.pb_d8,
                      '0409': self.pb_d9, '0410': self.pb_d10, '0411': self.pb_d11, '0412': self.pb_d12,
                      '0413': self.pb_d13, '0414': self.pb_d14, '0415': self.pb_d15, '0416': self.pb_d16}

        self.now = self.rules  # выбрана стандартная кнопка
        self.turn = 'w'  # ход игрока white
        self.action_points = 0

        self.rules.clicked.connect(self.rule)
        self.fire.clicked.connect(self.canon_fire)  # реакции на нажатие кнопок
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
        if self.now == self.rules and self.sender().text() != '' and self.sender().text()[4] == self.turn:
            # если выбрана стандартная кнопка, и если нажата не пустая клетка и это танк игрока,
            self.now = self.sender()  # то сохраняем название кнопки и выделяем её цветом
            self.now.setStyleSheet('background-color: rgb(228, 230, 78)')

            self.action_points = TANKS_DESCRIPTION[self.sender().text()[5]][0]
        elif self.now != self.rules and self.action_points == TANKS_DESCRIPTION[self.now.text()[5]][0]:
            # если танк ничего не делал в ходу,
            self.now.setStyleSheet('')  # то очищаем выбор
            self.now = self.rules
            if self.sender().text() != '' and self.sender().text()[4] == self.turn:  # если нажата не пустая клетка,
                self.now = self.sender()  # и это танк игрока, то сохраняем название кнопки и выделяем её цветом
                self.now.setStyleSheet('background-color: rgb(228, 230, 78)')
                self.action_points = TANKS_DESCRIPTION[self.sender().text()[5]][0]

    def rule(self):
        self.win = Rule()  # создаём объект класса Rule
        self.win.show()

    def rotate(self, direction):
        if self.action_points != 0 and self.now != self.rules:  # если танк выбран, и у него есть очки действия
            if direction == 'left':  # если нажата кнопка поворот на лево
                if int(self.now.text()[6]) - 1 == 0:
                    self.now.setText(self.now.text()[:6] + '8')
                else:
                    self.now.setText(self.now.text()[:6] + str(int(self.now.text()[6]) - 1))
                self.action_points -= 1
                '''
                self.now.setIcon(QIcon(''))
                '''
            elif direction == 'right':  # если нажата кнопка поворот на право
                if int(self.now.text()[6]) + 1 == 9:
                    self.now.setText(self.now.text()[:6] + '1')
                else:
                    self.now.setText(self.now.text()[:6] + str(int(self.now.text()[6]) + 1))
                self.action_points -= 1

    def riding_back(self):
        pass

    def riding_up(self):
        pass

    def canon_fire(self):
        pass


class Rule(QMainWindow):
    def __init__(self):
        super(Rule, self).__init__()
        uic.loadUi('rules_des.ui', self)

        self.name = './pic/rules_0.png'  # задаём путь к первой картинке
        im = QPixmap(self.name)
        self.label.setPixmap(im)  # ставим картинку на надпись
        self.num = 0  # номер картинки

        self.last.clicked.connect(self.last_png)
        self.next.clicked.connect(self.next_png)  # реакции на нажатие кнопок
        self.pb_close.clicked.connect(self.close_rule)

    def last_png(self):
        if self.num - 1 != -1:
            self.num -= 1
            self.name = f'./pic/rules_{self.num}.png'

            im = QPixmap(self.name)
            self.label.setPixmap(im)

    def next_png(self):
        if self.num + 1 != 5:
            self.num += 1
            self.name = f'./pic/rules_{self.num}.png'

            im = QPixmap(self.name)
            self.label.setPixmap(im)

    def close_rule(self):
        self.window().close()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TankChess()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
