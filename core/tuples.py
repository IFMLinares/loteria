from datetime import datetime, time

# Tupla de 9:00AM - 7:00PM
HOUR_CHOICES = [(time(hour=i, minute=0).strftime('%I:%M %p'), time(hour=i, minute=0).strftime('%I:%M %p')) for i in range(9, 20)]

# Tupla de 8:00AM - 7:00PM
HOUR_CHOICES_SP = [(time(hour=i, minute=0).strftime('%I:%M %p'), time(hour=i, minute=0).strftime('%I:%M %p')) for i in range(8, 20)]

# Tupla de 8:30AM - 7:30PM
HOUR_CHOICES_GP = [(time(hour=i, minute=j).strftime('%I:%M %p'), time(hour=i, minute=j).strftime('%I:%M %p')) for i in range(8, 21) for j in (30,) if not (i == 8 and j == 0)]

# Tupla de 7:00AM - 6:00PM
HOUR_CHOICES_LG = [(time(hour=i, minute=0).strftime('%I:%M %p'), time(hour=i, minute=0).strftime('%I:%M %p')) for i in range(8, 20)]

# Tupla de 9:05AM - 7:05PM
HOUR_CHOICES_RC = [(time(hour=i, minute=5).strftime('%I:%M %p'), time(hour=i, minute=5).strftime('%I:%M %p')) for i in range(9, 20)]

# Tupla de 8:00AM - 5:00PM
HOUR_CHOICES_GA = [(time(hour=i, minute=0).strftime('%I:%M %p'), time(hour=i, minute=0).strftime('%I:%M %p')) for i in range(8, 17)]

# Lista de animales para ChanceAnimalitos
ANIMALITO_CHOICES = [
    ("00", "Ballena"),
    ("0", "Delfín"),
    ("1", "Carnero"),
    ("2", "Toro"),
    ("3", "Ciempies"),
    ("4", "Alacran"),
    ("5", "León"),
    ("6", "Sapo"),
    ("7", "Loro"),
    ("8", "Ratón"),
    ("9", "Águila"),
    ("10", "Tigre"),
    ("11", "Gato"),
    ("12", "Caballo"),
    ("13", "Mono"),
    ("14", "Paloma"),
    ("15", "Zorro"),
    ("16", "Oso"),
    ("17", "Pavo"),
    ("18", "Burro"),
    ("19", "Cabra"),
    ("20", "Cochino"),
    ("21", "Gallo"),
    ("22", "Camello"),
    ("23", "Cebra"),
    ("24", "Iguana"),
    ("25", "Gallina"),
    ("26", "Vaca"),
    ("27", "Perro"),
    ("28", "Zamuro"),
    ("29", "Elefante"),
    ("30", "Caimán"),
    ("31", "Lapa"),
    ("32", "Ardilla"),
    ("33", "Pescado"),
    ("34", "Venado"),
    ("35", "Jirafa"),
    ("36", "Culebra")
]

# Lista Para la granja plus
ANIMALITO_GRANA_PLUS_CHOICES = [
    ("1", "Carnero"),
    ("2", "Toro"),
    ("3", "Ciempies"),
    ("4", "Alacran"),
    ("5", "León"),
    ("6", "Rana"),
    ("7", "Perico"),
    ("8", "Ratón"),
    ("9", "Águila"),
    ("10", "Tigre"),
    ("11", "Gato"),
    ("12", "Caballo"),
    ("13", "Mono"),
    ("14", "Paloma"),
    ("15", "Zorro"),
    ("16", "Oso"),
    ("17", "Pavo"),
    ("18", "Burro"),
    ("19", "Chivo"),
    ("20", "Cochino"),
    ("21", "Gallo"),
    ("22", "Camello"),
    ("23", "Cebra"),
    ("24", "Iguana"),
    ("25", "Gallina"),
    ("26", "Vaca"),
    ("27", "Perro"),
    ("28", "Zamuro"),
    ("29", "Elefante"),
    ("30", "Caimán"),
    ("31", "Lapa"),
    ("32", "Ardilla"),
    ("33", "Pescado"),
    ("34", "Venado"),
    ("35", "Jirafa"),
    ("36", "Culebra")
]

