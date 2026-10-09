.. _Transport-and-Commissioning:

Transport and Commissioning
***************************

.. _Quick-Start-Guide:

Quick Start Guide
+++++++++++++++++

The following table provides a brief overview for robot usage:

.. csv-table:: Quick start guide
   :file: ./tables/Quick start guide.csv
   :encoding: utf-8-sig
   :widths: 7 17 46 30
   :header-rows: 1
   :class: merge-empty-vertical

.. _Transport and Storage:

Transport and Storage
+++++++++++++++++++++

.. _Transport Requirements:

Transport Requirements
======================

Please use the original packaging to transport the robot. If you want to move the robot later, please keep the original packaging.

When lifting the robot, secure and position it appropriately to prevent injury or damage caused by unexpected movement. See :ref:`Lifting` for the procedure.

When moving the robot from its packaging to the installation position, it should be supported by at least 2 persons until all screws at the robot base are securely fastened.

.. warning::

   - Ensure that the back or other body parts of the operators are not overloaded when the equipment is lifted. Use appropriate lifting equipment. JAKA is not responsible for damage incurred during the transport of the equipment. The robot must be supported by at least two persons depending on the model.
   - Please comply with the relevant lifting regulations in each region and country.
   - Ensure that installation instructions are strictly followed when the robot is installed.

.. attention::

   If the robot is transported without using its original packaging, all warranties will be voided.

.. _Storage Conditions:

Storage Conditions
==================

| 1. Storage temperature: -10 to 50°C (14 to 122°F)
| For long-term storage, maintain the temperature at 25 ± 10°C (59 to 95°F) to preserve reliability. Avoid rapid temperature changes of 10°C/h (18°F/h) or more.

| 2. Storage humidity: 20% to 85% RH
| For long-term storage, to maintain robot system reliability, it is recommended to keep the humidity within 45%~65%. Avoid condensation and mold growth.

| 3. Electrostatic discharge protection
| It is easy to generate static when kept in extremely dry conditions. The shock of electrostatic discharge may damage the semiconductor. Please store the robot system in an anti-static bag.

| 4. Other environmental conditions
| Please keep robot system in an environment that does not produce toxic gases, contaminants, and dust. Do not place heavy objects on it during storage.

.. _Unpacking:

Unpacking
+++++++++

The following figure presents the packaging of the JAKA robot and the control cabinet.

.. figure:: ../../images/07_运输及调试/机器人或控制柜外包装箱.*
   :width: 10cm
   :align: center

   Robot or control cabinet box

1. Open the box top side.
2. Lift up and remove the upper inner packaging part.
3. Inspect the robot and the control cabinet for transport damage.

.. _Handling:

Handling
+++++++++

.. _Robot Handling:

Robot Handling
==================

The table below shows the joint angle of packaging orientation. The robot can automatically change to this orientation by configuring it in the |jaka_app|. It is recommended to transport the robot in this orientation.

.. list-table:: Handling joint angle
   :widths: 16 14 14 14 14 14 14
   :header-rows: 1

   * - **Robot Module**
     - **Joint 1**
     - **Joint 2**
     - **Joint 3**
     - **Joint 4**
     - **Joint 5**
     - **Joint 6**

   * - A5L
     - -90°
     - 0°
     - 152°
     - 120°
     - 0°
     - 0°

   * - A12L
     - 90°
     - 180°
     - -180°
     - 180°
     - 90°
     - 90°

At least two persons are required for lifting and securing the robot during transportation. 
One person should hold the connection places between joint 1 and lower arm with both hands, while the other holds the connection places between joint 3 and lower arm with one hand, 
holds the connection places between joint 3 and upper arm with another hand, as shown in the figure below.

.. figure:: ../../images/07_运输及调试/正确搬运方式.*
   :width: 9.95cm
   :align: center

   Correct handling method

Lifting the robot by grabbing the robot's upper arm or joint 4/5/6 is strictly prohibited, as shown in the figure below. This action may cause damage to the internal structure of the robot.

.. figure:: ../../images/07_运输及调试/错误搬运方式.*
   :width: 9.15cm
   :align: center

   Incorrect handling method

.. _Control Cabinet Handling:

Control Cabinet Handling
==========================

CAB V3 can be handled by following two methods.

- Top lifting: Lift the control cabinet by pulling the top handle located on the cabinet's upper surface.

.. figure:: ../../images/07_运输及调试/提拉搬运CAB_L、CAB_H.*
   :width: 8.31cm
   :align: center

   Lifting CAB L and CAB H


