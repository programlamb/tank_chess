import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QInputDialog
from board import Tank_chess
from rule import Rules


TANKS_DESCRIPTION = {'1': [5, (1, 0, 0), 1, 3, 2], '2': [4, (2, 1, 0), 2, 3, 2], '3': [3, (3, 2, 1), 3, 3, 2],
                     '4': [5, (1, 0, 0), 1, 3, 2]}
TRANSFORM_ROTATE = {'1': [(0, 1), ''], '2': [(1, 1), ''], '3': [(1, 0), ''], '4': [(1, -1), ''], '5': [(0, -1), ''],
                    '6': [(-1, -1), ''], '7': [(-1, 0), ''], '8': [(-1, 1), '']}


class TankChess(QMainWindow, Tank_chess):
    def __init__(self):
        super(TankChess, self).__init__()
        self.setupUi(self)
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
                      '0413': self.pb_d13, '0414': self.pb_d14, '0415': self.pb_d15, '0416': self.pb_d16,
                      '0501': self.pb_e1, '0502': self.pb_e2, '0503': self.pb_e3, '0504': self.pb_e4,
                      '0505': self.pb_e5, '0506': self.pb_e6, '0507': self.pb_e7, '0508': self.pb_e8,
                      '0509': self.pb_e9, '0510': self.pb_e10, '0511': self.pb_e11, '0512': self.pb_e12,
                      '0513': self.pb_e13, '0514': self.pb_e14, '0515': self.pb_e15, '0516': self.pb_e16,
                      '0601': self.pb_f1, '0602': self.pb_f2, '0603': self.pb_f3, '0604': self.pb_f4,
                      '0605': self.pb_f5, '0606': self.pb_f6, '0607': self.pb_f7, '0608': self.pb_f8,
                      '0609': self.pb_f9, '0610': self.pb_f10, '0611': self.pb_f11, '0612': self.pb_f12,
                      '0613': self.pb_f13, '0614': self.pb_f14, '0615': self.pb_f15, '0616': self.pb_f16,
                      '0701': self.pb_g1, '0702': self.pb_g2, '0703': self.pb_g3, '0704': self.pb_g4,
                      '0705': self.pb_g5, '0706': self.pb_g6, '0707': self.pb_g7, '0708': self.pb_g8,
                      '0709': self.pb_g9, '0710': self.pb_g10, '0711': self.pb_g11, '0712': self.pb_g12,
                      '0713': self.pb_g13, '0714': self.pb_g14, '0715': self.pb_g15, '0716': self.pb_g16,
                      '0801': self.pb_h1, '0802': self.pb_h2, '0803': self.pb_h3, '0804': self.pb_h4,
                      '0805': self.pb_h5, '0806': self.pb_h6, '0807': self.pb_h7, '0808': self.pb_h8,
                      '0809': self.pb_h9, '0810': self.pb_h10, '0811': self.pb_h11, '0812': self.pb_h12,
                      '0813': self.pb_h13, '0814': self.pb_h14, '0815': self.pb_h15, '0816': self.pb_h16,
                      '0901': self.pb_i1, '0902': self.pb_i2, '0903': self.pb_i3, '0904': self.pb_i4,
                      '0905': self.pb_i5, '0906': self.pb_i6, '0907': self.pb_i7, '0908': self.pb_i8,
                      '0909': self.pb_i9, '0910': self.pb_i10, '0911': self.pb_i11, '0912': self.pb_i12,
                      '0913': self.pb_i13, '0914': self.pb_i14, '0915': self.pb_i15, '0916': self.pb_i16,
                      '1001': self.pb_j1, '1002': self.pb_j2, '1003': self.pb_j3, '1004': self.pb_j4,
                      '1005': self.pb_j5, '1006': self.pb_j6, '1007': self.pb_j7, '1008': self.pb_j8,
                      '1009': self.pb_j9, '1010': self.pb_j10, '1011': self.pb_j11, '1012': self.pb_j12,
                      '1013': self.pb_j13, '1014': self.pb_j14, '1015': self.pb_j15, '1016': self.pb_j16,
                      '1101': self.pb_k1, '1102': self.pb_k2, '1103': self.pb_k3, '1104': self.pb_k4,
                      '1105': self.pb_k5, '1106': self.pb_k6, '1107': self.pb_k7, '1108': self.pb_k8,
                      '1109': self.pb_k9, '1110': self.pb_k10, '1111': self.pb_k11, '1112': self.pb_k12,
                      '1113': self.pb_k13, '1114': self.pb_k14, '1115': self.pb_k15, '1116': self.pb_k16,
                      '1201': self.pb_l1, '1202': self.pb_l2, '1203': self.pb_l3, '1204': self.pb_l4,
                      '1205': self.pb_l5, '1206': self.pb_l6, '1207': self.pb_l7, '1208': self.pb_l8,
                      '1209': self.pb_l9, '1210': self.pb_l10, '1211': self.pb_l11, '1212': self.pb_l12,
                      '1213': self.pb_l13, '1214': self.pb_l14, '1215': self.pb_l15, '1216': self.pb_l16,
                      '1301': self.pb_m1, '1302': self.pb_m2, '1303': self.pb_m3, '1304': self.pb_m4,
                      '1305': self.pb_m5, '1306': self.pb_m6, '1307': self.pb_m7, '1308': self.pb_m8,
                      '1309': self.pb_m9, '1310': self.pb_m10, '1311': self.pb_m11, '1312': self.pb_m12,
                      '1313': self.pb_m13, '1314': self.pb_m14, '1315': self.pb_m15, '1316': self.pb_m16,
                      '1401': self.pb_n1, '1402': self.pb_n2, '1403': self.pb_n3, '1404': self.pb_n4,
                      '1405': self.pb_n5, '1406': self.pb_n6, '1407': self.pb_n7, '1408': self.pb_n8,
                      '1409': self.pb_n9, '1410': self.pb_n10, '1411': self.pb_n11, '1412': self.pb_n12,
                      '1413': self.pb_n13, '1414': self.pb_n14, '1415': self.pb_n15, '1416': self.pb_n16,
                      '1501': self.pb_o1, '1502': self.pb_o2, '1503': self.pb_o3, '1504': self.pb_o4,
                      '1505': self.pb_o5, '1506': self.pb_o6, '1507': self.pb_o7, '1508': self.pb_o8,
                      '1509': self.pb_o9, '1510': self.pb_o10, '1511': self.pb_o11, '1512': self.pb_o12,
                      '1513': self.pb_o13, '1514': self.pb_o14, '1515': self.pb_o15, '1516': self.pb_o16,
                      '1601': self.pb_p1, '1602': self.pb_p2, '1603': self.pb_p3, '1604': self.pb_p4,
                      '1605': self.pb_p5, '1606': self.pb_p6, '1607': self.pb_p7, '1608': self.pb_p8,
                      '1609': self.pb_p9, '1610': self.pb_p10, '1611': self.pb_p11, '1612': self.pb_p12,
                      '1613': self.pb_p13, '1614': self.pb_p14, '1615': self.pb_p15, '1616': self.pb_p16}
        # словарь координат кнопок и их обЪектов для обращения

        self.now = self.rules  # выбрана стандартная кнопка
        self.visible_enemy = []
        self.turn = 'w'  # ход игрока white
        self.action_points = 0

        self.rules.clicked.connect(self.rule)
        self.end.clicked.connect(self.end_turn)  # реакции на нажатие кнопок
        [i.clicked.connect(self.choice) for i in self.squares.buttons()]

    def keyPressEvent(self, event):  # реакции на нажатие кнопок клавиатуры
        if self.action_points != 0 and self.now != self.rules:  # если танк выбран, и у него есть очки действия
            if event.key() == Qt.Key_Left or event.key() == Qt.Key_A:
                self.rotate('left')
            if event.key() == Qt.Key_Right or event.key() == Qt.Key_D:
                self.rotate('right')

            if event.key() == Qt.Key_Up or event.key() == Qt.Key_W:
                self.riding('up')
            if event.key() == Qt.Key_Down or event.key() == Qt.Key_S:
                self.riding('back')

            if event.key() == Qt.Key_Space or event.key() == Qt.Key_Enter:
                self.end_turn()

    def end_turn(self):
        if self.now != self.rules and self.action_points != TANKS_DESCRIPTION[self.now.text()[5]][0]:
            # если танк выбран и он что-то сделал в ходу
            for i in self.visible_enemy:
                i.setStyleSheet('')  # очищаем видимых врагов
            self.visible_enemy.clear()
            self.now.setStyleSheet('')
            self.now = self.rules  # очищаем выбор танка
            if self.turn == 'w':
                self.turn = 'b'
            else:
                self.turn = 'w'

    def choice(self):
        if self.sender() in self.visible_enemy and self.action_points != TANKS_DESCRIPTION[self.now.text()[5]][0]:
            self.canon_fire()
        elif self.now == self.rules and self.sender().text()[4] == self.turn and self.sender().text()[-1] != '0':
            # если выбрана стандартная кнопка, и если нажата не пустая клетка, не преграда и это танк игрока,
            self.now = self.sender()  # то сохраняем название кнопки и выделяем её цветом
            self.now.setStyleSheet('background-color: rgb(228, 230, 78)')
            self.visible()  #

            self.action_points = TANKS_DESCRIPTION[self.sender().text()[5]][0]
        elif self.now != self.rules and self.action_points == TANKS_DESCRIPTION[self.now.text()[5]][0]\
                and self.sender().text()[-1] != '0':
            # если танк ничего не делал в ходу,
            self.now.setStyleSheet('')  # то очищаем выбор
            self.now = self.rules
            for i in self.visible_enemy:
                i.setStyleSheet('')
            self.visible_enemy.clear()
            if self.sender().text() != '' and self.sender().text()[4] == self.turn:  # если нажата не пустая клетка,
                self.now = self.sender()  # и это танк игрока, то сохраняем название кнопки и выделяем её цветом
                self.now.setStyleSheet('background-color: rgb(228, 230, 78)')
                self.action_points = TANKS_DESCRIPTION[self.sender().text()[5]][0]
                self.visible()

    def rule(self):
        self.win = Rule()  # создаём объект класса Rule
        self.win.show()

    def rotate(self, direction):
        if direction == 'left':  # если нажата кнопка поворот на лево
            if int(self.now.text()[6]) - 1 == 0:
                self.now.setText(self.now.text()[:6] + '8')
            else:
                self.now.setText(self.now.text()[:6] + str(int(self.now.text()[6]) - 1))
        elif direction == 'right':  # если нажата кнопка поворот на право
            if int(self.now.text()[6]) + 1 == 9:
                self.now.setText(self.now.text()[:6] + '1')
            else:
                self.now.setText(self.now.text()[:6] + str(int(self.now.text()[6]) + 1))
        self.action_points -= 1
        self.visible()

    def riding(self, direction):
        x = ''.join([self.now.text()[x] for x in range(2) if x == 1 or self.now.text()[x] != '0'])
        y = ''.join([self.now.text()[x + 2] for x in range(2) if x == 1 or self.now.text()[x + 2] != '0'])
        # узнаём начальные координаты танка в str без 0

        if direction == 'up':
            new_x = str(int(x) + TRANSFORM_ROTATE[self.now.text()[6]][0][0])
            new_y = str(int(y) + TRANSFORM_ROTATE[self.now.text()[6]][0][1])  # вычисляем новые координаты
        elif self.action_points == TANKS_DESCRIPTION[self.now.text()[5]][0]:
            new_x = str(int(x) - TRANSFORM_ROTATE[self.now.text()[6]][0][0])
            new_y = str(int(y) - TRANSFORM_ROTATE[self.now.text()[6]][0][1])
        else:
            new_x = False
            new_y = False

        if new_x:
            x, y = new_x, new_y
            if len(new_x) == 1:
                x = '0' + new_x
            if len(new_y) == 1:  # добавляем нули обратно
                y = '0' + new_y
        if int(new_x) in range(1, 17) and int(new_y) in range(1, 17) and self.board[x + y].text()[4] == '0':
            # проверяем координаты на правильность
            if len(new_x) == 1:
                new_x = '0' + new_x
            if len(new_y) == 1:
                new_y = '0' + new_y

            self.board[new_x + new_y].setText(new_x + new_y + self.now.text()[4:])
            self.now.setText(self.now.text()[:4] + '000')
            self.now.setStyleSheet('')  # обновляем значения кнопок
            self.now = self.board[new_x + new_y]
            self.now.setStyleSheet('background-color: rgb(228, 230, 78)')

            if direction == 'up':
                self.action_points -= 1
            elif direction == 'back':
                self.action_points = 0
            self.visible()

            if self.now.text()[4] == '4' and self.turn == 'w' and self.now.text()[2:4] == '16':
                name, ok_pressed = QInputDialog.getText(self, 'Белый игрок выиграл!', 'Введите имя для доски почёта:')
                if ok_pressed:
                    ex.close()
            elif self.now.text()[4] == '4' and self.turn == 'b' and self.now.text()[2:4] == '01':
                name, ok_pressed = QInputDialog.getText(self, 'Чёрный игрок выиграл!', 'Введите имя для доски почёта:')
                if ok_pressed:
                    ex.close()

    def visible(self, enemy=''):
        for i in self.visible_enemy:
            i.setStyleSheet('')
        self.visible_enemy.clear()

        x = int(''.join([self.now.text()[x] for x in range(2) if x == 1 or self.now.text()[x] != '0']))
        y = int(''.join([self.now.text()[x + 2] for x in range(2) if x == 1 or self.now.text()[x + 2] != '0']))
        #

        if int(self.now.text()[6]) - 1 == 0:
            self.direc = '8'
        else:  #
            self.direc = str(int(self.now.text()[6]) - 1)

        f = False
        for i in range(3):
            new_x = x
            new_y = y
            j = False
            while i:
                new_x = str(int(new_x) + TRANSFORM_ROTATE[self.direc][0][0])
                new_y = str(int(new_y) + TRANSFORM_ROTATE[self.direc][0][1])
                #

                if int(new_x) not in range(1, 17) or int(new_y) not in range(1, 17):
                    break

                if len(new_x) == 1:
                    new_x = '0' + new_x
                if len(new_y) == 1:
                    new_y = '0' + new_y

                if self.board[new_x + new_y].text()[4] != self.turn\
                        and self.board[new_x + new_y].text()[6] != '0' and j:
                    self.board[new_x + new_y].setStyleSheet('background-color: rgb(255, 0, 8)')
                    self.visible_enemy.append(self.board[new_x + new_y])
                    if enemy == self.board[new_x + new_y]:
                        f = True
                if self.board[new_x + new_y].text()[4] != '0':
                    break
                j = True
            if f:
                break
            if int(self.direc) + 1 == 9:
                self.direc = '1'
            else:
                self.direc = str(int(self.direc) + 1)

    def canon_fire(self):
        self.visible(self.sender())
        if abs(int(self.sender().text()[6]) - int(self.direc)) == 4:
            hit = TANKS_DESCRIPTION[self.now.text()[5]][2] - TANKS_DESCRIPTION[self.sender().text()[5]][1][0]
        elif self.sender().text()[6] == self.direc:
            hit = TANKS_DESCRIPTION[self.now.text()[5]][2] - TANKS_DESCRIPTION[self.sender().text()[5]][1][2]
        else:
            hit = TANKS_DESCRIPTION[self.now.text()[5]][2] - TANKS_DESCRIPTION[self.sender().text()[5]][1][1]
        if hit > 0:
            if self.sender().text()[4] == '4':
                if self.turn == 'w':
                    message = 'Белый игрок выиграл!'
                else:
                    message = 'Чёрный игрок выиграл!'
                name, ok_pressed = QInputDialog.getText(self, message, 'Введите имя для доски почёта:')
                if ok_pressed:
                    ex.close()
            self.sender().setText(self.sender().text()[:4] + 'b00')

        self.end_turn()


class Rule(QMainWindow, Rules):
    def __init__(self):
        super(Rule, self).__init__()
        self.setupUi(self)

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
