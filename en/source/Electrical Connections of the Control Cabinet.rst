.. _Overview:

Overview
========

This chapter introduces the interfaces on the control cabinet.

.. attention::
    
    Always inspect connectors for dirt or damage before connecting them to the control cabinet. Clean or replace any damaged parts.

.. _Grounding and Shielding Connections:

Grounding and Shielding Connections
===================================

.. _Grounding Requirements:

Grounding Requirements
----------------------

The control cabinet protective earth must be connected to the power-supply PE conductor. 

   - The grounding cable must be green/yellow. 
   - The control cabinet, robot arm, and peripheral equipment must share the same ground, preferably an equipotential bonding network (mesh). 
   - Grounding points must provide a stable metal-to-metal connection, such as a bolted connection. Remove paint, dust, rust, and other insulating material from the contact surfaces. 

For marking requirements for power grounding connections inside the control cabinet, see UL 508C. 
For further guidance on grounding-system design, see IEC 61000-5-2. For PE conductor cross-sectional area requirements, see IEC 60204-1.

.. _Grounding Position:

Grounding Position
--------------------

The following illustration shows the location of protective earth.

Both CAB L and CAB H are equipped with five protective earth terminals. Two terminals are pre-assigned at factory settings. Select appropriate grounding positions from the remaining three terminals based on site-specific requirements.

.. figure:: ../../images/07_运输及调试/CAB_L、CAB_H接地位置.*
   :width: 10cm
   :align: center

   Grounding position of CAB L and CAB H

.. figure:: ../../images/07_运输及调试/CAB_LiteAC接地位置.*
   :width: 10cm
   :align: center

   Grounding position of CAB LiteAC

.. figure:: ../../images/07_运输及调试/CAB_LiteDC接地位置.*
   :width: 10cm
   :align: center

   Grounding position of CAB LiteDC

.. _Power-Connection:

Power Connection
================

.. _prerequisites-1:

Prerequisites
-------------

Before power supply is connected to the control cabinet, the following prerequisites must be fulfilled:

- An external circuit breaker or fuse must be installed.
- The cabinet must be connected to protective earth.
- A residual current device (RCD) must be installed.

.. _Locking-out-Electrical-Power:

Locking out Electrical Power
----------------------------

Refer to IEC60204 Safety of Machinery - Electrical Equipment and UL508A Safety Standard for Industrial Control Panels. To prevent personnel injury or property loss caused by the unreasonable release of dangerous energy, it is recommended that the plugs of all equipment in the application of the robot are equipped with power plug locks to lock and tag them during maintenance.

The figure below shows the location of the safety lock on the power input switch.

.. figure:: ../../images/07_运输及调试/挂锁位置.*
   :width: 7.04cm
   :align: center

   Power lock position

The following illustration shows the dimension of the lock.

.. figure:: ../../images/07_运输及调试/挂锁尺寸.*
   :width: 8.15cm
   :align: center

   Power lock dimension

.. _power-connection-1:

Power Connection
----------------

The following illustration shows the power connection location of control cabinet.

.. figure:: ../../images/07_运输及调试/CAB_L、CAB_H电源接口位置.*
   :width: 10cm
   :align: center

   Power connection position of CAB L and CAB H

.. figure:: ../../images/07_运输及调试/CAB_LiteAC电源接口位置.*
   :width: 10cm
   :align: center

   Power connection position of CAB LiteAC

.. figure:: ../../images/07_运输及调试/CAB_LiteDC电源接口位置.*
   :width: 10cm
   :align: center

   Power connection position of CAB LiteDC

The model of connector connecting the control cabinet is DGH4-01P-1Y, DEGSON. 
Refer to :ref:`Wire Specifications of Control Cabinet Interfaces <Wire-Specifications-of-Control-Cabinet-Interfaces>` for wire specifications.

The following shows the power connection steps for CAB LiteDC.

#. Remove three screws on the power connector by a slotted screwdriver.

  .. figure:: ../../images/07_运输及调试/螺钉拆卸.*
     :width: 10cm
     :align: center

     Remove screws

#. Insert the PE wire (Protective Earth) and the positive/negative power wires into the power terminal block in the sequence shown in the figure below.

  .. figure:: ../../images/07_运输及调试/电源接口示意.*
     :width: 10cm
     :align: center

     Power connector illustration

