.. _Technical-Data:

Technical Data
**************

.. _Technical Specifications:

Technical Specifications
+++++++++++++++++++++++++++

.. _Robot-Technical-Specifications:

Robot Technical Specifications
===============================

.. csv-table:: Robot technical specifications
   :file: ./tables/Robot technical specifications.csv
   :encoding: utf-8-sig
   :widths: 20 20 20 20 20
   :header-rows: 1

.. container:: table-notes

   | :sup:`1` This capability can be achieved through a software upgrade.
   | :sup:`2` When the ambient temperature is below 10°C, warm up the robot before use; otherwise, the robot may stop or operate at a reduced speed.

.. _Control cabinet technical specifications:

Control cabinet technical specifications
=========================================

.. csv-table:: Control cabinet technical specifications
   :file: ./tables/Control cabinet technical specifications.csv
   :encoding: utf-8-sig
   :widths: 16 12 18 17 20 17
   :header-rows: 1

.. _Camera-Technical-Specifications:

Camera Technical Specifications
================================

.. list-table:: Camera technical specifications
   :widths: 25 75
   :header-rows: 0

   * - Max. resolution
     - 10M

   * - Max. frame rate
     - 60fps

   * - Shutter type
     - Global

   * - Image format
     - Color, B&W

   * - Lens mount
     - M12 interface with auto-focus

   * - Focal length
     - Standard 12 mm (0.5 in), optional 8 mm (0.3 in)/16 mm (0.6 in)

   * - Light source
     - Standard white light; optional red/blue, polarized/non-polarized

   * - Communication
     - Gigabit Ethernet

   * - Power supply
     - 9~26 V DC, 1 A input

   * - Power consumption
     - <18 W

   * - IP
     - IP65

   * - Operating temperature
     - 0~50°C (32~122°F)

   * - Storage temperature
     - –30~70°C (–22~158°F)

   * - Operating humidity
     - 25~95% RH, non-condensation

.. _Dimensional-Drawings:

Dimensional Drawings
++++++++++++++++++++

.. _Robot Outline Dimensions:

Robot Outline Dimensions
==========================

The sizes of the |product_name| robots are shown below. During the installation, the motion range of the robot must be considered to avoid injury to or collision with surrounding personnel and equipment.

.. figure:: ../../images/06_技术规格/A5L_外形尺寸图.*
   :width: 6cm
   :align: center

   A5L outline dimensions

.. figure:: ../../images/06_技术规格/A12L_外形尺寸图.*
   :width: 6cm
   :align: center

   A12L outline dimensions

.. _Robot-Working-Space:

Robot Working Space
====================

When the robot is mounted, a cylindrical space must be considered. Due to the robot being in close proximity of a singularity, it is recommended to keep the robot end outside of this workspace. If the previously mentioned recommendations are not followed, the robot might perform at lower efficiency and create difficulties in the risk assessment. The working space of the |product_name| robots are shown below.

.. figure:: ../../images/06_技术规格/A5L_工作空间.*
   :width: 12cm
   :align: center

   A5L working space

.. figure:: ../../images/06_技术规格/A12L工作空间.*
   :width: 12cm
   :align: center

   A12L working space

.. _Control Cabinet Dimension:

Control Cabinet Dimension
==========================

.. figure:: ../../images/06_技术规格/CAB_L、CAB_H外形尺寸.*
   :width: 17.21cm
   :align: center

   Outline dimensions of CAB L/H

.. figure:: ../../images/06_技术规格/CAB_LiteAC外形尺寸.*
   :width: 12.35cm
   :align: center

   Outline dimensions of CAB LiteAC

.. figure:: ../../images/06_技术规格/CAB_LiteDC外形尺寸.*
   :width: 13.17cm
   :align: center

   Outline dimensions of CAB LiteDC

.. _Electrical Specifications:

Electrical Specifications
+++++++++++++++++++++++++++

.. include:: Electrical Specifications.rst

.. _Indicators:

Indicators
+++++++++++++

.. _Ring-Shaped-Light:

