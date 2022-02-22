# Insertar velocidad del asteroide #
v=19 # km/s #
if v>=20:
    print('Un asteroide se dirige hacia la tierra a una velocidad elevada. ¡Búscalo en el cielo como un rayo de luz!')
    if vistacielo==true: # Variable imaginaria #
        print('¡Wow, se ve hermoso!')
    else:
        print('¡Suerte para la próxima!')
else:
    print('Se dirige un asteroide a la tierra pero es posible que la atmósfera lo desintegre antes de tocar suelo.')
# Se me ocurrió colocar la variable vistacielo sólo porque sabía que dado que la velocidad era de 19 km/s, no entraría en el "if" y no me cuestionaría el valor de la variable #