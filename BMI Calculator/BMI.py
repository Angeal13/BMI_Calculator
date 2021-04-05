class BMI():
    def __init__(self,height,weight):
        self.height=height
        self.weight=weight
    
    def calculate(self):
        self.bmi=self.weight/(self.height**2)
        return self.bmi

    def clasifier(self):
      if (self.bmi < 18.5): 
       self.status="UnderWeight"
      elif ( self.bmi >= 18.5 and self.bmi < 24.9): 
        self.status="Healthy" 
      elif ( self.bmi >= 24.9 and self.bmi < 30): 
        self.status="Overweight" 
      elif ( self.bmi >=30): 
        self.status="Suffering from Obesity"

    def status(self):
      return self.status


    def information(self):
        self.information={
            'Height(m)': self.height,
            'Weight(Kg)': self.weight,
            'bmi': self.bmi,
            'status':self.status
            }
        return self.information
