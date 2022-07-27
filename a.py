import os
file = open("1. Introduccion a bases de datos", "w")
for i in range(24):
    if i<10:
        file.write("![](http://kunusoft.com/slides/bd1/bd101_intro/Diapositiva0"+str(i)+".JPG)" + os.linesep)
    else:
        file.write("![](http://kunusoft.com/slides/bd1/bd101_intro/Diapositiva"+str(i)+".JPG)" + os.linesep)

file.close()