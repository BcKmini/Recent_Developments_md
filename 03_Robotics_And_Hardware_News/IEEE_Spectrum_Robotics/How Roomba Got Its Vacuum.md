# How Roomba Got Its Vacuum

**출처:** [IEEE_Spectrum_Robotics](https://spectrum.ieee.org/irobot-roomba-history)

## 요약
![](https://spectrum.ieee.org/media-library/roomba-vacuum-signed-by-irobot-team-showing-control-buttons-on-wooden-floor.jpg?id=61715049&width=1200&height=600&coordinates=0%2C365%2C0%2C365)  
  

Adapted from [*Dancing With Roomba*](https://dancingwithroomba.com/), written by Joe Jones, who was iRobot’s first full-time employee and the original designer of the Roomba robot vacuum.

*After developing a prototype robot that was effective at cleaning both hard floors and carpets using a relatively simple* [**carpet-sweeping mechanism**](https://en.wikipedia.org/wiki/Carpet_sweeper)*, iRobot vice president Winston Tao and the iRobot marketing team have organized a focus group so that Roomba’s engineers can witness the reaction of potential first customers.*

**One pleasant midsummer day** in 2001, Roomba’s engineers, Winston Tao, and several other iRobot folk rendezvoused at an unremarkable, multistory office building on the Cambridge side of the Charles River, across from Boston. We assembled in a narrow room. A long table occupied the room’s center. Snacks and sodas were set out along the back wall; the lighting was subdued. The dominant feature of this cramped chamber was a big one-way mirror occupying almost the entire front wall. Sitting at the table, one could see through the looking glass into a wonderland of market research on the other side. In that much larger, brightly lit room were comfortable chairs, an easel with a large pad of paper, and our hired facilitator. Although this was a familiar trope I’d seen a hundred times on TV, actually lurking in an observation room like this felt a touch surreal.

iRobot vs Focus Group
---------------------

We’d paid maybe US $10,000 for the privilege of setting up some focus groups—probably the most the company had ever spent on a market research event. But we needed to know how potential customers would react to our Roomba prototype when they saw one in the (plastic) flesh cleaning the floor at their feet. At the appointed hour, our facilitator welcomed eight to 10 bona fide ordinary people as they filed into the large room and sat in the chairs. Our mind-child was about to receive its first critical judgment from strangers.

aspect\_ratio![Book cover: Roomba with signatures and red dance shoes on wooden floor.](https://spectrum.ieee.org/media-library/book-cover-roomba-with-signatures-and-red-dance-shoes-on-wooden-floor.jpg?id=61715094&width=980)This article was adapted from the author’s new book, [Dancing with Roomba: Cracking the Robot Riddle and Building an Icon](https://www.routledge.com/Dancing-with-Roomba-Cracking-the-Robot-Riddle-and-Building-an-Icon/Jones/p/book/9781032890616) (Routledge 2025).Joe Jones

The facilitator prepared participants by encouraging them to state their honest views and not to be swayed by the comments of others. “You are the world’s expert in your own opinion,” she told them.

At first the facilitator described Roomba without showing the group any photos or the device itself. She was met with skepticism that such a thing would actually work. Then she demonstrated one of the prototypes we had prepared for the event. As participants watched Roomba go about its business on both carpets and hard floors, their doubts ebbed. Even those who stated that they would never purchase such a device couldn’t help being intrigued. As the group discussion proceeded, soccer moms (representing “early mass-market adopters”) emerged as the most interested. They saw Roomba as a time-saver. This surprised and pleased us, as we’d expected the much smaller market of gadget geeks would be the first to fall in love.

![Transparent blue Roomba vacuum on wooden floor near a doorway.](https://spectrum.ieee.org/media-library/transparent-blue-roomba-vacuum-on-wooden-floor-near-a-doorway.jpg?id=61715051&width=980)iRobot built about 20 of its third major Roomba prototype, the T100, all with 3D-printed shells.Joe Jones

But we could take neither interest nor love to the bank. We needed to know how much customers would pay. Our facilitator eased into that part of the gathering’s proceedings. She did not inquire directly but rather asked, “If you saw this product in a store, what would you expect the price to be?”

The focus group’s responses were all over the map. Some people mentioned a price close to the $200 we intended to charge. A few folks we regarded as saints-in-training expected an even higher number. But most were lower. One woman said she’d expect Roomba to be priced at $25. Later when asked what she thought a replacement battery might cost, she said, “$50.” That hurt. For this lady, attaching our robot to a battery devalued the battery.

Floor Cleaner or Robot?
-----------------------

Throughout the proceedings our facilitator had been careful to leave a couple of things unmentioned. First, she never referred to Roomba as a robot, calling it instead an “automatic floor cleaner.” Three separate groups, comprising an aggregate of around two dozen people, gave their opinions that day. Of these, only two individuals spontaneously applied the term “robot” to Roomba.

The second unmentioned characteristic was the nature of Roomba’s cleaning mechanism. That is, the facilitator had revealed no details about how it worked. Participants had seen the demo, they observed Roomba cleaning effectively, they had given their opinion about the price. They’d all assumed that a vacuum was at work, several used that term to refer to the robot. But now the facilitator told them, “Roomba is a carpet sweeper, not a vacuum.” Then she asked again what they would expect to pay. On average, focus-group members from all three groups cut their estimates in half. Participants who had previously said $200 now said $100.

The focus group’s brutal revaluation exploded our world. The enabling innovation that made the energy budget work, that made Roomba technically and economically feasible, was cleaning with a carpet sweeper rather than a vacuum. People had seen that the carpet-sweeper-Roomba really did work. Yet they chose to trust conventional wisdom about vacuums versus carpet sweepers rather than their own apparently lying eyes. If we were forced to cut the robot’s price in half, we would lose money on every unit sold, and there would be no Roomba.

At the end of the evening, before any member of our stunned team could stagger out the door, Winston said simply, “Roomba has to have a vacuum.” A shotgun wedding was in the offing for bot and vac.

![Round white robot with cartoon puppy sticker, named "Scamp," on a desk.](https://spectrum.ieee.org/media-library/round-white-robot-with-cartoon-puppy-sticker-named-scamp-on-a-desk.jpg?id=61715054&width=980)Scamp, the earliest Roomba prototype, was built in 1999.Joe Jones

The next day at work we gathered to discuss the focus group’s revelation. A half-hearted attempt or two to deny reality quickly faded—electrical engineer Chris Casey saw to that—and we accepted what we needed to do. But changing things now would be a huge challenge in multiple ways. We were deep into development, closer to launch than kickoff. All the electrical power our battery could supply was already spoken for. None was available for a new system that would likely be more power hungry than all the robot’s other systems combined. And where could we put a vacuum? All the space in the robot was also fully assigned. Our mandate to clean under furniture and between chair legs wouldn’t let us make the robot any bigger.

Making Roomba a Vacuum
----------------------

One escape hatch beckoned, but no one was eager to leap through it. Chris articulated what we were all thinking. “We could build a vestigial vacuum,” he said. That is, we could design a tiny, pico-power vacuum—one that consumes almost no power and does almost nothing—strap it on the robot, and call it done. Perversely, that seemed reasonable. The robot already cleaned the floor well; our cleaning tests proved it. Customers, however, didn’t know that. They were all steeped in the dogma of vacuum supremacy. Reeducating the masses wasn’t possible—we didn’t have the funds. But if we could assert on the box that Roomba had a vacuum, then everyone would be satisfied. We could charge the price that makes our economics work. Customers would deem that cost reasonable and wouldn’t have to unlearn their vacuum bias.

But it felt wrong. If we must add a new system to the robot, we wanted it—like all the other systems—to earn its keep honestly, to do something useful. Through further discussion and calculation, we concluded that we could afford to devote about 10 percent of the robot’s 30-watt power budget to a vacuum. Conventional manual vacuums typically gorged themselves on 1,200 watts of power, but if we could develop a system that provided useful cleaning while consuming only 3 W (0.25 percent of 1,200) then we would feel good about adding it to the robot. It just didn’t seem very likely.

![Black and red Roomba vacuum on a gray carpet next to a plaid multicolored blanket.](https://spectrum.ieee.org/media-library/black-and-red-roomba-vacuum-on-a-gray-carpet-next-to-a-plaid-multicolored-blanket.jpg?id=61715075&width=980)iRobot built two identical second-generation Roomba prototypes, named Kipper and Tipper, one of which is shown here.Joe Jones

I sometimes find that solving a problem is largely a matter of staring at the problem’s source. Gaze long and intently enough at something and, Waldo-like, the solution may reveal itself. So I took one of the team’s manual vacuums and stared at it. What exactly made it use as much power as it did? I knew the answer was partly marketing rather than reality. There was no simple, objective way to compare cleaning efficacy between vacuums. Lacking a results-based method, shoppers looked at inputs. For example, a vacuum with a 10-ampere motor sounds as though it should clean better than a vacuum with a 6-amp motor. But the bigger number might only mean that the manufacturer with the 10-amp claim was using a less-efficient motor—the 6-amp (720-W) motor might clean just as well.

But even when you corrected for the amperage arms race, a vacuum was still a power glutton. Staring at the vacuum cleaner, I began to see why. The vacuum fixed in my gaze that day used the standard configuration: a cylindrical beater brush occupied the center of a wide air inlet. A motor, attached by a belt, spun the brush. Another motor, deeper in the machine, drove a centrifugal blower that drew air in through the inlet. To keep dirt particles kicked up by the beater brush entrained in the airstream, the air needed to move fast. The combination of a wide inlet and high velocity meant that every second the vacuum motor had to gulp a huge volume of air.

Accelerating all that air took considerable power—the physics was inescapable. If we wanted a vacuum that sipped power rather than guzzled it, we had to move a much smaller volume of air per second. We could accomplish that—without reducing air velocity—if, instead of a wide inlet, we used a narrow one. To match the manual vacuum’s air velocity using only a 3-W motor, I computed that we would need a narrow opening indeed: only a millimeter or two.

That instantly disqualified Roomba from using the standard vacuum configuration—we could not put our bristle brush in the middle of the air inlet. That would require an inlet maybe 20 times too wide. We’d have to find another arrangement.

A Micro Vacuum that Doesn’t Suck
--------------------------------

To test the narrow-inlet idea I turned to my favorite prototyping materials: cardboard and packing tape. Using these, I mocked up my idea. The inlet for my test vacuum was as long as Roomba’s brush but only about 2 millimeters wide. To provide suction I repurposed the blower from a defunct heat gun. Then I applied my jury-rigged contraption to crushed Cheerios and a variety of other dirt stand-ins. My novel vacuum was surprisingly effective at picking up small debris from a hard surface. Using an anemometer to measure the speed of the air rushing through my narrow inlet showed that it was, as desired, as fast as the airstream in a standard vacuum cleaner.

RELATED: [Roombas at the End of the World](https://spectrum.ieee.org/south-pole-roombas)

The next step was to somehow shoehorn our microvacuum into Roomba. To form the narrow inlet we used two parallel vanes of rubber. Small rubber bumps protruding from one vane spanned the inlet, preventing the vanes from collapsing together when vacuum was applied. We placed the air inlet parallel to and just behind the brush. The only plausible space for the vacuum [impeller](https://en.wikipedia.org/wiki/Impeller), motor, and filter (needed to separate the dirt from the flowing air) was to take over a corner of the dust cup. Drawing on his now well-honed skills of packing big things into tiny spaces where they had no business fitting, mechanical engineer Eliot Mack managed somehow to accomplish this. But we did get help from an outside consultant to design the intricate shape the impeller needed to move air efficiently.

In general, regular vacuums perform better on carpet than on hard floors. But Roomba inverted that relationship. Our vacuum operated like a squeegee, pulling dirt from tile, linoleum, and wooden floors. But it was less effective on other surfaces. The sweeper mechanism did the heavy lifting when cleaning carpet.

![Silver and gray Roomba robotic vacuum on a hardwood floor.](https://spectrum.ieee.org/media-library/silver-and-gray-roomba-robotic-vacuum-on-a-hardwood-floor.jpg?id=61715088&width=980)iRobot released its first production version of the Roomba in September 2002.Joe Jones

Despite the team’s reluctance to add a vacuum and despite the unit’s low power, the vacuum genuinely improved Roomba’s cleaning ability. We could demonstrate this convincingly. First, we disabled Roomba’s new vacuum by disconnecting the power and then cleaned a hard floor relying only on the carpet-sweeper mechanism. If we then walked across the floor barefoot, we would feel a certain amount of grit underfoot. If we repeated the exercise with vacuum power on, the floor was pristine. Bare feet would detect no grit whatsoever.

![Seven people pose in front of shelves displaying awards and a gold iRobot Roomba; casual attire.](https://spectrum.ieee.org/media-library/seven-people-pose-in-front-of-shelves-displaying-awards-and-a-gold-irobot-roomba-casual-attire.jpg?id=61715091&width=980)The Roomba contributors present on the occasion of the 500,000th Roomba include Steve Hickey, Eliot Mack [front row], Paul Sandin, Chris Casey, Phil Mass, Joe Jones, and Jeff Ostaszewski [back row].Joe Jones

Years later I learned that the focus group had a back story no one mentioned at the time. While the Roomba team had swallowed the carpet-sweeper concept hook, line, and sinker, Winston had not. He was uneasy with the notion that customers would be cleaning-mechanism agnostic—thinking instead that they simply wouldn’t believe our robot would clean their floors if it didn’t have a vacuum. He found at least indirect support for that position when he scoured marketing data from our earlier collaboration with SC Johnson.

But Winston, well-attuned to the engineering psyche, knew he couldn’t just declare, “Roomba has to have a vacuum.” We’d have pushed back, probably saying something like, “What your business-school-addled brain doesn’t appreciate is that it’s the carpet sweeper that makes the whole concept work!” Winston had to show us. That was a key purpose of the focus group, to demonstrate to the Roomba team that we had made a deal-breaking omission.

**Dancing With Roomba** [is now available for preorder](https://www.routledge.com/Dancing-with-Roomba-Cracking-the-Robot-Riddle-and-Building-an-Icon/Jones/p/book/9781032890616).
