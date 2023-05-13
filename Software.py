# importing necessary modules
import tkinter as tk
from tkinter import ttk
from tkinter import font
from ctypes import windll
from PIL import Image, ImageTk
import import_ipynb
import connector
import importlib
importlib.reload(connector)

windll.shcore.SetProcessDpiAwareness(1) #stops blur in windows

# design constants
class colors:
    BG = "#1b222f"
    TEXT = "white"
    GREEN = "#386053"
    RED = "#66111f"
    GREY = "#29303d"
class fonts:
    LARGE = ("Georgia", 32)
    MEDIUM = ("Georgia", 18)
    STANDART = ("Serif", 12)
    SMALL = ("Serif", 10)

# this class contains all the frames of the app and help switch between them
class tkinterApp(tk.Tk):
     
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
         
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        self.wm_title("Predicting the Results of the Simple Simulator")
        #self.geometry("%dx%d" % (1000, 600))

        # creating a container
        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
        # initializing frames to an empty array
        self.frames = {} 
  
        # iterating through a dictionary consisting
        # of the different page layouts
        for F in (StartPage, AboutTheSimulation, MakePrediction, GuessingGame, AboutTheProject):
  
            frame = F(container, self)
  
            # initializing frame of that objects
            self.frames[F] = frame
  
            frame.grid(row=0, column=0, sticky ="nsew")
  
        self.show_frame(StartPage)
  
    # this function displays the current frame passed as parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
  

# menu frame
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=colors.BG)
         
        tk.Label(self, font=fonts.SMALL, text="", bg= colors.BG, fg= colors.TEXT).pack()  
        tk.Label(self, font=fonts.LARGE, text="Welcome to", bg= colors.BG, fg= colors.TEXT).pack(ipady=20)
        tk.Label(self, font=fonts.LARGE, text="Predicting the Results of the Simple Simulator", bg= colors.BG, 
                 fg= colors.TEXT).pack(ipadx =20)
        tk.Label(self, font=fonts.STANDART, text="", bg= colors.BG, fg= colors.TEXT).pack()  
        
        about_the_project = tk.Button(self, text="About the Project", font= fonts.STANDART, bg= colors.GREEN, fg= colors.TEXT, 
                                         width=30, borderwidth=0, command = lambda : controller.show_frame(AboutTheProject))
        about_the_simulation = tk.Button(self, text="About the Simulation", font= fonts.STANDART, bg= colors.GREEN, fg= colors.TEXT, 
                                         width=30, borderwidth=0, command = lambda : controller.show_frame(AboutTheSimulation))
        make_prediction = tk.Button(self, text="Make a prediction", font= fonts.STANDART, bg= colors.GREEN, fg= colors.TEXT, width=30, 
                            borderwidth=0, command = lambda : controller.show_frame(MakePrediction))
        guessing_game = tk.Button(self, text="Guessing game", font= fonts.STANDART, bg= colors.GREEN, fg= colors.TEXT, width=30,
                          borderwidth=0, command = lambda : controller.show_frame(GuessingGame))
        
        about_the_project.pack(ipady=5, pady =15)
        about_the_simulation.pack(ipady=5, pady =15)
        make_prediction.pack(ipady=5, pady =15)
        guessing_game.pack(ipady=5, pady =15)

        tk.Label(self, font=fonts.SMALL, text="בסמת 2023", bg= colors.BG).pack(ipady =20, side=tk.BOTTOM)

# frame that contains info about the project   
class AboutTheProject(tk.Frame):
    def __init__(self, parent, controller):        
        tk.Frame.__init__(self, parent, bg=colors.BG)
      
        backToMenu = tk.Button(self, text="Back to Main page",font= fonts.STANDART, bg= colors.GREEN, fg= colors.TEXT,
                               borderwidth=0, command = lambda : controller.show_frame(StartPage))
        backToMenu.grid(row=0, column=0, padx = 30, pady=15)
        
        tk.Label(self, text ="About the project", font = fonts.MEDIUM, bg= colors.BG, fg= colors.TEXT).grid(row=0, column=1, padx=150)

        load = Image.open("pictures/About the project.png")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=32, y=60)