- Side gripping: Raise the control cabinet by firmly gripping the two side handles on both lateral sides.

.. figure:: ../../images/07_运输及调试/抓握搬运CAB_L、CAB_H.*
   :width: 8.39cm
   :align: center

   Gripping CAB L and CAB H

.. figure:: ../../images/07_运输及调试/抓握搬运CAB_LiteAC、CAB_LiteDC.*
   :width: 8.67cm
   :align: center

   Gripping CAB LiteAC and CAB LiteDC

.. _Lifting:

Lifting
+++++++

Before securing the robot, move it to a suitable position. Lifting equipment must be used for robots weighing 30 kg (66.1 lb) or more. 
The following figure shows the lifting orientations for different mounting orientations. 
Lift the robot as shown.

.. _Robot lifting steps:

.. figure:: ../../images/07_运输及调试/吊装步骤图示.*
   :width: 15.33cm
   :align: center

   Robot lifting steps

.. list-table:: Robot lifting steps
   :widths: 6 25 45 24
   :header-rows: 1
   :class: merge-empty-vertical

   * -
     - **Description**
     - **Operations**
     - **References**
   * - 1
     - Transport
     -
     - :ref:`Transport and Storage` 
   * - 2~7
     - Opening the box
     - Remove the external foam, unwrap the carton and remove the internal foam.
     -
   * - 8~9
     - Lifting robot from box using sling
     - | Make robot in packing orientation and take 2 straps. One end of the first strap is located at the junction between joint three and the upper arm, crossing the rope at this location, with the other end at the junction between joint three and the lower arm. One end of the second strap is located at the junction between joint one and joint two, crossing the strap at this location, with the other end at the junction between joint two and the lower arm.
       | Once the straps are in place, use a hook to lift the two straps.
     - :ref:`Robot lifting steps` 
   * - 10
     - Floor mounting
     - Secure the robot to the mounting plane.
     - :ref:`Mounting the Robot <Mounting-the-Robot>`
   * - 11
     - Wall mounting
     - Adjust the robot position and secure the robot to the mounting plane.
     -
   * - 12
     - Inverted mounting
     - Secure the robot to the mounting plane.
     -

The sling should conform to the following standards:

| BS EN 1492-1 :2000+A1 :2008 Textile slings - Safety - Flat woven webbing slings, made of man-made fibers, for general purpose use.
| BS EN 1492-2 :2000+A1 :2008 Textile slings - Safety - Round slings, made of man-made fibers, for general purpose use.
| The lifting capacity of sling should be greater than 800 kg (1763.70 lb), the length of sling should be longer than 2 m (78.74 in).

.. warning::

   - Carefully inspect the sling before and after use.
   - Do not use the sling if it is cracked, ripped, or the stitching is loose.
   - Do not use the sling if there are signs of heat damage.
   - When using the sling, protect it against sharp edges and friction.
   - When lifting the robot, personnel must not, under any circumstances, be present under the sling and the robot.

.. _Mechanical-Installation:

Mechanical Installation
+++++++++++++++++++++++

.. _Mechanical Installation Safety Notice:

Mechanical Installation Safety Notice
=====================================

.. warning::

   - Ensure that the robot is installed correctly and safely.
   - The installation surface must be vibration-resistant and have sufficient load-bearing capacity.

.. warning::

   - Ensure that the end effector is installed correctly and safely.
   - Ensure the tool's safety to prevent any accidental falling of parts that could pose a danger.

.. warning::

   - Ensure that the control cabinet and cables are not exposed to liquids. A damp control cabinet can pose a risk of electric shock or fatal injury.
   - The control cabinet must not be exposed in dusty or humid environments exceeding IP44 levels. Pay close attention to environments with conductive dust.

.. warning::

   If the robot is submerged in water for an extended period, it may be damaged. Robots should not be installed in water or a humid environment.

.. _Mounting-the-Robot:

Mounting the Robot
==================

The robot can be mounted in various different positions. Several typical mounting methods are shown in figure below:

.. figure:: ../../images/07_运输及调试/机器人安装方式.*
   :width: 18cm
   :align: center

   Robot mounting positions

| 1 Floor mounting
| 2 Inverted mounting
| 3-4 Wall mounting

.. _Mounting-Surface-Requirements:

Mounting Surface Requirements
-----------------------------

