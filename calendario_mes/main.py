# importa bibliotecas
import calendar
from datetime import date

# declaração de variáveis
mes = date.today().month
ano = date.today().year

# imprime o calendário do mês
print(calendar.month(ano, mes))