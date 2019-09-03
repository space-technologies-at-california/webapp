# A resource rover is an extraterrestrial vehicle used for space exploration as well as resource extraction on various celestial bodies.

Lunar colonization has been a goal of the aerospace community, and humanity at large, for decades. With the discovery of water-ice in the permanently shadowed regions near the poles of the moon, there has been a designated focus on harnessing it for use as fuel, drinking water, etc. in order to help make the dream of establishing a lunar base a reality.

In collaboration with the NASA Ames Research Center on their Lunar Commercial Operation and Transfer Services (LCOTS) concept, STAC will contribute to the manifestation of a lunar base by prototyping an autonomous resource rover, capable of detecting, extracting, and storing lunar resources, ultimately taking them back to the central lunar base for further refinement.

The rover prototype will comprise a robust mechanical body, capable of navigating the lunar terrain, an end effector for collecting lunar regolith, resource extraction modules, and a resource storage unit.

![Figure 1: Map of water distribution over the moon](img/projects/resourcerover/water_dist.png)

**Objectives**

Our experimental setup sought to extract the water-ice from lunar regolith by microwaving it  and depositing the extracted ice in a vacuumed, liquid nitrogen cooled chamber to mimic a lunar environment. The overall purpose is to determine the viability of using microwaves to extract the ice from regolith, and the crystal geometry, density, distribution, and the rate of ice deposition. If applicable, a water extraction module to load on the rover will be designed and implemented.

**Materials/Methods**

In order to develop a proof-of-concept for the liberation of water trapped in lunar regolith, the methodology and physical mechanisms of how this water is extracted from the soil and stored for further processing must be determined. To gain valuable data on the rates and geometry of ice deposition in a moon-like environment, a sample of ice was placed in a Büchner flask, with tubing connecting the flask to a custom-made vacuum chamber with a viewing port and, and a large copper cold plate.

From this setup, the copper cold plate was then submerged in liquid nitrogen, effectively causing the copper to act as a thermal heat sink, and a vacuum (~10^-5 Pa) was pulled on the entire system. Immediately, the ice sublimated, and the gaseous water traveled through the tubing before finally deposing on the heat sink.

Throughout this experiment, two major pieces of information will be gleaned: the geometry of the resulting ice deposition, and the rate at which the ice sublimates and deposes onto the copper. This information is crucial in making a sound theoretical model of the proof-of-concept, and allows for a baseline to which values from the resulting proof-of-concept can be compared to.

![Figure 2: Experiment setup](img/projects/resourcerover/setup.png)

**Current Progress**

During the first trial of our experiment, a high vacuum was achieved (10-8 Atm), but the pressure in the chamber spiked as soon as water vapor was introduced into the system, which caused the ice to melt instead of sublimating, and ice was not able to be recrystallized in the vacuum chamber. The reasons for this failure include too much internal surface area in the path that the water vapor has to travel through, too little heat transfer out of cold trap, and a possible leak in flask/hose.

We ran the experiment again, with a new setup that addressed possible issues from the first run, minimizing surface area and maximizing LN2 exposure. This set up produced a thermal shock on the chamber so large that the solder joints likely cracked.

**References**

1. Li and Milliken, “Water on the surface of the Moon as seen by the Moon Mineralogy Mapper: Distribution, abundance, and origins”, 13 Sep 2017
2. M. G. Bekker, Introduction to Terrain-Vehicle Systems. Ann Arbor, MI: University of Michigan Press, 1969.
3. S. Moreland, K. Skonieczny, H. Inotsume, and D. Wettergreen, “Soil behavior of wheels with grousers for planetary rovers,” IEEE Aerospace, Big Sky, 2012.
4. Zuniga, A., Rasky, D., Pittman, R., Zapata, E., Lepsch, R., “Lunar COTS: An Economical and Sustainable Approach to Reaching Mars,” AIAA Paper 2015-4408, AIAA Space 2015 Conference, Pasadena, CA, Sep 2015.
5. Zuniga, A., Turner, M., Rasky, D., Pittman, R., Zapata, E., “Kickstarting a New Era of Lunar Industrialization via Campaigns of Lunar COTS Missions,” AIAA Paper 2016-5220, AIAA Space 2016 Conference, Long Beach, CA, Sep 2016
6. Visscher, P. (2011). New Developments in Planetary Rover Traction Systems. AIAA SPACE 2011. Long Beach, CA, USA.
