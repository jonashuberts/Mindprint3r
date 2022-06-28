import re

buscar = re.compile(r'([XYZ])([0-9.]+)')

primer = 0

lletra_ultima_x = 'ABC'
valor_ultima_x = 0
lletra_ultima_y = 'ABC'
valor_ultima_y = 0

valor_ultima_z = 0

with open('x.gcode', 'r') as x:
    with open('ev3.rtf', 'w') as ev3:
        for match in buscar.finditer(x.read()):

            if primer == 0:
                if match.group(1) == 'Z':
                    ev3.write('0' + '\n')
                    ev3.write('0' + '\n')
                    ev3.write('0' + '\n')
                    valor_ultima_z = match.group(2)
                    primer = 1

            if lletra_ultima_x == 'X':
                if lletra_ultima_y == 'Y':
                    if match.group(1) == 'Z':
                        ev3.write(str(valor_ultima_x) + '\n')
                        ev3.write(str(valor_ultima_y) + '\n')
                        ev3.write(match.group(2) + '\n')
                        valor_ultima_z = match.group(2)
                    else:
                        ev3.write(str(valor_ultima_x) + '\n')
                        ev3.write(str(valor_ultima_y) + '\n')

                        ev3.write(str(valor_ultima_z) + '\n')

            lletra_ultima_x = str(lletra_ultima_y)
            valor_ultima_x = str(valor_ultima_y)

            lletra_ultima_y = match.group(1)
            valor_ultima_y = match.group(2)

        

        ev3.write(str(valor_ultima_x) + '\n')
        ev3.write('-1' + '\n')
