# SFIA2_Project

## Introduction
### SFIA2 Project Brief
*

### How does my design fit this brief?

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
*
  
### Webhook
  
### Affect of the Missing Stages on a Rolling Update
  
## Architectures
  ### Docker-Compose
  ### Docker Swarm
  ### NGINX
  ### Ansible

## System Configuration


## Future Improvements
