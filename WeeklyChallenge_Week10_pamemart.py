#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" 
Level 1. Weekly Challenge 10: Regex Challenge

"""

__author__ = "Pam Martínez"
__contact__ = "pamemart@cisco.com"
__copyright__ = "Copyright 2021, Cisco Systems"
__credits__ = ["MXC Programming Club, Luis Uribe"]
__date__ = "2021/03/02"
__deprecated__ = False
__email__ =  "pamemart@cisco.com"
__maintainer__ = "Pam Martínez"
__status__ = "Development"
__version__ = "0.0.1"


import re


"""
Usando el siguiente texto, crea tres regrex para capturar lo siguiente en 
grupos de captura:
- Enlaces
 
- Contenido de los parrafos
 
- HTML tags
<p>This is a paragraph.<h1>Header1</h1></p><p>This is another paragraph .</p>
<a href="link1" class="doc">...</a>
<a href="link2" class="doc">...</a>
"""


texto = """
<p>This is a paragraph.<h1>Header1</h1></p><p>This is another paragraph .</p>
<a href="link1" class="doc">...</a>
<a href="link2" class="doc">...</a>
"""

url = 'cisco.com?id=133&cec=luribegu&team=aci'
url2 = 'cisco.com?id=&cec=luribegu&team=aci'

correo1 = 'pamema_rt@cisco.com'

ips = [
'192.168.1.33',
'255.300.0.0',
'33.9.92.1',
'3.100.0.1',
'256.9.9.9',
'0.0.0.0',
'200.200.200.1000'
]

operaciones = [
'- 12 + 75 = 63',
'15 - 13 = 2',
'10 - 86 = -76',
'5 * 11 = 55',
'9 + 5i - 12 = - 3 + 5i',
'- 1 - 10i + 6 - 3i = 5 - 7i',
'1 + 2i + 11i = 1 + 12i',
'4 + 2x + 1 = 5 - 2x',
]

def busca(valor,patron,cadena):
    resultados = re.findall(patron, cadena, re.DOTALL)
    if resultados:
        print(f"{valor}: {resultados}")
    else:
        print(f'No se encontró el patrón buscado')

def valida(patron,cadena):
    resultados = re.match(patron, cadena)
    if resultados:
        print(f"{resultados.group()} es un valor correcto.")
    else:
        print(f"{cadena} no es válido.")

def operacion(oper_real, oper_complejo, cadena):
    real = re.match(oper_real, cadena)
    complejo = re.match(oper_complejo, cadena)
    if real:
        print(f"{real.group()} es una suma o resta de números reales.")
    elif complejo:
        print(f"{complejo.group()} es una suma o resta de números complejos.")
    else:
        print(f"{cadena} es una operación no válida.")

def main():
    patron = {
        'enlaces' : 'href=".+?"',
        'parrafos' : '<p>.+?<\/p>', 
        'tags' : '<.+?>', 
        'id' : 'id=[0-9]+', 
        'cec' : 'cec=[a-z]+',
        'team' : 'team=[a-z]+', 
        'correo' : '^[a-z][a-z|0-9|_]+[a-z|0-9]\@cisco\.com$',
        'ip' : '^((2[0-4][0-9]|25[0-5]|[0-1]{0,1}[0-9]{1,2})\.){3}(2[0-4][0-9]|25[0-5]|[0-1]{0,1}[0-9]{1,2})$$',
        'oper_real' : '^(([-|+]\s){0,1}\d+\s)+\=\s([-|+]){0,1}\d+$',
        'oper_complejo' : '^(([-|+]\s){0,1}\d+i{0,1}\s)+\=\s([-|+]\s){0,1}\d+\s[+|-]\s\d+i'
    }

    print(f"Texto:{texto}")
    busca('Enlaces',patron['enlaces'], texto);  
    busca('Párrafos',patron['parrafos'], texto)
    busca('Tags',patron['tags'], texto)

    print(f"\n\nURL: {url2}\n")
    busca('Id',patron['id'], url2)
    busca('CEC',patron['cec'], url2)
    busca('Team',patron['team'], url2)

    print(f"\n\nCorreo: {correo1} <--", end=' ')
    valida(patron['correo'], correo1)

    print(f"\n\nIPs: {ips}\n")
    for ip in ips:
        valida(patron['ip'], ip)

    print(f"\n\nOperacioness: {operaciones}\n")
    for oper in operaciones:
        operacion(patron['oper_real'],patron['oper_complejo'], oper)


if __name__ == "__main__":
    main()