#. Tighten screws by a slotted screwdriver, then gently pull the wire to test if it is inserted firmly.

  .. figure:: ../../images/07_运输及调试/螺钉安装.*
     :width: 10cm
     :align: center

     Secure screws

.. _Isolated-Power-Supply-Connection:

Isolated Power Supply Connection
--------------------------------

When using the CAB LiteDC, if its serial number meets the **LiteDC10** xxxxxx or **LiteDC11** xxxxxx, it must be connected to a 48 V DC-DC converter (isolated). The recommended model is the SD-1000L-48 or the LITEON DD-2102-3LA. The following illustrations show the wiring.

.. figure:: ../../images/07_运输及调试/隔离电源接线.*
   :width: 10cm
   :align: center

   Isolated power supply connection

| A: DC-DC converter (isolated)
| B: Power supply
| C: Other devices

.. _Power-Cord-Type:

Power Cord Type
---------------

Different countries and regions have different standards, and JAKA supports corresponding plugs when products are exported overseas. Specifications are as follows:

.. csv-table:: Specifications of power cords
   :file: ./tables/Specifications of power cords.csv
   :encoding: utf-8-sig
   :widths: 10 12 13 12 11 11 8 8 15
   :header-rows: 1
   :class: merge-empty-vertical

.. _Robot-Connection:

Robot Connection
================

The following illustration shows the location of the robot connection interface.

.. figure:: ../../images/07_运输及调试/CAB_L、CAB_H机器人连接线接口位置.*
   :width: 6.16cm
   :align: center

   Robot connection position of CAB L and CAB H

.. figure:: ../../images/07_运输及调试/CAB_LiteAC、CAB_LiteDC机器人连接线接口位置.*
   :width: 7.38cm
   :align: center

   Robot connection position of CAB LiteAC and CAB LiteDC

Robot connection steps:

#. Align the circular mark and triangular mark on the robot-side connector with the triangular mark on the cabinet-side connector, ensuring all three markers are in a straight line.

  .. figure:: ../../images/07_运输及调试/对齐标记.*
     :width: 7.38cm
     :align: center

     Align marks

#. Insert the two terminals into each other. If you feel resistance, slightly rotate the connector to align it properly—do not force the connection.

   .. figure:: ../../images/07_运输及调试/对插端子.*
      :width: 7.13cm
      :align: center

      Insert connectors

#. Once inserted, rotate the robot-side connector according to the indicator arrow on the robot-side connector to lock it in place.

   .. figure:: ../../images/07_运输及调试/锁紧端子.*
      :width: 6.96cm
      :align: center

      Lock connectors

.. _Control-Stick-Connection:

Control Stick Connection
=========================

The following illustration shows the location of the control stick connection interface.

.. figure:: ../../images/07_运输及调试/CAB_L、CAB_H手柄接口位置.*
   :width: 6.97cm
   :align: center

   Control stick connection position of CAB L and CAB H

The connection steps of control stick are the same as those for the robot. Refer to :ref:`Robot Connection <Robot-Connection>`.

.. figure:: ../../images/07_运输及调试/CAB_LiteAC-DC手柄接口位置（旧）.*
   :width: 8cm
   :align: center

   Control stick connection position of CAB LiteAC/DC (Legacy version)

.. _fig-Control stick connection position of CAB LiteAC/DC (Latest version):

.. figure:: ../../images/07_运输及调试/CAB_LiteAC-DC手柄接口位置（新）.*
   :width: 8cm
   :align: center

   Control stick connection position of CAB LiteAC/DC (Latest version)

.. note::
    
    For control cabinets with serial numbers LiteAC11000006, LiteDC11000006 and above, see :ref:`fig-Control stick connection position of CAB LiteAC/DC (Latest version)` .

.. _Bottom-Panel-Interfaces:

Bottom Panel Interfaces
=======================

.. _Bottom-Panel-of-CAB-H-L:

Bottom Panel of CAB H/L
-----------------------

The following shows the interfaces on the bottom panel.

.. figure:: ../../images/07_运输及调试/CAB_L、CAB_H底面板（旧）.*
   :width: 8.6cm
   :align: center

   Bottom panel of CAB L and CAB H (Legacy version)

