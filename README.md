# RoomSimulation

Room Simulation for the Transnavigator's Voice Controlled Wheelchair

To run:

python Simulator.py



Contents:

Main Program (runner)
Simulator.py - GUI and runner of the simulation

Controller
Environment.py - Holds all the components and steps through the animation

Objects
Wheelchair.py - Wheelchair object (holds data pertaining to the wheelchair)
Person.py - Person object (holds data pertaining to the person)
Obstacle.py - Obstacle object (holds data pertaining to an obstacle)

Sensors
Alexa.py - Voice control interface
Lidar.py - Lidar interface
Localino.py - Localino interface


#TODO

-Thread the simulation class for running the program
-Implement Methods in Environment.py
    -step()
    -verify()
-Graphics for library
 