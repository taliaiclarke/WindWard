# WindWard
This is the repository for WindWard, an innovative sailing technology designed to simplify data interpretation for sailors.




WindWard

Problem Overview 
Growing up sailing I learned quickly how much knowledge it takes to sail and race boats. The process of sailing is extremely complicated as it takes in depth knowledge of many variables. These variables are constantly changing and hard to predict for novices. The difference between boats that win in races and boats that lose come down to small decisions that without years of practice and learning are difficult to obtain. 

Many sailboats have technology on them to help sailors understand the variables around them better. These devices display in depth information about tides, underwater landscapes affecting drift, wind direction, wind type, wave direction and course maps. All of these variables get combined into a device called a digital chart. While sailing has remained a mostly unchanged practice overtime the introduction of digital charts into the sport has had a great effect. They allow the sailors to be more intune with their surroundings and have a better understanding of changing variables. As sailors are more informed they make better decisions. Good decisions compound on eachother during races and become the determining factor in winning. Even with good wind, tides and waves a sailboat that makes bad choices stands no chance for first place. 

While these charts have been mostly helpful they, like the sport, are extremely complicated to understand. Take for example this chart featured by Yachting Monthly. Even for an expert digitals charts are difficult to read and get the right information needed for split second decisions. There is too much noise created when presenting this data to a beginner sailor. Tools like this digital map become more of a hindrance than a help.

Task Analysis and Human Factors Alignment 
 A piece of technology is needed to display a simplified version of  current digital charts and that only includes necessary information. This information needs to be shown in a highly user friendly way so that there is a small learning curve to using the device and reading the data. This design needs to be a more user friendly version of pre-existing digital chart maps. One important thing to take into consideration is the efficiency of the data, and only the basic data points should be included. Following the 80/20 rule, I will include the 20% of data that the user uses 80% of the time. This will help simplify the design and enhance the usability. By being a simpler design it will also be quicker to use when sailing. This aspect is important because the time a user spends looking at the device is time they are not looking at the water for other boats and obstacles. This relates to the safety of the user as a simpler design is a safer design in this case.  This device also makes it safer to sail by keeping them up to date on their surrounding conditions. This device will show small craft warnings, incoming high winds and other environmental factors that could be dangerous. This design also is satisfying for the user as a simple design can be mastered quickly.  Wanting to obtain mastery overskills is a key source of human motivation as mastering a skill is a highly satisfactory achievement (NeuroLaunch).

To observe the user objectively I will view how the user uses the product. From here I would note their language when talking about their experience using the device, taking note of what they say and how they say statements. Here I am observing what they do, think and believe. I would also note their actions and activities. Here I would note what they do, how they use the product and how they behave with the product. This information is crucial to understanding points of confusion for users. Correcting common points of confusion is vital. At this point I would also remember the HCI phrase,‘don’t blame the user’. This means instead of trying to correct the users actions I would correct the design to be inline with user intuition and preconceived expectations. A general plan for observing includes determining what I want to research and focus on. Then find participants that match my target demographic. Here I would want the widest possible range of uses and make sure to include users with visual impairments. After I would test the users on the product, record the data and analyze for the changes needed to my design. 

Human-Tech Ladder: 
Physical: When designing this product I have taken into account its physical attributes. This device was created with easy mounting in mind as it has two ways to connect it to the boat. This design aspect shows how I accounted for the physical constraints that exist when sailing. I also took into account the physical conditions that one would be using this device in. I prioritized large bold fonts that could be easily seen in harsh weather conditions.

Psychological: By following the 80/20 rule I focused on including essential data points only. This was done to not overwhelm the sailor. By including only the top 20 most needed data points I have reduced the cognitive load on the sailor allowing them to focus on sailing and not waste time trying to understand the chart. A tradeoff here is that there is not all necessary information shown, only the top 80% most commonly used. This means that there are still some key data points that could be needed that are missing. 

Team: Sailing is rarely an individual sport, with most types of races and outing being a team activity. This type of device helps to facilitate communication and understanding of current events between team members. By having real time data shared between people this can reduce the amount of miscommunications by promoting a common understanding. It also helps teams of sailors organize quickly to take advantage of current tacks and wind information.

Organizational: For organized racing teams and sailing organizations having a device that is uniform across boats and fleets is key. This reduces the learning curve, as there is a standardized device between all boats and no need to learn new systems for different boats. It ensures that complex sailing data is always organized for sailors.

