import Pipes
import Valves
import Tank



def traverse(strt, previous):
    if (strt is None):
        return
    else:
        if (type(strt) is Pipes.Pipe):
            print("PIPE")
            strt.setState(True)
            if (strt.right != previous and type(strt.right) is not None):
                traverse(strt.right, strt)
            if (strt.bottom != previous and type(strt.bottom) is not None):
                traverse(strt.bottom, strt)
            if (strt.left != previous and type(strt.left) is not None):
                traverse(strt.left, strt)
        elif (type(strt) is Tank.Tank):
            print("TANK")
            if (strt.right != previous and type(strt.right) is not None):
                traverse(strt.right, strt)
            if (strt.bottom != previous and type(strt.bottom) is not None):
                traverse(strt.bottom, strt)
            if (strt.left != previous and type(strt.left) is not None):
                traverse(strt.left, strt)
        elif (type(strt) is Valves.Orifice):
            print('ORIFICE')
        elif (type(strt) is Valves.PressureSensor):
            print('PRESSURE SENSOR')
        elif (type(strt) is Valves.TempSensor):
            print('TEMP SENSOR')
        elif (type(strt) is Valves.Solenoid):
            print('SOLENOID')
        elif (type(strt) is Valves.Stepper):
            print('STEPPER')
            '''pipes = [False, False, False, False]
            
            strt.setPipes(pipes[0], pipes[1], pipes[2], pipes[3])
            if(strt.getState()):
                print("OPEN")
            else:
                return'''

