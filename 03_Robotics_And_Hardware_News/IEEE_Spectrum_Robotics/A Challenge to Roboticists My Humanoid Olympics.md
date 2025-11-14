# A Challenge to Roboticists: My Humanoid Olympics

**출처:** [IEEE_Spectrum_Robotics](https://spectrum.ieee.org/humanoid-robot-olympics)

## 요약
![](https://spectrum.ieee.org/media-library/a-collection-of-8-video-stills-showing-a-man-in-a-silver-bodysuit-doing-tasks-including-picking-up-dog-poop-wiping-a-window-pe.jpg?id=61943822&width=1200&height=600&coordinates=0%2C500%2C0%2C500)  
  

I was a little disappointed by China’s [World Humanoid Robot Games](https://apnews.com/article/humanoid-robot-games-beijing-china-artificial-intelligence-f0bdd670fae9904aea2c4df398cdcb1a).[1](https://spectrum.ieee.org/feeds/topic/robotics.rss#note1) As fun as real-life [Rock ‘Em Sock ‘Em Robots](https://en.wikipedia.org/wiki/Rock_%27Em_Sock_%27Em_Robots) is, what people *really* care about is [robots doing their chores](https://spectrum.ieee.org/ai-robots). This is why robot laundry folding videos are so popular: we didn’t know how to do that even a few years ago. And it is certainly something that people want! But as [this article](https://itcanthink.substack.com/p/why-is-everyones-robot-folding-clothes) so nicely articulates, basic laundry folding is in a sweet spot given the techniques we have now. It might feel like if our AI techniques can fold laundry, maybe they can do anything—but that isn’t true, and we’re going to have to invent new techniques to be really general purpose and useful.

With that in mind I am issuing a challenge to roboticists: Here are **my** Humanoid Olympic events. Each event will require us to push the state of the art and unlock new capabilities in robotic manipulation. I will update [my Substack](https://generalrobots.substack.com/p/benjies-humanoid-olympic-games) as folks achieve these milestones, and will mail actual real-life medals to the winners.

Current State of The Art
------------------------

In order to talk about why each of these challenges pushes the state of the art in robotic manipulation, let’s first talk about what’s working now. What I’m seeing working is learning from demonstration. Generally, folks are using puppeteering interfaces. Most common seems to be two copies of the robot so that a human can grab and move one of them while the other follows, or a virtual reality headset with controllers for hand tracking. They then record some 10-30 second activity hundreds of times over. Fromm that data, a neural network is trained to mimic those examples. This technique has unlocked tasks that have steps that are somewhat chaotic (like pulling a corner of a towel to get it to lay flat) or have a high state space (like how a towel can be bunched up in myriad different ways).

Thinking about this method of training robots to do things, it should be clear what some of the limitations are. Each of these has exceptions, but together they form a general trend.

1. **No force feedback at the wrists.**[2](https://spectrum.ieee.org/feeds/topic/robotics.rss#note2) The robot can only ever perform as well as the human teleoperating it, but we don’t yet have good standardized ways of getting high resolution force information to the human teleoperator.
2. **Limited finger control.**[3](https://spectrum.ieee.org/feeds/topic/robotics.rss#note3) It’s hard for the teleoperator (and for a foundation model) to see and control all of a robot’s fingers with much more finesse than just opening and closing them.
3. **No sense of touch.**[4](https://spectrum.ieee.org/feeds/topic/robotics.rss#note4) Human hands are packed absolutely full of sensors. Getting anywhere near that kind of sensing out of robot hands in a way that’s usable by a human teleoperator is not currently possible.
4. **Medium precision.**[5](https://spectrum.ieee.org/feeds/topic/robotics.rss#note5) Based on videos I’ve seen, I think we’ve got about 1-3 cm precision for tasks.

Now, on to the events!

#### [Event 1: Doors](https://spectrum.ieee.org/feeds/topic/robotics.rss#event1)

#### [Event 2: Laundry](https://spectrum.ieee.org/feeds/topic/robotics.rss#event2)

#### [Event 3: Tools](https://spectrum.ieee.org/feeds/topic/robotics.rss#event3)

#### [Event 4: Fingertip Manipulation](https://spectrum.ieee.org/feeds/topic/robotics.rss#event4)

#### [Event 5: Wet Manipulation](https://spectrum.ieee.org/feeds/topic/robotics.rss#event5)

Event 1: Doors
--------------

Things like doors are tricky because of the asymmetric forces: you need to grasp and twist the handle or knob quite hard, but if you pull hard outside of the arc of the door you tend to slip your grasp. Also, moving through a door requires whole body manipulation, which is more than I’ve seen from anyone yet.

### Bronze Medal: Entering a round-knob push door

[  Your browser does not support the video tag. ](https://roar-assets-auto.rbl.ms/runner%2Fround_door_silent-%25281%2529.mp4)Benjie Holson

I think this is very close to state of the art (or maybe it has happened and I didn’t see it). I expect this medal to be claimed by December.

### Silver Medal: Entering a lever-handle self-closing push door

[  Your browser does not support the video tag. ](https://roar-assets-auto.rbl.ms/runner%2Fpush_selfclose_silent.mp4)Benjie Holson

Adding self-closing makes this significantly more challenging because of the force involved, though the lever handle is arguably easier (I just don’t see many round-knob self-closing doors).[6](https://spectrum.ieee.org/feeds/topic/robotics.rss#note6)

### Gold Medal: Entering a lever-handle self-closing pull door

[  Your browser does not support the video tag. ](https://roar-assets-auto.rbl.ms/runner%2Fpull_selfclose_silent.mp4)Benjie Holson

The boss fight of doors.[7](https://spectrum.ieee.org/feeds/topic/robotics.rss#note7) You need to either use a second limb to block the door from re-closing, or go through the door fast enough to use dynamics.

Event 2: Laundry
----------------

We’re just getting started on laundry.

### Bronze Medal: Fold an inside-out T-shirt

[  Your browser does not support the video tag. ](https://roar-assets-auto.rbl.ms/runner%2Ftshirt_silent.mp4)Benjie Holson

This is probably doable using the techniques we have now, but it’s a longer horizon task and might require some tricky two-handed actions to pull the shirt through to right-side-out.[8](https://spectrum.ieee.org/feeds/topic/robotics.rss#note8)

### Silver Medal: Turn a sock inside-out

[  Your browser does not support the video tag. ](https://roar-assets-auto.rbl.ms/runner%2Freverse_sock_silent.mp4)Benjie Holson

I think both the hand-insertion and the action of pinching the inside of the sock are interesting new challenges.

### Gold Medal: Hang a men’s dress-shirt

[  Your browser does not support the video tag. ](https://roar-assets-auto.rbl.ms/runner%2Fdress_shirt_silent.mp4)Benjie Holson

The size medium shirt starts unbuttoned with one sleeve inside-out. It must end up on the hanger correctly with the sleeve fixed and at least one button buttoned. I think this one is 3-10 years out, both because buttons are really hard and because getting a strong, dexterous hand small enough to fit into a sleeve is going to be hard.

Event 3: Tools
--------------

Humans are creatures of technology and, as useful as our hands are, we mostly use them to hold and manipulate tools. This challenge is about building the strength and dexterity to use basic tools.

### Bronze Medal: Window cleaner and paper towels

[  Your browser does not support the video tag. ](https://roar-assets-auto.rbl.ms/runner%2Fwindex_silent.mp4)Benjie Holson

The window cleaning fluid bottle is super forgiving in terms of how you grasp it, but you do need to independently articulate a finger, and the finger has to be pretty strong to get fluid to spray out.[9](https://spectrum.ieee.org/feeds/topic/robotics.rss#note9)

### Silver Medal: Peanut butter sandwiches

[  Your browser does not support the video tag. ](https://roar-assets-auto.rbl.ms/runner%2Fsandwich.mp4)Benjie Holson

The challenge here is to pick up a knife and then adjust the grasp to be strong and stable enough to scoop and spread the peanut butter. Humans use a ‘strong tool grasp’ for all kinds of activities, but it’s very challenging for robot grippers.[10](https://spectrum.ieee.org/feeds/topic/robotics.rss#note1)

### Gold Medal: Use a key

[  Your browser does not support the video tag. ](https://roar-assets-auto.rbl.ms/runner%2Fkeys_silent.mp4)Benjie Holson

A keyring with at least 2 keys and a keychain is dropped into the robot’s waiting palm/gripper*. Without putting the keys down,* get the correct key aligned and inserted and turned in a lock. This requires very challenging in-hand manipulation, along with high precision forceful interaction.

Event 4: Fingertip Manipulation
-------------------------------

We humans do all kinds of in-hand manipulation using the structure of our hands to manipulate things that we are holding.

### Bronze Medal: Roll matched socks

[  Your browser does not support the video tag. ](https://roar-assets-auto.rbl.ms/runner%2Froll_socks_silent.mp4)Benjie Holson

Requires dexterity and precision, but not very much force.

### Silver Medal: Use a dog poop bag

[  Your browser does not support the video tag. ](https://roar-assets-auto.rbl.ms/runner%2Fmock_poo_silent.mp4)Benjie Holson

When I use a dog-bag I have to do a slide-between-the-fingertips action to separate the opening of the bag which is a tricky forceful interaction as well as a motion that I’m not even sure most robot hands are capable of. Also tricky is tearing off a single bag rather than pulling a big long spool out of the holder, if you choose to use one.[11](https://spectrum.ieee.org/feeds/topic/robotics.rss#note1)

### Gold Medal: Peel an orange

[  Your browser does not support the video tag. ](https://roar-assets-auto.rbl.ms/runner%2Forange_silent.mp4)Benjie Holson

Done without external tools. This is super tricky: high force yet high precision fingertip actions.

Event 5: Wet Manipulation
-------------------------

If you sit down and write out what you might want a robot to do for you, a lot of tasks end up being kind of wet. Robots usually don’t like being wet, but we’ll have to change that if we want to have them clean for us. And wet things can be difficult to grasp and use.

### Bronze Medal: Wipe a counter-top with a sponge

[  Your browser does not support the video tag. ](https://roar-assets-auto.rbl.ms/runner%2Fsponge_silent.mp4)Benjie Holson

Mildly damp, but with exciting risk of getting the whole hand in the water if you aren’t careful. Probably requires at least splash resistant hands (or a whole bunch of spares).

### Silver Medal: Clean peanut butter off your manipulator

[  Your browser does not support the video tag. ](https://roar-assets-auto.rbl.ms/runner%2Fpeanutbutter_silent.mp4)Benjie Holson

This one naturally follows after the sandwich one. Water everywhere. Seems like an important skill to have after a few hours collecting training data on the dog-poop task.

### Gold Medal: Use a sponge to wash grease off a pan in a sink

[  Your browser does not support the video tag. ](https://roar-assets-auto.rbl.ms/runner%2Fpan_silent.mp4)Benjie Holson

Water, soap, grease, and an unpleasant task no one wants to do.

Terms and Conditions
--------------------

To be eligible to win, a general purpose manipulator robot running autonomously must demonstrate successful task completion in a real-time video with no cuts. You are allowed a maximum of 10x the time I took to do each task (a 4 second task can take your robot up to 40 seconds). I reserve the right to be arbitrary in deciding if things aren’t following in the spirit of the challenge. First robot to achieve this wins the prize!

To claim your medallion email [bmholson+olympics@gmail.com](mailto:bmholson+olympics@gmail.com) with an address for me to ship it to. If you give me a photo of your robot wearing a medal I will be tickled pink. I will also accept future challengers that are at least 25% faster than the current winner. Some medals have already been claimed; you can see the winning videos [here](https://generalrobots.substack.com/p/benjies-humanoid-olympic-games). Good luck and may the odds be ever in your favor.

Thanks to [Jeff Bingham](https://www.linkedin.com/in/jeffrey-bingham-aab292122/) for advice, fact checking and cool robot videos. And thanks to my patient wife for spending an hour filming me doing silly things in a silly costume.

##### Notes

1 As far as I can tell, kickboxing was just the [Unitree mini-humanoid robot](https://robotsguide.com/robots/unitree-g1), and everyone had the same code running, so… I guess it won?

2 TRI has some [pretty cool stuff](https://medium.com/toyotaresearch/tris-robots-learn-new-skills-in-an-afternoon-here-s-how-2c30b1a8c573) with force control using a big training rig.

3 Tesla’s Optimus has 22 degrees of freedom using cable drives (cause you can’t fit those motors in a hand). In 2008 I worked on [this robot](https://www.google.com/search?sca_esv=40416cf4ac9e8052&udm=7&q=anybots+monty&sa=X&ved=2ahUKEwjuwvuU27uPAxVSH0QIHbJdEP8Q8ccDKAR6BAgYEAY&biw=1415&bih=1059&dpr=2#fpstate=ive&ip=1&vld=cid:41ab6a35,vid:pdEuFhJit0o,st:0) which also had 22 degrees of freedom and controlling it was crazy hard (as was keeping all the cables correctly tensioned). The other hand was a big two-finger gripper which I ended up using for most teleop tasks.

4 Meta has been working with some [in-finger vision systems](https://www.youtube.com/watch?v=eyUZX-lCj4M) which seem cool.

5 This is likely more a teleoperation precision limitation than a model limitation. [Here is a video](https://www.youtube.com/watch?v=1sZ2c2EMNcg) of Generalist Robotics doing sub-cm precision tasks. I love that hockey sticks have become the traditional “mess with a robot” tool even for ridiculous things like this.

6 Yes, I did wear this at my workplace in order to get this video. You’re welcome.

7 I have programmed (not trained) a general purpose mobile manipulator to pass through a self-close pull door, but it took over 4 minutes (disqualified for taking too long) and required a special doorstop. Also the video isn’t public (also disqualified). Also it’s really tacky to put up a competition and award yourself gold before it even starts.

8 T-shirt starts fully inside-out in a wad. Finishes tolerably folded, right-side out.

9 You must spray 3 good spritzes on the window, and wipe them up with paper towels so there are no ugly streaks. Paper towels start on the paper-towel roll, not pre-torn and pre-wadded.

10 Peanut butter jar starts and ends closed. Sandwich should be cut in half. (Triangle or rectangular cuts are both acceptable, though your three-year-old might disagree).

11 Mock poo allowed. Bag starts on the roll but can be in a standard dog-bag holder, held by the robot.

*This post originally appeared on [General Robots](https://generalrobots.substack.com/p/benjies-humanoid-olympic-games), Benjie Holson’s Substack about making a general purpose robot company.*
