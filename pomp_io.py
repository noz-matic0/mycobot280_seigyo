import time
from pymycobot.mycobot import MyCobot

# Describe this function...
def do_something():
  mc.send_coords([(-11.2),68.4,412.67,(-83.55),(-6.09),75.61],20,0)
  time.sleep(2)


mc = MyCobot('COM4',115200)
do_something()
for count in range(2):
  time.sleep(2)
  mc.set_basic_output(2,0)
  mc.set_basic_output(5,0)
  time.sleep(2)
  mc.set_basic_output(2,1)
  mc.set_basic_output(5,1)
  time.sleep(2)
do_something()