Mount the robot on a rigid mounting surface. The surface must withstand the torques specified in :ref:`Forces and Torques on Robot Base <Forces-and-Torques-on-Robot-Base>` and must be sufficiently stiff to prevent deformation or vibration from causing significant tool center point (TCP) deviation. 
A steel mounting surface at least 20 mm (0.787 in) thick is recommended. Avoid mounting the robot directly on a hollow enclosure, as this can cause resonance and abnormal noise. 
If the robot is mounted on a linear axis or moving platform, keep the mounting-base acceleration low; high acceleration can cause false collision detection and stop the robot.

Account for the torque applied to the mounting surface during normal robot operation. See :ref:`Forces and Torques on Robot Base <Forces-and-Torques-on-Robot-Base>` for the applicable values.

.. warning::

   Do not connect the power during the robot mounting process.

.. attention::

   - When mounting the robot at a different angle, update the mounting angle in the software. See the |jaka_app| Software User Manual for details.
   - It is normal that the mounting holes of the robot are rusted or have traces of use. The JAKA robot needs to accept a series of performance tests before leaving the factory. Therefore, there will be traces in the mounting hole, which is not a quality problem and does not affect its use.
   - If the robot is not fixed on the foundation firmly, the mechanical structure of the robot may be unstable, and it may tip over.
   - When inverted mounting or wall mounting is adopted, the rigidity and stability of the mounting plane should be ensured, it is very dangerous to mount the robot on the wall or ceiling with insufficient intensity and rigidity, which may cause the robot to fall or vibrate, leading to severe injuries or serious damage to the robot.
   - The robot needs to be used in an environment that matches its IP level, which helps reduce the failure and extend the service life of the robot.

.. _Dimensions-of-Robot-Base:

Dimensions of Robot Base
------------------------

The following figure presents the installation dimensions of robot base.

.. figure:: ../../images/07_运输及调试/A5L_底座安装尺寸图.*
   :width: 15cm
   :align: center

   A5L base dimensions

.. figure:: ../../images/07_运输及调试/A12L_底座安装尺寸图.*
   :width: 15cm
   :align: center

   A12L base dimensions

.. _Robot Mounting Procedure:

Robot Mounting Procedure
------------------------

#. Use a lifting device when necessary for lifting up the robot out of the transport packaging.
#. Place the robot on the mounting surface and hold it in place while completing the next step.
#. Fasten the robot base to the mounting surface by using the four through holes. For additional fixing, centering pins can be added. The following table presents the tightening torque and size.

.. csv-table:: Robot mounting data
   :file: ./tables/Robot mounting data.csv
   :encoding: utf-8-sig
   :widths: 10 12 12 25 21 20
   :header-rows: 1

.. note::
   
   Grade 12.9 hexagon socket head cap screws are recommended. 
   The thread engagement depth should be 1.5 to 2 times the nominal thread diameter.

.. _Control Cabinet Installation:

Control Cabinet Installation
=============================

.. include:: Control Cabinet Installation.rst

.. _Electrical-Connections-of-the-Robot:

Electrical Connections of the Robot
+++++++++++++++++++++++++++++++++++

.. _Robot-Connection-Cable-Interface:

Robot Connection Cable Interface
================================

Use the robot connection cable provided by JAKA to connect the robot and the control cabinet. Before powering on the robot, ensure that the connector is locked firmly. Before disconnecting the robot connection cable, the robot must be powered off. The definition of the robot connection cable connector is shown as follows.

.. figure:: ../../images/07_运输及调试/A12L机器人连接线.*
   :width: 10cm
   :align: center

   Robot connection cable

**1 Y-Connector:** Dimensions as shown in the figure below.

.. figure:: ../../images/07_运输及调试/连接器尺寸.*
   :width: 10cm
   :align: center

   Connector dimension

**2** Plug with female connector includes housing and insert. 
Connect to the robot connection cable connector of CAB V3. 
For precise location, refer to :ref:`Bottom-Panel-Interfaces`.

Connector size and pin meanings are as table below.

.. figure:: ../../images/07_运输及调试/AL圆形连接器.*
   :width: 12cm
   :align: center

   Connector dimensions and pins

| A：DC+
| D：DC–
| PE
| 1：CAN_H
| 2：CAN_L

**3 RJ-45 Connector:** Connect to the LAN 1 port on the bottom panel of the JAKA CAB V3. 
For precise location, refer to :ref:`Bottom-Panel-Interfaces`.

Size of robot connection cable and connector are shown in figure below.

