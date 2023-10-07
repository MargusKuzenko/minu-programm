def on_button_pressed_a():
    global x, pikkus, stuff, asukoht, asukoht2, counter
    x += 1
    led.plot(x, y)
    keha.append(x)
    keha.append(y)
    led.unplot(keha[0], keha[1])
    if x == asukoht and y == asukoht2:
        pikkus += 1
        stuff = True
        while stuff:
            asukoht = randint(0, 4)
            asukoht2 = randint(0, 4)
            counter = 0
            for index in range(pikkus):
                if list2[counter] == asukoht and list2[counter + 1] == asukoht2:
                    break
                    stuff = True
                else:
                    stuff = False
                counter += 2
    else:
        keha.shift()
        keha.shift()
        led.plot_brightness(asukoht, asukoht2, 1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global y, pikkus, stuff, asukoht, asukoht2, counter
    y += 1
    led.plot(x, y)
    keha.append(x)
    keha.append(y)
    led.unplot(keha[0], keha[1])
    if x == asukoht and y == asukoht2:
        pikkus += 1
        stuff = True
        while stuff:
            asukoht = randint(0, 4)
            asukoht2 = randint(0, 4)
            counter = 0
            for index2 in range(pikkus):
                if list2[counter] == asukoht and list2[counter + 1] == asukoht2:
                    break
                    stuff = True
                else:
                    stuff = False
                counter += 2
    else:
        keha.shift()
        keha.shift()
        led.plot_brightness(asukoht, asukoht2, 1)
input.on_button_pressed(Button.B, on_button_pressed_b)

list2: List[number] = []
counter = 0
stuff = False
asukoht2 = 0
asukoht = 0
keha: List[number] = []
y = 0
x = 0
pikkus = 0
pikkus = 1
x = 0
y = 2
keha = [x, y]
led.plot(x, y)
asukoht = randint(0, 4)
asukoht2 = randint(0, 4)
led.plot_brightness(asukoht, asukoht2, 1)

def on_forever():
    global x, pikkus, stuff, asukoht, asukoht2, counter, y
    if x == 5 or y == 5:
        if x == 5:
            x = 0
            led.plot(x, y)
            keha.append(x)
            keha.append(y)
            led.unplot(keha[0], keha[1])
            if x == asukoht and y == asukoht2:
                pikkus += 1
                stuff = True
                while stuff:
                    asukoht = randint(0, 4)
                    asukoht2 = randint(0, 4)
                    counter = 0
                    for index3 in range(pikkus):
                        if list2[counter] == asukoht and list2[counter + 1] == asukoht2:
                            break
                            stuff = True
                        else:
                            stuff = False
                        counter += 2
            else:
                keha.shift()
                keha.shift()
                led.plot_brightness(asukoht, asukoht2, 1)
        else:
            y = 0
            led.plot(x, y)
            keha.append(x)
            keha.append(y)
            led.unplot(keha[0], keha[1])
            if x == asukoht and y == asukoht2:
                pikkus += 1
                stuff = True
                while stuff:
                    asukoht = randint(0, 4)
                    asukoht2 = randint(0, 4)
                    counter = 0
                    for index4 in range(pikkus):
                        if list2[counter] == asukoht and list2[counter + 1] == asukoht2:
                            break
                            stuff = True
                        else:
                            stuff = False
                        counter += 2
            else:
                keha.shift()
                keha.shift()
                led.plot_brightness(asukoht, asukoht2, 1)
basic.forever(on_forever)
