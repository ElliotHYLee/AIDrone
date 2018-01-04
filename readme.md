# Gesture Classification using Kinect

Deep learning for controller optimization.<br>


[Click for Youtube video:<br>
<img src="https://github.com/ElliotHYLee/AIDrone/blob/master/Images/simplePID.jpg" width="300">](https://www.youtube.com/watch?v=AIXz85A91rk)


## Prereq.s

Tensorflow

python libraries:

```
chmod +x pythonReady.sh
yes "yes" | sudo sh pythonReady.sh
```

## run

```
python main.py
```


## ToDo
- Implement NN in Propeller
- Try RNN
- Try Q-Learning to optimize the controller performance

## Problem Setup

Stage 1: Show NN can perform PID less than equal to the performance of PID controller. <br>
Stage 2: Show Q-learning can optimize NN structure. 


## Results

MSE = 1.6

Red: Actual PID output for ESC signal
Blue: NN output for ESC signal

<img src="https://github.com/ElliotHYLee/AIDrone/blob/master/Images/Figure_1.png" width="700">

