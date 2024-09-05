from pymycobot.mycobot import MyCobot
import time


mc = MyCobot('COM4',115200)
for count in range(5):
  mc.send_angles([90.61,(-1.49),0.88,0.08,83.75,62.84],40)
  time.sleep(0.5)
  mc.send_angles([90.61,(-1.49),36.43,0.43,83.75,62.84],40)
  time.sleep(0.5)
  mc.send_angles([90.61,(-1.49),0.88,0.08,83.75,62.84],40)
  time.sleep(0.5)
  mc.send_angles([90.61,(-1.49),(-25),0.43,83.75,62.84],40)
  time.sleep(0.5)
  mc.send_angles([90.61,(-1.49),0.88,0.08,83.75,62.84],40)