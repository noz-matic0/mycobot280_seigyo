from pymycobot.mycobot import MyCobot
import time

# Describe this function...
def stanBay():
  mc.set_color(0,0,250)
  mc.send_coords([(-30.7),74.7,410.3,(-90.65),(-36.63),75.89],60,0)
  time.sleep(1)
  mc.set_color(173,216,230)
  time.sleep(1)


mc = MyCobot('COM4',115200)
for count in range(5):
  stanBay()
  mc.set_color(0,0,255)
  mc.send_coords([53.3,49.7,251.2,(-93.16),(-36.5),78.17],60,0)
  time.sleep(1)
  mc.set_color(225,0,225)
  time.sleep(1)
  mc.set_color(173,216,230)
  mc.send_coords([(-151.1),109.3,202.8,(-175.3),0.12,110.22],60,0)
  time.sleep(1)
  mc.set_color(0,0,225)
  time.sleep(1)
  mc.set_color(173,216,230)
  mc.send_coords([(-105.9),63.3,213.9,(-142.84),27.22,123.14],60,0)
  time.sleep(1)
  mc.set_color(0,0,225)
  time.sleep(1)
  mc.set_color(173,216,230)
  mc.send_coords([11,103,247.1,119.91,(-6.35),133.36],60,0)
  mc.set_color(0,0,225)
  time.sleep(1)
  mc.set_color(173,216,230)
  time.sleep(1)
  stanBay()
mc.release_all_servos()