Ring-Shaped Light
====================

Ring‑shaped indicator light on the Joint 6 lid indicates the robot status. 
The position of the ring-shaped lights is shown in figure below.

.. figure:: ../../images/06_技术规格/机器人末端灯.*
  :width: 8.11cm
  :align: center

  Ring-shaped light

.. list-table:: Meaning of ring-shaped light color
   :widths: 46 54
   :header-rows: 1

   * - **Color**
     - **Robot State**

   * - Blue
     - Powered on but disabled

   * - Green
     - Enabled

   * - Red
     - Failure/Protective stop

   * - Yellow
     - Freedrive mode

   * - Yellow flash
     - Pause

   * - Yellow flash
     - Single-step program debugging

.. _Camera-Light:

Camera Light
=============

A 2.5D camera is integrated at the robot’s end effector flange, supporting applications such as dimensional measurement, positioning guidance, color recognition, track-and-grasp operations, presence/absence detection. Two status indicator lights are mounted on both sides of the camera, with color meanings as follows.

.. figure:: ../../images/06_技术规格/相机灯.*
   :width: 13cm
   :align: center

   Camera light

.. list-table:: Meaning of camera light color
   :widths: 46 54
   :header-rows: 1

   * - **Color**
     - **Robot State**

   * - Red
     - Camera powered up, and offline

   * - Green
     - Camera powered up, and online

   * - Green flash
     - Camera live imaging

.. _I-O-Indicators:

I/O Indicators
==============

.. figure:: ../../images/06_技术规格/I-O指示灯.*
   :width: 16.86cm
   :align: center

   I/O indicators

| **1** I/O indicators
| **2** PNP/NPN indicators

The I/O indicator lights are on the right of the interface on the front panel of the control cabinet, displaying a yellow-green color. The indicator lights illuminate when the interface is connected. Besides the I/O indicator lights on the right side of the interface, there are two PNP and NPN indicator lights above the P7 to P10 interfaces. The NPN indicator displays blue, and the PNP indicator displays yellow-green. When the interface is configured as NPN and connected, the upper blue indicator light illuminates. When the interface is configured as PNP and connected, the upper yellow-green indicator light illuminates.

.. _Maintenance-Indicator:

Maintenance Indicator
=====================

Maintenance indicators are on the front panel of the control cabinet to display the status of the control cabinet.

.. figure:: ../../images/06_技术规格/维护指示灯.*
   :width: 8cm
   :align: center

   Maintenance indicator

.. list-table:: Meaning of maintenance indicator
   :widths: 14 13 73
   :header-rows: 1

   * - **Name**
     - **Color**
     - **Description**

   * - 5V_S
     - Green
     - Slave MCU power supply status indicator. Indicator is lit when power supply is normal.

   * - 5V_M
     - Green
     - Master MCU power supply status indicator. Indicator is lit when power supply is normal.

   * - B_L
     - Red
     - Button cell indicator. Indicator is lit when battery is low, which means the button cell should be replaced immediately according to procedures in the CAB V3 Service Manual.

   * - B_H
     - Green
     - Button cell indicator. Indicator is lit when battery charge is sufficient.

   * - Power
     - Green
     - Robot powering on indicator. Indicator is lit when robot is powered on.

   * - E_M
     - Red
     - Master MCU status indicator. Indicator is lit during Master MCU malfunctions.

   * - E_S
     - Red
     - Slave MCU status indicator. Indicator is lit during Slave MCU malfunctions.

   * - 24V_IN
     - Green
     - Control cabinet powering on indicator. Indicator is lit when control cabinet is powered on.

   * - 4G
     - Green
     - 4G status indicator. Indicator is lit when 4G connection is normal.

   * - Wi-Fi
     - Green
     - Wi-Fi status indicator. Indicator is lit when wireless connection is established.

   * - IPC
     - Green
     - IPC status indicator. Indicator is lit when IPC functions normally.

   * - ER_M
     - Red
     - EtherCAT communication status indicator of Master MCU. Indicator is lit during communication abnormalities.

   * - ER_S
     - Red
     - EtherCAT communication status indicator of Slave MCU. Indicator is lit during communication abnormalities.

