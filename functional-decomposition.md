# Functional Decomposition

## Vending machine from a human perspective (Example from class)

You get a bag of chips from a vending machine
- Approach machine
    - Walk until you are within arms reach
- Determine the number for the flavour I want
    - Search for the specific flavour
    - Look just below it for the ID number (Remember that number)
- Put in appropriate amount of money
    - Look beside the ID number for the cost of the snack
    - Get out some money greater or equal to that amount
    - Place that money into the intake
- Key-in the number for the flavour
- Get bag from bottom of machine
    - Bend down
    - Put arm through slot
    - Grab chips
    - Pull your arm out (with the chips)

## Vending machine from the machine's perspective 

You are waiting for someone to give you money so you can give them a snack
- Awaiting input from a user
    - Display a message such as 'awaiting input' on the display panel
- Determine which snack was chosen by the user
    - Read the ID number punched into the machine
    - Compare this ID number with all the available ID numbers (ID numbers indicating the snack)
    - If the ID number matches with a specified snack, store it in memory
- Determine if they paid enough money for that chosen snack
    - Read how much the specified snack costs
    - Read how much the user paid in the intake
    - Compare the money paid to the cost of the selected snack
    - If they did not pay enough, display 'Too few coins', if they paid enough, move on to the next step
- Dispense the snack and return change
    - Release one of the selected snacks into the funnel that leads to the bottom of the machine
    - If the user paid more than needed, return the coins back into the intake
        - Find the difference between the amount needed and the amount paid
- Wait for the next user to get a snack
    - Display 'awaiting input' again on the panel after snack has been dispensed and money has been received
    
    
## The Cookie Is Too Big For The Glass (How Do You Fix This Problem?)

