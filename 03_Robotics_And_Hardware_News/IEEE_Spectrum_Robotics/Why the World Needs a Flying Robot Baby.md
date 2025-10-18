# Why the World Needs a Flying Robot Baby

**출처:** [IEEE_Spectrum_Robotics](https://spectrum.ieee.org/ironcub-jet-powered-flying-robot)

## 요약
![](https://spectrum.ieee.org/media-library/advanced-robot-torso-with-mechanical-arms-and-visible-cables.jpg?id=61668516&width=1200&height=800&coordinates=0%2C50%2C0%2C50)  
  

One of the robotics projects that I’ve been most excited about for years now is [iRonCub](https://ami.iit.it/aerial-humanoid-robotics), from Daniele Pucci’s [Artificial and Mechanical Intelligence Lab](https://ami.iit.it/) at the Italian Institute of Technology (IIT) in Genoa, Italy. [Since 2017](https://spectrum.ieee.org/jet-powered-icub-could-be-the-first-flying-humanoid-robot), Pucci has been developing a jet-propulsion system that will enable an [iCub](https://robotsguide.com/robots/icub) robot (originally designed in 2004 to be the approximate shape and size of a 5-year-old child) to fly like Iron Man.

Over the summer, after nearly 10 years of development, [iRonCub3 achieved lift-off and stable flight for the first time](https://opentalk.iit.it/en/iit-demonstrates-that-a-humanoid-robot-can-fly/), with its four jet engines lifting it 50 centimeters off the ground for several seconds. The long-term vision is for iRonCub (or a robot like it) to operate as a disaster response platform, Pucci tells us. In an emergency situation like a flood or a fire, iRonCub could quickly get to a location without worrying about obstacles, and then on landing, start walking for energy efficiency while using its hands and arms to move debris and open doors. “We believe in contributing to something unique in the future,” says Pucci. “We have to explore new things, and this is wild territory at the scientific level.”

Obviously, this concept for iRonCub and the practical experimentation attached to it is really cool. But coolness in and of itself is usually not enough of a reason to build a robot, especially a robot that’s a (presumably rather expensive) multi-year project involving a bunch of robotics students, so let’s get into a little more detail about why a flying robot baby is actually something that the world needs.

---

In an emergency situation like a flood or a fire, iRonCub could quickly get to a location without worrying about obstacles, and then on landing, start walking for energy efficiency while using its hands and arms to move debris and open doors. IIT

Getting a humanoid robot to do this sort of thing is quite a challenge. Together, the jet turbines mounted to iRonCub’s back and arms can generate over 1000 N of thrust, but because it takes time for the engines to spool up or down, control has to come from the robot itself as it moves its arm-engines to maintain stability.

“What is not visible from the video,” Pucci tells us, “is that the exhaust gas from the turbines is at 800 °C and almost supersonic speed. We have to understand how to generate trajectories in order to avoid the fact that the cones of emission gases were impacting the robot.”

Even if the exhaust doesn’t end up melting the robot, there are still aerodynamic forces involved that have until this point really not been a consideration for humanoid robots at all—in June, Pucci’s group [published a paper in *Nature Engineering Communications*](https://www.nature.com/articles/s44172-025-00447-w), offering a “comprehensive approach to model and control aerodynamic forces [for humanoid robots] using classical and learning techniques.”

“The exhaust gas from the turbines is at 800 °C and almost supersonic speed.” **—Daniele Pucci, IIT**

Whether or not you’re on board with Pucci’s future vision for iRonCub as a disaster-response platform, derivatives of current research can be immediately applied beyond flying humanoid robots. The algorithms for thrust estimation can be used with other flying platforms that rely on directed thrust, like eVTOL aircraft. Aerodynamic compensation is relevant for humanoid robots even if they’re not airborne, if we expect them to be able to function when it’s windy outside.

More surprising, Pucci describes a recent collaboration with an industrial company developing a new pneumatic gripper. “At a certain point, we had to do force estimation for controlling the gripper, and we realized that the dynamics looked really similar to those of the jet turbines, and so we were able to use the same tools for gripper control. That was an ‘ah-ha’ moment for us: first you do something crazy, but then you build the tools and methods, and then you can actually use those tools in an industrial scenario. That’s how to drive innovation.”

What’s Next for iRonCub: Attracting Talent and Future Enhancements
------------------------------------------------------------------

There’s one more important reason to be doing this, he says: “It’s really cool.” In practice, a really cool flagship project like iRonCub not only attracts talent to Pucci’s lab, but also keeps students and researchers passionate and engaged. I saw this firsthand when I visited IIT last year, where I got a similar vibe to watching the [DARPA Robotics Challenge](https://spectrum.ieee.org/darpa-robotics-challenge-amazing-moments-lessons-learned-whats-next) and [DARPA SubT](https://spectrum.ieee.org/collections/darpa-subterranean-challenge/)—when people know they’re working on something **really cool**, there’s this tangible, pervasive, and immersive buzzing excitement that comes through. It’s projects like iRonCub that can get students to love robotics.

In the near future, a new jetpack with an added degree of freedom will make yaw control of iRonCub easier, and Pucci would also like to add wings for more efficient long-distance flight. But the logistics of testing the robot are getting more complicated—there’s only so far that the team can go with their current test stand (which is on the roof of their building), and future progress will likely require coordinating with the Genoa airport.

It’s not going to be easy, but as Pucci makes clear, “This is not a joke. It’s something that we believe in. And that feeling of doing something exceptional, or possibly historical, something that’s going to be remembered—that’s something that’s kept us motivated. And we’re just getting started.”
