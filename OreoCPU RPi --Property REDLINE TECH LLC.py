# Oreo CPD 20220420
import time
import RPi.GPIO as GPIO


                                    ##########   GPIO Setup   ##########

# Use the board layout for gpio headers rather than bcm
GPIO.setmode(GPIO.BCM) 

# Define GPIO pins
sub_amp=12
fwd_acc=16
pwr_invt=20
rad_det=21
lig_mod=26
com_scn=19
sir_pa=13
null_func=6


# Prepare GPIO headers
GPIO.setup(sub_amp, GPIO.OUT)
GPIO.setup(fwd_acc, GPIO.OUT)
GPIO.setup(pwr_invt, GPIO.OUT)
GPIO.setup(rad_det, GPIO.OUT)
GPIO.setup(lig_mod, GPIO.OUT)
GPIO.setup(com_scn, GPIO.OUT)
GPIO.setup(sir_pa, GPIO.OUT)
GPIO.setup(null_func, GPIO.OUT)

                            ##########   Activate and Deavtivate Modules     ###########

# Turn Modules On
    ###     Citizen Stuff   ###
def sub_on():
    GPIO.output(sub_amp, GPIO.HIGH)
    print("Amplifier [Active]")
    print("")
    time.sleep(2)

def acc_on():
    GPIO.output(fwd_acc, GPIO.HIGH)
    print("Accecories [Active]")
    print("")
    time.sleep(2)

def inv_on():
    GPIO.output(pwr_invt, GPIO.HIGH)
    print("Inverter [Active]")
    print("")
    time.sleep(2)

def rad_on():
    GPIO.output(rad_det, GPIO.HIGH)
    print("Radar [Active]")
    print("")
    time.sleep(2)

    ###    Polide Equiptment    ###
def lig_on():
    GPIO.output(lig_mod, GPIO.HIGH)
    print("Lighting [Active]")
    print("")
    time.sleep(2)

def com_on():
    GPIO.output(com_scn, GPIO.HIGH)
    print("Comms [Active]")
    print("")
    time.sleep(2)

def sir_on():
    GPIO.output(sir_pa, GPIO.HIGH)
    print("Sirens [Active]")
    print("")
    time.sleep(2)

def nul_on():
    GPIO.output(null_func, GPIO.HIGH)
    print("Null_ [Active]")
    print("")
    time.sleep(2)

# Turn Modules Off
    ### Civvie Stuff ###
def sub_off():
    GPIO.output(sub_amp, GPIO.LOW)
    print("Amplifier [Inactive]")
    print("")
    time.sleep(2)

def acc_off():
    GPIO.output(fwd_acc, GPIO.LOW)
    print("Accessories [Inactive]")
    print("")
    time.sleep(2)


def inv_off():
    GPIO.output(pwr_invt, GPIO.LOW)
    print("Inverter [Inactive]")
    print("")
    time.sleep(2)

def rad_off():
    GPIO.output(rad_det, GPIO.LOW)
    print("Radar [Inactive]")
    print("")
    time.sleep(2)

    ###     Police Equiptment  ###
def lig_off():
    GPIO.output(lig_mod, GPIO.LOW)
    print("Lighting [Inactive]")
    print("")
    time.sleep(2)

def com_off():
    GPIO.output(com_scn, GPIO.LOW)
    print("Comms [Inactive]")
    print("")
    time.sleep(2)

def sir_off():
    GPIO.output(sir_pa, GPIO.LOW)
    print("Sirens [Inactive]")
    print("")
    time.sleep(2)

def nul_off():
    GPIO.output(null_func, GPIO.LOW)
    print("Null_ [Inactive]")
    print("")
    time.sleep(2)


                                ###############     Programs        #############

#   Startup loop enables all devices by default... If no means to control the system are avalible, everything stays on, it's amazing!
def startup():
    print("System Starting()")
    print("")
    sub_on()
    acc_on()
    inv_on()
    rad_on()
    lig_on()
    com_on()
    sir_on()
    nul_on()

#   Dark Car Preset allows Subwoofer to be active while not allowing power to in-cab light emiting devices
def dark_car():
    print("Dark Car Preset Selected")
    print("")
    sub_on()
    acc_off()
    inv_off()
    rad_off()
    lig_off()
    com_off()
    sir_off()
    nul_off()

#  Daily Driver preset enables subs, accessory poerts, and radar detector
def daily_driver():
    print("Daily Driver Preset Selected")
    print("")
    sub_on()
    acc_on()
    inv_on()
    rad_on()
    lig_off()
    com_on()
    sir_off()
    nul_off()

while True: #   This is literally the program, everything else is setup and definitions for functions, this is the beans
    startup()
    time.sleep(1)
    dark_car()
    time.sleep(1)
    daily_driver()
    time.sleep(1)