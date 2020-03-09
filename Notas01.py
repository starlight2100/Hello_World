def help():
    print("É necessário informar o valor da nota.")
    print("Sintaxe: {0} <valor>".format(sys.argv[0]))


def nota(valor):
    if 9.0 < valor <= 10.0:
        return "A"
    elif 8.0 < valor <= 9.0:
        return "A-"
    elif 7.0 < valor <= 8.0:
        return "B"
    elif 6.0 < valor <= 7.0:
        return "B-"
    elif 5.0 < valor <= 6.0:
        return "C"
    elif 4.0 < valor <= 5.0:
        return "C-"
    elif 3.0 < valor <= 4.0:
        return "D"
    elif 2.0 < valor <= 3.0:
        return "D-"
    elif 1.0 < valor <= 2.0:
        return "E"
    elif 0.0 < valor <= 1.0:
        return "E-"
    else:
        return "Nota inválida"


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
        sys.exit(errno.EPERM)
    else:
        valor = float(sys.argv[1])
        print(nota(valor))