.. figure:: ../../images/07_运输及调试/机器人连接线及连接器尺寸.*
   :width: 12cm
   :align: center

   Size of robot connection cable and connector

.. warning::

   - Do not disconnect the robot connection cable while the robot is not powered off.
   - Do not extend or modify the original cable.

.. _Bending-Radius-of-Robot-Connection-Cable:

Bending Radius of Robot Connection Cable
----------------------------------------

When using robot connection cables with a cable carrier, to reduce cable wear, it is important to restrict the bending radius, speed, and acceleration of the cable carrier. 
The following table shows the diameter (OD) of the robot connection cables, the minimum bending radius, and the maximum speed and acceleration of the cable carrier for various robot models:

.. csv-table:: Specifications of robot connection cable
   :file: ./tables/Specifications of robot connection cable.csv
   :encoding: utf-8-sig
   :widths: 11 18 23 25 23
   :header-rows: 1
   :class: merge-empty-vertical

.. _Tool I/O Port:

Tool I/O Port
=============

The tool input/output interface (TIO) is located on the side of the robot flange. It provides two digital inputs, two digital outputs, and two analog inputs, and two channels can also be used for RS485 signals. See :ref:`Definition of End Effector Side <Definition of End Effector Side>` for the interface definition.

The TIO cable connector features a foolproof design to ensure correct installation. Align the raised part of the TIO connector with the concave groove on the TIO connector of the flange and insert the cable. The TIO position is as shown in the figure below.

.. figure:: ../../images/07_运输及调试/机器人工具I-O.*
   :width: 10.47cm
   :align: center

   Robot tool I/O

1 TIO

The definition and specifications of the TIO cable are as follows.

.. figure:: ../../images/07_运输及调试/TIO线尺寸图.*
   :width: 18cm
   :align: center

   TIO cable dimensions

| 1 Connect the robot flange
| 2 Connect the end effector

.. _Definition of End Effector Side:

Definition of End Effector Side
-------------------------------

The definition table of the TIO V3.0 interfaces is as follows:

.. list-table:: Specifications of TIO pins
   :widths: 9 19 9 12 51
   :header-rows: 1

   * - **Pin**
     - **Definition**
     - **I/O**
     - **Color**
     - **Description**

   * - 1
     - +24V
     - -
     - Red
     - Positive electrode, 24V/12V (switchable); configurable for enabling or disabling; continuous current capacity 1A; peak output current up to 2A.

   * - 2
     - DI1
     - I
     - Blue
     - Digital input 1: sink or source configurable

   * - 3
     - DI2
     - I
     - Green
     - Digital input 2: sink or source configurable

   * - 4
     - DO1/RS485A_1
     - O
     - Yellow
     - Digital output 1: sink, source, or push-pull configurable by application; current output capability ≤1A

       Multiplexed as RS485-1 communication A+

   * - 5
     - DO2/RS485B_1
     - O
     - Pink
     - Digital output 2: sink, source, or push-pull configurable by application; current output capacity ≤1A

       Multiplexed as RS485-1 communication B-

   * - 6
     - AIN1/RS485A_2
     - I
     - Brown
     - Analog input 1: detection range 0-10V 

       Multiplexed as RS485-2 communication A+

   * - 7
     - AIN2/RS485B_2
     - I
     - White
     - Analog input 2: detection range 0-10V

       Multiplexed as RS485-2 communication B-

   * - 8
     - GND
     - -
     - Gray
     - 24V negative electrode

.. _Wiring of End effector Side:

Wiring of End effector Side
---------------------------

.. _Digital Input:

Digital Input
-------------

The TIO provides two user DI channels compatible with both NPN and PNP signals. Configure the input type in the App; see the |jaka_app| Software User Manual for details.

**Dry contact input**

When the DI input is configured as sink:

The dry contact input (switch-type input) is connected to GND of TIO (gray wire) at one end, and to the digital input (blue or green wire) at the other end.

.. figure:: ../../images/07_运输及调试/NPN型干接点输入接线.*
   :width: 9.67cm
   :align: center

   Sink wiring of digital input

When the DI input is configured as source:

Connect one side of the dry-contact input (switch input) to 24 V on the TIO (red wire) and the other side to the digital input (blue or green wire).

.. figure:: ../../images/07_运输及调试/PNP型干接点输入接线.*
   :width: 9.72cm
   :align: center

   Source wiring of digital input

**Connecting NPN/PNP Devices**

