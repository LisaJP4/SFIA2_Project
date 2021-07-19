# SFIA2_Project

## Introduction
### SFIA2 Project Brief
* For this project, we were required to create a service-orientated architecture for our application, which must be composed of at least 4 services that work together:
- Service #1 was the core service, which rendered Jinja2 (HTML) templates required to interact with the application. It also communicated with the other 3 services and persisted data in a data base.
- Service #2 and #3 generated random "Objects", which could be a random number, letter, or other more complex method.
- Service #4 also created an "Object", this time based on the outcome of what the previous two services had generated.

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
![CI_CD pipeline](https://user-images.githubusercontent.com/84873140/126086154-ae2562ba-b038-43f2-9142-e0613b4aa3d7.png)
Above I have provided a simple diagram showing the CI/CD Pipeline. Here is how each phase is implemented: 
- *1 - Development Environment* - The Python logo represents the development enviornment in which code for each of the services is written.
- *2 - Version Control System* - Using GitHub, I was able to keep track of the different versions of my code. I also implemented using feature-branches in order to separate new changes from the main source code. 
- *3 - Project Management* - I implemented a Kanban board, represented by the Trello logo. This helped me to prioritise tasks as I went through the development and pipeline process.
- *4 - Pytest* - This tests the code that has been written for the quality and function.
- *5 - Jenkins* - This is the CI Server: it hepls to automate the building, testing and deploment of our application, and can be linked with a webhook to our VCS.
-  *6 - Docker-Compose* - Through our docker-compose.yaml file in our directory, we can build images quickly and easily. These images can also be pushed to Dockerhub.
-  *7 - Dockerhub* - This is the most commonly used registry for official Docker images. It allows us to store images we have created, as well as pulling down images we can use in our projects.
-  *8 - Ansible* - A configuration management tool, Ansible allows us to quickly conigure virtual machines with packages and dependencies. 
-  *9 - Docker-Swarm* - Finally, Docker-Swarm allows us to deploy our applications. Using Docker Stack, we can float services as containers across multiple virtual machines. 

<img width="176" alt="feature branch model" src="https://user-images.githubusercontent.com/84873140/126086542-e8685a12-10a1-4c1b-b86b-8fa16dfefc1d.png">

### How was Jenkins used to Build, Test and Deploy my applcation
<img width="464" alt="failed build 2" src="https://user-images.githubusercontent.com/84873140/126086581-93d24482-9977-49a4-a01b-0fdd52993dbe.png">
* Once my application had been designed and tested, I wanted to automate the building, testing and deployment using Jenkins. I did this by creating a Jenkinsfile in my repository and writing the commands into it which Jenkins would follow. After linking Jenkins to the *Dev* branch on my Github for the project, I encountered many errors and many failed builds; originally, I just created three simple stages: 
- Build - I pulled my latest images of my services from Dockerhub. 
- Test - I wanted to enable Jenkins to test the files from my repository as I had in my terminal when creating the tests.  
- Deploy - I wanted to get Jenkins to deploy the stack that I had created for my containers. This should have then allowed me to perform a rolling update - an update where a user experiences no downtime from an application. 

### Missing Stage of the Pipeline
* Testing
<img width="718" alt="failed test" src="https://user-images.githubusercontent.com/84873140/126085583-3008a1dd-36d8-4634-85c6-24a2578c5dc9.png">

  
### Webhook

<img width="187" alt="webhook is set up" src="https://user-images.githubusercontent.com/84873140/126086510-1ccfb121-a083-499d-a5c9-983a21ae4367.png">

  
### Affect of the Missing Stages on a Rolling Update
  
## Architectures
  ### Docker-Compose
  ### Docker Swarm
  ### NGINX
  
  <img width="241" alt="nginx bad gateway" src="https://user-images.githubusercontent.com/84873140/126086520-0f49685a-9133-41bf-968e-ba4b0530f631.png">


## System Configuration


## Future Improvements