.. _Buttons:

Buttons
+++++++++

.. _Pause/Resume Button:

Pause/Resume Button
======================

A membrane button, serving as the Pause/Resume button, is located on the end cover of robot's Joint 6.

During program execution, pressing this button pauses the robot's motion. Pressing it again resumes motion. 
The button location is shown in the figure below.

.. figure:: ../../images/06_技术规格/暂停恢复按钮.*
  :width: 8.95cm
  :align: center

  Pause/Resume button

.. warning::

   User must first assess the risks of a sudden stop or start before using the Pause/Resume button. 
   Sudden stops or starts may cause injury to personnel or damage to the equipment.

.. _Free-and-Point-Buttons:

Free and Point Buttons
=========================

The robot is equipped with a tool I/O interface (TIO) and two buttons on the side of the flange. 
The two buttons are a freedrive button (FREE) and a point recording button (POINT), 
as shown in figure below.

.. figure:: ../../images/06_技术规格/末端法兰按钮.*
  :width: 14cm
  :align: center

  Free and point button

| **1** Free button
| **2** Point button

When the Free button is pressed, the robot enters the freedrive mode. 
The robot can be dragged to the desired position manually.

The Point button is used with the Coboπ. When this button is pressed, 
the corresponding position will show up in the programming interface of the App as a command (see Coboπ Software User Manual for details).

.. warning::
  
  User must first assess the risks before using the free drive and point buttons. 
  Ensure that the robot’s mounting orientation, end payload, TCP, and other parameters are correctly set, 
  otherwise it may cause injury to personnel or damage to the equipment.

.. _Reset-button:

Reset button
================

.. figure:: ../../images/06_技术规格/复位按钮.*
   :width: 20cm
   :align: center

   Reset button

There are two reset buttons on the control panel front: RST SYS and RST Wi-Fi, with the following functions:

**RST SYS:** User password reset button. Press and hold for 8 seconds, 
the administrator password for the currently connected robot will revert to default password (jakazuadmin) when connecting the robot through Coboπ.

**RST Wi-Fi:** Control cabinet's Wi-Fi reset button. Press and hold for 8 seconds, 
the Wi-Fi configuration is restored to factory default settings. 
This includes all parameters configured within the Coboπ “Wi-Fi Settings > AP Device Networking” interface.

The reset button is housed in a 2 mm diameter bore and can be depressed using a 1.5 mm slotted ESD-safe screwdriver.

.. _Robot Calibration Orientation:

Robot Calibration Orientation
+++++++++++++++++++++++++++++++

The robot calibration orientation is the orientation adopted during robot calibration. Calibration marks are 
engraved at joints and tubes, being used for recalibration after joint replacement. When all adjacent marks are 
aligned, the robot is in the calibration orientation. 

The joint angles for the calibration are listed below.

**A5L:**

.. list-table:: A5L calibration joint angle
   :widths: 17 17 17 17 17 15
   :header-rows: 1

   * - **Joint 1**
     - **Joint 2**
     - **Joint 3**
     - **Joint 4**
     - **Joint 5**
     - **Joint 6**

   * - 0°
     - 90°
     - 0°
     - 90°
     - 180°
     - 0°

.. figure:: ../../images/06_技术规格/A5L_标定姿态.*
   :width: 3cm
   :align: center

   A5L calibration orientation

**A12L:**

.. list-table:: A12L calibration joint angle
   :widths: 17 17 17 17 17 15
   :header-rows: 1

   * - **Joint 1**
     - **Joint 2**
     - **Joint 3**
     - **Joint 4**
     - **Joint 5**
     - **Joint 6**

   * - 180°
     - 90°
     - 0°
     - 0°
     - 90°
     - 180°

.. figure:: ../../images/06_技术规格/A12L_标定姿态.*
   :width: 2.5cm
   :align: center

   A12L calibration orientation

.. _Robot-Rotation-Direction:

