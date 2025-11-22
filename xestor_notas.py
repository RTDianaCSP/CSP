def introducir_notas():
    notas = []
    print("Introduce as notas dos estudiantes (entre 0 y 10). Escribe -1 para rematar.")
    while True:
        try:
            nota = float(input("Nota: "))
            if nota == -1:
                break
            elif 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("ERROR:A nota debe estar entre 0 e 10")
        except ValueError:
            print("ERROR: Debes introducir un número válido")
    return notas

def calcular_estatisticas(notas):
    if not notas:
        print("ERROR: Non se introduciron notas")
        return
    media = sum(notas) / len(notas)
    mejor = max(notas)
    peor = min(notas)
    aprobados = len([n for n in notas if n >= 5])
    suspensos = len(notas) - aprobados

    print("\n📊 Estatísticas:")
    print(f"- Media: {media:.2f}")
    print(f"- Mellor nota: {mejor}")
    print(f"- Peor nota: {peor}")
    print(f"- Aprobados: {aprobados}")
    print(f"- Suspensos: {suspensos}")

def main():
    print("****XESTOR DE NOTAS DE ESTUDANTES*****")
    notas = introducir_notas()
    calcular_estatisticas(notas)
    print("\n****Programa finalizado****")

if __name__ == "__main__":
    main()