The connection method of sink and source type digital input devices: V+ is connected to 24V of TIO (red wire), 0V is connected to GND of TIO (gray wire), and the signal wire is connected to the digital input of TIO (blue or green wire).

.. figure:: ../../images/07_运输及调试/连接外部NPN设备接线.*
   :width: 9cm
   :align: center

   Wiring of sink device for digital input

| A External sink device
| B TIO V3
| C Main circuit

.. _Digital Outputs:

Digital Outputs
-----------------

When the digital output interface is sink or source output, it adopts open drain output and the maximum continuous current output is 1A. Connection method: the external input interface is connected to the digital output of TIO (yellow or pink wire), V+ side of external device is connected to 24V of TIO (red wire), and 0V side of external device is connected to GND of TIO (gray wire).

.. figure:: ../../images/07_运输及调试/连接外部NPN设备接线_2.*
   :width: 9cm
   :align: center

   Wiring of sink device for digital output

| A External sink device
| B TIO V3
| C Main circuit

.. _RS485:

RS485
-----

Using the RS485 function, the wiring method: external RS485+ is connected to RS485+ of TIO (yellow or brown wire), external RS485- is connected to RS485- of TIO (pink or white wire), the V+ of external device is connected to the 24V of TIO (red wire), and 0V of external device is connected to the GND of TIO (gray wire).

.. figure:: ../../images/07_运输及调试/RS485接线.*
   :width: 9cm
   :align: center

   Wiring of RS485

| A External sink device
| B TIO V3
| C Main circuit

.. _Analog Inputs:

Analog Inputs
---------------

TIO supports 2 analog voltage input interfaces, and the voltage input range is 0-10V. The wiring method: the external analog voltage positive electrode is connected to AIN1/AIN2 of TIO (white and brown wire), and the internal circuit of the negative electrode on the TIO board is grounded. The V+ of external device is connected to the 24V of TIO (red wire), and 0V of external device is connected to the GND of TIO (gray wire).

.. figure:: ../../images/07_运输及调试/模拟输入接线.*
   :width: 9cm
   :align: center

   Wiring of analog input

| A External sink device
| B TIO V3
| C Main circuit

.. _Electrical Connections of the Control Cabinet:

Electrical Connections of the Control Cabinet
+++++++++++++++++++++++++++++++++++++++++++++

.. include:: Electrical Connections of the Control Cabinet.rst

.. _Initial-Start-Up:

Initial Start-Up
++++++++++++++++

.. include:: Initial Start-Up.rst

.. _Mounting-the-End-Effector:

Mounting the End-Effector
+++++++++++++++++++++++++

.. _mounting-end-effector-prerequisites:

Prerequisites
=============

Observe the following prerequisites to help avoid incorrect operation of the robot:

- Verify that the load conforms to the specified payloads for the robot before operating.
- Limit the maximum payload of the robot in accordance with the maximum load capacity of the robot. For further information, refer to :ref:`Load-Capacity-of-the-Robot`.

.. _Dimensions of Robot Flange:

Dimensions of Robot Flange
===========================

The following figure presents the installation dimensions of robot flange.

.. figure:: ../../images/07_运输及调试/A5L_末端法兰尺寸图.*
   :width: 16.79cm
   :align: center

   A5L flange dimensions

.. figure:: ../../images/07_运输及调试/A12L末端法兰尺寸图.*
   :width: 16.79cm
   :align: center

   A12L flange dimensions

.. _mounting-the-end-effector-1:

Mounting the End-Effector
=========================

End-effector mounting steps:

#. Fasten the end-effector to the mounting points provided for this purpose on the robot tool flange (**1**)
   
  | Pitch circle diameter DIN ISO 9409-1, 50 mm (1.97 in): 4x M6 (**2**), tightening torque: 13 Nm (115.05 lbf·in), property class of the screw: 12.9 or greater
  | Pitch circle diameter 50 mm (1.97 in): 1x fitting hole diameter 6 H7 (**3**)

   .. figure:: ../../images/07_运输及调试/AL末端法兰.*
      :width: 9cm
      :align: center

      Robot flange

   .. note::

      For robot flange dimensions, see :ref:`Dimensions of Robot Flange`.

#. Set the payload in |jaka_app|. See the |jaka_app| Software User Manual for the procedure.

.. note::

   - Observe the permissible weights and distances that results in load capacity of the robot.
   - According to ISO9409-1: 2004, the location pin hole center shall be aligned with the mechanical interface coordinate system (ISO 9787:2013)+Xm, and our product is offset 45° clockwise on this basis.