.. _fig-Bottom panel of CAB L and CAB H (Latest version):

.. figure:: ../../images/07_运输及调试/CAB_L、CAB_H底面板（新）.*
   :width: 9.24cm
   :align: center

   Bottom panel of CAB L and CAB H (Latest version)

**1 Cable gland:** Used to route internal cables out of the control cabinet. The operation steps are as follows:

  - Loosen the two M3 screws using a hex screwdriver and remove the cable gland assembly.

    .. figure:: ../../images/07_运输及调试/形_1_4.*
      :width: 10.28cm
      :align: center

  - Remove the two support plates.

    .. figure:: ../../images/07_运输及调试/形_1_5.*
      :width: 6.25cm
      :align: center

  - Select and remove the appropriate rubber grommet based on the diameter of wire bundle.

    .. figure:: ../../images/07_运输及调试/形_1_6.*
      :width: 7.4cm
      :align: center

  - Install the two support plates onto the cable gland assembly.

    .. figure:: ../../images/07_运输及调试/形_1_7.*
      :width: 6.28cm
      :align: center

  - Align the screw holes of the cable gland assembly with those on the control cabinet's bottom panel. Tighten the two M3 screws using a hex screwdriver to secure the cable gland assembly.

    .. figure:: ../../images/07_运输及调试/形_1_8.*
      :width: 10.26cm
      :align: center

    .. figure:: ../../images/07_运输及调试/形_1_9.*
      :width: 10.26cm
      :align: center

  - Route the internal wire bundle of the control cabinet out through this cable gland.

    .. figure:: ../../images/07_运输及调试/形_1_10.*
      :width: 10.09cm
      :align: center

| **2 Robot connection cable interface:** Connection interface between the robot arm and the control cabinet.
| **3 LAN outlet:** This port is used to lead out the internal network port from the control cabinet. There are two network ports, both of which are Gigabit Ethernet ports. This outlet is specifically for LAN1; LAN2 can be led out from other cable outlets. The network ports are configured as follows:

  - LAN1: Can be configured for dynamic or static IP. Default is static IP (10.5.5.100).
  - LAN2: Can be configured for dynamic or static IP. Default is dynamic IP.

The interface type can be quickly identified via the front-panel label.

.. note::
    
    Control cabinets with serial numbers CABH11000021, CABL11000031 and above feature an additional cable outlet on the bottom panel, 
    providing a dedicated outlet for each of the two network ports, 
    as shown in :ref:`Bottom panel of CAB L and CAB H (Latest version) <fig-Bottom panel of CAB L and CAB H (Latest version)>`. 
    These are designated as 3a for LAN1 and 3b for LAN2.

| **4 Control stick cable interface:** Connection interface to the control stick or teach pendant.
| **5 Power cord interface:** Connection interface to the external AC power outlet.

.. _Bottom-Panel-of-CAB-LiteAC:

Bottom Panel of CAB LiteAC
--------------------------

.. figure:: ../../images/07_运输及调试/CAB_LiteAC底面板.*
   :width: 12cm
   :align: center

   Bottom panel of CAB LiteAC

| **1** **Expansion I/O interface:** Used when installing optional expansion I/O modules.
| **2** **SD card slot** (currently disabled).
| **3** **HDMI interface:** Internal debugging port.
| **4** **USB interface:** Internal debugging port.
| **5** **LAN1:** Gigabit Ethernet port. Can be configured for dynamic or static IP. Default is static IP (10.5.5.100).
| **6** **LAN2:** Gigabit Ethernet port. Can be configured for dynamic or static IP. Default is dynamic IP.
| **7** **Control stick cable interface:** Connection interface to the control stick or teach pendant. The Ethernet port (LAN3) provides network for the Touch I tablet or for the Touch II.

  - LAN3: It is set to a static IP (192.168.101.1) by default and cannot be modified.

| **8** **Power cord interface:** Connection interface to the external AC power outlet.
| **9** **Robot connection cable interface:** Connection interface between the robot arm and the control cabinet.
| **10** **Wire fixing post:** Used to secure wires. Must be used with cable tie mounts (recommended model: KSS HC-1S).

.. _Bottom-Panel-of-CAB-LiteDC:

Bottom Panel of CAB LiteDC
--------------------------

