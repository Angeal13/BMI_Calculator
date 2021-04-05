from BMI import BMI

if __name__=='__main__':
    height=float(input('Your length is : '))
    weight=float(input('Your Mass is: '))

    bmi=BMI(height,weight)
    bmi.calculate()
    bmi.clasifier()
    info=bmi.information()
    print(info)n