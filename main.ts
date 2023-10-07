input.onButtonPressed(Button.A, function () {
    x += 1
    led.plot(x, y)
    keha.push(x)
    keha.push(y)
    led.unplot(keha[0], keha[1])
    if (x == asukoht && y == asukoht2) {
        pikkus += 1
        stuff = true
        while (stuff) {
            asukoht = randint(0, 4)
            asukoht2 = randint(0, 4)
            counter = 0
            for (let index = 0; index < pikkus; index++) {
                if (list[counter] == asukoht && list[counter + 1] == asukoht2) {
                    break;
stuff = true
                } else {
                    stuff = false
                }
                counter += 2
            }
        }
    } else {
        keha.shift()
        keha.shift()
        led.plotBrightness(asukoht, asukoht2, 1)
    }
})
input.onButtonPressed(Button.B, function () {
    y += 1
    led.plot(x, y)
    keha.push(x)
    keha.push(y)
    led.unplot(keha[0], keha[1])
    if (x == asukoht && y == asukoht2) {
        pikkus += 1
        stuff = true
        while (stuff) {
            asukoht = randint(0, 4)
            asukoht2 = randint(0, 4)
            counter = 0
            for (let index = 0; index < pikkus; index++) {
                if (list[counter] == asukoht && list[counter + 1] == asukoht2) {
                    break;
stuff = true
                } else {
                    stuff = false
                }
                counter += 2
            }
        }
    } else {
        keha.shift()
        keha.shift()
        led.plotBrightness(asukoht, asukoht2, 1)
    }
})
let list: number[] = []
let counter = 0
let stuff = false
let asukoht2 = 0
let asukoht = 0
let keha: number[] = []
let y = 0
let x = 0
let pikkus = 0
pikkus = 1
x = 0
y = 2
keha = [x, y]
led.plot(x, y)
asukoht = randint(0, 4)
asukoht2 = randint(0, 4)
led.plotBrightness(asukoht, asukoht2, 1)
basic.forever(function () {
    if (x == 5 || y == 5) {
        if (x == 5) {
            x = 0
            led.plot(x, y)
            keha.push(x)
            keha.push(y)
            led.unplot(keha[0], keha[1])
            if (x == asukoht && y == asukoht2) {
                pikkus += 1
                stuff = true
                while (stuff) {
                    asukoht = randint(0, 4)
                    asukoht2 = randint(0, 4)
                    counter = 0
                    for (let index = 0; index < pikkus; index++) {
                        if (list[counter] == asukoht && list[counter + 1] == asukoht2) {
                            break;
stuff = true
                        } else {
                            stuff = false
                        }
                        counter += 2
                    }
                }
            } else {
                keha.shift()
                keha.shift()
                led.plotBrightness(asukoht, asukoht2, 1)
            }
        } else {
            y = 0
            led.plot(x, y)
            keha.push(x)
            keha.push(y)
            led.unplot(keha[0], keha[1])
            if (x == asukoht && y == asukoht2) {
                pikkus += 1
                stuff = true
                while (stuff) {
                    asukoht = randint(0, 4)
                    asukoht2 = randint(0, 4)
                    counter = 0
                    for (let index = 0; index < pikkus; index++) {
                        if (list[counter] == asukoht && list[counter + 1] == asukoht2) {
                            break;
stuff = true
                        } else {
                            stuff = false
                        }
                        counter += 2
                    }
                }
            } else {
                keha.shift()
                keha.shift()
                led.plotBrightness(asukoht, asukoht2, 1)
            }
        }
    }
})
