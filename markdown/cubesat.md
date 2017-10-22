
# A CubeSat is a standard cubic box that can be tailored to hold a desired payload.  The CubeSat deployer mechanism essentially deploys a smaller swarm of Printable Circuit Board satellites (PCBsats).  

STAC is interested in this technology because recent work on directed energy propulsion of small wafer-scale spacecraft has enabled a technically-sound conversation on achieving relativistic interstellar spaceflight. This work comes out of NASA-funded work through the NASA Innovative Advanced Concept funded programs DEEP-IN and DEIS, led by Professor Philip Lubin of the UCSB Experimental Cosmology Group. 

One of the first steps to achieving this grander scale innovation in interstellar travel requires the use of laser communication.  Our CubeSat deployer project runs a proof-of-concept and provides initial framework for laser communication by designing and fabricating an incremental deployment of PCBsats.  

_REPLACE THIS LINE WITH IFRAME CODE_

# CubeSat Deployer Prototype

Our 1U-3U CubeSat will deploy several PCBSats that are held within the CubeSat. This CubeSat will act as a communication link and mothership for all the PCBSats once they are deployed.  We plan to deploy each individual PCBSat individually and with a time delay so that there are more opportunities to test laser communication. 

The deployment mechanism works similarly to a trigger mechanism, where the 1U-3U CubeSat acts as the barrel for ejecting PCBSats. With this deployment scheme, the PCBSats are deployed in such a way that the PCBSats are tangential to a sphere centered about the CubeSat. This will allow the CubeSat to orient itself and communicate with the PCBSats quite rapidly. 

We will have altitude control, a radio link down to Earth, GPS, and numerous other electronic components within the CubeSat. This will provide a great technological and scientific demonstration PCBSat's for in-space missions.
 
![Figure 1: Artistic Rendition of CalSat Deployer of PCBSats](img/projects/cubesat/rendition-of-CalSat.png)


**Altitude Control**

We are working on developing our Avionics for the CalSat Deployer by using Torque Coils.

**Communication**
We will plan to develop a Laser-Comm Link or Radio link between each PCBSat (once deployed) and the CalSat Deployer. The Deployer will act as the data link from the PCBSats back down to Earth.

**Power**

The objective is to develop a low power CubeSat. Proposed components include:
- Photovoltaics on the outside of CubeSat
- LIPO battery onboard
- Power distribution board and power controller
- Everything will run on 3.3V and 5V power

**Electronics**

Proposed electronic components of the Cubesat command and data handling (C&DH) board are:

- CPU (either a processor or microcontroller)
- Running a Linux real-time operating system (RTOS)
- NAND and/or NOR Flash memory
- SRAM and/or SDRAM memory
- Serial communication (SPI, I2C, UART, RS-422, etc.) capabilities
- 3.3V and 5V Voltage regulators
- Uplink/Downlink communication bus
- Digital I/O and Analog sensing capabilities
- Stackable connector pins
- Backup battery
- Radio

**Testing Prototype**

With our partnership with the Space Sciences Laboratory (SSL), we will be running vibration tests and thermo-vacuum chamber tests at the SSL facilities.

# Goals of CubeSat Deployer

- Provide cost effective and flexible test platform for developing spacecraft and communications technology
- Allow for integration of various sensor systems to support data capture and manipulation
- Utilize readily available materials and integrated circuits to support quick revision turnaround times and system re-designs
- Explore the limits of rigid PCB manufacturing capabilities for future use
- Test and validate early-life directed energy technologies
- Test and validate early-life propulsion and orientation systems
- Test and validate CalSat Deployer on Earth in the lab and with balloons at high-altitudes
- Test controls for CubeSat and PCBSat with UC Davis SSS Air Bearing and with SSL facilities
- Provide a starting point from which future revisions/systems can be based on
- Provide an inexpensive platform to deploy multiple experiments in a single launch
- Produce data, feedback and calculations in order to drive future development
- The CubeSat Deployer could also have a laser onboard to test photon propulsion

---

# PCB Spacecraft Prototype (UCSB and STAC)

Because the PCBsat fabrication is done with our partner at UCSB, more details on PCBsat specs can be found [on their site](http://www.deepspace.ucsb.edu/projects/wafer-scale-spacecraft-development).

![Figure 2: Initial revision of waferSat on a PC Board](img/projects/cubesat/waferSat1.png)

Above is the initial revision of waferSat on a PC Board developed at UCSB. It includes subsystems for altitude control, digital image acquisition, inter-system communications, and photovoltaic power source.

**Development Path and Timeline**

![Figure 3: Evolution of PCBSats to Wafer Spacecraft for Interstellar Travel](img/projects/cubesat/evolution-of-PCBSats.png)


1. Develop and 3D-print initial CalSat design
2. Develop electronics and power for CalSat
3. Develop Altitude and control systems with suntracker and torque coils
4. Test PCBSat on ground with UCSB
5. 2nd prototype of CalSat deployer
6. Combine electronic avionics with CalSat deployer
7. Develop comm-link for ground
8. Raise funding and awareness for the CalSat
9. Testing prototype at SSL
10. Fix any prototype flaws
11. Prepare for launch - mid 2018
