
    x = accelerometer.get_x()
        y = accelerometer.get_y()
            
                if x < -300:   # inclinación izquierda
                        display.show(Image.ARROW_W)
                            elif x > 300:  # inclinación derecha
                                    display.show(Image.ARROW_E)
                                        elif y < -300:  # inclinación adelante
                                                display.show(Image.ARROW_N)
                                                    elif y > 300:   # inclinación atrás
                                                            display.show(Image.ARROW_S)
                                                                else:          # en reposo
                                                                        display.show(Image.HEART)