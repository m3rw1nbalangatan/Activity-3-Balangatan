class evComputed():
    def computeEV (base, iv, ev, level, md, stats):
        M=(((2*base)+iv+(ev/4)) * ( level/100))
        statMds = stats/md
        return (((((statMds - M) * 400 )) / level) / 4 ) * 4