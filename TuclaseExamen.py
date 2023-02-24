def arithmetic_arranger(problems, show_answers=False):
    # Verificar si el número de problemas es mayor que 5
    if len(problems) > 5:
        return "Error: Too many problems."

    # Inicializar variables para la salida
    arriba = ""
    abajo = ""
    linea = ""
    result = ""

    for problem in problems:
        # Separar los operandos y el operador
        operands = problem.split()
        operator = operands[1]
        num1 = operands[0]
        num2 = operands[2]

        # Verificar si el operador es válido
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        # Verificar si los operandos contienen sólo dígitos
        if not num1.isdigit() or not num2.isdigit():
            return "Error: Numbers must only contain digits."

        # Verificar si los operandos tienen un máximo de 4 dígitos
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Calcular la longitud del número más largo
        length = max(len(num1), len(num2)) + 2

        # Crear las líneas superiores e inferiores para cada problema
        arriba += num1.rjust(length) + "    "
        abajo += operator + num2.rjust(length - 1) + "    "
        linea += "-" * length + "    "

        # Calcular el resultado si show_answers es True
        if show_answers:
            if operator == '+':
                res = int(num1) + int(num2)
            else:
                res = int(num1) - int(num2)

            result += str(res).rjust(length) + "    "

    # Construir la salida final
    arranged_problems = arriba.rstrip() + "\n" + abajo.rstrip() + "\n" + linea.rstrip()

    # Añadir los resultados si show_answers es True
    if show_answers:
        arranged_problems += "\n" + result.rstrip()

    return arranged_problems

    