.. figure:: ../../images/07_运输及调试/CAB_LiteDC底面板.*
   :width: 12cm
   :align: center

   Bottom panel of CAB LiteDC

| **1 Expansion I/O interface:** Used when installing optional expansion I/O modules.
| **2 SD card slot** (currently disabled).
| **3 HDMI interface:** Internal debugging port.
| **4 USB interface:** Internal debugging port.
| **5 LAN1:** Gigabit Ethernet port. Can be configured for dynamic or static IP. Default is static IP (10.5.5.100).
| **6 LAN2:** Gigabit Ethernet port. Can be configured for dynamic or static IP. Default is dynamic IP.
| **7 Control stick cable interface:** Connection interface to the control stick or teach pendant. The Ethernet port (LAN3) provides network for the Touch I tablet or for the Touch II.

  - LAN3: It is set to a static IP (192.168.101.1) by default and cannot be modified.

| **8 Power cord interface:** Connection interface to the external DC power outlet. Refer to :ref:`Power-Connection` for details of interfaces.
| **9 Robot connection cable interface:** Connection interface between the robot arm and the control cabinet.
| **10 Wire fixing post:** Used to secure wires. Must be used with cable tie mounts (recommended model: KSS HC-1S).

.. _Front-Panel-Interfaces:

Front Panel Interfaces
======================

.. figure:: ../../images/07_运输及调试/控制柜前面板接口.*
   :width: 20cm
   :align: center

   Front panel of control cabinet

Upon opening the control cabinet door, the following front panel interfaces are visible:

- Emergency stop, protective stop, and remote power on/off interfaces (P1)
- 16 safety digital inputs (P2 and P3)
- 16 safety digital outputs (P4 and P5)
- RS485 and encoder interfaces (P6)
- 16 digital inputs (P7 and P8)
- 16 digital outputs (P9 and P10)
- Power interfaces (P11)
- Power and internal debug interfaces (P12)

Interfaces above feature status indicators that illuminate when activated.

.. _Electrical-Interface:

Electrical Interface
--------------------

.. csv-table:: Descriptions of interfaces on front panel
   :file: ./tables/Descriptions of interfaces on front panel.csv
   :encoding: utf-8-sig
   :widths: 9 20 9 10 52
   :header-rows: 1

.. _Remote-On-Off-Interfaces:

Remote On/Off Interfaces
------------------------

The interfaces are located on pin7 and pin8 of P1. 
This interface allows powering up/down the control cabinet remotely without using |jaka_app| or the teach pendant. 
Users can integrate it into a PLC system for remote control.

The interface is triggered when receiving 24V power (reference ground is V-). 
It is equivalent to the control stick's **Power** button.

.. _Remote-On:

Remote On
---------

.. figure:: ../../images/07_运输及调试/远程开机接口.*
   :width: 3cm
   :align: center

   Remote on interfaces

The following illustrations show the wiring of remote on.

.. figure:: ../../images/07_运输及调试/远程开机-内部电源.*
   :width: 3cm
   :align: center

   Remote on (Connect internal power)

.. figure:: ../../images/07_运输及调试/远程开机-外部电源.*
   :width: 3cm
   :align: center

   Remote on (Connect external power)

.. _Remote-Off:

Remote Off
----------

.. figure:: ../../images/07_运输及调试/远程关机接口.*
   :width: 3cm
   :align: center

   Remote off interfaces

The following illustrations show the wiring of remote off.

.. figure:: ../../images/07_运输及调试/远程关机-内部电源.*
   :width: 3cm
   :align: center

   Remote off (Connect internal power)

.. figure:: ../../images/07_运输及调试/远程关机-外部电源.*
   :width: 3cm
   :align: center

   Remote off (Connect external power)

.. attention::

   Remote on and off interfaces cannot be shorted at the same time.

.. _Emergency-Stop-Interface:

Emergency Stop Interface
------------------------

Emergency stop interfaces are located on pin3 and pin4 of P1, which can make robot stop in emergency condition. Emergency stop interfaces are paired (redundant), 
thus, the function can be activated when either signal is valid. If you intend to use external safety devices, 
please select devices that support dual-channel design. Users can access security doors, security light curtains, sensors, etc., 
according to actual safety requirements.

.. figure:: ../../images/07_运输及调试/急停接口.*
   :width: 3cm
   :align: center

   Emergency stop interfaces

