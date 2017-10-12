# RoomSimulation

Room Simulation for the Transnavigator's Voice Controlled Wheelchair

To run:

python Simulator.py



Contents:

Main Program (runner)
Simulator.py - GUI and runner of the simulation

Controller
Environment.py - Holds all the components and steps through the animation
Pi.py - Represents the R-Pi (the brains of the wheelchair)

Objects
Wheelchair.py - Wheelchair object (holds data pertaining to the wheelchair)
Person.py - Person object (holds data pertaining to the person)
Obstacle.py - Obstacle object (holds data pertaining to an obstacle)

Wheelchair sensors
Lidar.py - Lidar sensor
Encoder.py - Encoder sensor
BerryIMU - Interial Measurement unit

Services
Alexa.py - Voice control interface
Localino.py - Location interface




#TODO

-Thread the simulation class and all sensors for running the program
-Implement Methods in Environment.py
    -step()
    -verify()
-Graphics for wheelchair

simulate sensor and service data

 