Political: This device was built with accessibility in mind, especially for those who are visually impaired. As many sailors are elderly they can struggle with vision impairments. This device allows them to be a contributing member of the sailing team for as long as possible. This device is inline with larger political movements that promote emerging technology to have accessible features taken into account from early design stages. One trade off here is that large bulky fonts conflict with the sleek minimalist design idea I originally had.

Proposed Design
To start this process I went to the whiteboard to lay out all my ideas, possible types of data, plan of action and the physical prototype. I was very inspired by my grandfather, a lifelong sailor, when creating this design. One thing he had one his boat that he uses to fill this technological gap is an etch a sketch. He was able to convey the important information and ideas to others on the boat and write down stats and numbers needed for later. This device was the original inspiration for what I wanted my new product to do, display only the most important data points and do so clearly.

My first step in the sketching process was to determine all of the data parts and components I wanted to be included. After editing the list for what I wanted to keep, add or scratch I ended up with two features. The first feature ‘Basic’ would have data in it such as wind direction, wind strength, heading, tides and temperature. These are all the most basic information needed when sailing. There is also a second feature to be used when racing called ‘Race’. This would have the course, current position, start clock countdown, position and life favor.

After I decided the content I wanted I needed to figure out how to organize this. One main constraint when figuring out the layout is how large the physical device will be. To get a better understanding of this constraint I built a mock version. The inspiration for the shape and function come from my grandfather's etch a sketch which had velcro on the back to attach to the boat. My new device would have that as well as slots for velcroing it around a mast on smaller boats. 

Once I could visualize the physical components of this deceive I started to lay out the data. I was inspired by medical devices. They face some of the same issues I had with trying to display a lot of numerical data that needs to be distinct from each other and clear upon first glance. To start my initial designs I took inspiration for blood pressure and heart monitor machines. One thing they all had in common was bold legible fonts and the use of color to help differentiate data. 

I practiced laying out data for my prototype. I adjusted based on viability. I tried my best to recreate the conditions when sailing by squirting at the device, viewing from far away, viewing from strange angels, and viewing at the device while light is in my eye. This helped me think about how I wanted the data organized. One thing I noticed was how important separation of the data was to finding values quickly. 

Python Prototype Implementation 
In the python implementation I used input handling by creating simulated data which can be seen in the boat1 instance. (boat1 = basic("NW", "17.2 kn", "18.1 - 19.2 kn", "Close-Reach", "Low : 4.59 ft", "45.5 F", "34 F")). The implementation then returns feedback to the user in the form of  two graphs. The upper graphs contain the heading directions and the heading map. The bottom graphic has all the other data points. This was done to help separate features and keep their groups distinct. 

The python print out includes  the basic features to be displayed. One thing I focused on here was readability for the user. I made sure to have high contrasts between my background and the text. The contrast ratios for my colors are extremely high in hopes of aiding all types of sailors especially elderly ones with lower vision. This type of accessibility is very important as even sailors without vision issues face conditions that impair their ability to see such as strong winds, rain, and sun.  

Color Contrast Ratios: 
Red Text to Background: 7.93:1 
Blue Text to Background:  13.59:1 
Green Text to Background : 8.93:1
Black Text to Background: 21.00:1

All the colors used have a significantly higher ratio than what is commonly required, 4.5:1. Another way I made this interface accessible is to separate information for viewers who are color blind. This physical separation will help to differentiate data types for users who are color blind. This helps the user to quickly find the point they are looking for. I also used shape to help guide the viewer's eyes. One of the most important data points on this visualization is what tack the boat is on. This is important as the tack determines which boat has right of way over other boats. By adding a background and changing the shape regarding this data point the eye is more drawn to this point than the other uniform data displays. This is key as this data point, tack, is something that needs to be known quickly in a race. The tack often determines who wins in a race and keeps collisions from happening. 


Works Cited
Fortescue, Sam. “How to choose the right digital charts for your sailing.” Yachting Monthly, 2021, https://www.yachtingmonthly.com/gear/how-to-choose-the-right-digital-charts-for-your-sailing-76535.
Green, Debbie. “What Does The Sailing Word Tack Mean?” Travel With The Greens, November 2024, https://travelwiththegreens.com/what-does-the-sailing-word-tack-mean.html.
NeuroLaunch. “Mastery Motivation: Definition, Components, and Impact on Learning.” NeuroLaunch, 2024, https://neurolaunch.com/mastery-motivation-definition/.
Oxford Reference. “Oxford Reference.” Oxford Reference, https://www.oxfordreference.com/display/10.1093/oi/authority.20110803095823167.

