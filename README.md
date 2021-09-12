# stanCode_AI
## Pedestrian crossing aid by machine learning


## Introduction
https://github.com/lily71903/stanCode_AI_Project/issues

When crossing intersection...
  * It is hard for them to perform safety evaluation
  * In Taipei city, only 6.9% (185/2679) of intersections have audio-assisted pedestrian signals


## Current Researches
Convolution neural network (CNN) based traffic light detection and recognition
Current application:
  *	Self-driving vehicles
  *	Driving assistance

## Our Proposal
A vision-based model for detecting the real-time intersection condition
1.	Traffic light recognition
2.	Crosswalk clearance
3.	Estimated time of crossing

## Methodology
Dataset & Data-preprocessing
  * Self-constructed, 1148 in total
  * Images of intersections in both Taipei city and Taoyuan city
  * Raw data to trainable data: label → convert file → resize(1024*1024), crop, rotate → rename → create subsets
  * Allocate our data into training, validation, and testing set by stratification in (90:5:5 ratio)
![image](https://user-images.githubusercontent.com/83638647/132990419-ea1e8f85-fe56-41e4-8010-e53b30ed7439.png)
![image](https://user-images.githubusercontent.com/83638647/132990421-ee5919b7-a339-4994-8af3-b79c82a64ab6.png)
![image](https://user-images.githubusercontent.com/83638647/132990424-fdadd7b1-8dbc-49fb-9acb-867f283419cb.png)
![image](https://user-images.githubusercontent.com/83638647/132990425-d6d4b2f0-7a01-4472-b998-c962d897a723.png)
![image](https://user-images.githubusercontent.com/83638647/132990433-9b7637e3-d3f3-42d8-9762-5fa848c92d9c.png)
![image](https://user-images.githubusercontent.com/83638647/132990437-7c1eff7e-31cf-416e-9489-5cdf94685c0f.png)


 
## Results
![image](https://user-images.githubusercontent.com/83638647/132990192-6f9892e6-f66b-4967-8061-dab32100bdfd.png)
![image](https://user-images.githubusercontent.com/83638647/132990194-05ec6fac-8aff-4460-a812-19abbdc2e51e.png)

