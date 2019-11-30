class Mood(object): 
    # 로직이 좋지 않음. 여러분이 잘 짜세요~

    GENERIC   = 1
    HIGH_TEMP = 2
    LOW_TEMP  = 3
    HIGH_DUST = 4
    LOW_DUST  = 5

    def decision(self, data):
        temp = float(data[0])
        dust = float(data[1])
    
        if temp <= 0:
            return self.LOW_TEMP

        if temp > 30:
            return self.HIGH_TEMP

        if 80 <= dust < 200:
            return self.LOW_DUST

        if dust >= 200:
            return self.HIGH_DUST

        if (0 < temp <=30) and (dust < 80):
            return self.GENERIC
