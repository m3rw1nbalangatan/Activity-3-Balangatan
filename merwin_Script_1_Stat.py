class statcomputation ():
    def health (base, ev, level, iv):
        return ((((2*base+iv+(ev/4))*level)/100))+level+10
        
    def otStat(base, iv, ev, level, nature):
        return ((((((2 * base) + iv + (ev /4) ) * level)) / 100 ) + 5 ) * nature