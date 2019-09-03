
# We have been working on the next set of microgravity experiments, after our initial set of [microgravity experiments](/projects/time1). We plan to reuse our chassis (or enclosure) and communication systems design from the TIME project for future payload launches to space.

Extended spaceflight is known to inhibit immune function, making astronauts more susceptible to illnesses like bacterial infection. Both *in vitro* and *in vivo*, bacteria have been shown to be more resistant to antibiotics in microgravity.

However, microbial physiology in space is still poorly understood due to large prohibitive costs and extensive technical challenges surrounding the logistics of sending bacteria to space. Fortunately, the advent of commercial spaceflight heralds cheaper, more accessible experimentation in microgravity.

Here, we aim to detail an experimental workflow preceding launch into microgravity as well as demonstrate the ease and capability of modularized microbiology payloads with low barrier of entry for commercial spaceflight. The Interstellar Microgravity Experiment is a suborbital payload flying on Blue Origin’s New Shepard spacecraft.

On our 2U payload, we aim to host an autonomous biological experiment that models antibiotic  efficacy in space. Our payload, with a 500g mass budget, remains inside the pressurized crew capsule for the duration of the flight and experiences 2 – 3 minutes of continuous microgravity.

**Growing *E. Coli* in Modeled Microgravity**

The gold standard for testing growth in modeled microgravity involves use of low-shear modeled microgravity in rotating wall vessels (high aspect rotating vessels).

The concept of low-shear microgravity is dependent on the idea that by randomizing the pull of gravity and growing cells in low turbulence (low shear) conditions, we can create a state of functional weightlessness.[3] We can then utilize this environment to simulate the conditions in our experiment.

Due to limited budget constraints and the general unavailability of models in the Bay Area, we are interested in engineering a prototype based on a paper by Ray Schwarz published in 1992.[3] We plan to generate an open-source, inexpensive alternative for rapid testing of modeled microgravity.

![The basic schematic of the 1992 paper describing construction of the rotating wall vessel.](img/projects/time2/schematic.png)

**Gene Expression in Response to Antibiotics**

Previously, it has been shown that *E. coli* have increased resistance to the antibiotic gentamycin in microgravity.[4] Also, studies have shown that antibiotic use in simulated microgravity can cause persistent resistance to antibiotics.[5]

Our ultimate goal is to perform RNA-seq on the *E. coli* strain MG1655 after exposure to the antibiotic gentamicin in microgravity. However, we first plan to validate the results of these previous experiments in simulated microgravity with qPCR of known stress genes followed by RNA-seq.  

**Payload and Testing**

Design of the payload began with a simple overview of the necessary components to perform the experiment. Our prototype currently consists of a 2 mL main reaction chamber, with antibiotics located in a small reservoir behind a small capillary force valve. RNAlater is introduced via serpentine channels at various points during the experiment. The serpentine channels are designed to create turbulent flow to increase mixing in the main reaction chamber. Fluid flow is currently modeled with COMSOL and supporting avionics software is being developed for concurrent use in modeled microgravity.

Payload weight and space constraints are the main engineering obstacles with regards to payload design and testing. In addition to the stringent mass and weight budget, the payload will also be subjected to vibration, degas, electrical, and flammability safety testing prior to launch. We plan to iterate on previous designs from TIME I, the predecessors to our current experiment, who are also launching with Blue Origin.

![Figure 2: Single microfluidic plate design](img/projects/time2/plate_design.png)

**Experiment Launch and Overview**

We have a three-part experimental overview that will be accomplished before sending our samples into space:

1. Growing *E. coli* in modeled microgravity conditions
2. Testing gene expression in response to antibiotics
3. Designing, prototyping, and testing various payload designs

![Figure 3: Projected altitude, Sensed acceleration profile of the payload](img/projects/time2/graphs.png)

In Figure 3, The New Shepard rocket will reach an altitude of approximately 325,000 ft. (approximately 100 km) above sea level in suborbital flight. In the image to the right, note the brief exposure to microgravity from 150 seconds to 350 seconds.

**Future Directions**

1. qPCR validation of gene expression
2. Bacterial growth in simulated microgravity and prototyped microfluidic plates
3. Simulating fluid flow in COMSOL for the microfluidic plate
4. Launching with Blue Origin

**References**

1. Tixador R, Richoilley G, Gasset G, Templier J, Bes JC, Moatti N, Lapchine L. (1985). Study of minimal inhibitory concentration of antibiotics on bacteria cultivated in vitro in space (Cytos 2 experiment). Aviat Space Environ Med. 56(8); 748-51
2. Purevdorj-Gage B, Sheehan K, Hyman L. (2006). Effects of Low-Shear Modeled Microgravity on Cell Function, Gene Expression, and Phenotype in Saccharomyces cerevisiae. Appl. Environ. Microbiol. 72 (7); 4569-4575;
3. Schwarz R, Goodwin T, Wolf D. (1992). Cell Culture for Three-Dimensional Modeling in Rotating-Wall Vessels: an Application of Simulated Microgravity. J. Tissue Meth. 14:51-58
4. Matin AC, et al. (2017). Payload hardware and experimental protocol development to enable future testing of the effect of space microgravity on the resistance to gentamicin of uropathogenic Escherichia coli and its σs-deficient mutant
5. Tirumalai M, et al. (2019). Evaluation of Acquired Antibiotic Resistance in Escherichia coli Exposed to Long-Term Low-Shear Modeled Microgravity and Background Antibiotic Exposure. mBio. 10 (1) e02637-18