.. _Default-Configuration:

Default Configuration
---------------------

Emergency stop interface is shorted to the internal 24V by default. The following illustration shows the wiring.

.. figure:: ../../images/07_运输及调试/急停接口出厂接线.*
   :width: 3.01cm
   :align: center

   Default wiring of emergency stop

.. _Connect-External-Devices:

Connect External Devices
------------------------

In most applications, to facilitate safety-related operations, one or more additional emergency stop switch is needed. The following illustration shows the wiring.

.. figure:: ../../images/07_运输及调试/急停接线-单路.*
   :width: 6.42cm
   :align: center

   Connect emergency stop device (single)

.. figure:: ../../images/07_运输及调试/急停接线-多路.*
   :width: 6.42cm
   :align: center

   Connect emergency stop device (multiple)

It is possible to operate the robot without the control stick. 
In this case, an additional emergency stop device should be connected. 
You can use the emergency stop interfaces on the front panel of the control cabinet to connect the emergency stop switch to ensure safety.

.. warning::
    
    - If the control stick is detached or disconnected from the robot, the emergency stop button is no longer active. You must remove the control stick from the vicinity of the robot.
    - The power supply for the emergency stop interface must be provided internally by the control cabinet via pin 11 and pin 12 of the P1 interface. The use of an external power supply is prohibited. Using an external power supply may damage the internal safety circuits of the control cabinet, resulting in equipment failure or safety hazards.

.. _Protective-Stop-Interface:

Protective Stop Interface
-------------------------

Protective stop interfaces are located on pin5 and pin6 of P1, which can make robot stop in certain condition. 
Protective stop interfaces are paired (redundant), thus, the function can be activated when either signal is valid. 
If you intend to use external safety devices, please select devices that support dual-channel design. 
Users can access security doors, security light curtains, sensors, etc., according to actual safety requirements.

.. figure:: ../../images/07_运输及调试/保护性停止接口.*
   :width: 3cm
   :align: center

   Protective stop interfaces

.. _default-configuration-1:

Default Configuration
---------------------

Protective stop interface is shorted to the internal 24V by default. The following illustration shows the wiring.

.. figure:: ../../images/07_运输及调试/保护性停止接口出厂接线.*
   :width: 3.05cm
   :align: center

   Default wiring of protective stop

.. _Connect-Protective-Stop-Devices:

Connect Protective Stop Devices
-------------------------------

In most applications, to facilitate the safety-related operations, one or more additional protective stop switch is needed. The following illustration shows the wiring.

.. figure:: ../../images/07_运输及调试/保护性停止接线-单路.*
   :width: 5.09cm
   :align: center

   Connect protective stop device (single)

.. figure:: ../../images/07_运输及调试/保护性停止接线-多路.*
   :width: 5.03cm
   :align: center

   Connect protective stop device (multiple)

.. warning::
    
    The power supply for the emergency stop interface must be provided internally by the control cabinet via pin 11 and pin 12 of the P1 interface. 
    The use of an external power supply is prohibited. 
    Using an external power supply may damage the internal safety circuits of the control cabinet, resulting in equipment failure or safety hazards.

.. _Safety-I-O-Interface:

Safety I/O Interface
--------------------

.. figure:: ../../images/07_运输及调试/P12接口.*
   :width: 2.71cm
   :align: center

   P12 interface

The safety I/O can be powered by the 24V internal supply from the control cabinet, with a peak current output of 3A (output shutdown on overload; recommended sustained output ≤2 A).

IN_V+ is positive electrode of internal power, IN_V- is internal GND, V+ is positive electrode of all digital I/O interfaces, and V- is negative electrode of all digital I/O interfaces.

.. _default-configuration-2:

Default Configuration
---------------------

Safety I/O interface is shorted to the internal power supply by default. The following illustration shows the wiring.

.. figure:: ../../images/07_运输及调试/安全I-O接口出厂接线.*
   :width: 3cm
   :align: center

   Default wiring of safety I/O

.. _Connect-External-Power-Supply:

Connect External Power Supply
-----------------------------

When requiring higher power output, an external 24V power supply can be connected to the V+. 
Current of single channel cannot exceed 0.5 A. Please remove the jumpers of IN_V+ and V+, IN_V– and V– before connecting external power.

