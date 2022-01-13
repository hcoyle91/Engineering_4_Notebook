# Engineering_4_Notebook
### Top

## Table of Contents

* [Python_Dice_Roller](#PythonDiceRoller)
* [Python_Calculator](#Python_Calculator)
* [Quadratic Solver](#Quadratic_Solver)
* [String and Loops](#String_and_Loops)
* [Hangman Game](#Hangman_Game)
* [Swing Arm](#Swing_Arm)
* [Skateboard](#Skateboard)
* [Lego Duck](#Lego_Duck)
* [Blinking LED](https://github.com/hcoyle91/Engineering_4_Notebook/blob/main/README.md#blinking-led)
* [Rasberry Pi Safe Shutdown](https://github.com/hcoyle91/Engineering_4_Notebook/blob/main/README.md#rasberry-pi-safe-shutdown)
* [Accelerometer With display](https://github.com/hcoyle91/Engineering_4_Notebook/blob/main/README.md#accelerometer-with-display)

## Python_Dice_Roller
* [Back to the top](#Top)
### Assignment Description

The purpose of this assignment was to create a program that can automatically roll dice. The program also took user input to decide whether another dice should be rolled, or if the program should exit. The spicy version added complexity by asking the user to specify the number of sides on the dice and the number of dice to be rolled at a time. The user was then asked whether they wanted to roll again with the same settings, change the settings, or exit the program. 

### Evidence 

[Dice roller code](https://github.com/hcoyle91/Engineering_4_Notebook/blob/651558c1388b116f6b990f86defce5e58e8503f5/dice_roller.py)

Vanilla version:

![Screenshot 2021-09-10 3 15 26 PM](https://user-images.githubusercontent.com/89222808/133513775-a3eafb43-f836-4e4f-8aa6-e28ca584901f.png)

Spicy version:

![Screenshot 2021-09-10 3 18 38 PM](https://user-images.githubusercontent.com/89222808/133513750-727cdb6c-1c27-4c8a-83d4-50ea9136a221.png)

### Wiring

N/A

### Reflection

This assignment was relatively simple, but was challenging because I had not coded in Python for several months. I learned that I could import parts of toolboxes without importing the entire thing, but that changes the syntax of how I call the function later. I also learned about using a while loop to control whether a user wants to exit the program. For the spicy version, I needed to use nested loops. Python determines what is inside a loop by the indent level of each line of text, rather than brackets like some other coding styles. That means I need to be really careful with my tabs!


## Python_Calculator
* [Back to the top](#Top)
### Assignment Description
For this assignment I had to prompt the user for two integers as inputs and give the user the sum, quotient, difference, and modulo of those two numbers. However I had to use a function to do this. 

### Evidence 

[Calculator code](https://github.com/hcoyle91/Engineering_4_Notebook/blob/f3f58cea85cc076b055f1b8116edd3728a5aaac2/Caclulator.py)

![calculator](https://user-images.githubusercontent.com/56696954/133629581-2fd6e22a-339d-410e-9cea-f26c9e717492.png)

### Wiring
N/A

### Reflection

This was a benficial assignment because I learned how to use functions and realised what I can do with them. At first it was very confuysing looking at how to use function but now I understand that they take in variables and you have to use 'return' inside the function in order to output values.


## Quadratic_Solver
* [Back to the top](#Top)
### Assignment_Description

For this assignment I had to make a program that prompted the user for 3 inputs and printed two roots if ithe function had two roots or 1 root if the function had one root or no roots if the function had no roots. I had to offer an option to run the program again and I had to code all this using a function.

### Evidence

![Quadratic Solver code link](https://github.com/hcoyle91/Engineering_4_Notebook/blob/7da46dbfb64fa784498be89d48edc14250971438/Quadratic%20Solver)

![Quadratic Solver](https://user-images.githubusercontent.com/56696954/134513839-b5a395ac-a990-4da3-b246-7ceafe3bb1ee.png)

### Wiring

N/A

### Reflection

This was a fun assignment overall. My main promblems included not reading the dirrections and figuring out a little more about functions. I started out with making a function identical to the one made in calulator assignment. But it turns out I needed to use if statements within the function. I also learned the length function which was very useful in determining how many roots there were using an array. Lastly, I didn't thoroughly read the dirrections so I did not see that the asssignment must include an option to solve again. Next time I will make sure to do this so I dont have to go back and change my code so much.


## String_and_Loops
* [Back to the top](#Top)
### Assignment_Description

For this assignment I had to make a program that takes in a phrase and outputs the letters on their own line with a dash instead of a space. 

### Evidence

![String and loops code link](https://github.com/hcoyle91/Engineering_4_Notebook/blob/46a77b3b627d3b2b35461f3899bb7ee713fd0a06/String%20and%20loops%20code)
![String and loops](https://user-images.githubusercontent.com/56696954/134517662-f8ac86db-58ed-404a-937e-e41469bd4929.png)

### Wiring

N/A

### Reflection

Although the for loop would have been easier, I used the while loop and an if statment to determine wether the computer should include a dash and not a space. I could have made it smaller by using a for loop or icluding functions on the same line.


## Hangman_Game
* [Back to the top](#Top)

### Assignment_Description

For this assignment I had to create a program that succesfully works as a hangman game for two players. It had to have everything that a normal hangman game has and use a visual representation of the body. 

### Evidence

[Hangman Code link](https://github.com/hcoyle91/Engineering_4_Notebook/blob/75dde71ef95aed83a23c6a8d0d55649973db8ee8/Hangman%20Code)

![Hangman Game](https://github.com/hcoyle91/Engineering_4_Notebook/blob/efadc078cb9588c23be128efe12fb4a166712d94/hangman%20code.png)

### Wiring

N/A

### Reflection

This assignment took me a while because of how messy my code was. It was hard to get help with it when I needed it because my code was so confusing. So, next time, I need to plan out my code better and put in a little extra work as to make it concise and clear and efficient. Also, this is my first python assignment that was not just one function but rather a long proccess. I learned that maybe seudo code would be very benficial to me.



## Swing_Arm

* [Back to the top](#Top)

### Assignment_Description
For this assignment I had to create a swing arm based off 3 drawings with some dimensions and constraints. In order to recieve full credit, I had to make sure there were to variables defining the length, angle, and diameter of the circle, that I could change. I then had to enter the mass for certain materials of my newly made swing arm.

### Evidence

Configuration #1:

![Configuration #1](https://github.com/hcoyle91/Engineering_4_Notebook/blob/574947b9f60208457454b733bb0110503a37fa34/Swing%20arm%20config%202.png)

Configuration #2:

![Configuration #2](https://github.com/hcoyle91/Engineering_4_Notebook/blob/21123c6febb82cfc39c4be0d5e7691560ae96086/swing%20arm%20config%201.png)

### Part Link

[Link to Swing arm on Onshape](https://cvilleschools.onshape.com/documents/53745f923252b197bcc4f511/w/bb4d42c4e0848b24960fa052/e/ce94cd0d490ef80f2a243cc9?renderMode=0&uiState=616ec74c5481d67049eccd3d)

### Reflection

This project was hard and time consuming. The drawings were precise but because I needed to make configurations, most things needed the right constraits rather than just mesurements. At first, when I finished and tried to change the configuratiojns, it completely messed up the entire swing arm. I had to go back and make sure everything was relative to each other. Another challange was that it was at sometimes hard to find how things were built based on just drawings because if I just got one thing wrong, the mass would be off.


## Skateboard
* [Back to the top](#Top)
### Assignment_Description
For this assignment I had to follow a CAD intro tutorial to build a skateboard. I had to have the correct mass at the end of building it and submit it on canvas.


### Evidence

![Skateboard #1](https://github.com/hcoyle91/Engineering_4_Notebook/blob/8addbc8bbe12d70ebb3cf03edb708e6ceeca134b/Skateboard%20Picture%20%231.png)


### Part Link

[Link to skateboard on Onshape](https://cvilleschools.onshape.com/documents/8ad4fd086495715212304f9d/w/44b543475aa9129af2833029/e/be289c7b1f85a5f018b27f3c?renderMode=0&uiState=616d852671a12e39d3c3b6c9)

### Reflection

This project was fun because I built a skateboard. It was fairly easy and simple; however, I kept wanting to go ahead but had to stick to the instructions or else I would miss small steps and mess up the mass. I did learn a couple new tools: the replicate tool and how wheel bearings work. The replicate tool is very helpful for things like screws and nuts that need to be mated in a lot of places.


## Lego_Duck
* [Back to the top](#Top)

### Assignment_Description
For this assignment I had to create a series of functional lego bricks using configurations and the snap mate. Then, using the bricks, I made a small duck and messed around and made a ship. I then had to create a complete instruction manual using drawings and BOM tables for the duck.

### Evidence

<img src="https://github.com/hcoyle91/Engineering_4_Notebook/blob/c1c7ba2a7e49849af011d7bcde7095fcb9e67794/duck%203.png" alt="" data-canonical-src="https://gyazo.com/eb5c5741b6a9a16c692170a41a49c858.png" width="350" height="400" />     <img src="https://github.com/hcoyle91/Engineering_4_Notebook/blob/f225c07e3628fc0826004b559e9948180bde147d/ship.png" alt="" data-canonical-src="https://gyazo.com/eb5c5741b6a9a16c692170a41a49c858.png" width="350" height="400" />
<img src="https://github.com/hcoyle91/Engineering_4_Notebook/blob/d928899e13408f8fd8fce89d6873369d1c6988a7/duck%201.png" alt="" data-canonical-src="https://gyazo.com/eb5c5741b6a9a16c692170a41a49c858.png" width="600" height="400" />  <img src="https://github.com/hcoyle91/Engineering_4_Notebook/blob/9b3632809568e57cb8cb063e5f6c47091d438c08/duck%202.png" alt="" data-canonical-src="https://gyazo.com/eb5c5741b6a9a16c692170a41a49c858.png" width="600" height="400" />
 

### Part Link

[Link to Duck on Onshape](https://cvilleschools.onshape.com/documents/364d4c61a1e277d6125d86fb/w/a92d60206453172e3fd0164b/e/189d09167cffb32a5af74697?renderMode=0&rightPanel=explodedViewPanel&uiState=6176b4719d97c9185b2bb5e1)

### Reflection

I really enjoyed this asignment. It really showed the power of configurations; I was able to create a configuration table for color, name, size, and brick type. In order to make sure I could mate the bricks together later in an assembly, I created mate connectors from the original sketch: these mate connectors were centered around a circle which fit perfectly into the bottom of another brick. So, later I could snap mate the bricks together. I didn't face many challenges but also really enjoyed creating the drawings. I learned the exploding tool and how you can make different views in drawing based off different exploded views. I also leearned the specifics of drawings' tools an how to accurately represent my work.

## Blinking LED
* [Back to the top](#Top)

### Description: 

For this assignment I had to make two LED's of different colors to bink back and forth. I used Rasberry Pi and an Ada fruit t-cobbler.

### Evidence: 
Code:
#### LED blinking program - (ENGR4)
#Written by Henry Coyle
#November 29th 2021

import RPi.GPIO as GPIO		// imports GPIO library

import time		// Imports library that allows me to make the program pause for a few moments

GPIO.setmode(GPIO.BCM)		// Makes the GPIO read the pins as BCM scale

LED1=20	// Defines these two variables, LED1 and 2 as there own pins

LED2=21

GPIO.setup(LED1, GPIO.OUT, initial=GPIO.LOW)		//Initializes both LED's as off or low

GPIO.setup(LED2, GPIO.OUT, initial=GPIO.LOW)


while True:		//Starts loop automatically
	GPIO.setwarnings(False)			// Sets the automatic warnings to hidden
	
	GPIO.output(LED2, GPIO.HIGH)
	
	print('LED2 on')			// Turns on one LED, pauses that repeats with the other. It prints 'on'when led is on and vice versa.
	
	time.sleep(1.0)
	
	GPIO.output(LED2, GPIO.LOW)
	
	print('LED2 off')
	
	GPIO.output(LED1, GPIO.HIGH)
	
	print('LED1 on')
	
	time.sleep(1.0)
	
	GPIO.output(LED1, GPIO.LOW)
	
	print('LED1 off')

https://user-images.githubusercontent.com/56696954/144445381-9dba2712-172d-4cbf-9b8f-09a9061f5f58.mp4



### Wiring: 

<img src="https://github.com/hcoyle91/Engineering_4_Notebook/blob/5edf260b5c224ff4faea8f8490656305ea283c0c/LED%20Wiring%201.jpeg" width="350" height="400" />  <img src="https://github.com/hcoyle91/Engineering_4_Notebook/blob/5edf260b5c224ff4faea8f8490656305ea283c0c/LED%20wiring%202.jpeg" width="350" height="400" />  

### Reflection: 
 
My biggest challenges within this assignment was to learn more about the Rasberry pi's codeing language. The wiring was fairly easy (2 LED's, 2 220 resistors, and some jumber wires). The code was easy once I got used to using GPIO methods as I only needed to make onje while loop.

## Rasberry Pi Safe Shutdown

* [Back to the top](#Top)

### Description:

For this assignment I had to wire a button and make a program where the Raspberry pi is restarted when I press it once and shutdown when I held the button.

### Evidence: 


https://user-images.githubusercontent.com/56696954/145420749-08e04c66-38ac-42b6-a5a5-4c127a0ffa7f.mp4


### Wiring/Code: 
Code:
https://github.com/hcoyle91/Engineering_4_Notebook/blob/fa7890833356ede25112181d7adb84aa8b329ef3/Shutdown%20code
<img src="https://github.com/hcoyle91/Engineering_4_Notebook/blob/553e5f39970ecea17b9d345aab84a840a0cca2f7/shutdown%20wiring.jpeg" width="350" height="400" />  <img src="https://github.com/hcoyle91/Engineering_4_Notebook/blob/553e5f39970ecea17b9d345aab84a840a0cca2f7/shutdown%20wiring%202.jpeg" width="350" height="400" />  

### Reflection: 
The wiring was very simple for this project: I only needed a jumper froom the button to ground and to a pin. The code was provided by my teacher and was difficu;t to understand at first. The next step in this assignment is to make this program run in the backround while I can work on other projects. That was it will be a usefull and quick way to shutdown or restart without typing it out.

## Accelerometer with Display

* [Back to the top](#Top)

### Description:

### Evidence:

#### Code:

#### Wiring:
![623A6841-525C-4505-874B-2A54D500C0CE](https://user-images.githubusercontent.com/56696954/149358190-87279a71-d2c1-4d99-acf7-2c652065cc2a.jpeg)
![4255ACAB-F4AB-4C57-9E30-B323A903E10E](https://user-images.githubusercontent.com/56696954/149358208-66d65f79-0f33-4c0a-834e-7d600d58f13f.jpeg)

### Wiring/Code:

### Reflection:

