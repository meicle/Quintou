class ANSI (): # terminal color changing codes
    def red(letter):
        return "\33[1;91m".format(letter=letter)
    
    def yellow(letter):
        return "\33[1;93m".format(letter=letter)
    
    def green(letter):
        return "\33[1;92m".format(letter=letter)