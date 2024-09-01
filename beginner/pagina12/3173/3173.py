import math
from datetime import datetime, timedelta

n = int(input())

jupyter_AT=11.9
saturns_AT=29.6
initial=datetime.strptime("21/12/2020", "%d/%m/%Y")

jupyter_bissexto=round(11.9 * n / 4)
saturns_bissexto=math.floor(29.6 * n / 4)

def calcularDias(AT: float):
  return 365 * AT

jupyter_days=n*calcularDias(jupyter_AT) + jupyter_bissexto
saturns_days=n*calcularDias(saturns_AT) + saturns_bissexto

def defineData(dias):
  global initial
  nova_data = initial + timedelta(days=dias)
  return nova_data.strftime("%Y-%m-%d")

print(f"Dias terrestres para Jupiter = {int(jupyter_days)}")

print(f"Data terrestre para Jupiter: {defineData(jupyter_days)}")

print(f"Dias terrestres para Saturno = {int(saturns_days)}")

print(f"Data terrestre para Saturno: {defineData(saturns_days)}")