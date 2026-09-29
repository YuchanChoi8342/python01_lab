# This example is not working in Spyder directly (F5 or Run)
# Please type '!python turtle_runaway.py' on IPython console in your Spyder.
import tkinter as tk
import turtle, random

class RunawayGame:
    def __init__(self, canvas, runner, chaser, catch_radius=50):
        self.canvas = canvas
        self.runner = runner
        self.chaser = chaser
        self.catch_radius2 = catch_radius**2

        # Initialize 'runner' and 'chaser'
        self.runner.shape('triangle') #물고기를 표현
        self.runner.color('orange')
        self.runner.penup()

        self.chaser.shape('turtle')
        self.chaser.color('green')
        self.chaser.penup()

        # Instantiate another turtle for drawing
        self.drawer = turtle.RawTurtle(canvas)
        self.drawer.hideturtle()
        self.drawer.penup()

        self.drawer.color('green')
        self.drawer.pensize(5)
        
        # 첫 번째 해초
        self.drawer.penup() 
        self.drawer.goto(150, -300)
        self.drawer.pendown()
        self.drawer.setheading(70)
        self.drawer.forward(40)
        self.drawer.left(20)
        self.drawer.forward(40)
        self.drawer.right(20)
        self.drawer.forward(40)

        self.drawer.penup()
        self.drawer.goto(165, -300)
        self.drawer.pendown()
        self.drawer.setheading(70)
        self.drawer.forward(40)
        self.drawer.left(20)
        self.drawer.forward(40)
        self.drawer.right(20)
        self.drawer.forward(40)
        
        self.drawer.penup()
        self.drawer.goto(175, -315)
        self.drawer.pendown()
        self.drawer.setheading(50)
        self.drawer.forward(40)
        self.drawer.left(20)
        self.drawer.forward(40)
        self.drawer.right(20)
        self.drawer.forward(40)
        

        # 두 번째 해초
        self.drawer.penup()
        self.drawer.goto(-150, 30)
        self.drawer.pendown()
        self.drawer.setheading(80)
        self.drawer.forward(120)
        self.drawer.forward(30)
        self.drawer.left(20)
        self.drawer.forward(40)
        self.drawer.right(20)
        self.drawer.forward(40)
        
        self.drawer.penup()
        self.drawer.goto(-165, 32)
        self.drawer.pendown()
        self.drawer.setheading(70)
        self.drawer.forward(40)
        self.drawer.left(20)
        self.drawer.forward(40)
        self.drawer.right(20)
        self.drawer.forward(40)
        
        self.drawer.penup()
        self.drawer.goto(175, -315)
        self.drawer.pendown()
        self.drawer.setheading(50)
        self.drawer.forward(40)
        self.drawer.left(20)
        self.drawer.forward(40)
        self.drawer.right(20)
        self.drawer.forward(40)

        # 세 번째 해초
        self.drawer.penup()
        self.drawer.goto(0, -300)
        self.drawer.pendown()
        self.drawer.setheading(100)
        self.drawer.forward(80)
        self.drawer.forward(30)
        self.drawer.left(25)
        self.drawer.forward(35)
        self.drawer.right(15)
        self.drawer.forward(40)

        self.drawer.penup()
        self.drawer.goto(15, -315)
        self.drawer.pendown()
        self.drawer.setheading(50)
        self.drawer.forward(40)
        self.drawer.left(20)
        self.drawer.forward(40)
        self.drawer.right(20)
        self.drawer.forward(40)
        
        self.drawer.penup()
        self.drawer.goto(10, -310)
        self.drawer.pendown()
        self.drawer.setheading(40)
        self.drawer.forward(40)
        self.drawer.left(20)
        self.drawer.forward(40)
        self.drawer.right(20)
        self.drawer.forward(40)


        self.drawer.penup() #바위 추가
        self.drawer.goto(100, 100)
        self.drawer.pendown()
        self.drawer.fillcolor("gray")
        self.drawer.begin_fill()
        self.drawer.circle(30)
        self.drawer.end_fill()

    def is_catched(self):
        p = self.runner.pos()
        q = self.chaser.pos()
        dx, dy = p[0] - q[0], p[1] - q[1]
        return dx**2 + dy**2 < self.catch_radius2

    def start(self, init_dist=400, ai_timer_msec=100):
        self.runner.setpos((-init_dist / 2, 0))
        self.runner.setheading(0)
        self.chaser.setpos((+init_dist / 2, 0))
        self.chaser.setheading(180)
        
        self.score = 0
        self.time_left = 30
        # TODO) You can do something here and follows.
        self.info = turtle.RawTurtle(self.canvas)
        self.info.hideturtle()
        self.info.penup()
        self.info.goto(-300, 320)
        
        self.ai_timer_msec = ai_timer_msec
        self.canvas.ontimer(self.step, self.ai_timer_msec)

    def step(self):
        self.runner.run_ai(self.chaser.pos(), self.chaser.heading())
        self.chaser.run_ai(self.runner.pos(), self.runner.heading())

        self.time_left = self.time_left - 0.1

        if self.is_catched():
            self.score = self.score + 1

            if self.score >= 5:
                self.info.clear()
                self.info.goto(-300, 320)
                self.info.write(f'GAME OVER!  Score: {self.score}')
                return

            self.runner.setpos((-200, 0))
            self.runner.setheading(0)

            self.chaser.setpos((200, 0))
            self.chaser.setheading(180)
            
        self.info.clear()
        self.info.goto(-300, 320)
        self.info.write(
            f'Time: {int(self.time_left)}   Score: {self.score}'
        )

        if self.time_left <= 0:
            self.info.clear()
            self.info.goto(-300, 320)
            self.info.write(f'TIME OVER!  Score: {self.score}')
            return

        self.canvas.ontimer(self.step, self.ai_timer_msec)

