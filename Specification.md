# URL to repo:
https://github.com/Dennis-Shih/Requirements

# Team members:
* Dennis Shih: https://github.com/Dennis-Shih
* James Ta: https://github.com/jamesta99


**Product Name:** TaskLab

**Problem Statement:** The purpose of this product is to allow users to complete tasks of various sizes in an efficient and organized manner. 

# Use cases

**Use Case Name:** Start/Create new task

**Date:** 4/6/2021

## Summary 
A new task must be created or started by the actor. 
## Actors
The user of the product, likely a person, who aims to create a new task.
## Preconditions
The actor must be logged in to an account.
## Triggers
The actor clicks a button such as "New Task".
## Primary Sequence
1. System prompts user for a name for the task.
2. User enters a name in a text field or does not name it.
3. System starts new task if a valid name is entered or if name is left blank.
## Primary Postconditions
A new task should have been created under the title entered by the user, or 'Untitled' if left blank.
## Alternate Sequences
2. The title of the task is invalid (such as any potential illegal characters)
a. System refuses to create new task  
b. System prompts user for a valid name for task

 

### Alternate Trigger
The user enters a task name with illegal characters

### Alternate Postconditions
No new task with the invalid name is created.

**Use Case Name:** Delete/Cancel task

**Date:** 4/7/2021

## Summary
The user wants to cancel or delete a task
## Actors
A person
## Preconditions
* The actor must be logged in to an account
* The actor must have an active task
## Triggers
The actor selects a button named 'Cancel Task'
## Primary Sequence
1. System opens a dialogue box to confirm the actor's action
2. System removes the task and its data

## Primary Postconditions
* The data of the selected task must be deleted


**Use Case Name:** Login or Sign in

**Date:** 4/6/2021
## Summary
The actor attempts to sign in to an account on the task manager.
## Actors
A person or bot
## Preconditions 
* The actor is not already signed in.
## Triggers
* Actor selects a 'Sign in' button
## Primary Sequence
1. System prompts the user with a username and password.
2. User types in a username and password.
3. System logs in the user assuming a valid username and password.
## Primary Postconditions
User must be logged in to their account.

## Alternate Sequences
2. The password or username is invalid
a. System refuses to sign in
b. System prompts user to log in again

 

### Alternate Trigger
The user enters an invalid username or password

### Alternate Postconditions
System does not log user into account.



**Use Case Name:** Register for new account

**Date:** 4/6/2021
## Summary
The actor attempts to create an account.
## Actors
A person or bot
## Preconditions 
* The actor is logged out.
## Triggers
* Actor selects a 'Sign in' button
## Primary Sequence
1. System prompts the user with a username and password.
2. System creates account with entered username and password.
## Primary Postconditions
System must have created a new account. 

## Alternate Sequences
1. The username entered by the user belongs to an existing account.
  a. System notifies user that account name already in use.
  b. System prompts user to change username.

 

### Alternate Trigger
The user attempts to create an account with an existing username.

### Alternate Postconditions
System does not create an account.

**Use Case Name:** Log out

**Date:** 4/7/2021
## Summary
Actor wants to sign out of their account
## Actors
A person or bot
## Preconditions
* The actor must be signed in
## Triggers
* Actor selects a 'Sign out' button
## Primary Sequence
1. System opens a dialogue box to confirm the user's action.
2. System logs out of user's account.
## Primary Postconditions
The user must not be logged in.

**Use Case Name:** Save

**Date:** 4/6/2021
## Summary
The actor wants to save their progress on a task
## Actors
A person or bot
## Preconditions 
* The task must have unsaved progress or changes
## Triggers
* Actor selects a 'Save' button or icon
## Primary Sequence
1. System saves the changes when user presses the respective button.
## Primary Postconditions
System must have saved any unsaved progress made on a task.


**Use Case Name:** Save as