Robot Rotation Direction
++++++++++++++++++++++++++

Refer to :ref:`Robot-Technical-Specifications` for robot rotation range. 
The rotation direction is as follows:

.. figure:: ../../images/06_技术规格/A5L_机器人旋转方向.*
   :width: 4.08cm
   :align: center

   A5L rotation direction

.. figure:: ../../images/06_技术规格/机器人旋转方向.*
   :width: 6cm
   :align: center

   A12L rotation direction

Robot Coordinate System
++++++++++++++++++++++++++

Base coordinate system:  

The origin is located at the center of the robot base. In the floor mounting orientation: 

- The +Z axis points vertically upward from the base toward the robot. 
- The +X axis points from the base center toward the interface of the robot connection cable port. 
- The +Y axis is defined by the right-hand rule. 

.. figure:: ../../images/06_技术规格/基座坐标系.*
   :width: 6cm
   :align: center

   Base coordinate system

Flange coordinate system (A5L): 

The origin is located at the center of the robot end flange. 

- The +Z axis points outward perpendicular to the flange. 
- The +Y axis points from the flange center toward the TIO interface. 
- The +X axis is defined by the right-hand rule.

.. figure:: ../../images/06_技术规格/法兰坐标系.*
   :width: 6cm
   :align: center

   A5L flange coordinate system

Flange coordinate system (A12L): 

The origin is located at the center of the robot end flange. 

- The +Z axis points outward perpendicular to the flange. 
- The -X axis points from the flange center toward the camera. 
- The +Y axis is defined by the right-hand rule.

.. figure:: ../../images/06_技术规格/A12L_法兰坐标系.*
   :width: 6cm
   :align: center

   A12L flange coordinate system

.. _Robot-Singularity:

Robot Singularity
++++++++++++++++++

Singularities are positions described in Cartesian space that have no impact on MoveJ. When the robot is at a singularity, replace the Cartesian movement by MoveJ if the motion can be achieved by MoveJ. If there is singularity in the middle of the robot’s motion path, the robot’s trajectory can be changed to bypass the singularity. You can also change the robot's mounting position or the size of the end effector to change the value of Cartesian points in the robot's joint space. A singularity is a robot arm configuration where one or more degrees of freedom are lost causing the robot to be stuck in a position and unable to move. This usually occur when joint axes align in one way or another.

When a robot is at a singularity, the following effects may occur:

- Robots cannot move in one or more directions.
- The robot cannot find a suitable set of joint angles for the TCP to move to the desired position.
- The robot joint should move at high speed to achieve the desired TCP speed.
- Intense movements near singularities will result in accidents and shorten the lifespan of robot joints.

.. _A5L Singularity:

A5L Singularity
==================

The JAKA A5L robot has three types of singularities: shoulder singularities, elbow singularities and wrist singularities. Descriptions and avoidance methods of the singularity are as follows.

**Shoulder singularity:** When the axes intersection of the joint 5 and joint 6 lies on the plane of axes of joint 1 and joint 2, the robot is at shoulder singularity.

.. figure:: ../../images/06_技术规格/肩部奇异姿态.*
   :width: 6cm
   :align: center

   Shoulder singularity

Ways to avoid shoulder singularity:

- Ensure that the robot TCP is not directly above the robot base. TCP cannot reach the positions directly above the robot. A shoulder singularity will occur if the TCP approaches a position directly in line with the base Z axis.
- Do not use MoveL when the angle of joint 1 is 180 between two points in space. When the difference is about 180°, the robot reaches shoulder singularity. You can use MoveJ to avoid singularity or set an intermediate transition point outside the shoulder singularity range.

**Elbow singularity:** When joints 2, 3 and 4 are coplanar or when joint 3 is 0°, the robot is at elbow singularity.

.. figure:: ../../images/06_技术规格/肘部奇异姿态.*
   :width: 7.23cm
   :align: center

   Elbow singularity

Ways to avoid elbow singularity:

