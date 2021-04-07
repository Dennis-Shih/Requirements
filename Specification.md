# URL to repo:
https://github.com/Dennis-Shih/Requirements

# Team members:
* https://github.com/Dennis-Shih
* https://github.com/jamesta99


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
2. System starts new task if a valid name is entered or if name is left blank.
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
2. System logs in the user assuming a valid username and password.
## Primary Postconditions
User must be logged in to their account.

## Alternate Sequences
1. The password or username is invalid
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


## Non-functional Requirements

 

## Glossary
