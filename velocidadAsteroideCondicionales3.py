# Declarar variables #
v=19 # km/s #
t=18 # m #
if v>=20: # If de velocidad #
    print('Un asteroide se dirige hacia la tierra a una velocidad elevada. ¡Búscalo en el cielo como un rayo de luz!')
    if vistacielo==true: # Variable imaginaria #
        print('¡Wow, se ve hermoso!')
    else:
        print('¡Suerte para la próxima!')
else:
    print('Se dirige un asteroide a la tierra pero es posible que la atmósfera lo desintegre antes de tocar suelo.')
if t<25: #If de tamaño #
    print('Se dirige un asteroide muy pequeño a la tierra.')
elif t>25 and t<1000:
    print('¡Se dirige un asteroide a la tierra y podría causar serios daños!')
