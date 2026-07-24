class workout:
    def __init__ (self,exercise,sets,reps):
        self.exercise=exercise
        self.sets=sets
        self.reps=reps

    def show(self):
        print(self.exercise,"-",self.sets,"sets",self.reps,"reps")

    
class ChestWorkout(workout):
    def __init__(self,exercise,sets,reps,chest_type):
        super().__init__(exercise,sets,reps)
        self.type=chest_type



c1= [ChestWorkout("Bench Press",3,4,"upper"),
     ChestWorkout("Pec dec",3,4,"mid")]



class LegWorkout(workout):
    def __init__(self,exercise,sets,reps,leg_type):
        super().__init__(exercise,sets,reps)
        self.type=leg_type

c2= [LegWorkout("Squat",3,4,"Quads"),
     LegWorkout("Leg press",3,4,"Quads")]


class ShoulderWorkout(workout):
    def __init__(self, exercise, sets, reps,shoulder_type):
        super().__init__(exercise, sets, reps)
        self.type=shoulder_type
        
c3= ShoulderWorkout("Shoulder Press",3,4,"front Delt")


class BackWorkout(workout):
    def __init__(self, exercise, sets, reps,back_type):
        super().__init__(exercise, sets, reps)
        self.type=back_type

c4=BackWorkout("Lat pull down",3,4,"upper back")

class ArmsWorkout(workout):
    def __init__(self, exercise, sets, reps,arms_type):
        super().__init__(exercise, sets, reps)
        self.type=arms_type

c5=ArmsWorkout("Bicep curls ",3,4,"Long head")

class day:
    def __init__(self, day_name,workouts):
        self.day_name=day_name
        self.workouts=workouts

    def show_day(self):
        print(f"\n==={self.day_name}===")
        for w in self.workouts:
            print(w.exercise,"-",w.type)
            w.show()
    

d1=day("Chest Day",c1)
d2=day("Leg day",c2)
d3=day("Shoulder day",c3)
d4=day("Back day",c4)
d5=day("Arms day",c5)

#workouts=[c1,c2,c3,c4,c5]

#for w in workouts:
 




