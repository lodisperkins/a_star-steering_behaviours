| Lodis Perkins|
| :---          	|
| s188043       	|
| Introduction to C# |
| FSM Factory Documentation |

## I. Requirements

1. **Description of Problem**

      **Name**:  AI Demo

      **Problem Statement**:

       Creation of a real time application that demonstrates Artificial Intelligence Behaviour

     **Problem Specifications**:  
     -   Game entities displaying the implemented artificial intelligence behaviours and decision-making techniques as specified in the Artificial Intelligence Behaviour Plan
      - Implementation must include at least one of the following decision-making techniques (or another as negotiated with your instructor):
   	 -   Game entities using a suitable pathfinding search algorithm
   	 -  Game entities using a suitable pathfinding search algorithm
	


2. **Input Information**
 'A'- Shows a graphical representation of the A* algorithm
 'S' - Creates two game objects that demonstrate seek,flee, and wander behaviour
 'P' - Creates two game objects that demonstrate pursue,avoid, and arrive behaviour
3.  **Output Information**  
    - The program displays a graphical representation of a*, seek behaviour, or pursue behaviour based on the user input
4. **User Interface Information**
    - The UI displays the frame rate, playtime, and controls
## II. Design

1. _System Architecture_
    
	All objects inherit from the gameobject class. Each gameobject is responsible for drawing, updating and making decisions. Each gameobject has a behaviour associated with it from the objectbehaviour class. Based on the objects current behaviour, its velocity is changed accordingly. Nodes, have no velocity and therfore no behaviour. Instead, nodes positions are set based on their position in the graph. Whether the gameobjects are created as a graph or as agents depends on the user input. If A* is initialized, gameobjects become nodes and a graph is drawn to the screen showing the steps of A*. If seek behaviour is choosen, two agents are created that play an endless game of tag. If pursue behaviour is chosen, two agents are created. One is place at the bottom center of the screen and attempts to move to the top. The other is placed on the far left of the screen and attempts to catch the other by seeking where it will be instead of where it is. After it is caught the first agent then begins to evade; the two then rotate in a circle indefinitely as one evades while the other pursues.

