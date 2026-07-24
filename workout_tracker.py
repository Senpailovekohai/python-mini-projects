import json



class workout:
    def __init__(self,exercise,sets,reps):
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
        
c3= [ShoulderWorkout("Shoulder Press",3,4,"front Delt"),
     ShoulderWorkout("Shoulder ",3,4,"Side Delt")]


class BackWorkout(workout):
    def __init__(self, exercise, sets, reps,back_type):
        super().__init__(exercise, sets, reps)
        self.type=back_type

c4=[BackWorkout("Lat pull down",3,4,"upper back"),
    BackWorkout("T bar curl",3,4,"upper back")]

class ArmsWorkout(workout):
    def __init__(self, exercise, sets, reps,arms_type):
        super().__init__(exercise, sets, reps)
        self.type=arms_type

c5=[ArmsWorkout("Bicep curls ",3,4,"Long head"),
ArmsWorkout("Hammer curls ",3,4,"Long head")]



class WorkoutTracker:
    def __init__ (self):
       
        self.days=[]
        self.load_from_json()
       

    def load_from_json(self):
        try:
            with open("workout.json","r") as file:
                data= json.load(file)
                self.days=data

        except:
            self.days=[]
       
    def days_to_dict(self):
        days_list=[]
        for day_obj in self.days:
            day_dict={
                "day_name": day_obj.day_name,
                "workouts": [{"exercise": w.exercise, "sets": w.sets, "reps": w.reps, "type": w.type} 
                        for w in day_obj.workouts]
            }
            days_list.append(day_dict)
        return days_list

            

    def save_to_json(self):
        with open("workout.json","w") as file:
                json.dump(self.days_to_dict(),file)
      
    
    def menu(self):
        while True:
            print("1.Add day")
            print("2.View all")
            print("3.save")
            print("4.Exit")

            choice=input("Enter choice:")

            if choice == "1":
                print("1.Chest day")
                print("2.Leg day")
                print("3.Shoulder day")
                print("4.Back day")
                print("5.Arms day")

                day_choice=input("Select day:")
                exercise=input("Enter exercise:")
                sets=int(input("Enter numbers of sets:"))
                reps=int(input("Enter the numbers of reps:"))
                part=input("Enter the part it target in muscle:")

                if day_choice=="1":
                    workout=ChestWorkout(exercise,sets,reps,part)
                    c1.append(workout)
                if day_choice=="2":
                    workout=LegWorkout(exercise,sets,reps,part)
                    c2.append(workout)
                if day_choice=="3":
                    workout=ShoulderWorkout(exercise,sets,reps,part)
                    c3.append(workout)
                if day_choice=="4":
                    workout=BackWorkout(exercise,sets,reps,part)
                    c4.append(workout)
                if day_choice=="5":
                    workout=ArmsWorkout(exercise,sets,reps,part)
                    c5.append(workout)
                
               

            elif choice =="2":
                for view in self.days:
                    view.show_day()

                pass

            elif choice=="3":
                self.save_to_json()
                print("Saved!")

            elif choice=="4":
                break                    



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


tracker= WorkoutTracker()
tracker.days=[d1,d2,d3,d4,d5]
tracker.save_to_json()
tracker.menu()





    
    