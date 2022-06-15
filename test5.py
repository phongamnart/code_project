from machine import Pin, PWM

s = PWM(Pin(0))
s.freq(50)
continuar = True

while continuar:
    a = input("Digite: ")
    if a == "fin":
        cuntinuar=False
        s.dedinit()
        print("FIN")
    else:
        ton = (int(a)+45)*100000/9
        s.duty_ns(int(ton))