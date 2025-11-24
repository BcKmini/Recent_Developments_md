# This Soft Robot Is 100% Edible, Including the Battery

**출처:** [IEEE_Spectrum_Robotics](https://spectrum.ieee.org/soft-edible-robot)

## 요약
![](https://spectrum.ieee.org/media-library/sands-shift-in-a-glass-box-as-an-orange-robotic-worm-surfaces.gif?id=62162692&width=2000&height=1500&coordinates=23%2C0%2C23%2C0)  
  

While there are many useful questions to ask when encountering a new robot, “can I eat it” is generally not one of them. I say ‘generally,’ because [edible robots are actually a thing](https://spectrum.ieee.org/tag/edible-robots)—and not just edible in the sense that you can technically swallow them and suffer [both the benefits and consequences](https://spectrum.ieee.org/magnetic-pill-sized-robot-cartwheel), but **ingestible**, where you can [take a big bite out of the robot](https://spectrum.ieee.org/edible-robots-2667244222), chew it up, and swallow it.

Yum.

But so far these ingestible robots have included a very please-don’t-ingest-this asterisk: the motor and battery, which are definitely toxic and probably don’t taste all that good. The problem has been that soft, ingestible actuators run on gas pressure, requiring pumps and valves to function, neither of which are easy to make without plastic and metal. But in [a new paper](https://advanced.onlinelibrary.wiley.com/doi/10.1002/advs.202509350), researchers from [Dario Floreano’s Laboratory of Intelligent Systems at EPFL in Switzerland](https://www.epfl.ch/labs/lis/) have demonstrated ingestible versions of both of batteries and actuators, resulting in what is, as far as I know, the first entirely ingestible robot capable of controlled actuation.

---

![An ingestible actuator.](https://spectrum.ieee.org/media-library/an-ingestible-actuator.jpg?id=62176243&width=980) EPFL

Let’s start with the battery on this lil’ guy. In a broad sense, a battery is just a system for storing and releasing energy. In the case of this particular robot, the battery is made of gelatin and wax. It stores chemical energy in chambers containing liquid citric acid and baking soda, both of which you can safely eat. The citric acid is kept separate from the baking soda by a membrane, and enough pressure on the chamber containing the acid will puncture that membrane, allowing the acid to slowly drip onto the baking soda. This activates the battery and begins to generate CO2 gas, along with sodium citrate (common in all kinds of foods, from cheese to sour candy) as a byproduct.

![GIF of an ingestible battery operating.](https://spectrum.ieee.org/media-library/gif-of-an-ingestible-battery-operating.gif?id=62177237&width=980) EPFL

The CO2 gas travels through gelatin tubing into the actuator, which is of a [fairly common soft robotic design](https://spectrum.ieee.org/soft-selfhealing-materials-for-robots-that-cannot-be-destroyed) that uses interconnected gas chambers on top of a slightly stiffer base that bends when pressurized. Pressurizing the actuator gets you one single actuation, but to make the actuator wiggle (wiggling being an absolutely necessary skill for any robot), the gas has to be cyclically released. The key to doing this is the other major innovation here: an ingestible valve.

![GIF of an ingestible valve snap-buckling.](https://spectrum.ieee.org/media-library/gif-of-an-ingestible-valve-snap-buckling.gif?id=62166207&width=980) EPFL

The valve operates based on the principle of snap-buckling, which means that it’s happiest in one shape (closed), but if you put it under enough pressure, it rapidly snaps open and then closed again once the pressure is released. The current version of the robot operates at about four bending cycles per minute over a period of a couple of minutes before the battery goes dead.

And so there you go: a battery, a valve, and an actuator, all ingestible, makes for a little wiggly robot, also ingestible. Great! But **why**?

“A potential use case for our system is to provide nutrition or medication for elusive animals, such as wild boars,” says lead author Bokeon Kwak. “Wild boars are attracted to live moving prey, and in our case, it’s the edible actuator that mimics it.” The concept is that you could infuse something like a swine flu vaccine into the robot. Because it’s cheap to manufacture, safe to deploy, completely biodegradable, and wiggly, it could potentially serve as an effective strategy for targeted mass delivery to the kind of animals that nobody wants to get close to. And it’s obviously not just wild boars—by tuning the size and motion characteristics of the robot, what triggers it, and its smell and taste, you could target pretty much any animal that finds wiggly things appealing. And that includes humans!

Kwak says that if you were to eat this robot, the actuator and valve would taste a little bit sweet, since they have glycerol in them, with a texture like gummy candy. The pneumatic battery would be crunchy on the outside and sour on the inside (like a lemon) thanks to the citric acid. While this work doesn’t focus specifically on taste, the researchers have made other versions of the actuator that were flavored with grenadine. They [served these actuators out to humans earlier this year](https://swissnex.org/news/first-tasting-of-the-robocake-epfl/), and are working on an ‘analysis of consumer experience’ which I can only assume is a requirement before announcing a partnership with Haribo.

Eatability, though, is not the primary focus of the robot, says PI Dario Floreano. “If you look at it from the broader perspective of environmental and sustainable robotics, the pneumatic battery and valve system is a key enabling technology, because it’s compatible with all sorts of biodegradable pneumatic robots.” And even if you’re not particularly concerned with all the environmental stuff, which you really should be, in the context of [large swarms of robots in the wild](https://spectrum.ieee.org/otherlab-apsara-aerial-delivery-system) it’s critical to focus on simplicity and affordability just to be able to usefully scale.

This is all part of the EU-funded [RoboFood project](https://www.robofood.org/research/), and Kwak is currently working on other edible robots. For example, the elastic snap-buckling behavior in this robot’s valve is sort of battery-like in that it’s storing and releasing elastic energy, and with some tweaking, Kwak is hoping that edible elastic power sources might be the key for [tasty little jumping robots that jump right off the dessert plate and into your mouth](https://advanced.onlinelibrary.wiley.com/doi/10.1002/admt.202401230).

[Edible Pneumatic Battery for Sustained and Repeated Robot Actuation](https://advanced.onlinelibrary.wiley.com/doi/10.1002/advs.202509350), by Bokeon Kwak, Shuhang Zhang, Alexander Keller, Qiukai Qi, Jonathan Rossiter, and Dario Floreano from EPFL, is published in **Advanced Science**

.
