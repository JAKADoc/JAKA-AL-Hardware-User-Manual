.. _Optional-Equipment:

Optional Equipment
******************

.. _Teach-Pendant:

Teach Pendant
+++++++++++++

CAB V3 is compatible with Touch I and Touch II teach pendant. For detailed specifications and operating instructions, please refer to the JAKA Touch I User Manual and the JAKA Touch II User Manual.

.. _Expansion-Module:

Expansion Module
++++++++++++++++

If PROFINET controller or CC‑Link slave communication is required, an expansion module can be installed. The expansion module must be purchased separately.

The currently supported expansion module model is CIFX M3042100BM‑RE\\F, which supports PROFINET controller and CC‑Link slave. This expansion module consists of two boards: a core board installed on the IPDU board of the control cabinet, and an Ethernet port board installed on the mounting plate of the IPDU board.

.. figure:: ../../images/08_选配设备/扩展模块.*
   :width: 10cm
   :align: center

   Expansion module

| 1 Core board
| 2 Ethernet port board

.. _Expansion-Module-Installation:

Expansion Module Installation
=============================

Before installing the expansion module, prepare the following tools:

.. list-table:: Tool list
   :widths: 7 41 52
   :header-rows: 1

   * - **No.**
     - **Name**
     - **Specification**

   * - 1
     - Control cabinet key
     - /

   * - 2
     - Phillips screwdriver
     - PH1

   * - 3
     - Phillips screwdriver
     - PH2

   * - 4
     - Allen key
     - 2 mm

   * - 5
     - Tweezer
     - /

Installation procedure (taking CAB L/H as an example):

#. Ensure the control cabinet is powered off and wear an anti-static wrist strap.
#. Use the control cabinet key to open the door.

   .. figure:: ../../images/08_选配设备/开控制柜门.*
      :width: 10cm
      :align: center

#. Use a PH2 screwdriver to remove the two M4 screws securing the front panel. Pull down the panel.

   .. figure:: ../../images/08_选配设备/形_1_19.*
      :width: 12cm
      :align: center

#. Insert the core board into the slot on the IPDU board, and use a 2 mm Allen key to tighten one M2.5 screw to secure the core board.

   .. figure:: ../../images/08_选配设备/形_1_20.*
      :width: 10cm
      :align: center

#. Place the Ethernet port board into position, and use a PH1 screwdriver to tighten two M2.5 Phillips screws to secure it.

   .. figure:: ../../images/08_选配设备/形_1_21.*
      :width: 9cm
      :align: center

#. Connect the cable harness to the core board and the Ethernet port board of the expansion module.

   .. figure:: ../../images/08_选配设备/形_1_22.*
      :width: 8cm
      :align: center

#. Connect one end of an Ethernet cable to the RJ45 port on the Ethernet port board, and the other end to the external communication device.
#. Reconnect the control cabinet power. Press about one second and release the power button on the control stick; the buzzer will sound, indicating the cabinet has powered up.

   .. figure:: ../../images/08_选配设备/形_1_23.*
      :width: 8cm
      :align: center


   .. figure:: ../../images/08_选配设备/形_1_24.*
      :width: 3cm
      :align: center

#. Open the Coboπ software, connect to the robot, and navigate to **Settings > Hardware and Communication > Extended Communication** to configure the expansion I/O.
   For details, refer to the Coboπ Software User Manual.

   .. image:: ./images/image_108.*
      :align: center