# La grajita
ANIMALITO_GRANJITA_LOTTO_ACTIVO_SELVA_PLUS_CHOICES = [
    ("00", "Ballena"),
    ("0", "Delfín"),
    ("1", "Carnero"),
    ("2", "Toro"),
    ("3", "Ciempies"),
    ("4", "Alacran"),
    ("5", "León"),
    ("6", "Rana"),
    ("7", "Perico"),
    ("8", "Ratón"),
    ("9", "Águila"),
    ("10", "Tigre"),
    ("11", "Gato"),
    ("12", "Caballo"),
    ("13", "Mono"),
    ("14", "Paloma"),
    ("15", "Zorro"),
    ("16", "Oso"),
    ("17", "Pavo"),
    ("18", "Burro"),
    ("19", "Chivo"),
    ("20", "Cochino"),
    ("21", "Gallo"),
    ("22", "Camello"),
    ("23", "Cebra"),
    ("24", "Iguana"),
    ("25", "Gallina"),
    ("26", "Vaca"),
    ("27", "Perro"),
    ("28", "Zamuro"),
    ("29", "Elefante"),
    ("30", "Caimán"),
    ("31", "Lapa"),
    ("32", "Ardilla"),
    ("33", "Pescado"),
    ("34", "Venado"),
    ("35", "Jirafa"),
    ("36", "Culebra")
]

# lA RICACHONA
ANIMALITO_LA_RICACHONA_CHOICES = [
    ("00", "Ballena"),
    ("1", "Carnero"),
    ("2", "Toro"),
    ("3", "Ciempies"),
    ("4", "Alacran"),
    ("5", "León"),
    ("6", "Rana"),
    ("7", "Perico"),
    ("8", "Ratón"),
    ("9", "Águila"),
    ("10", "Tigre"),
    ("11", "Gato"),
    ("12", "Caballo"),
    ("13", "Mono"),
    ("14", "Paloma"),
    ("15", "Zorro"),
    ("16", "Oso"),
    ("17", "Pavo"),
    ("18", "Burro"),
    ("19", "Chivo"),
    ("20", "Cochino"),
    ("21", "Gallo"),
    ("22", "Camello"),
    ("23", "Cebra"),
    ("24", "Iguana"),
    ("25", "Gallina"),
    ("26", "Vaca"),
    ("27", "Perro"),
    ("28", "Zamuro"),
    ("29", "Elefante"),
    ("30", "Caimán"),
    ("31", "Lapa"),
    ("32", "Ardilla"),
    ("33", "Pescado"),
    ("34", "Venado"),
    ("35", "Jirafa"),
    ("36", "Culebra")
]

ANIMALITO_GUACHARO_ACTIVO_CHOICES = [
    ("00", "Ballena"),
    ("0", "Delfín"),
    ("1", "Carnero"),
    ("2", "Toro"),
    ("3", "Ciempies"),
    ("4", "Alacran"),
    ("5", "León"),
    ("6", "Rana"),
    ("7", "Perico"),
    ("8", "Ratón"),
    ("9", "Águila"),
    ("10", "Tigre"),
    ("11", "Gato"),
    ("12", "Caballo"),
    ("13", "Mono"),
    ("14", "Paloma"),
    ("15", "Zorro"),
    ("16", "Oso"),
    ("17", "Pavo"),
    ("18", "Burro"),
    ("19", "Chivo"),
    ("20", "Cochino"),
    ("21", "Gallo"),
    ("22", "Camello"),
    ("23", "Cebra"),
    ("24", "Iguana"),
    ("25", "Gallina"),
    ("26", "Vaca"),
    ("27", "Perro"),
    ("28", "Zamuro"),
    ("29", "Elefante"),
    ("30", "Caimán"),
    ("31", "Lapa"),
    ("32", "Ardilla"),
    ("33", "Pescado"),
    ("34", "Venado"),
    ("35", "Jirafa"),
    ("36", "Culebra"),
    ("37", "Tortuga"),
    ("38", "Búfalo"),
    ("39", "Lechuza"),
    ("40", "Avispa"),
    ("41", "Canguro"),
    ("42", "Tucán"),
    ("43", "Mariposa"),
    ("44", "Chiguire"),
    ("45", "Garza"),
    ("46", "Puma"),
    ("47", "Pavo Real"),
    ("48", "Puercoespín"),
    ("49", "Pereza"),
    ("50", "Canario"),
    ("51", "Pelícano"),
    ("52", "Pulpo"),
    ("53", "Caracol"),
    ("54", "Grillo"),
    ("55", "Oso Hormiguero"),
    ("56", "Tiburón"),
    ("57", "Pato"),
    ("58", "Hormiga"),
    ("59", "Pantera"),
    ("60", "Camaleón"),
    ("61", "Panda"),
    ("62", "Cachicamo"),
    ("63", "Cangrejo"),
    ("64", "Gavilán"),
    ("65", "Araña"),
    ("66", "Lobo"),
    ("67", "Avestruz"),
    ("68", "Jaguar"),
    ("69", "Conejo"),
    ("70", "Bisonte"),
    ("71", "Guacamaya"),
    ("72", "Gorila"),
    ("73", "Hipopótamo"),
    ("74", "Turpial"),
    ("75", "Guácharo")
]