class ManualMover(turtle.RawTurtle):
    def __init__(self, canvas, step_move=10, step_turn=10):
        super().__init__(canvas)
        self.step_move = step_move
        self.step_turn = step_turn

        # Register event handlers
        canvas.onkeypress(lambda: self.forward(self.step_move), 'Up')
        canvas.onkeypress(lambda: self.backward(self.step_move), 'Down')
        canvas.onkeypress(lambda: self.left(self.step_turn), 'Left')
        canvas.onkeypress(lambda: self.right(self.step_turn), 'Right')
        canvas.listen()

    def run_ai(self, opp_pos, opp_heading): 
         x = self.xcor()
         y = self.ycor()

        # 거북이가 가까이 오면 반대 방향으로 도망
         if abs(x - opp_pos[0]) < 100 and abs(y - opp_pos[1]) < 100:
            if x > opp_pos[0]:
                self.setheading(0)
            else:
                self.setheading(180)

         else:
             mode = random.randint(0, 2)

             if mode == 0:
                 self.forward(self.step_move)

             elif mode == 1:
                 self.left(self.step_turn)
                 self.forward(self.step_move)

             elif mode == 2:
                 self.right(self.step_turn)
                 self.forward(self.step_move)

class RandomMover(turtle.RawTurtle):  #도망가는 물고기의 속도 UP!
    def __init__(self, canvas, step_move=15, step_turn=10):
        super().__init__(canvas)
        self.step_move = step_move
        self.step_turn = step_turn

    def run_ai(self, opp_pos, opp_heading):
        mode = random.randint(0, 2)

        if mode == 0:
            self.forward(self.step_move)

        elif mode == 1:
            self.left(self.step_turn)
            self.forward(self.step_move)

        elif mode == 2:
            self.right(self.step_turn)   
            self.forward(self.step_move)

if __name__ == '__main__':
    # Use 'TurtleScreen' instead of 'Screen' to prevent an exception from the singleton 'Screen'
    root = tk.Tk()
    canvas = tk.Canvas(root, width=700, height=700)
    canvas.pack()
    screen = turtle.TurtleScreen(canvas)

    screen.bgcolor('skyblue') #바닷속을 표현하기 위한 배경색


    # TODO) Change the follows to your turtle if necessary
    runner = RandomMover(screen)
    chaser = ManualMover(screen)

    game = RunawayGame(screen, runner, chaser)
    game.start()
    screen.mainloop()
