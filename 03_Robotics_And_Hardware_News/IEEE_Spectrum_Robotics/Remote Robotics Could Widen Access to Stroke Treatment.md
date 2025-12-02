# Remote Robotics Could Widen Access to Stroke Treatment

**출처:** [IEEE_Spectrum_Robotics](https://spectrum.ieee.org/remote-robotic-stroke-treatment-evt)

## 요약
![](https://spectrum.ieee.org/media-library/dr-vitor-pereira-remotely-performing-a-surgical-procedure-using-remedy-robotics-n1-system.jpg?id=62225319&width=1200&height=800&coordinates=56%2C0%2C56%2C0)  
  

When treating strokes, every second counts. But for patients in remote areas, it may take hours to receive treatment.

The standard treatment for a common type of stroke, caused by large clots interrupting blood flow to the brain, is a procedure called endovascular thrombectomy, or EVT. During the procedure, an experienced surgeon pilots catheters through blood vessels to the blockage, accessed through a major channel such as the femoral artery in the groin. This is typically aided by X-ray imaging, which shows the position of blood vessels.

“Good outcomes are directly associated with early treatment,” says [Cameron Williams](https://findanexpert.unimelb.edu.au/profile/821474-cameron-williams), a neurologist at the University of Melbourne and fellow with the Australian Stroke Alliance. In fact, “time is brain” is [a common refrain](https://www.ahajournals.org/doi/10.1161/01.str.0000196957.55928.ab) in stroke treatment. While blood flow is stopped, about 2 million neurons die each minute. Over an hour, that adds up to 3.6 years of typical age-related brain cell loss.

But in remote places like Darwin, in the north of Australia, this treatment isn’t available. Instead, it could take 6 hours or more and an expensive aeromedical transfer to get a patient to a medical center, says Williams. There are similar geographical challenges to stroke treatment access all over the world. Sparing a rural patient hours of transfer time to a hospital with an on-site expert could save their life, prevent disability, or preserve years of their quality of life.

That’s why there is a particular interest in the possibility of emergency stroke treatment [performed remotely](https://spectrum.ieee.org/telemedicine-and-surgery) with the help of robotics. Machines placed in smaller population centers could connect patients to expert surgeons miles away, and shave hours off of time to treatment. Two companies have recently demonstrated their remote capabilities. In September, doctors in Toronto completed a series of increasingly distant brain angiograms, the X-ray imaging element of an EVT, eventually performing two angiograms between crosstown hospitals using the N1 system from [Remedy Robotics](https://www.remedyrobotics.com/). And in October, [Sentante](https://sentante.com/) equipment facilitated a simulated EVT between a surgeon in Jacksonville, Fla., and a cadaver with artificial blood flow in Dundee, Scotland.

“All those stories connected is not only proof of concept. It’s coming to realization and implementation that robotic and remote interventions can be performed, and soon will be the reality for many centers in rural areas,” says [Vitor Pereira](https://unityhealth.to/physician-directory/dr-vitor-mendes-pereira/), a neurosurgeon at Unity Health who performed the Toronto procedures.

Two Approaches to Remote EVT
----------------------------

One challenge of performing these remote procedures is maintaining strong, fast connections at large distances. “Is there a real life need to do this transatlantically? Probably not,” says [Edvardas Satkauskas](https://sentante.com/#tm), CEO of Sentante. “It demonstrates the capabilities. Even this distance is feasible.” Although performing a procedure remotely introduces issues related to latency, the pace of EVT—while urgent—is not reliant on instant reactions, says Satkauskas.

Redundant connections should also be an important safeguard for dropped connections. Remedy has taken measures, for instance, to ensure that its robot monitors connection quality, and doesn’t make any harmful movements due to a poor connection, says [David Bell](https://www.linkedin.com/in/david-bell-rr), the company’s CEO.

Though both companies are careful about disclosing details of products and research that are still in development, there are notable differences between their approaches.

“Our device leans heavily on artificial intelligence,” says Bell. Machine learning is incorporated into how the Remedy device manipulates guide wires and creates an informational overlay atop X-ray images for remote physicians, who can control the robot with a laptop and software interface. The long-term goal is for a surgeon to be able to log on to Remedy software at short notice from a central location to interact with Remedy robots in multiple hospitals as needed.

In contrast, Sentante uses a control console meant to look and feel like the catheters and guide wires that surgeons are accustomed to manipulating in manual EVT, including force feedback that mimics the resistance they would feel in person.

“It’s very intuitive to use this,” says [Ricardo Hanel](https://www.baptistjax.com/doctors/neurosurgeon/dr-ricardo-hanel-md), a neurosurgeon with Baptist Health in Jacksonville, who was on the piloting end of the Sentante demonstration. Naturalistic feeling in the transatlantic procedure came with reported latency of around 120 milliseconds. Hanel is also on Sentante’s medical advisory board.

Sentante has not yet implemented AI-assisted movements of its robot, though a plan is in place to capture as much training data as possible, both from images and force measurements. “As we joke, we had to build a sophisticated piece of hardware to become a software company,” says CEO Satkauskas.

The Path to Clinical Use
------------------------

Hanel expressed optimism that any control system would be easily learned by surgeons.

“I think the main limitation for robotics is that you are still dependent on bedside interventionists,” says [Ahmet Gunkan](https://radiology.medicine.arizona.edu/profile/ahmet-gunkan-md), an interventional radiologist at the University of Arizona, who has written about [robots and endovascular interventions](https://link.springer.com/article/10.1007/s10143-024-03155-9).

Depending on the system, these bedside assistants might be responsible for a variety of tasks related to preparing and communicating with the patient, sterilizing and preparing equipment, loading step-specific parts, and repositioning X-ray or robotic equipment. Both CEOs note that while proper training will be essential, there are ways to reduce the burden on health care providers at the patient site.

In the case of remote operations, “it was important to us that the robot [could do the entire thing](https://spectrum.ieee.org/star-autonomous-surgical-robot),” says Bell. Remedy’s system has been designed to handle as much of the procedure as possible, and streamline moments when bedside human interaction is necessary. For example, even since the older version used in Toronto, changes have been made to maintain a clean line of communication between bedside and remote clinicians, facilitated by the Remedy system, says Bell.

![A neurovascular surgical team carefully monitors a procedure in an operating room.](https://spectrum.ieee.org/media-library/a-neurovascular-surgical-team-carefully-monitors-a-procedure-in-an-operating-room.jpg?id=62225325&width=980) A team at St. Michael’s Hospital in Toronto performs, for the world’s first time, a robot-assisted neurovascular procedure remotely over a network, on 28 August 2025. Katie Cooper and Kevin Van Paassen/Unity Health Toronto

Though remote EVT is a high priority, systems capable of the procedure may first be approved for [other endovascular procedures](https://spectrum.ieee.org/fiber-optic-probe) performed locally. The hope is that precision robotics leads to better patient outcomes, whether the surgeon is in the next room or the next county.

Remedy has a clinical trial planned in 2026 for on-premise neurointerventions, and has partnered with the [Australian Stroke Alliance](https://www.remedyrobotics.com/articles/remedy-asa-partnership) to distribute its N1 system and conduct a future clinical trial for remote procedures. Eventually the robot could be used to treat as many as 30 different conditions, says Bell.

Satkauskas views Sentante’s equipment as a flexible platform for endovascular procedures throughout the body, which could help keep bedside clinicians familiar with the device. The system may go to market in the EU next year for peripheral vascular interventions, which restore blood flow to the limbs, and it has a [breakthrough device designation](https://sentante.com/sentante-stroke-system-receives-fda-breakthrough-device-designation/) from the U.S. FDA for remote stroke treatment.

There are other players in the space. For example, an early telerobotic effort from a company called Corindus is [still ongoing](https://www.fiercebiotech.com/medtech/stryker-siemens-healthineers-team-develop-stroke-treating-robot) after the company’s acquisition by Siemens in 2019. And Pereira notes that [Xcath](https://xcath.com/about.html) has also demonstrated a [long-distance simulated EVT](https://neuronewsinternational.com/xcath-successfully-performs-first-public-telerobotic-mechanical-thrombectomy-demonstration/) and looks to perform local robotic EVT with live patients soon.

“I think it’s an exciting time to be a neurointerventionalist,” says Hanel.