**Date:** 4/7/2021
## Summary
The actor wants to save a task under a new name.
## Actors
A person or bot
## Preconditions 
* The task must have unsaved progress or changes
## Triggers
* Actor selects a 'Save as' button or icon
## Primary Sequence
1. System shows user a text field in which they can edit what name to save the task under.
2. System saves the task under the name specified.
## Primary Postconditions
System must have saved any unsaved progress made on a task, under the new task name.

## Alternate Sequences
2. The name entered is already being used by another task.

   a. The system asks if the user wants to overwrite the existing file.
   
   b. File is overwritten if the user confirms, otherwise does nothing.
 


### Alternate Trigger
The name the user attempts to save under is already being used.

### Alternate Postconditions
System overrides existing file if the actor demands it, or does not if the actor does not wish to override.




**Use Case Name:** Make a copy

**Date:** 4/7/2021
## Summary
The actor wants to create a duplicate of a task
## Actors
A person or bot
## Preconditions 
* The task must have unsaved progress or changes
* User must be logged in
* User must have the task open
## Triggers
* Actor selects a 'Make a copy' button
## Primary Sequence
1. System creates a copy of the selected task under a name that indicates that it is a copy.



## Primary Postconditions
A file whose contents are identical to the original must have been created in the same location.

## Alternate Sequences
2. The name entered is already being used by another task.

   a. The system asks if the user wants to overwrite the existing file.
   
   b. File is overwritten if the user confirms, otherwise does nothing.


**Use Case Name:** Invite collaborators

**Date:** 4/7/2021
## Summary
The actor wants to allow other users to work on a task.
## Actors
* The person or bot doing the inviting
* The users being invited
## Preconditions 
* The collaborators must not already be able to work on the file
## Triggers
* Actor selects a button to invite users to the task
## Primary Sequence
1. System prompts user to tell it which users to invite, and does not show any users that are already collaborators.
2. User adds any other users they want to have access to the task.
3. System invites selected users and grants them the ability to work on the task.

## Primary Postconditions
Invited users should be able to work on the task.

**Use Case Name:** Remove collaborators

**Date:** 4/7/2021
## Summary
The actor wants to remove a user from a task
## Actors
The person removing the user
## Preconditions
* The actor must be logged in
* The actor must have an active task with other collaborators
## Triggers
Actor selects a button to remove users from a task 
## Primary Sequence
1. System displays a list of currently collaborating users
2. Actor selects the users they would like to remove
3. System removes the users from the task, making them unable to work on it

## Primary Postconditions
* The selected users cannot work on the task they were removed from


**Use Case Name:** Comment

**Date:** 4/7/2021

## Summary
The actor wants to write a comment on a task
## Actors
The person writing the comment
## Preconditions
* The actor must be logged in
* Actor should have task open
## Triggers
The actor selects a 'Comment' button
## Primary Sequence
1. System opens a text field for the actor to write their comment in
2. Actor types in text field
3. After the actor selects a 'Post' button, the system shows the actor's comment beneath the task

## Primary Postconditions
* The written comment should be visible to users viewing the task


**Use Case Name:** Set deadline

**Date:** 4/7/2021
## Summary
The actor wants to attribute a certain date to a task, so that they know when they should be finished with said task, or want to modify the deadline. The deadline merely serves as a reminder, and can be changed by the user(s).
## Actors
* The person or bot
## Preconditions 
* The file must exist
## Triggers
* Actor selects 'Set deadline' option
## Primary Sequence
1. System prompts user to enter a date/time. Generally, the system will default to the computer's set time, but if a deadline is already set, the system should default to that deadline's date.
2. User confirms choice by hitting a confirm button.



## Primary Postconditions
A date and/or time values should be highlighted as a deadline and attributed to the task.



## Non-functional Requirements
* The product must load pages in under 4 seconds.
* Users must be able to understand how to use the interface within 15 seconds of seeing it
* The product must format dates in the form month/day/year

## Glossary
User: The person who wants to perform a task under the task manager

Account: User accesses their work by signing in.
