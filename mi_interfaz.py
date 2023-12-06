import PySimpleGUI as pg

pg.theme("DarkPurple1")

layout = [
    [pg.Text("MI PRIMERA INTERFAZ")],
    [pg.Button("SUMAR"), pg.Button("BOTON 2")],
    [pg.InputText(key="num_1"),pg.InputText(key="num_2")],
    #[pg.Slider((0,10), orientation = "horizontal")],
    [pg.Output(size=(45,10))],
]

ventana = pg.Window("MI APLICACION", layout)

def sumar(*args):
    return sum(args)

def multp(*args):
    return sum(args)

while True:
    evento, valor = ventana.read()
    if evento == pg.WIN_CLOSED:
        ventana.close()
        break
    if evento == "SUMAR":
        print(sumar(int(valor["num_1"]),int(valor["num_2"])))
    if evento == "BOTON 2":
        print(multp(int(valor["num_1"]),int(valor["num_2"])))