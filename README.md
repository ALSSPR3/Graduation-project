# 🏎️ 졸업 프로젝트: ROS 기반 자율주행 레이스카
> LiDAR와 Camera 센서 퓨전을 활용한 실시간 장애물 회피 및 차선 인식 자율주행 시스템 개발

## 📅 프로젝트 기간
* **2022년 09월 28일 ~ 2023년 06월 01일**

## 🛠️ 기술 스택 (Tech Stack)
* **OS:** Ubuntu 18.04 / 20.04 (ROS Melodic / Noetic)
* **Language:** C++, Python, Shell Script
* **Hardware:** NVIDIA Jetson, ZED Stereo Camera, RPLidar A1/A2, VESC (Electronic Speed Controller)
* **Libraries:** OpenCV, PCL (Point Cloud Library), Eigen

## 🧠 주요 알고리즘 (Key Algorithms)

### 1️⃣ Wall Following & PID Control
* **거리 유지:** LiDAR 데이터를 분석하여 벽과의 거리를 실시간으로 계산합니다.
* **조향 제어:** P(비례), I(적분), D(미분) 제어기를 통해 주행 오차를 최소화하고 부드러운 코너링을 구현했습니다.

### 2️⃣ Localization (Particle Filter)
* **위치 추정:** `range_libc` 기반의 고속 레이 캐스팅을 사용하여 로봇의 현재 위치를 확률적으로 추정합니다.
* **정확도:** 수천 개의 파티클을 통해 동적인 환경에서도 안정적으로 로봇의 전역 좌표를 파악합니다.

### 3️⃣ SLAM (Hector SLAM)
* **지도 생성:** 별도의 Odometry 없이 LiDAR 스캔 매칭만으로 2D 점유 격자 지도(Occupancy Grid Map)를 생성합니다.
* **경로 기록:** 실시간으로 지도를 그리며 로봇의 이동 궤적을 기록합니다.

## 📂 주요 패키지 구성
* `racecar_simulator`: 가상 환경 시뮬레이션 및 알고리즘 검증용 테스트 베드
* `lane_detection`: OpenCV 기반 차선 인식 및 경로 추종 알고리즘
* `obstacle_detector`: 장애물 감지 및 충돌 방지(E-Stop) 시스템
* `zed-ros-wrapper`: 스테레오 카메라를 이용한 깊이(Depth) 정보 추출
* `vesc`: 하드웨어 모터 제어 및 데이터 통신

## 🚀 실행 방법

### 1. 워크스페이스 빌드
```bash
# 워크스페이스 이동 및 빌드
cd ~/catkin_ws
catkin_make

# 환경 변수 적용
source devel/setup.bash

## 📄 관련 문서 (Documents)
* [최종 발표 자료 (PPT)](./path/to/your/presentation.pptx)
* [졸업 논문 보고서 (HWP)](./path/to/your/report.hwp)
* [시스템 설계서 (PDF)](./path/to/your/design.pdf)