- When the robot is at an elbow singularity, it indicates that the target position is close to the limits of the working range of the robot. At this point, it is necessary to adjust the robot mounting position or extend the length of the end effector.

**Wrist singularity:** When joint 4 and joint 6 are collinear or when joint 5 is 0°, the robot is in wrist singularity.

.. figure:: ../../images/06_技术规格/腕部奇异姿态.*
   :width: 6cm
   :align: center

   Wrist singularity

Ways to avoid wrist singularity:

- The wrist singularity typically occurs in movements with orientation changes. Therefore, in cases of considerable orientation change, it is advisable to prioritize MoveJ and not use Cartesian motions such as MoveL or MoveC.

.. _A12L Singularity:

A12L Singularity
==================

Due to the scattered locations of A12L singularities, it is not possible to list them all. The following figure shows typical singularity orientations. For specific singularities, the singularity prompts on the Coboπ will be the standard.

**1** When the joint 5 and joint 6 close to the plane of axes of the joint 1 and joint 2, the robot approaches singularity.

.. figure:: ../../images/06_技术规格/奇异姿态.*
   :width: 4.9cm
   :align: center

   A12L type 1 singularity

Ways to avoid singularity:

- Ensure that robot TCP do not near the area directly above the robot base. There are positions directly above the robot where the TCP cannot reach and the robot may in singularities during approaching this position.

- Do not use MoveL when the joint 1 difference between two points is around 180°. When the difference is about 180°, the robot may at singularity. You can use MoveJ to avoid singularity, or set an intermediate transition point outside the singularity range.

**2** When the joints 2, 3 and 4 close to coplanar, the robot approaches singularity.

.. figure:: ../../images/06_技术规格/奇异姿态_2.*
   :width: 5.41cm
   :align: center

   A12L type 2 singularity

Ways to avoid singularity:

- When the robot is at singularity, it indicates that the target position is close to the maximum workspace of the robot. At this point, it is necessary to adjust the robot mounting position or extend the length of the end effector.

**3** When the joint 4 and joint 6 close to coplanar, the robot approaches singularity.

.. figure:: ../../images/06_技术规格/奇异姿态_3.*
   :width: 6.01cm
   :align: center

   A12L type 3 singularity

Ways to avoid singularity:

- This singularity typically occurs in movements with orientation changes. Therefore, in cases of considerable orientation change, it is advisable to prioritize MoveJ and do not use Cartesian motions such as MoveL or MoveC.

.. _Button-Cell:

Button Cell
+++++++++++

The button cell is used to provide power for BIOS of the IPC and is located at the button cell compartment behind the control cabinet’s front panel. The following illustration shows the location of the button cell compartment. The button cell compartment location of CAB LiteAC and CAB LiteDC is identical with figure above and not shown repeatedly.

The cell model is CR2032.

.. figure:: ../../images/06_技术规格/纽扣电池位置.*
   :width: 7.95cm
   :align: center

   Position of button cell

Refer to CAB V3 Service Manual for button cell replacement.

.. _Wi-Fi-Function-Specification:

Wi-Fi Function Specification
++++++++++++++++++++++++++++

The control cabinet is equipped with a built-in Wi-Fi module. 
Its default network name (SSID) corresponds to the control cabinet's serial number, and the default password is “JKadmin123”.

.. csv-table::
   :file: ./tables/Wi-Fi specification.csv
   :encoding: utf-8-sig
   :widths: 26 16 28 30
   :header-rows: 2

.. container:: table-notes

   | :sup: `1` Alternatively: 100 mW (e.i.r.p = equivalent isotropically radiated power) 
   | :sup: `2` For 5,150...5,720 MHz. Alternatively: 200 mW (e.i.r.p = equivalent isotropically radiated power)
   | :sup: `3` For 5,720...5,825 MHz. Alternatively: 2000 mW (e.i.r.p = equivalent isotropically radiated power)

.. _Control-Stick-Buttons:

Control Stick Buttons
+++++++++++++++++++++

.. include:: Control Stick Buttons.rst

.. _Performance-Data:

Performance Data
++++++++++++++++

