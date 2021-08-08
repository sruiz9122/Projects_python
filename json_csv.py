import json

a = {"nombre" : "Gabriel",
     "asignatura" : "Matematicas",
     "vaPerdiendo": True,
     "notas":[1,3.5]
     }

with open("alumnoGabriel.jason",'w') as f:
    json.dump(a,f)

al_gabriel = {
    "1" : "Gabriel",
    "asignatura" : "matematicas",
    "laVaPerdiendo" : True,
    "notasActuales" : [1.0, 3.5]

}
json_hilera = json.dumps(al_gabriel)

with open("alumnoGabriel.json", 'r', encoding="utf-8") as f:
    nuevo_alumno = json.load(f)