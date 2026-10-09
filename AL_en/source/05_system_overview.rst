.. _System Overview:

System Overview
***************

.. _Compatibility:

Compatibility
++++++++++++++++

The compatibility between the |product_name| and the CAB V3 is as follows.

.. csv-table:: Compatibility
   :file: ./tables/Compatibility.csv
   :encoding: utf-8-sig
   :widths: 20 20 20 20 20
   :header-rows: 1
   :class: no-auto-merge

.. container:: table-notes

   :sup:`1` When pairing A12L with the CAB V3, the CAB L is required for regions with an input voltage of 200–240 V, while the CAB H is used in regions with an input voltage of 100–200 V.

.. _System Architecture:

System Architecture
+++++++++++++++++++++

When the robot is used with CAB L/H, the required components are as shown in figure below. 

.. figure:: ../../images/05_系统概述/机器人系统组成部件.*
   :width: 15cm
   :align: center

   Components with CAB L/H

When the robot is used with CAB LiteAC, the required components are as shown in figure below.

.. figure:: ../../images/05_系统概述/CAB_LiteAC系统部件.*
   :width: 15cm
   :align: center

   Components with CAB LiteAC

1. Control stick: Equipped with an emergency stop button and a three-position enabling switch. Used to start up or shut down the robot system, configure parameters, and move the robot.
2. Control cabinet: The control cabinet includes the core computing components and various electrical interfaces.
3. (User-supplied) Router and network cable: CAB V3 has a built-in Wi-Fi module which is accessible by any android, IOS or windows device. This allows the user to connect the JAKA App to the controller wirelessly with the SSID being the control cabinet serial number, and default password being JKadmin123. It is also possible to use a wired teach pendant, or connect the cabinet network port of the control cabinet to the router and the operation terminal to the wireless network of this router at the same time. It is recommended to configure a specialized router for the robot to prevent conflicts with other devices.
4. Control cabinet power cord: Provides power to the control cabinet.
5. Robot: A six axes robotic arm which moves as programmed by the user. It consists of a ring-shaped light; buttons for dragging and point teaching and a I/O interface for connecting tools (the TIO interface) on joint 6.
6. Robot connection cable: Connect the robot and the control cabinet.

When paired with the CAB LiteDC, the robot can be integrated into mobile platforms such as AGVs and powered directly by the AGV’s built‑in 48V traction battery. The control cabinet features a compact design, simplifies integration. The components necessary are illustrated in the figure below.

.. figure:: ../../images/05_系统概述/CAB_LiteDC系统部件.*
   :width: 15cm
   :align: center

   Components with CAB LiteDC

1. Control stick: Equipped with an emergency stop button and a three-position enabling switch. Used to start up or shut down the robot system, configure parameters, and move the robot.
2. Control cabinet: The control cabinet includes the core computing components and various electrical interfaces.
3. (User-supplied) Router and network cable: CAB V3 has a built-in Wi-Fi module which is accessible by any android, IOS or windows device. This allows the user to connect the JAKA App to the controller wirelessly with the SSID being the control cabinet serial number, and default password being JKadmin123. It is also possible to use a wired teach pendant, or connect the cabinet network port of the control cabinet to the router and the operation terminal to the wireless network of this router at the same time. It is recommended to configure a specialized router for the robot to prevent conflicts with other devices.
4. Robot: A six axes robotic arm which moves as programmed by the user. It consists of a ring-shaped light; buttons for dragging and point teaching and a I/O interface for connecting tools (the TIO interface) on joint 6.
5. Robot connection cable: Connect the robot and the control cabinet.
6. DC Power Supply: The control cabinet operates on DC power, with a 48V power supply recommended.

.. _Components Overview:

Components Overview
++++++++++++++++++++

The robot contains six joints and two connection arms. The base is used to connect the robot to the foundation, and the tool end flange is used to connect the robot to the end effector. The end effector can move and rotate in the workspace of the robot. This chapter will introduce the basic precautions during the installation of each component of the robot system.

The robot consists of six rotary joints and two connecting links: the upper arm and forearm. The wrist is equipped with a robot status light and a pause/resume button, and two buttons are located on the outside of the tool flange.

.. figure:: ../../images/05_系统概述/A5L_机器人.*
   :width: 7cm
   :align: center

   A5L robot

- 1 Base
- 2 Joint 1
- 3 Joint 2
- 4 Lower arm
- 5 Joint 3
- 6 Upper arm
- 7 Joint 4
- 8 Joint 5
- 9 Joint 6
- 10 Ring-shaped light
- 11 Flange and camera

.. figure:: ../../images/05_系统概述/机器人.*
   :width: 10cm
   :align: center

   A12L robot

- 1 Base
- 2 Joint 1
- 3 Joint 2
- 4 Lower arm
- 5 Joint 3
- 6 Joint 4
- 7 Upper arm
- 8 Joint 5
- 9 Joint 6
- 10 Ring-shaped light
- 11 Flange and camera

.. _Control Cabinet:

Control Cabinet
+++++++++++++++++

The JAKA CAB V3 is available in four models: CAB L, CAB H, CAB LiteAC, and CAB LiteDC. Among them, CAB L and CAB H are standard models powered by AC, while the CAB LiteAC and CAB LiteDC are compact models designed for integration into AGVs, CAB LiteAC is powered by AC and CAB LiteDC is powered by DC.

The JAKA control cabinet provides:

- Provide power supply for the robot
- Interface to connect the control stick
- Interface for the operator terminal either via cable or Wi-Fi connection
- Interfaces for several inputs and outputs of different kinds

.. _Control Stick:

Control Stick
+++++++++++++++++

The JAKA control stick provides:

- Emergency stop button to stop the robot in emergency
- Buttons to move the robot to specific orientation
- Button to start and stop the program
- Button to power up/down the control cabinet and power on/off or enable/disable the robot