.. _Load-Capacity-of-the-Robot:

Load Capacity of the Robot
==========================

The maximum payload of the robot is related to the offset of the gravity center, and degree of the offset is related to the distance between the center of robot end flange and the payload centroid. Figures below show the relation between the payload and the offset of the gravity center:

- X: Center of gravity offset
- Y: Payload

.. figure:: ../../images/06_技术规格/A5负载偏心图.*
   :width: 15cm
   :align: center

   Load capacity of the A5L

.. figure:: ../../images/06_技术规格/A12L负载偏心图.*
   :width: 15cm
   :align: center

   Load capacity of the A12L

.. note::

   Offset distance is the center of gravity distance from the center of the flange.

.. _Stopping-Time-and-Distance:

Stopping Time and Distance
==========================

The time from the application of a stop signal to the standstill of the robot is measured. 
This measurement is carried out for various reaches and velocities (measurement according to ISO 10218-1).

Safety stopping time is the time it takes to stop the robot from the moment when the emergency stop button is pressed or a safety protection function is triggered. 
The stopping distance is the distance the end of the robot moves during the safety stopping time. Among them, pressing the emergency stop button falls into Cat.1, 
while triggering the safety protection function falls into Cat.2. During this period, the robot is still moving and may harm the personnel or other equipment. 
Therefore, users and integrators should consider this time and distance in risk assessment.

The test conditions are as follows:

- Speed: 100%, 66%, 33%
- Reach: 100%, 66%, 33%

.. list-table::
   :class: no-auto-merge
   :widths: 9 30 29 32
   :header-rows: 1

   * -
     - **100% Reach**
     - **66% Reach**
     - **33% Reach**

   * - **Joint 1**
     - .. figure:: ../../images/06_技术规格/J1-100.*
          :width: 4cm
          :align: center

     - .. figure:: ../../images/06_技术规格/J1-66.*
          :width: 3.6cm
          :align: center

     - .. figure:: ../../images/06_技术规格/J1-33.*
          :width: 3.6cm
          :align: center

.. list-table::
   :class: no-auto-merge
   :widths: 9 30 29 32
   :header-rows: 1

   * -
     - **100% Reach**
     - **66% Reach**
     - **33% Reach**

   * - **Joint 2**
     - .. figure:: ../../images/06_技术规格/J2-100.*
          :width: 4.29cm
          :align: center

     - .. figure:: ../../images/06_技术规格/J2-66.*
          :width: 3.6cm
          :align: center

     - .. figure:: ../../images/06_技术规格/J2-33.*
          :width: 3.6cm
          :align: center

.. list-table::
   :class: no-auto-merge
   :widths: 20 40 40
   :header-rows: 1

   * -
     - **100% Reach**
     - **66% Reach**

   * - **Joint 3**
     - .. figure:: ../../images/06_技术规格/J3-100.*
          :width: 2.76cm
          :align: center
     - .. figure:: ../../images/06_技术规格/J3-66.*
          :width: 2cm
          :align: center

- Load: See the table below.

.. list-table:: Load of stopping time and distance test
   :widths: 48 52
   :header-rows: 1

   * - **Model**
     - **Payload**

   * - A5L
     - 5 kg (11 lb)，7 kg (15.4 Ib)
   * - A12L
     - 12 kg (26.4 lb)

See :ref:`Appendix 1: Stopping Time and Distance` for the respective stopping distance and time of Cat.1 and Cat.2.

.. warning::

   **Breakdown of the internal joint holding brake:**

   - Take into account a possible breakdown of the internal joint holding brake during your risk assessment.
   - Take into account that the internal joint holding brake of the JAKA robot only withstands a limited number of brake operations.

   Failure to follow these instructions can result in death, serious injury, or equipment damage.

If there is a power interruption of the control system, the brakes are applied and the robot mechanics may leave the planned trajectory.

