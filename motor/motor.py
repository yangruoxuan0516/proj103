from PCA9685 import PCA9685

Dir = [
    'forward',
    'backward',
]
pwm = PCA9685(0x40, debug=False)
pwm.setPWMFreq(50)

class MotorDriver():
    def __init__(self):
        self.PWMA = 0
        self.AIN1 = 1
        self.AIN2 = 2
        self.PWMB = 5
        self.BIN1 = 3
        self.BIN2 = 4

    def MotorRun(self, motor, index, speed):
        if speed > 100:
            return
        if(motor == 0):
            pwm.setDutycycle(self.PWMA, speed)
            if(index == Dir[0]):
                pwm.setLevel(self.AIN1, 0)
                pwm.setLevel(self.AIN2, 1)
            else:
                pwm.setLevel(self.AIN1, 1)
                pwm.setLevel(self.AIN2, 0)
        else:
            pwm.setDutycycle(self.PWMB, speed)
            if(index == Dir[0]):
                pwm.setLevel(self.BIN1, 0)
                pwm.setLevel(self.BIN2, 1)
            else:
                pwm.setLevel(self.BIN1, 1)
                pwm.setLevel(self.BIN2, 0)

    def MotorStop(self, motor):
        if (motor == 0):
            pwm.setDutycycle(self.PWMA, 0)
        else:
            pwm.setDutycycle(self.PWMB, 0)


def forward(Motor,vitesse): # 左前 右前
    Motor.MotorRun(0, 'forward', vitesse) # 右前
    Motor.MotorRun(1, 'backward', vitesse) # 左前

def backward(Motor,vitesse): # 左后 右后
    Motor.MotorRun(0, 'backward', vitesse) # 右后
    Motor.MotorRun(1, 'forward', vitesse) # 左后

def left(Motor,vitesse): # 左后 右前
    Motor.MotorRun(0, 'forward', vitesse) # 右前
    Motor.MotorRun(1, 'forward', vitesse) # 左后

def right(Motor,vitesse): # 左前 右后
    Motor.MotorRun(0, 'backward', vitesse) # 右后
    Motor.MotorRun(1, 'backward', vitesse) # 左前

def stop(Motor):
    Motor.MotorStop(0)
    Motor.MotorStop(1)
    
def leftforward(Motor,vitesse):
    Motor.MotorRun(0, 'forward', vitesse) # 右前
    Motor.MotorRun(1, 'backward', vitesse/2) # 左前

def rightforward(Motor,vitesse):
    Motor.MotorRun(0, 'forward', vitesse/2) # 右前
    Motor.MotorRun(1, 'backward', vitesse) # 左前

def leftbackward(Motor,vitesse):
    Motor.MotorRun(0, 'backward', vitesse) # 右后
    Motor.MotorRun(1, 'forward', vitesse/2) # 左后    

def rightbackward(Motor,vitesse):
    Motor.MotorRun(0, 'backward', vitesse/2) # 右后
    Motor.MotorRun(1, 'forward', vitesse) # 左后    