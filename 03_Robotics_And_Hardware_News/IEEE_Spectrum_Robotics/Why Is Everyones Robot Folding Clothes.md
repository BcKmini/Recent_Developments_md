# Why Is Everyone’s Robot Folding Clothes?

**출처:** [IEEE_Spectrum_Robotics](https://spectrum.ieee.org/robots-folding-clothes)

## 요약
![](https://spectrum.ieee.org/media-library/a-silver-and-black-bipedal-humanoid-uses-its-five-fingered-hands-to-gray-towels-a-towel-to-be-folded-sits-on-one-side-and-on-t.gif?id=62207438&width=1200&height=400&coordinates=0%2C168%2C0%2C169)  
  

It seems like every week there’s a new video of a robot folding clothes. We’ve had some fantastic demonstrations, like [this semi-autonomous video from Weave Robotics on X](https://x.com/weaverobotics/status/1954951502671515897).

It’s awesome stuff, but Weave is far from the only company producing these kinds of videos. [Figure 02 is folding clothes](https://x.com/Figure_robot/status/1955290971660251220). [Figure 03 is folding clothes](https://youtu.be/Eu5mYMavctM?t=292). [Physical Intelligence](https://www.physicalintelligence.company/) launched their flagship vision-language-action model, pi0, with an [amazing video of a robot folding clothes](https://www.physicalintelligence.company/blog/pi0) after unloading a laundry machine. You can see robots folding clothes [live at robotics expos](https://x.com/MeRTcooking/status/1955551828038541662). Even before all this, Google showed clothes folding in their work, [ALOHA unleashed](https://aloha-unleashed.github.io/). [7X Tech](https://7xr.tech/) is even planning to sell robots to fold clothes!

And besides folding actual clothes, there are other clothes-folding-like tasks, like Dyna’s [napkin folding](https://x.com/DynaRobotics/status/1940443709621109186)— which leads to what is probably my top [robot video of the year](https://www.dyna.co/dyna-1/research), demonstrating 18 hours of continuous napkin folding. So why are all of these robotic manipulation companies suddenly into folding?

Reason 1: We basically couldn’t do this before
----------------------------------------------

There’s work [going back over a decade](https://ieeexplore.ieee.org/document/6095109) that shows some amount of robotic clothes folding. But these demonstrations were extremely brittle, extremely slow, and not even remotely production ready. Previous solutions existed (even learning based solutions!) but they relied on precise camera calibration, or on carefully hand-designed features, meaning that these clothes folding demos generally worked only on one robot, in one environment, and may have only ever worked a single time—just enough for the recording of a demo video or paper submission.

![A series of 6 stills show an older humanoid robot called a PR2 making efforts to fold a tshirt.](https://spectrum.ieee.org/media-library/a-series-of-6-stills-show-an-older-humanoid-robot-called-a-pr2-making-efforts-to-fold-a-tshirt.jpg?id=62207442&width=980) With a little bit of help from a creatively patterned shirt, PR2 was folding things back in 2014.[Bosch/IEEE](https://ieeexplore.ieee.org/document/6095109)

Take a look at [this example](https://spectrum.ieee.org/pr2-close-to-completing-laundry-cycle) of UC Berkeley’s PR2 [folding laundry](https://spectrum.ieee.org/is-there-a-future-for-laundry-folding-robots) from 2014. This robot is, in fact, using a neural network policy. But that policy is very small and brittle; it picks and places objects against the same green background, moves very slowly, and can’t handle a wide range of shirts. Making this work in practice would require larger models, pretrained on web-scale data, and better, more general techniques for imitation learning.

And so 10 years later, with the appropriate demonstration data, many different startups and research labs have been able to implement clothes-folding demos; it’s something we have seen from numerous hobbyists and startups, using broadly similar tools (like [LeRobot from HuggingFace](https://github.com/huggingface/lerobot)), without intense specialization.

Reason 2: It looks great and people want it!
--------------------------------------------

Many of us who work in robotics have this ‘north star’ of a robot butler which can do all the chores we don’t want to do. Mention clothes folding, and many, many people will chime in about how they don’t ever want to fold clothes again and are ready to part with basically any amount of money to make that happen.

This is important for the companies involved as well. Companies like Figure and 1x have been raising large amounts of money predicated on the idea that they will be able to automate many different jobs, but increasingly these companies seem to want to start in the home.

![A robotic system with two robot arms with grippers on the end work in tandem to fold a white towel.](https://spectrum.ieee.org/media-library/a-robotic-system-with-two-robot-arms-with-grippers-on-the-end-work-in-tandem-to-fold-a-white-towel.gif?id=62207449&width=980) Dyna Robotics can fold an indefinite number of napkins indefinitely.Dyna Robotics

And that’s part of the magic of these demos. While they’re slow, and imperfect, everyone can start to envision how this technology becomes the thing that we all want: a robot that can exist in our house and mitigate all those everyday annoyances that take up our time.

Reason 3: It avoids what robots are still bad at
------------------------------------------------

These robot behaviors are produced by models trained via imitation learning. Modern imitation learning methods like [Diffusion Policy](https://diffusion-policy.cs.columbia.edu/) use techniques inspired by generative AI to produce complex, dexterous robot trajectories, based on examples of expert human behavior that’s been provided to them—and they often need many, many trajectories. The work [ALOHA Unleashed](https://aloha-unleashed.github.io/) by Google is a great example, needing about 6,000 demonstrations to learn how to, for example, tie a pair of shoelaces. For each of these demonstrations, a human piloted a pair of robot arms while performing the task; all of this data was then used to train a policy.

We need to keep in mind what’s hard about these demonstrations. Human demonstrations are never **perfect**, nor are they perfectly consistent; for example, two human demonstrators will never grab the **exact** same part of an object with sub-millimeter precision. That’s potentially a problem if you want to screw a cover in place on top of a machine you’re building, but it’s not a problem at all for folding clothes, which is fairly forgiving. This has two knock-on effects:

* It’s easier to collect the demonstrations you need for folding clothes, as you don’t need to throw out every training demonstration that’s a millimeter out of spec.
* You can use cheaper, less repeatable hardware to accomplish the same task, which is useful if you suddenly need a fleet of robots collecting thousands of demos, or if you’re a small team with limited funding!

For similar reasons, it’s great that with cloth folding, you can fix your cameras in just the right position. When learning a new skill, you need training examples with “coverage” of the space of environments you expect to see at deployment time. So the more control you have, the more efficient the learning process will be—the less data you’ll need, and the easier it will be to get a flashy demo. Keep this in mind when you see a robot folding things on a plain tabletop or with an extremely clean background; that’s not just nice framing, it helps the robot out a lot!

And since we’ve committed to collecting a ton of data—dozens of hours—to get this task working well, mistakes will be made. It’s very useful, then, if it’s easy to **reset** the task, i.e. restore it to a state from which you can try the task again. If something goes wrong folding clothes, it’s fine. Simply pick the cloth up, drop it, and it’s ready for you to start over. This wouldn’t work if, say, you were stacking glasses to put away in a cupboard, since if you knock over the stack or drop one on the floor, you’re in trouble.

Clothes folding also avoids making forceful contact with the environment. Once you’re exerting a lot of pressure, things can break, the task can become non-resettable, and demonstrations are often much harder to collect because forces aren’t as easily observable to the policy. And every piece of variation (like the amount of force you’re exerting) will end up requiring more data so the model has “coverage” of the space it’s expected to operate in.

What To Look Forward To
-----------------------

While we’re seeing a lot of clothes-folding demos now, I still feel, broadly, quite impressed with many of them. As mentioned above, Dyna was one of my favorite demos this year, mostly because longer-running robot policies have been so rare until now. But they were able to demonstrate zero-shot folding (meaning folding without additional training data) at a couple of different conferences, including [Actuate in San Francisco](https://actuate.foxglove.dev/) and the [Conference on Robot Learning (CoRL)](https://www.corl.org/) in Seoul. This is impressive and actually very rare in robotics, even now.

In the future, we should hope to see robots that can handle more challenging and dynamic interactions with their environments: moving more quickly, moving heavier objects, and climbing or otherwise handling adverse terrain while performing manipulation tasks.

But for now, remember that modern learning methods will come with their own strengths and weaknesses. It seems that, while not easy, clothes folding is the kind of task that’s just really well suited for what our models can do right now. So expect to see a lot more of it.
