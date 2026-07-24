class workout:
    def __init__(self,exercise,sets,reps):
        self.exercise=exercise
        self.sets=sets
        self.reps=reps
    def show(self):
        print (self.exercise,"-",self.sets,"sets",self.reps,"reps")
        
w1= workout("Bench Press",3,4)
w2=workout("Chest Press",3,4)
w3=workout("Bicep curls",3,4)
w4=workout("Hammer Curls",3,4)
w5=workout("Leg Squat",3,4)
workouts=[w1,w2,w3,w4,w5]
for w in workouts:
    w.show()
