# Perseverance Smashes Autonomous Driving Record on Mars

**출처:** [IEEE_Spectrum_Robotics](https://spectrum.ieee.org/perseverance-mars-rover-autonomous-driving)

## 요약
![](https://spectrum.ieee.org/media-library/a-self-portrait-captured-by-nasa-s-perseverance-rover-while-traversing-mars-rocky-surface.jpg?id=65007226&width=1200&height=400&coordinates=0%2C729%2C0%2C730)  
  

*This article is part of our exclusive [IEEE Journal Watch series](https://spectrum.ieee.org/collections/journal-watch/) in partnership with [IEEE Xplore](https://spectrum.ieee.org/tag/ieee-xplore).*

In past missions to Mars, like with the [*Curiosity*](https://spectrum.ieee.org/nasa-mars-curiosity-rover-autonomous-driving-mode) and *Opportunity* rovers, the robots relied mostly on human instructions from millions of miles away in order to safely navigate the Martian landscape. The *Perseverance* rover, on the other hand, has zipped across the alien, boulder-ridden land almost completely autonomously, smashing previous records for autonomous driving on Mars.

Whereas the *Curiosity* rover completed about 6.2 percent of its travels autonomously,*Perseverance* had completed about 90 percent of its travels autonomously, as of its 1,312th Martian day since landing (28 October 2024). *Perseverance* was able to accomplish such a feat—using remarkably little computing power—thanks to its specially designed autonomous driving algorithm, Enhanced Autonomous Navigation, or ENav.

The full details on ENav’s inner workings and how well it has performed on Mars are described in a [study](https://ieeexplore.ieee.org/document/11265757) published in [*IEEE Transactions on Field Robotics*](https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=10495159) in November 2025.

There are some advantages, but some serious challenges when it comes to autonomous navigation on Mars. On the plus side, almost nothing on the planet moves. Rocks and gravel slopes—while formidable obstacles—remain stationary, offering rovers consistency and predictability in their calculations and pathfinding. On the other hand, Mars is in large part uncharted terrain.

“This enormous uncertainty is the major challenge,” says [Masahiro “Hiro” Ono](https://www-robotics.jpl.nasa.gov/who-we-are/people/masahiro_ono/), supervisor of the Robotic Surface Mobility Group at NASA’s Jet Propulsion Laboratory, who helped develop ENav.

Creating a Highly Autonomous Rover
----------------------------------

While some images from the space-borne Mars Reconnaissance Orbiter exist, these are usually not high enough resolution for ground-based navigation by a rover. In December, NASA engineers performed the first [test of a navigation technique](https://spectrum.ieee.org/perseverance-rover-nasa-anthropic-ai) that uses a model based on Anthropic’s AI to analyze MRO images and generate waypoints—the coordinates used to guide the rover’s path—for more complete automation.

RELATED: [NASA Let AI Drive the Perseverance Rover](https://spectrum.ieee.org/perseverance-rover-nasa-anthropic-ai)

But in the majority of today’s navigation, *Perseverance* must rely on images the rover itself takes, analyze these to assess thousands of different paths, and choose the right route that won’t end in its own demise. The kicker? It must do so with the equivalent computing capacity of an [iMac G3](https://en.wikipedia.org/wiki/IMac_G3), an Apple computer sold in the late 1990s.

This is because older CPUs can undergo [radiation hardening](https://spectrum.ieee.org/europa-clipper), a process that makes them resilient to the extreme levels of solar radiation and cosmic rays experienced on Mars. Newer CPUs with more computing power, on the other hand, cannot work under such extreme conditions. Therefore, researchers must work with what they have—a computer core from the 1990s.

Given its limited computing resources, the ENav algorithm was strategically designed to do the heaviest computing only when driving on challenging terrains. It works by analyzing images of its surroundings and assessing about 1,700 possible paths forward, typically within 6 meters from the rover’s current position. Assessing factors such as travel time and terrain roughness, it ranks possible paths. Finally, it runs a computationally heavy collision-checking algorithm, called ACE (approximate clearance estimation) on only on a handful of top-ranked potential paths.

![The driving path of NASA's Perseverance rover across Mars' surface, spanning 18.65 miles.](https://spectrum.ieee.org/media-library/the-driving-path-of-nasa-s-perseverance-rover-across-mars-surface-spanning-18-65-miles.jpg?id=65007264&width=980) As of October 2024, Perseverance has driven more than 30 kilometers (18.65 miles) and collected 24 samples of rock and regolith. Source: JPL-Caltech/ASU/MSSS/NASA

Exploring the Red Planet with ENav
----------------------------------

*Perseverance* landed on Mars on 18 February 2021. In their study, Ono and his colleagues describe how the rover was initially deployed with strong human navigation oversight during its first 64 Martian days on the Red Planet, but then went on to predominantly use ENav to travel to one of the major exploration targets: the delta formed by an ancient river that once flowed into Jezero Crater billions of years ago. Scientists believe it could be a prime spot for finding evidence of past alien life, if life ever existed on Mars.

After a brief exploration of an area southwest of its landing site, *Perseverance* jetted counterclockwise around sand dunes toward the ancient river delta at a crisp pace, averaging 201 meters per Martian day. (It’s too cold for the rover to travel at night.) Over the course of just 24 Martian days of driving, the rover traveled about 5 kilometers into the foothill of the delta. 95 percent of all driving that month was performed using the autonomous driving mode, resulting in an unprecedented amount of autonomous driving on Mars.

Past rovers, such as *Curiosity*, had to stop and “think” about their paths before moving forward. “That was the main speed bump for *Curiosity*, why it was so slow to drive autonomously,” Ono explains.

In contrast, *Perseverance* is able to think and drive at the same time. “Sometimes [*Perseverance*] has to stop and think, particularly when it cannot figure out a safe path quickly. But most of the time, particularly on easy terrains, it can keep driving without stopping,” Ono says. “That made its autonomous driving an order of magnitude faster.”

*Opportunity* held the previous record for autonomous driving on Mars, traveling 109 meters in a single Martian day. But on 3 April 2023, *Perseverance* set a new record by driving 331.74 meters autonomously (and 347.69 meters in total) in a single Martian day.

Ono says that fine-tuning the ENav algorithm took a lot of work, but he is happy with its performance. He also emphasizes that efforts to continue advancing autonomous navigation are critical if humans want to continue exploring even deeper into space, where Earthly communication with rovers and other spacecraft will become increasingly difficult.

“The automation of the space systems is unstoppable direction that we have to go if we want to explore deeper in space,” Ono says. “This is the direction that we must go to push the boundaries and frontiers of space exploration.”
