"""
1. Chequeador de tiempo de entradas y salidas de auto en estacionamiento:
Tarifa por hora: $10 pesos, en horario diurno de 9.00 a 21.00 hrs
Tarifa por noche: $50 pesos, la noche se considera 21.00 a 9.00 hrs
Tolerancia de 15 minutos, si entra y sale en ese periodo no debe pagar.

Condiciones especiales:
Si un auto entra 10 mins. antes de 21.00, no debe cobrarle la hora fraccionada y solo la noche.

Generar 4 escenarios al gusto, indicando monto a pagar y desglose de horas y noches utilizadas.
"""

import datetime
import math

tarifa_dia = 10
tarifa_noche = 50


def checador(entrada, salida):
    cobro = 0
    (hora_entrada, minuto_entrada) = entrada.split(":")
    (hora_salida, minuto_salida) = salida.split(":")
    hora_entrada = int(hora_entrada)
    hora_salida = int(hora_salida)
    minuto_entrada = int(minuto_entrada)
    minuto_salida = int(minuto_salida)

    diferencia = datetime.timedelta(
        hours=int(hora_salida),
        minutes=int(minuto_salida)
    ) - datetime.timedelta(
        hours=int(hora_entrada),
        minutes=int(minuto_entrada)
    )

    minutos_total = int(diferencia.seconds / 60)

    if hora_entrada == hora_salida and minuto_entrada == minuto_salida:
        return 0, minutos_total

    if minutos_total < 15:
        return 0, minutos_total

    if hora_entrada < hora_salida:
        if hora_entrada < 9:
            if hora_salida < 9:
                return 50, minutos_total

            if hora_salida < 21:
                cobro = 50
                cobro += (minuto_salida / 60) * 10
                cobro += (hora_salida - 8) * 10
                return cobro, minutos_total

            if hora_salida >= 21:
                return 230, minutos_total

        if hora_entrada < 21:
            if hora_salida < 21:
                cobro = (minuto_salida / 60) * 10
                cobro += (hora_salida - hora_entrada) * 10
                return cobro, minutos_total

            if hora_salida >= 21:
                if hora_entrada == 20 and minuto_entrada >= 50:
                    return 50, minutos_total
                cobro = (21 - hora_entrada) * 10
                cobro += 50
                return cobro, minutos_total

        if hora_salida >= 21:
            return 50, minutos_total

    if hora_entrada == hora_salida:
        if minuto_entrada < minuto_salida:
            if hora_entrada < 9:
                if hora_salida < 9:
                    return 50, minutos_total

                if hora_salida < 21:
                    if hora_entrada == 20 and minuto_entrada >= 50:
                        return 50, minutos_total
                    cobro = (minuto_salida / 60) * 10
                    cobro += (hora_salida - 9) * 10
                    return cobro, minutos_total

            if hora_entrada < 21:
                if hora_salida < 21:
                    if hora_entrada == 20 and minuto_entrada >= 50:
                        return 50, minutos_total
                    cobro = (minuto_salida / 60) * 10
                    cobro += (hora_salida - hora_entrada) * 10
                    return cobro, minutos_total

            if hora_salida >= 21:
                return 50, minutos_total

        if minuto_entrada > minuto_salida:
            if hora_entrada < 9:
                return 230, minutos_total

            if hora_entrada < 21:
                cobro = (minuto_salida / 60) * 10
                cobro += (26 - hora_entrada) * 10
                cobro += (hora_salida - 9) * 10
                return cobro, minutos_total

            if hora_entrada >= 21:
                return 230, minutos_total

    if hora_entrada > hora_salida:
        if hora_entrada < 9:
            return 230, minutos_total

        if hora_entrada < 21:
            if hora_salida < 9:
                if hora_entrada == 20 and minuto_entrada >= 50:
                    return 50, minutos_total
                cobro = (26 - hora_entrada) * 10
                return cobro, minutos_total

            if hora_salida < 21:
                cobro = (minuto_salida / 60) * 10
                cobro += (26 - hora_entrada) * 10
                cobro += (hora_salida - 9) * 10
                return cobro, minutos_total

        if hora_entrada >= 21:
            if hora_salida < 9:
                return 50, minutos_total

            if hora_salida < 21:
                cobro = (minuto_salida / 60) * 10
                cobro += (hora_salida - 3) * 10
                return cobro, minutos_total

            if hora_salida >= 21:
                return 230, minutos_total

    return -1, minutos_total

def calcular(entrada, salida):
    res = checador(entrada, salida)
    print('Hora entrada', entrada)
    print('Hora salida ', salida)
    print('Tiempo total %2.0f:%2d horas' % (math.floor(res[1] / 60), res[1] % 60))
    print('Costo estacionamiento $%.1f' % res[0], end='\n\n')

if __name__ == "__main__":
    calcular('12:35', '19:21')
    calcular('21:55', '23:40')
    calcular('13:10', '11:31')
    calcular('10:51', '10:59')
    
    calcular('13:00', '18:59')
    
    
