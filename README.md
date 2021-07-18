# SFIA2_Project

## Introduction
### SFIA2 Project Brief
* For this project, we were required to create a service-orientated architecture for our application, which must be composed of at least 4 services that work together:
* - Service #1 was the core service, which rendered Jinja2 (HTML) templates required to interact with the application. It also communicated with the other 3 services and persisted data in a data base.
* - Service #2 and #3 generated random "Objects", which could be a random number, letter, or other more complex method.
* - Service #4 also created an "Object", this time based on the outcome of what the previous two services had generated.

### How does my design fit this brief?
For my service, I chose to design a simple app which generated the outcome of plague victims based on the number of days they had the illness, and whether their fortune was 'Lucky' or 'Unlucky'. You can see and example of Service 2, 3 and 4 highlighted from top to bottom as they were rendered by Service 1.

<img width="405" alt="service architecture" src="https://user-images.githubusercontent.com/84873140/126085812-3bc3624d-a0e5-47b8-9f66-a727c0c05eeb.png">


## Software Design
### Planning
* I used a Trello board to implement the planning for what tasks needed to be completed for this project. After I had put the tasks on the board, I then assigned them a priority based on the MoSCoW Prioritisation method: 
<img width="538" alt="Trello board" src="https://user-images.githubusercontent.com/84873140/126085909-6f3104c6-7d10-4385-9b96-bd2add8b4076.png">

### Database Design (Original and Adapted)
* Originally, I had planned for my Service 2 (Days) to be an Integar and my Service 3 (Fortune) to be a Boolean. Finally, my Service 4 (Outcome) could be a string returned in the Jinja2 template. However, as I begin the process of designing the microservices to communicate and render the information, I realised that the easiest way to make it work was through making everything a string:
![databases](https://user-images.githubusercontent.com/84873140/126086061-fa429529-1eb4-4bc3-b978-eec4cb6bf800.png)


### Risk Assessment 
* 

## CI/CD Pipeline
### Explanation of the Pipeline itself


### How was Jenkins used to Build, Test and Deploy my applcation


### Missing Stages of the Pipeline
* Testing
*  
<img width="718" alt="failed test" src="https://user-images.githubusercontent.com/84873140/126085583-3008a1dd-36d8-4634-85c6-24a2578c5dc9.png">

  
### Webhook
  
### Affect of the Missing Stages on a Rolling Update
  
## Architectures
  ### Docker-Compose
  ### Docker Swarm
  ### NGINX
  ### Ansible

## System Configuration


## Future Improvements