.. figure:: ../../images/07_运输及调试/安全I-O接口外接电源.*
   :width: 3cm
   :align: center

   Connect external power supply of safety I/O

.. _Safety-Function:

Safety Function
---------------

.. figure:: ../../images/07_运输及调试/安全I-O接口.*
   :width: 10.77cm
   :align: center

   Safety I/O interfaces

Safety I/O interfaces are located on P2 to P5.

Safety I/O is paired (redundant), where a failure in one channel will not compromise the safety function. 
Therefore, when wiring, both paired safety I/Os should be connected simultaneously. 
For example, when connecting DI1, DI2 must be connected simultaneously. 
The pairing relationship of the safety I/O is as follows:

.. list-table:: Safety I/O pairs
   :widths: 44 56
   :header-rows: 1

   * - **Digital Input**
     - **DO**

   * - DI1 & DI2
     - DO1 & DO2

   * - DI3 & DI4
     - DO3 & DO4

   * - DI5 & DI6
     - DO5 & DO6

   * - DI7 & DI8
     - DO7 & DO8

   * - DI9 & DI10
     - DO9 & DO10

   * - DI11 & DI12
     - DO11 & DO12

   * - DI13 & DI14
     - DO13 & DO14

   * - DI15 & DI16
     - DO15 & DO16

The wiring is as follows, take DI9&DI10 as an example, same as others.

.. figure:: ../../images/07_运输及调试/安全功能接线.*
   :width: 5.93cm
   :align: center

   Wiring of safety functions

A: Safety device

.. _Digital-Input-Interface:

Digital Input Interface
-----------------------

.. figure:: ../../images/07_运输及调试/数字输入接口.*
   :width: 5.27cm
   :align: center

   Digital input interface

The 16 digital input interfaces are located on the P7 and P8, which supports isolated signal input and are PNP/NPN configurable. 
DI1~DI8 must be configured collectively as either PNP or NPN, and DI9~DI16 must also be configured collectively as either PNP or NPN. 
Individual DI channel switching is not available.

V+ supports external 24V power input, shorted to internal 24V by default. 
When connecting external power, the jumpers should be unplugged. 
The factory default wiring is consistent with the safety I/O’s wiring. 
Refer to the :ref:`Default Configuration <default-configuration-2>`.

.. _Dry-contact-signal-as-input:

Dry contact signal as input
---------------------------

When the dry contact is input, one wire is connected to V+ (PNP) or V– (NPN), and the other is connected to the specified DI channel. 
When the circuit is connected (switch or relay is activated as shown in illustration below), the corresponding indicator on the panel illuminates. 
The corresponding indicator will light on in the |jaka_app| at the same time. The following illustrations show the wiring.

.. figure:: ../../images/07_运输及调试/干接点信号作为输入-PNP.*
   :width: 3.76cm
   :align: center

   PNP

.. figure:: ../../images/07_运输及调试/干接点信号作为输入-NPN.*
   :width: 2.99cm
   :align: center

   NPN

.. _PNP-Signal-as-Input:

PNP Signal as Input
-------------------

When the input signal is PNP type, the following illustration shows the wiring of DI, same as DI2~DI16.

Positive electrode of external device connects to V+ of control cabinet, the OUT signal wire connects to the specified DI, 
and negative electrode of external device connects to V- of control cabinet. When the signal is activated, 
the corresponding indicator on the panel illuminates. 
The corresponding indicator will light on in the |jaka_app| at the same time.

.. figure:: ../../images/07_运输及调试/PNP型信号作为输入接线.*
   :width: 8.33cm
   :align: center

   Wiring of digital input when PNP signal as input

.. _NPN-Signal-as-Input:

NPN Signal as Input
-------------------

When the input signal is NPN type, the following illustration shows the wiring of DI, same as DI2~DI16.

Positive electrode of external device connects to V+ of control cabinet, the OUT signal wire connects to the specified DI, 
and negative electrode of external device connects to V- of control cabinet. 
When the signal is activated, the corresponding indicator on the panel illuminates. 
The corresponding indicator will light on in the |jaka_app| at the same time.

.. figure:: ../../images/07_运输及调试/NPN型信号作为输入接线.*
   :width: 8.2cm
   :align: center

   Wiring of digital input when NPN signal as input

