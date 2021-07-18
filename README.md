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
* 

### Database Design (Original and Adapted)
* 

### Risk Assessment 
* Using Trello, I was able to keep track of the tasks I had to perform throughout the project's development: 
<img width="883" alt="trello" src="https://user-images.githubusercontent.com/84873140/123564903-0e105000-d7b3-11eb-9d14-3c56bcecb545.png">

## CI/CD Pipeline
### Explanation of the Pipeline itself


### How was Jenkins used to Build, Test and Deploy my applcation
* In my database, I implemented datetime to automatically timestamp the creation of the reports I was making. I also set the primary key for the Reports table to autoincrement. This would prove to be useful later when identifying reports to update or delete, as there were no other integers in the table: **_Reports.query.get(<primarykey>)_**

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
