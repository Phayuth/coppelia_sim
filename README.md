# ROS2 with CoppeliaSim
This package contain a tutorial on coppelia simulation with ROS2 and some code that I learn.

### Setup
1. Install ROS2
2. Download CoppeliaSim Edu. version https://www.coppeliarobotics.com/downloads
3. Extract CoppeliaSim to `Home` directory
4. Install Requirement Package `xsltpro` and `xmlschema`
    - `sudo apt-get install xsltproc`
    - `pip3 install xmlschema`
5. Create workspace and enter `mkdir -p ws_coppsim_ros2/src && cd ws_coppsim_ros2/src`
6. Clone `simExtROS2` package and `ros2_bubble_rob`
    - git clone https://github.com/CoppeliaRobotics/simExtROS2.git
    - git clone https://github.com/CoppeliaRobotics/ros2_bubble_rob.git
7. Backup one level and complile

    ```
    export COPPELIASIM_ROOT_DIR=~/coppeliaSim
    ulimit -s unlimited
    colcon build --symlink-install --cmake-args -DCMAKE_BUILD_TYPE=Release
    ```
    Edit `meta/interfaces.txt` for more support message type.

8. Start CoppeliaSim with `./coppeliaSim.sh`


### References
- https://www.coppeliarobotics.com/helpFiles/en/ros2Tutorial.html
- https://github.com/giulioturrisi/Differential-Drive-Robot