.. _Digital-Output-Interface:

Digital Output Interface
------------------------

.. figure:: ../../images/07_运输及调试/数字输出接口.*
   :width: 5.36cm
   :align: center

   Digital output interface

The 16 digital output interfaces are located on the P9 and P10, which supports isolated signal output and are PNP/NPN configurable. 
DO1~DI8 must be configured collectively as either PNP or NPN, and DO9~DI16 must also be configured collectively as either PNP or NPN. 
Individual DO channel switching is not available.

V+ supports external 24V power input, shorted to internal 24V by default. When connecting external power, 
the jumpers should be unplugged. The factory default wiring is consistent with the safety I/O’s wiring. 
Refer to the :ref:`Default Configuration <default-configuration-2>`.

.. _PNP-Mode:

PNP Mode
--------

When the DO is configured as PNP, the following illustration shows the wiring of DO9, same as DO10~DO16.

.. figure:: ../../images/07_运输及调试/PNP模式接线.*
   :width: 3.59cm
   :align: center

   Wiring of digital out in PNP mode

.. _NPN-Mode:

NPN Mode
--------

When the DO is configured as NPN, the following illustration shows the wiring of DO1, same as DO2~DO8.

.. figure:: ../../images/07_运输及调试/NPN模式接线.*
   :width: 3.37cm
   :align: center

   Wiring of digital out in NPN mode

Digital outputs can be controlled through the DO function in the |jaka_app|. 
The max current of one DO is 1 A, the total current cannot exceed 1.5 A.

.. attention::

    It is recommended to use flyback diodes for inductive load (such as the relay, electromagnet, and DC motor).

.. _High-Speed-Interface:

High Speed Interface
--------------------

.. figure:: ../../images/07_运输及调试/P6接口.*
   :width: 2.53cm
   :align: center

   P6 interface

High speed interfaces are located on P6, which can be connected to an external encoder for conveyor belt and other applications. 
Support 5V/24V internal encoder power supply; taking 5V as an example, the following illustration shows the wiring.

.. _Differential-Input:

Differential Input
------------------

Wiring of differential input encoder.

.. figure:: ../../images/07_运输及调试/差分输入外接编码器.*
   :width: 7.38cm
   :align: center

   Wiring of differential input encoder

**1** Encoder

.. _Single-Ended-Input:

Single-Ended Input
------------------

Wiring of single-ended input encoder.

.. figure:: ../../images/07_运输及调试/单端输入外接编码器.*
   :width: 7.3cm
   :align: center

   Wiring of single-ended input encoder

**1** Encoder

.. _RS485-Interface:

RS485 Interface
---------------

RS485 interfaces are located on pin1~pin4 of P6, which is used to communicate with other devices. 
Pin1 and pin2 are master interfaces and pin3 and pin4 are slave interfaces.

The control cabinet has a built-in 120Ω resistor. When using the RS485 interface, no external resistor is required. 
Simply enable or disable the resistor via the internal DIP switch. The following illustration shows the location of the DIP switch. 
The 120Ω resistor is disabled by default.

.. figure:: ../../images/07_运输及调试/电阻开关.*
   :width: 5cm
   :align: center

   Resistor switch

| **1** RS485 Master
| **2** RS485 Slave
| **ON** Connect 120Ω resistor

.. _Control-Cabinet-Acting-as-Master:

Control Cabinet Acting as Master
--------------------------------

The following illustrations show the wiring when the control cabinet acts as master.

.. figure:: ../../images/07_运输及调试/RS485主站接口.*
   :width: 3cm
   :align: center

   RS485 interfaces (master)

.. figure:: ../../images/07_运输及调试/控制柜作主站RS485接口接线.*
   :width: 7cm
   :align: center

.. figure:: ../../images/07_运输及调试/控制柜作主站RS485接口接线_2.*
   :width: 8cm
   :align: center

   RS485 wiring when the control cabinet acts as master

1, 2 External devices

.. _Control-Cabinet-Acting-as-Slave:

Control Cabinet Acting as Slave
-------------------------------

The following illustrations show the wiring when the control cabinet acts as slave.

.. figure:: ../../images/07_运输及调试/RS485从站接口.*
   :width: 3cm
   :align: center
   
   RS485 interfaces (slave)

