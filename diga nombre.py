# hcaer una funsion que pida 3 opciones

registro = {}


def gestiode_id(registro, cedula):
    coderf = None


for id, coder in registro.items():
    if coder["cedula"] == cedula:
        coderf = cedula


registro = {"1": {"id": 101682128,
                  "nombre": "sebas",
                  "edad": "22",
                  "nivel In": "A+1"},

            "2": {"id": 1123234323,
                  "nombre": "carlos",
                  "edad ": "15",
                  "nivel In": "B+1"},

            "3": {"id": 123434235,
                  "nombre": "hillary",
                  "edad": "19",
                  "nivel in": "A+1"}
            }

print(f"estado actual:{registro}")

borrar = ("digite para eliminar:")