# frame that contains info about the simulation 
class AboutTheSimulation(tk.Frame):
     
    def __init__(self, parent, controller):        
        tk.Frame.__init__(self, parent, bg=colors.BG)
      
        backToMenu = tk.Button(self, text="Back to Main page",font= fonts.STANDART, bg= colors.GREEN, fg= colors.TEXT,
                               borderwidth=0, command = lambda : controller.show_frame(StartPage))
        backToMenu.grid(row=0, column=0, padx = 30, pady=15)
        
        tk.Label(self, text ="About the simulation", font = fonts.MEDIUM, bg= colors.BG, fg= colors.TEXT).grid(row=0, column=1, padx=150)
        
        load = Image.open("pictures/About the simulation.png")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=32, y=60)


# frame where we can make prediction about certain simulation
class MakePrediction(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg= colors.BG)

        backToMenu = tk.Button(self, text="Back to Main page",font= fonts.STANDART, bg= colors.GREEN, fg= colors.TEXT,
                               borderwidth=0, command = lambda : controller.show_frame(StartPage))
        backToMenu.grid(row=0, column=0, padx = 10)
        
        settingLabel = tk.Label(self, font=fonts.LARGE, text="Settings", bg= colors.BG, fg= colors.TEXT)
        settingLabel.grid(row=0, column=1, columnspan=2)
        
        #skin cells settings
        startNumL = tk.Label(self, font=fonts.SMALL, text="Initial number of skin cells", bg= colors.BG, fg= colors.TEXT)
        startNum = tk.IntVar()
        startNumS = tk.Scale(self, from_ = 50, to=1000, orient="horizontal", border=0, variable=startNum, length=200,
                          bg= colors.BG, fg = colors.TEXT, troughcolor=colors.GREEN, highlightbackground=colors.BG)
        startNumL.grid(column=0, row=2, ipadx=10)
        startNumS.grid(column=1,row=2, ipadx=10)

        gVScRatioL = tk.Label(self, font=fonts.SMALL, text="Proportion of guards to civilians(%)", bg= colors.BG, fg= colors.TEXT)
        gVScRatio = tk.IntVar()
        gVScRatioS = tk.Scale(self, from_ = 5, to=50, orient="horizontal", border=0, variable=gVScRatio, length=200,
                          bg= colors.BG, fg = colors.TEXT, troughcolor=colors.GREEN, highlightbackground=colors.BG)
        gVScRatioL.grid(column=0, row=3, ipadx=10)
        gVScRatioS.grid(column=1,row=3, ipadx=10)

        lifespanSkinCellsL = tk.Label(self, font=fonts.SMALL, text="Lifespan of skin cells", bg= colors.BG, fg= colors.TEXT)
        lifespanSkinCells = tk.IntVar()
        lifespanSkinCellsS = tk.Scale(self, from_ = 1, to=3, orient="horizontal", border=0, variable=lifespanSkinCells, 
                                      length=200, bg= colors.BG, fg = colors.TEXT, troughcolor=colors.GREEN, 
                                      highlightbackground=colors.BG)
        lifespanSkinCellsL.grid(column=0, row=4, ipadx=10)
        lifespanSkinCellsS.grid(column=1,row=4, ipadx=10)

        civiliansProductivityL = tk.Label(self, font=fonts.SMALL, text="Amount of food that a civilian produces", 
        bg= colors.BG, fg= colors.TEXT)
        civiliansProductivity = tk.IntVar()
        civiliansProductivityS = tk.Scale(self, from_ = 1, to=5, orient="horizontal", border=0, variable=civiliansProductivity, 
                                          length=200, bg= colors.BG, fg = colors.TEXT, troughcolor=colors.GREEN, 
                                          highlightbackground=colors.BG)
        civiliansProductivityL.grid(column=0, row=5, ipadx=10)
        civiliansProductivityS.grid(column=1,row=5, ipadx=10)

        guardsProductivityL = tk.Label(self, font=fonts.SMALL, text="Number of bacteria that guard kills", 
                                          bg= colors.BG, fg= colors.TEXT)
        guardsProductivity = tk.IntVar()
        guardsProductivityS = tk.Scale(self, from_ = 1, to=5, orient="horizontal", border=0, variable=guardsProductivity, 
                                          length=200, bg= colors.BG, fg = colors.TEXT, 
                                          troughcolor=colors.GREEN, highlightbackground=colors.BG)
        guardsProductivityL.grid(column=0, row=6, ipadx=10)
        guardsProductivityS.grid(column=1,row=6, ipadx=10) 

        armyPriorityL = tk.Label(self, font=fonts.SMALL, text="Proportion of food given is to the army(%)", bg= colors.BG, fg= colors.TEXT)
        armyPriority = tk.IntVar()
        armyPriorityS = tk.Scale(self, from_ = 10, to=90, orient="horizontal", border=0, variable=armyPriority, length=200,
                          bg= colors.BG, fg = colors.TEXT, troughcolor=colors.GREEN, highlightbackground=colors.BG)
        armyPriorityL.grid(column=0, row=7, ipadx=10)
        armyPriorityS.grid(column=1,row=7, ipadx=10)

        #bacteria cells settings
        bacteriaStartPercentL = tk.Label(self, font=fonts.SMALL, text="Percent of bacteria to skin cells", 
                                         bg= colors.BG, fg= colors.TEXT)
        bacteriaStartPercent = tk.IntVar()
        bacteriaStartPercentS = tk.Scale(self, from_ = 20, to=100, orient="horizontal", border=0, variable=bacteriaStartPercent, 
                                         length=200, bg= colors.BG, fg = colors.TEXT, troughcolor=colors.GREEN, 
                                         highlightbackground=colors.BG)
        bacteriaStartPercentL.grid(column=2, row=2, ipadx=10)
        bacteriaStartPercentS.grid(column=3,row=2, ipadx=10)

        takingFoodEffectivityL = tk.Label(self, font=fonts.SMALL, text="Proportion of food that bacteria take(%)", 
                                          bg= colors.BG, fg= colors.TEXT)
        takingFoodEffectivity = tk.IntVar()
        takingFoodEffectivityS = tk.Scale(self, from_ = 10, to=90, orient="horizontal", border=0, variable=takingFoodEffectivity, 
                                          length=200, bg= colors.BG, fg = colors.TEXT, troughcolor=colors.GREEN, 
                                          highlightbackground=colors.BG)
        takingFoodEffectivityL.grid(column=2, row=3, ipadx=10)
        takingFoodEffectivityS.grid(column=3,row=3, ipadx=10)

        lifespanBacteriaL = tk.Label(self, font=fonts.SMALL, text="Lifespan of bacteria", bg= colors.BG, fg= colors.TEXT)
        lifespanBacteria = tk.IntVar()
        lifespanBacteriaS = tk.Scale(self, from_ = 0, to=2, orient="horizontal", border=0, variable=lifespanBacteria, length=200, 
                                      bg= colors.BG, fg = colors.TEXT, troughcolor=colors.GREEN, highlightbackground=colors.BG)
        lifespanBacteriaL.grid(column=2, row=4, ipadx=10)
        lifespanBacteriaS.grid(column=3,row=4, ipadx=10)

        chanceOfKillingGuardL = tk.Label(self, font=fonts.SMALL, text="Chance that bacteria will kill a guard", 
                                           bg= colors.BG, fg= colors.TEXT)
        chanceOfKillingGuard = tk.IntVar()
        chanceOfKillingGuardS = tk.Scale(self, from_ = 1, to=50, orient="horizontal", border=0, 
                                           variable=chanceOfKillingGuard, length=200,
                          bg= colors.BG, fg = colors.TEXT, troughcolor=colors.GREEN, highlightbackground=colors.BG)
        chanceOfKillingGuardL.grid(column=2, row=5, ipadx=10)
        chanceOfKillingGuardS.grid(column=3,row=5, ipadx=10)

        chanceOfKillingCivilianL = tk.Label(self, font=fonts.SMALL, text="Chance that bacteria will kill a civilian", 
                                            bg= colors.BG, fg= colors.TEXT)
        chanceOfKillingCivilian = tk.IntVar()
        chanceOfKillingCivilianS = tk.Scale(self, from_ = 1, to=100, orient="horizontal", border=0, 
                                            variable=chanceOfKillingCivilian, length=200,
                          bg= colors.BG, fg = colors.TEXT, troughcolor=colors.GREEN, highlightbackground=colors.BG)
        chanceOfKillingCivilianL.grid(column=2, row=6, ipadx=10)
        chanceOfKillingCivilianS.grid(column=3,row=6, ipadx=10)

        result  = ""
        prediction = ""
        def predict(startNum, gVScRatio, lifespanSkinCells, civiliansProductivity, guardsProductivity, armyPriority, 
                    bacteriaStartPercent, takingFoodEffectivity, lifespanBacteria, chanceOfKillingGuard, chanceOfKillingCivilian):
            prediction, result =connector.prediction_game(startNum, gVScRatio, lifespanSkinCells, civiliansProductivity, 
                                                            guardsProductivity, armyPriority, bacteriaStartPercent, 
                                                            takingFoodEffectivity, lifespanBacteria, chanceOfKillingGuard, 
                                                            chanceOfKillingCivilian)
            tk.Label(self, font=fonts.STANDART, text=prediction, bg= colors.BG, fg= colors.TEXT).grid(row=10, column=0, columnspan=2)
            tk.Label(self, font=fonts.STANDART, text=result, bg= colors.BG, fg= colors.TEXT).grid(row=10, column=2, columnspan=2)
            

        predictButton = tk.Button(self, text="Predict",font= fonts.STANDART, bg= colors.GREEN, fg= colors.TEXT, 
                                  command=lambda:predict(startNum.get(), gVScRatio.get()/100, lifespanSkinCells.get(), 
                                                         civiliansProductivity.get(), guardsProductivity.get(), 
                                                         armyPriority.get()/100, bacteriaStartPercent.get()/100, 
                                                          takingFoodEffectivity.get()/100, lifespanBacteria.get(), 
                                                          chanceOfKillingGuard.get(), 
                                                          chanceOfKillingCivilian.get()))
        predictButton.grid(column=3,row=7, pady=10)

        resultLabel = tk.Label(self, font=fonts.LARGE, text="Result", bg= colors.BG, fg= colors.TEXT)
        resultLabel.grid(row=8, column=1, columnspan=2)
        tk.Label(self, font=fonts.STANDART, text="95% correct", bg= colors.BG, fg= colors.TEXT).grid(row=9, column=0, columnspan=2)
        tk.Label(self, font=fonts.STANDART, text="100% correct", bg= colors.BG, fg= colors.TEXT).grid(row=9, column=2, columnspan=2)
        tk.Label(self, font=fonts.STANDART, text=prediction, bg= colors.BG, fg= colors.TEXT).grid(row=10, column=0, columnspan=2)
        tk.Label(self, font=fonts.STANDART, text=result, bg= colors.BG, fg= colors.TEXT).grid(row=10, column=2, columnspan=2)


