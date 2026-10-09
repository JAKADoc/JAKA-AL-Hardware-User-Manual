This chapter describes the electrical specifications and parameters of the CAB V3 interfaces and harnesses.

.. warning::

  Operate the robot and CAB V3 within the recommended electrical parameters. Exceeding the specified limits may cause permanent damage to the control cabinet hardware.

.. _Electrical-Specifications-of-Power:

Electrical Specifications of Power
==================================

Electrical specifications of CAB L, CAB H, and CAB LiteAC are as follow.

.. list-table:: Electrical specifications of CAB L, CAB H, and CAB LiteAC
   :widths: 38 16 16 17 13
   :header-rows: 1

   * - **CAB L, CAB H, CAB LiteAC**
     - **Min.**
     - **Typ.**
     - **Max.**
     - **Unit**

   * - Power Input
     - AC 100
     - AC 220
     - AC 240
     - V

   * - Internal 24V Power Output Current
     - 0
     - 2
     - 3
     - A

Recommended operating conditions for CAB LiteDC:

.. list-table:: Electrical specifications of CAB LiteDC
   :widths: 31 16 22 18 13
   :header-rows: 1

   * - **CAB LiteDC**
     - **Min.**
     - **Typ.**
     - **Max.**
     - **Unit**

   * - Power Input
     - DC 36
     - DC 48
     - DC 56
     - V

   * - Internal 24V Power Output Current
     - 0
     - 2
     - 3
     - A

.. attention::
  
  The control cabinet surface temperature rises during operation. Ensure sufficient airflow for the control cabinet, especially if the device is installed in an enclosure.
  
  Failure to follow these instructions can result in equipment damage.

.. _Electrical-Specifications-of-Safety-I-O-Interfaces:

Electrical Specifications of Safety I/O Interfaces
==================================================

The safety I/O is designed in accordance with IEC 61131-2. It supports 16 channels of digital input and 16 channels of digital output. The electrical specifications for the safety I/O are shown in the table below:

.. csv-table:: Electrical specifications of safety I/O interfaces
   :file: ./tables/Electrical specifications of safety IO interfaces.csv
   :encoding: utf-8-sig
   :widths: 20 22 15 14 14 15
   :header-rows: 1

.. _Electrical-Specifications-of-I-O-Interfaces:

Electrical Specifications of I/O Interfaces
===========================================

The I/O is designed in accordance with IEC 61131-2. It supports 16 channels of digital input and 16 channels of digital output. The electrical specifications for the I/O are shown in the table below:

.. csv-table:: Electrical specifications of I/O interfaces
   :file: ./tables/Electrical specifications of IO interfaces.csv
   :encoding: utf-8-sig
   :widths: 15 27 15 14 14 15
   :header-rows: 1

.. _Typical-Power-Consumption:

Typical Power Consumption
=========================

Typical power consumption of CAB L and CAB H:

.. list-table:: Typical power consumption of CAB L and CAB H
   :widths: 27 26 26 21
   :header-rows: 1

   * - **Parameters**
     - **Typ.**
     - **Max.**
     - **Unit**

   * - Standby Power Consumption
     - 2
     - 5
     - W

   * - Startup Power Consumption
     - 24
     - 50
     - W

   * - Robot Power On Consumption
     - 45
     - 60
     - W

Typical power consumption of CAB LiteAC and CAB LiteDC:

.. list-table:: Typical power consumption of CAB LiteAC and CAB LiteDC
   :widths: 27 26 26 21
   :header-rows: 1

   * - **Parameters**
     - **Typ.**
     - **Max.**
     - **Unit**

   * - Standby Power Consumption
     - 1
     - 5
     - W

   * - Startup Power Consumption
     - 12
     - 30
     - W

   * - Robot Power On Consumption
     - 25
     - 33
     - W

.. _Wire-Specifications-of-Control-Cabinet-Interfaces:

Wire Specifications of Control Cabinet Interfaces
===================================================

Wires connecting to front panel of control cabinet should comply with the following specifications:

.. csv-table:: Specifications of wires
   :file: ./tables/Specifications of wires.csv
   :encoding: utf-8-sig
   :widths: 16 21 23 25 15
   :header-rows: 1
   :class: merge-empty-vertical

The power interface of the CAB LiteDC is a 3‑pin terminal. The terminal model on the cabinet side and user side, and the cable specifications are listed in the table below.

.. list-table:: Wire specifications of CAB LiteDC
   :widths: 27 27 27 19
   :header-rows: 1

   * - **Terminal Model (Control Cabinet)**
     - **Terminal Model (User)**
     - **Wire Size**
     - **Stripping Length**

   * - DGH4-01P-1Y, DEGSON
     - E2510
     - 2.5 mm² or 14 AWG
     - 7~8 mm (0.28~0.31 in)

.. _ESD-Sensitive:

ESD Sensitive
================

ESD (electrostatic discharge) is the transfer of electrical static charge between two bodies at different potentials, either through direct contact or through an induced electrical field. When handling parts or their containers, personnel not grounded may potentially transfer high static charges. This discharge may destroy sensitive electronics.

Use one of the following alternatives:

- Use a wrist strap. Wrist straps must be tested frequently to ensure that they are not damaged and are operating correctly.
- Use an ESD protective floor mat. The mat must be grounded through a current-limiting resistor.
- Use a dissipative table mat. The mat should provide a controlled discharge of static voltages and must be grounded.

.. _Line-Fusing:

Line Fusing
=============

There is no integrated fuse inside the CAB V3. Add an external fuse (time-delay) or circuit breaker (class K) according to full load current in `4.3.2 <#electrical-specifications-of-power>`__ `Electrical Specifications of Power <#electrical-specifications-of-power>`__. The following table shows the recommended rating for an external fuse or circuit breaker.

.. list-table:: Fuse specifications
   :widths: 47 29 24
   :header-rows: 1

   * - **Robot**
     - **Current**
     - **Description**

   * - A5L
     - 100-240 VAC, 1 phase
     - 10 A

   * - A12L
     - 100-240 VAC, 1 phase
     - 10 A

.. _Residual-Current:

Residual Current
=================

An external earth fault protection (residual current device, RCD) is required based on the following residual current data in control cabinet:

.. list-table:: Residual current
   :widths: 62 38
   :header-rows: 1

   * - **Robot**
     - **Residual Current in Control Cabinet**

   * - A5L, A12L
     - ＜30 mA