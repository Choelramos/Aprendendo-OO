# Usando a bibliotela partial e operator com exemplos:

# Neste exemplo estamos adicionando mais um ao elemento:
import operator
from functools import partial
adiciona_um = partial(operator.add, 1)

print(adiciona_um(5))