| 
|:-----------
| ![User Interface gif](https://media.giphy.com/media/RK9DdjV1aqSMQZVsSt/giphy.gif)
| 


2. _Object Information_
   
	- **File Name**: State.cs
		- Name: Name(string)
			- Description: The name of the state
			- Visibility: public
        - Name: destinationName(string)
			- Description: Stores the name of the state that a state will transition to
			- Visibility: public
  		- Name: condition(bool)
			- Description: The state should switch to its destination state based on whether or no this is true or false
			- Visibility: public
    - **File Name**: Fsm.cs
		- Name: statesList(List<State>)
			- Description: Stores all of the states that are to be written to a file
			- Visibility: public
        - Name: add(void)
			- Description: Adds a state to the stateslist and sets current to the value of the state added
			- Visibility: public
			- Arguments: State
        - Name: switch(void)
			- Description: Switches the current state to another. Mainly used for testing 
			- Visibility: public
        - Name: current(State)
			- Description: Stores the value of the state the finite state machine is currently on
			- Visibility: public
  
	- **File Name**: FSM Application.cs
        - Name: current_Boxes(List(label))
			- Description: The list used for updating the first columns drop down boxes
			- Visibility: private
        - Name: transition_Boxes(List(ComboBox))
			- Description: The list used for updating the second columns drop down boxes
			- Visibility: private
        - Name: condition_Textt(List(string))
			- Description: The list used for updating the third columns drop down boxes
			- Visibility: private
       - Name: fsm(Fsm)
			- Description: The finite state machine that will be populated with the values entered
			- Visibility: public
       - Name: current_Drop(Label)
			- Description: The control that will populate the first column
			- Visibility: public
	    - Name: transition_Drop(ComboBox)
			- Description: The control that will populate the second column
			- Visibility: public
        - Name: condition_Drop(ComboBox)
			- Description: The control that will populate the third column
			- Visibility: public
        - Name: state_Text(string)
			- Description: Default text for the second columns drop down boxes
			- Visibility: public
        - Name: cond_Text(string)
			- Description: Default text for the second columns drop down boxes
			- Visibility: public
        - Name: cond_True(string)
			- Description: Opiton for the third columns dropdown boxes
			- Visibility: public
        - Name: cond_False(string)
			- Description: Opiton for the third columns dropdown boxes
			- Visibility: public
        - Name: file_Name(string)
			- Description: Name of the file that will be written to
			- Visibility: public
		- Name: mod_Form(Modify)
			- Description: Child form used for adding states
			- Visibility: public
		- Name: has_Saved(bool)
			- Description: Keeps track of whether or not the user has saved
			- Visibility: public
		- Name: warning(void)
			- Description: If the user closes the program without saving, this function creates a new form warning 
              them. If the user has saved, the program closes as normal.
			- Visibility: private
			- Arguments: sender(object), e(FormClosingEventArgs)
		- Name: updateText(void)
			- Description: updates the items in the list of each combobox
			- Visibility: private
			- Arguments: sender(object), e(EventArgs)
		- Name: updateTable(void)
			- Description: Updates the finite state machine after new states have been added in the modify FSM window
			- Visibility: private
			- Arguments: sender(object), e(EventArgs)
		- Name: addStateButton_Click(void)
			- Description: Opens the modify FSM window if clicked
			- Visibility: private
			- Arguments: sender(object), e(EventArgs)
		- Name: save(void)
			- Description: Creates and adds states to the FSM and then saves it to a json file
			- Visibility: private
			- Arguments: none  
		- Name: load(void)
			- Description: Checks to see if the file exists. If so, it loads the file into the fsm app
			- Visibility: private
			- Arguments: none    
        - Name: saveToolStripMenuItem_Click(void)
			- Description: Allows the user to select which file path to save their FSM to
			- Visibility: private
			- Arguments: sender(object), e(EventArgs) 
		 - Name: loadToolStripMenuItem_Click(void)
			- Description: Allows the user to select which file path to load their FSM from
			- Visibility: private
			- Arguments: sender(object), e(EventArgs)
		- Name: exitToolStripMenuItem_Click(void)
			- Description: Checks the see if the user has saved. If so the program closes as normally. Otherwise the warning window displays.
			- Visibility: private
			- Arguments: sender(object), e(EventArgs)  
	- **File Name**: Statepanel.cs     	

	    - Name: Statepanel()
    		- Description: Constructor that takes in an argument to set the text for the label the control contains.
    		- Visibility: public
    		- Arguments: string
    	- Name: name(string)
    		- Description: Gets and set the text for the label in the control
    		- Visibility: public     
    - **File Name**: Modify.cs  
        - Name: x(int)
    		- Description: x Location of each statepanel added
    		- Visibility: public
    	 - Name: y(int)
    		- Description: y Location of each statepanel added
    		- Visibility: public
    	 - Name: states(List<State>)
    		- Description: Stores a list of the states added
    		- Visibility: public
    	- Name: statePanels(List<Statepanel>)
    		- Description: Stores a list of the custom controls added
    		- Visibility: public  
    	- Name: hideWindow(void)
			- Description: Hides the window instead of closing if the close button is pressed
			- Visibility: private
			- Arguments: sender(object), e(EventArgs)
		- Name: panel_RightClick(void)
			- Description: Adds a right click menu to each of the custom controls
			- Visibility: private
			- Arguments: sender(object), e(EventArgs)
		- Name: loadStates(void)
			- Description: Loads the states from a previous session into the list of states
			- Visibility: public
			- Arguments: List<State> value
		- Name: button2_Click(void)
			- Description: Creates a new state and a new custom control to represent that state
			- Visibility: private
			- Arguments: sender(object), e(EventArgs)
		- Name: button1_Click(void)
			- Description: Updates the names of the states in the state list to the names of the custom controls and hides the window
			- Visibility: private
			- Arguments: sender(object), e(EventArgs)
		- Name: removeState(void)
			- Description: Removes a state and a custom control from their respective lists
			- Visibility: public
			- Arguments: index(int)
		- Name: deleteToolStripMenuItem_Clicke(void)
			- Description: Calls the remove state function the delete option is clicked
			- Visibility: private
			- Arguments: sender(object), e(EventArgs)  
	- **File Name**: Warning.cs
        - Name: cancelbutton_Click(void)
			- Description: Hides window if the cancel button is clicked
			- Visibility: private
			- Arguments: sender(object), e(EventArgs)    	 