# frame where AI compeat with a human 
class GuessingGame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg= colors.BG)

        backToMenu = tk.Button(self, text="Back to Main page",font= fonts.STANDART, bg= colors.GREEN, fg= colors.TEXT,
                               borderwidth=0, command = lambda : controller.show_frame(StartPage))
        backToMenu.grid(row=0, column=0, padx = 10)
        


        tk.Label(self, font=fonts.LARGE, text="AI   &   Human", bg= colors.BG, fg= colors.TEXT).grid(row=0, column=1,  padx=10)
        tk.Label(self, font=fonts.STANDART, text="Score", bg= colors.BG, fg= colors.TEXT).grid(row=1, column=0, pady=10)

        tk.Label(self, font=fonts.STANDART, text="Simulation Data", bg= colors.BG, fg= colors.TEXT).grid(row=2, column=0, pady=10, 
                                                                                                         columnspan=2)
        tk.Label(self, font=fonts.STANDART, text="Who will win?", bg= colors.BG, fg= colors.TEXT).grid(row=2, column=2, pady=10)
  

        #skin cells settings
        startNum = tk.IntVar()
        startNumS = tk.Scale(self, from_ = 50, to=1000, orient="horizontal", border=0, variable=startNum, length=300,
                          bg= colors.BG, fg = colors.TEXT, troughcolor=colors.GREY, highlightbackground=colors.BG,
                          label="Initial number of skin cells", state="disabled")
        startNumS.grid(row=3, column=0, padx=10)

        gVScRatio = tk.IntVar()
        gVScRatioS = tk.Scale(self, from_ = 5, to=50, orient="horizontal", border=0, variable=gVScRatio, length=300,
                          bg= colors.BG, fg = colors.TEXT, troughcolor=colors.GREY, highlightbackground=colors.BG,
                          label="Proportion of guards to civilians(%)", state="disabled")
        gVScRatioS.grid(row=4, column=0, padx=10)

        lifespanSkinCells = tk.IntVar()
        lifespanSkinCellsS = tk.Scale(self, from_ = 1, to=3, orient="horizontal", border=0, variable=lifespanSkinCells, length=300,
                          bg= colors.BG, fg = colors.TEXT, troughcolor=colors.GREY, highlightbackground=colors.BG,
                          label="Lifespan of skin cells", state="disabled")
        lifespanSkinCellsS.grid(row=5, column=0, padx=10)

        civiliansProductivity = tk.IntVar()
        civiliansProductivityS = tk.Scale(self, from_ = 1, to=5, orient="horizontal", border=0, variable=civiliansProductivity, 
                                          length=300, bg= colors.BG, fg = colors.TEXT, troughcolor=colors.GREY, 
                                          highlightbackground=colors.BG, label="Amount of food that a civilian produces", 
                                          state="disabled")
        civiliansProductivityS.grid(row=6, column=0, padx=10)

        guardsProductivity = tk.IntVar()
        guardsProductivityS = tk.Scale(self, from_ = 1, to=5, orient="horizontal", border=0, variable=guardsProductivity, 
                                          length=300, bg= colors.BG, fg = colors.TEXT, troughcolor=colors.GREY, 
                                          highlightbackground=colors.BG, label="Number of bacteria that guard kills", 
                                          state="disabled")
        guardsProductivityS.grid(row=7, column=0, padx=10)

        armyPriority = tk.IntVar()
        armyPriorityS = tk.Scale(self, from_ = 10, to=90, orient="horizontal", border=0, variable=armyPriority, length=300,
                          bg= colors.BG, fg = colors.TEXT, troughcolor=colors.GREY, highlightbackground=colors.BG,
                          label="Proportion of food given is to the army(%)", state="disabled")
        armyPriorityS.grid(row=8, column=0, padx=10)

        #bacteria cells settings
        bacteriaStartPercent = tk.IntVar()
        bacteriaStartPercentS = tk.Scale(self, from_ = 20, to=100, orient="horizontal", border=0, variable=bacteriaStartPercent, 
                                         length=300, bg= colors.BG, fg = colors.TEXT, troughcolor=colors.GREY, 
                                         highlightbackground=colors.BG, label="Percent of bacteria to skin cells", state="disabled")
        bacteriaStartPercentS.grid(row=3, column=1, padx=10)

        takingFoodEffectivity = tk.IntVar()
        takingFoodEffectivityS = tk.Scale(self, from_ = 10, to=90, orient="horizontal", border=0, variable=takingFoodEffectivity, 
                                          length=300, bg= colors.BG, fg = colors.TEXT, troughcolor=colors.GREY, 
                                          highlightbackground=colors.BG, label="Proportion of food that bacteria take(%)", 
                                          state="disabled")
        takingFoodEffectivityS.grid(row=4, column=1, padx=10)

        lifespanBacteria = tk.IntVar()
        lifespanBacteriaS = tk.Scale(self, from_ = 0, to=2, orient="horizontal", border=0, variable=lifespanBacteria, length=300,
                          bg= colors.BG, fg = colors.TEXT, troughcolor=colors.GREY, highlightbackground=colors.BG,
                          label="Lifespan of bacteria", state="disabled")
        lifespanBacteriaS.grid(row=5, column=1, padx=10)

        chanceOfKillingGuard = tk.IntVar()
        chanceOfKillingGuardS = tk.Scale(self, from_ = 1, to=50, orient="horizontal", border=0, 
                          variable=chanceOfKillingGuard, length=300,
                          bg= colors.BG, fg = colors.TEXT, troughcolor=colors.GREY, highlightbackground=colors.BG,
                          label="Chance that bacterium will kill a guard", state="disabled")
        chanceOfKillingGuardS.grid(row=6, column=1, padx=10)

        chanceOfKillingCivilian = tk.IntVar()
        chanceOfKillingCivilianS = tk.Scale(self, from_ = 1, to=100, orient="horizontal", border=0, 
                          variable=chanceOfKillingCivilian, length=300,
                          bg= colors.BG, fg = colors.TEXT, troughcolor=colors.GREY, highlightbackground=colors.BG,
                          label="Chance that bacterium will kill a civilian", state="disabled")
        chanceOfKillingCivilianS.grid(row=7, column=1, padx=10)


        bacteria = tk.Button(self, text="Bacteria", font= fonts.STANDART, bg= colors.GREEN, fg= colors.TEXT, width=30, 
                            borderwidth=0, command = lambda : userPrediction(1))
        immunity = tk.Button(self, text="Immunity", font= fonts.STANDART, bg= colors.GREEN, fg= colors.TEXT, width=30,
                          borderwidth=0, command = lambda : userPrediction(0))
        bacteria.grid(row=3, column=2, pady=5, padx=10)
        immunity.grid(row=4, column=2, pady=5, padx=10)

        tk.Label(self, font=fonts.STANDART, text="Result", bg= colors.BG, fg= colors.TEXT).grid(row=5, column=2, pady=20)
        nextButton = tk.Button(self, text="Next", font = fonts.STANDART, bg = colors.GREEN, fg=colors.TEXT, width=20,
                               borderwidth=0, command = lambda : goNext())
        nextButton.grid(row=8, column=2, pady=5, padx=10)
        
        score = [0,0]
        
        def randomData():
            x, result, ai_pred = connector.random_game()
            
            startNum.set(x[0][0])
            gVScRatio.set(x[0][1]*100)
            lifespanSkinCells.set(x[0][2])
            civiliansProductivity.set(x[0][3])
            guardsProductivity.set(x[0][4])
            armyPriority.set(x[0][5]*100)
            
            bacteriaStartPercent.set(x[0][6]*100)
            takingFoodEffectivity.set(x[0][7]*100)
            lifespanBacteria.set(x[0][8])
            chanceOfKillingGuard.set(x[0][9])
            chanceOfKillingCivilian.set(x[0][10])
            return result, ai_pred
        
        result, ai_pred = randomData()        
        
        def userPrediction(user_pred):            
            nonlocal score
            message1 = "You are "
            message2 = "AI is "
            if user_pred == result:
                message1 = message1 + "RIGHT"
                score[1]+=1
            else:
                message1 = message1 + "WRONG"
            if ai_pred == result:
                message2 = message2 + "RIGHT"
                score[0]+=1
            else:
                message2 = message2 + "WRONG"
            tk.Label(self, font=fonts.STANDART, text=message1, bg= colors.BG, fg= colors.TEXT, width=30).grid(row=6, column=2)
            tk.Label(self, font=fonts.STANDART, text=message2, bg= colors.BG, fg= colors.TEXT, width=30).grid(row=7, column=2)
            scoreText = f"{score[0]} : {score[1]}"
            tk.Label(self, font=fonts.STANDART, text=scoreText, bg= colors.BG, fg= colors.TEXT, width=30).grid(row=1, column=1)
            goNext()
                 
        def goNext():
            nonlocal result
            nonlocal ai_pred
            result, ai_pred = randomData()


# Driver Code
app = tkinterApp()
app.mainloop()