.. warning::

   **Leaving the planned trajectory of the robot mechanics:**

   - Use the buffering of the 24 V supply (UPS) in order to enable a controlled stop of the mechanics, in accordance with stop category 1, by making use of the stored residual mechanical and electrical energy.
   - Use a synchronous stop on the path to avoid collisions with obstacles.
   - Observe the extension of the run-on path while performing your risk assessment.

   Failure to follow these instructions can result in death, serious injury, or equipment damage.

.. _Forces-and-Torques-on-Robot-Base:

Forces and Torques on Robot Base
================================

The illustration shows the directions of the robot stress forces.

.. figure:: ../../images/06_技术规格/机器人底座力和转矩方向.*
   :width: 5.87cm
   :align: center

   Directions of forces and torques on robot base

| Fx: Force in X direction
| Mx: Bending torque in X direction
| Fy: Force in Y direction
| My: Bending torque in Y direction
| Fz: Force in Z direction
| Mz: Bending torque in Z direction

The table below shows the maximum forces and torques in various directions working on the robot base.

.. csv-table:: Forces and torques on robot base
   :file: ./tables/Forces and torques on robot base.csv
   :encoding: utf-8-sig
   :widths: 34 33 33
   :header-rows: 1

.. attention::

   These forces and torques are maximum values that are rarely encountered during operation. The values also never reach their maximum at the same time!

.. _Torques-on-Robot-Flange:

Torques on Robot Flange
=======================

The table below shows the maximum torques working on the robot flange.

.. csv-table:: Torques on robot flange
   :file: ./tables/Torques on robot flange.csv
   :encoding: utf-8-sig
   :widths: 34 33 33
   :header-rows: 1

.. _Camera-Field-of-View-(FOV):

Camera Field of View (FOV)
==========================

The camera's field of view (FOV) varies depending on the distance to the target object. Within this range, the FOV increases as the distance increases. Specific FOV values at key distances are shown in table below.

.. figure:: ../../images/06_技术规格/相机视野范围.*
   :width: 11cm
   :align: center

   Camera FOV

| a: Vertical field of view
| b: Horizontal field of view
| c: Working distance

.. list-table:: Camera FOV data of A5L
   :widths: 25 25 25 25
   :header-rows: 1

   * - **Working Distance (mm/in)**
     - **Vertical Field of View (mm/in)**
     - **Horizontal Field of View (mm/in)**
     - **Pixel Resolution (mm/px)**
   * - 100 (3.9)
     - 58.03 (2.3)
     - 69.36 (2.7)
     - 0.0283
   * - 200 (7.9)
     - 116.05 (4.6)
     - 138.72 (5.5)
     - 0.0567
   * - 300 (11.8)
     - 174.08 (6.9)
     - 208.08 (8.2)
     - 0.0850
   * - 400 (15.7)
     - 232.11 (9.1)
     - 277.44 (10.9)
     - 0.1133
   * - 500 (19.7)
     - 290.13 (11.4)
     - 346.80 (13.7)
     - 0.1417
   * - 600 (23.6)
     - 348.16 (13.7)
     - 416.16 (16.4)
     - 0.1700
   * - 1000 (39.4)
     - 580.27 (22.8)
     - 693.60 (27.3)
     - 0.2833

.. list-table:: Camera FOV data of A12L
   :widths: 32 32 36
   :header-rows: 1

   * - **Working Distance (mm/in)**
     - **Vertical Field of View (mm/in)**
     - **Horizontal Field of View (mm/in)**

   * - 80 (3.1)
     - 41 (1.6)
     - 55 (2.2)

   * - 150 (5.9)
     - 75 (3.0)
     - 99 (3.9)

   * - 230 (9.1)
     - 113 (4.4)
     - 149 (5.9)

   * - 300 (11.8)
     - 146 (5.7)
     - 194 (7.6)

   * - 400 (15.7)
     - 194 (7.6)
     - 257 (10.1)

   * - 600 (23.6)
     - 290 (11.4)
     - 383 (15.1)

   * - 1000 (39.4)
     - 481 (18.9)
     - 635 (25.0)

   * - 1500 (59.1)
     - 720 (28.3)
     - 951 (37.4)