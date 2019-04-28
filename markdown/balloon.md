# A high altitude balloon is an unmanned balloon meant to carry scientific payloads to perform experiments and collect data in near space environments.

STAC’s High Altitude Balloon (HAB) program is aiming to shift our balloon’s applications from terrestrial to space-oriented. Research concerning the colonization of Mars and planetary exploration in general has opened new avenues for HAB to follow in our coming projects. The High Altitude Balloon (HAB) program in STAC provides a standardized system to test research experiments in a near-space environment. While there are a variety of space applications for high altitude balloons, the current project will focus on the long term goal of creating a reliable method of conducting future STAC experiments. This allows for affordable observations above the Earth’s atmosphere.

We have launched three balloons to date, with a fourth launch planned in Fall of 2019. Our third launch, shown below, tested a revamped electronics core with real-time satellite locationing.

<iframe class='embed-responsive-item' width='800' height='500' src='https://www.youtube.com/embed/QLS7XfSBsL4' allowfullscreen='allowfullscreen'>STAC HAB 3 Launch Video</iframe>

## Electronics
Our electronics core is composed of a new STM microcontroller board that manages all of our sensors and data logging. The on board sensors include GPS, altimeter, 9 DOF IMU, and thermocouple. Additionally, the board is responsible for implementing the control logic and operating the actuators to adjust the trajectory of the balloon, as well as serving as a mode of communication for real time data through the Rockblock satellite network.

![](img/projects/balloon/schematic.png)

The fourth launch of HAB attempts to implement a controlled descent algorithm for targeted landing of the payload. Using information from the various onboard sensors, the algorithm will estimate the current position of the payload and reel in the appropriate amount of parachute line to steer the payload closer to the desired waypoint. This closed-loop system continually updates its predicted trajectory and the length of the parachute control line as new location information is collected from the sensors.

## Mechanical
The main focus of the mechanical subteam is to standardize recovery methods for more consistent future launches. In our fourth iteration of HAB we will be using a reversible reefing system which includes a cruciform-style parachute along with multiple winch actuators.

![](img/projects/balloon/hab_ascent_logo2.png)