.. figure:: ../../images/07_运输及调试/控制柜作从站RS485接口接线.*
   :width: 7cm
   :align: center

   RS485 wiring when the control cabinet acts as slave

1 External device

.. _Expansion-Communication:

Expansion Communication
=======================

.. _EtherCAT-Expansion-I-O:

EtherCAT Expansion I/O
----------------------

The CAB V3 control cabinet supports connecting external expansion boards to enable the robot to act as an EtherCAT master. The following two board models are supported:

- AIMOSUN EC1A-IO16R-AM6 (referred to as EC1A) Supports 16 digital inputs (NPN/PNP), 16 relay outputs, 4 analog inputs, and 2 analog outputs. The analog input/output voltage and current ranges are 0–10 V and 0–20 mA.
- AIMOSUN EC3A-AE0830 (referred to as EC3A) Supports 8 analog inputs with voltage and current ranges of 0–10 V and 0–20 mA, and 16‑bit accuracy.

Up to two boards can operate simultaneously, connected in series. The following six configurations are available:

- EC1A
- EC3A
- EC1A+ EC1A
- EC3A+ EC3A
- EC1A+ EC3A
- EC3A+ EC1A

.. attention::
    
    The board order configured in the software must match the physical hardware connection order. For example, if EC1A is connected to the control cabinet and EC3A is daisy‑chained after EC1A, the software configuration order should also be EC1A first, followed by EC3A.

Wiring for a single board:

- Connect the **24 V** of the expansion board to **V+** on the control cabinet front panel.
- Connect the **0 V** of the expansion board to **V–** on the control cabinet front panel.
- Connect the **RJ45** port of the expansion board to the **LAN2** port on the control cabinet bottom panel.

Wiring for two boards:

- Connect the **24 V** of the first expansion board to **V+** on the control cabinet front panel.
- Connect the **0 V** of the first expansion board to **V–** on the control cabinet front panel.
- Connect the **RJ45** port of the first expansion board to the **LAN2** port on the control cabinet bottom panel.
- Connect the **24 V** of the second expansion board to **V+** on the control cabinet front panel.
- Connect the **0 V** of the second expansion board to **V–** on the control cabinet front panel.
- Connect the **RJ45** port of the second expansion board to the **RJ45** port of the first expansion board.

After wiring, configuration must be performed in |jaka_app|. For details, refer to the |jaka_app| Software User Manual.

.. _Modbus-RTU-Master-Slave:

Modbus RTU Master/Slave
-----------------------

The CAB V3 control cabinet supports connecting external expansion boards for Modbus RTU communication, allowing the robot to act as either a master or a slave.

Recommended board models:

- SEEWE SRND‑CM‑TR1616. Supports 16 digital inputs and 16 transistor outputs.
- SEEWE SRND‑CM‑IO1616. Supports 16 digital inputs and 16 relay outputs.

Wiring methods are as follows:

- Connect **Vcc** of the expansion board to **V+** on the control cabinet front panel.
- Connect the **0 V** of the expansion board to **V–** on the control cabinet front panel.
- Connect **RS485A** of the expansion board to **M_A** or **S_A** on the control cabinet bottom panel.
- Connect **RS485B** of the expansion board to **M_B** or **S_B** on the control cabinet bottom panel.

.. note::
    
    If the robot acts as a Modbus master, connect to M_A and M_B; if it acts as a slave, connect to S_A and S_B.

After wiring, configuration must be performed in |jaka_app|. For details, refer to the |jaka_app| Software User Manual.

.. _PROFINET-IO-Device:

PROFINET I/O Device
--------------------

The CAB V3 control cabinet supports connecting external expansion boards for PROFINET communication, with the robot acting as a slave.

Recommended board model: SEEWE SRND‑VM‑IO1616. Supports 16 digital inputs and 16 relay outputs.

Wiring methods are as follows:

- Connect the **24 V** of the expansion board to **V+** on the control cabinet front panel.
- Connect the **0 V** of the expansion board to **V–** on the control cabinet front panel.
- Connect the **RJ45** port of the expansion board to the **LAN1** or **LAN2** port on the control cabinet bottom panel.

After wiring, configuration must be performed in |jaka_app|. For details, refer to the |jaka_app| Software User Manual.