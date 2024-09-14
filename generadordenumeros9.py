import random,math

def generateOTP():
    OTP = ""
    for i in range(10):  # Cambié el rango para que haga 6 iteraciones
        a = random.random()
        b = math.floor(a * 10)  # Cambié a 10 para generar dígitos del 0 al 9
        OTP += str(b)
    return OTP  # El return ahora está fuera del bucle

# Ejecutar la función y mostrar el OTP
print("OTP de 6 dígitos:", generateOTP())
