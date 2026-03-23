# 🏎️ 졸업 프로젝트: ROS 기반 자율주행 레이스카
> 프로젝트에 대한 짧은 설명을 적어주세요. (예: LiDAR와 Camera를 이용한 장애물 회피 주행)

## 📅 프로젝트 기간
* 202X.XX ~ 202X.XX

## 🛠️ 기술 스택 (Tech Stack)
* **OS:** Ubuntu 18.04 / 20.04
* **Platform:** ROS Melodic / Noetic
* **Language:** C++, Python
* **Hardware:** NVIDIA Jetson, ZED Camera, RPLidar

## 📂 주요 패키지 구성
* `racecar_simulator`: 가상 환경 시뮬레이션
* `lane_detection`: 차선 인식 알고리즘
* `obstacle_detector`: 장애물 감지 및 회피

## 🚀 실행 방법
```bash
# 워크스페이스 빌드
catkin_make
source devel/setup.bash

# 시뮬레이션 실행
roslaunch racecar_gazebo racecar_run.launch
