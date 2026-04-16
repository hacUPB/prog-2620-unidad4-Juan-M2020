📝 Plantilla de Autoevaluación: Gestión de Mantenimiento de Flota Aeronáutica ✈️
Instrucciones para los estudiantes: 

1. Hagan una copia de este archivo y guárdenlo en la raíz de su repositorio con el nombre AUTOEVALUACION.md. 
2. Lean cuidadosamente cada criterio de la rúbrica. 
3. En el apartado Nota Esperada, asignen una calificación numérica (de 0.0 a 5.0) que consideren justa para su trabajo en ese criterio. 
4. En el apartado Justificación, expliquen con sus propias palabras por qué merecen esa nota. Sean críticos y honestos. 
5. En el apartado Evidencia, inserten pantallazos de la ejecución de la consola, imágenes de su diagrama o bloques de código (usando la sintaxis de Markdown con ```) que respalden su justificación. 
6. Al final, calculen su nota definitiva esperada según los porcentajes.

>👥 1. Información del Equipo

Miembro 1: [Juan José Marín Cuartas] - [000577614]
Miembro 2:

>📊 2. Evaluación por Criterios

Criterio 1: Diagrama y Lógica (Valor: 20%)
Evalúa si el diagrama es claro, lógico y representa fielmente la estructura de datos utilizada (listas/diccionarios) y el flujo del programa.

Nota Esperada (0.0 - 5.0): [4.5]
Justificación: aunque el diagrama de flujo ilustra el programa muy bien hay pasos que se saltaron en el diagrama pero no se colocaron porque se volveria muy extenso el diagrama y a parte de eso me toco agregar una parte del codigo que no se hizo en el diagrama porque no lo tuve en cuenta con respecto a las reglas del reto


![Diagrama de Flujo](Diagrama%20sin%20título.png)

El diagrama de flujo representa paso a paso cómo funciona mi programa codigo. Muestra el inicio, el registro de aeronaves usando un ciclo for, y dentro de este el registro de componentes. También refleja cómo se guardan los datos en una lista de diccionarios. Finalmente, el diagrama incluye una decisión (if) para verificar si los componentes necesitan mantenimiento y mostrar el resultado en pantalla.


Criterio 2: Uso de Estructuras (Listas y Diccionarios) (Valor: 30%)
Evalúa si se utilizaron diccionarios y listas de manera correcta y anidada para almacenar los datos ingresados por el usuario, sin redundancias.

Nota Esperada (0.0 - 5.0): [5.0]
Justificación: se usos una lista principal donde se crean las 3 aeronaves con su respectiva informacion de matricula, modelo, horas de uso del avion y componente donde estas son claves y el valor es ingresado por el usuario y tambien se inicia un diccionario como valor en la clave "componentes" 

```
#se crea la lista de aviones
flota = []
for i in range(3):

    print(f"Aeronave #{i+1}")
    matricula = input("Ingrese la Matricula de la Aeronave: ")
    modelo = input("Ingrese el Modelo de la Aeronave: ")
    horas = float(input("Ingrese las Horas de uso de la Aeronave: "))

    aeronave = {
    "matricula" : matricula ,
    "modelo" : modelo ,
    "horas" : horas,
    "componentes" : {}
    }
```


Criterio 3: Cumplimiento de Restricciones Técnicas (Valor: 20%)
Evalúa el respeto total a las reglas: uso de ciclos clásicos (for/while), cero uso de list comprehensions, y ninguna librería/función avanzada no vista en clase.

Nota Esperada (0.0 - 5.0): [4.8]
Justificación: No se tilizo librerías externas ni list comprehensions se hizo uso del ciclo for para ir agregando los aviones a la lista y los componentes en el diccionario y tambien se hizo uso del while para crear un menú interactivo que se repite hasta que el usuario decida salir ,pero si se uso mucho los ejemplos de clase.


```
for aeronave in flota:
    print(f"\nAeronave: {aeronave['matricula']} - {aeronave['modelo']}")

    for nombre, datos in aeronave["componentes"].items():
        if datos["horas_uso"] >= datos["limite"]:
            print(f"⚠️ {nombre} REQUIERE mantenimiento")
        else:
            print(f"✅ {nombre} en buen estado")
```

```
while True:
    print("\n=== MENÚ DE MODIFICACIONES ===")
    print("1. Agregar nueva aeronave")
    print("2. Eliminar aeronave")
    print("3. Agregar componente a una aeronave")
    print("4. Eliminar componente de una aeronave")
    print("5. Ver reporte de mantenimiento")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")
```

Criterio 4: Funcionalidad del Código (Valor: 15%)
Evalúa si el programa pide datos correctamente, no se "crashea" y genera el reporte final de mantenimiento esperado.

Nota Esperada (0.0 - 5.0): [5.0]
Justificación: El programa pide correctamente las 3 aeronaves con sus componentes y hace su respectivo reporte de mantenimiento para finalmente mostrar un menu con varias opciones donde puedo hacer modificaciones como eliminar o agregar nuevas aeronaves y tambien la opcion de ver esas modificaciones haciendo un nuevo reporte de mantenimiento 


Evidencia: 
![imagen1](Captura%20de%20pantalla%202026-04-16%20143848.png)
![imagen2](Captura%20de%20pantalla%202026-04-16%20143919.png)


Criterio 5: Preparación para Sustentación (Valor: 15%)
Aunque esta nota la dará el profesor en la entrevista oral, autoevalúen su nivel de preparación y comprensión del código que entregaron.


Nivel de Confianza (Bajo / Medio / Alto): [Medio]
Justificación: Aunque el programa funciona muy bien me costo mucho hacerlo en ciertos puntos me toco mirar muchos los ejemplos de clase y con prueba y error pero al final se llego a un buen funcionamiento del programa y a lo requerido en el programa y cada linea del codigo se entiende perfectamente


Evidencia de preparación: yo hice el codigo guiandome con la estructura del diagrama de flujo y lo aprendido en clase haciendo linea por linea y revisando el correcto funcionamineto del programa


> 📈 3. Cálculo de Nota Definitiva Esperada

Multipliquen la nota asignada en cada criterio por su porcentaje respectivo y sumen los resultados para obtener su nota final esperada.


| Criterio                      | Nota | Peso | Subtotal |
| ----------------------------- | ---- | ---- | -------- |
| Diagrama y Lógica             | 4.5  | 20%  | 0.90     |
| Uso de Estructuras            | 5.0  | 30%  | 1.50     |
| Cumplimiento de Restricciones | 4.8  | 20%  | 0.96     |
| Funcionalidad                 | 5.0  | 15%  | 0.75     |
| Sustentación                  | 4.0  | 15%  | 0.60     |
*TOTAL [4,71]*

✨ ""La educación es para el carácter, no solo para la mente"." ✨





