The JAKA robot comes with a control stick, which can be used to control both the robot and the control cabinet. The functions of the control stick buttons are described as follows:

.. figure:: ../../images/06_技术规格/手柄.*
   :width: 7cm
   :align: center

   Control stick

.. list-table:: Control stick functions
   :widths: 8 19 73
   :header-rows: 1
   :class: merge-empty-vertical

   * - 
     - Name
     - Description
   * - 1
     - Control stick indicator
     - | When powering on the control cabinet, the control stick indicator cycles through red, blue, and green, accompanied by three beeps, and then it turns orange, waiting for the control cabinet to power up. After activating, the control stick indicator will flash blue.
       | After powering on the robot, the control stick indicator will flash blue.
       | After enabling the robot, the control stick indicator will flash green.
       | When the robot is in the emergency stop status and protective stop status, the control stick indicator flashes red.
   * - 2
     - Emergency stop button
     - | Press the button to emergency stop the robot; release the button to resume operation.
       | The emergency stop button is limited to emergencies and should not be used as regular power off equipment.
   * - 3
     - Reset button
     - | After the robot is enabled and the robot is not executing the program. Press and hold the reset button to control the robot to return to initial orientation set in the JAKA App. Continue holding the button when the robot has moved to initial orientation, the lock indicator will turn blue.
   * - 4
     - Start/stop button
     - | Start the program: Press the button to start the default program, execute the default program after the robot reaches the initial position of the program.
       | Stop the program: Press to stop the program when the robot runs the program.
   * - 5
     - Pause/Resume Button
     - | Pause: During the automatic operation of the robot, press the button to pause the program.
       | Resume: Press the button to resume the program when the program is paused.
   * - 6
     - Three-position enable button
     - | Refer to :ref:`Three-Position Enabling Device`.
   * - 7
     - Power up/down button
     - | Power up: Press the power button for 1 second and release. The buzzer beeps once, and the control cabinet is powered up.
       | Power down: Press and hold the power button for 3 seconds or more. The control stick beeps 6-7 times, and the control cabinet is powered down.
   * - 8
     - Enable button
     - | Robot power on: Press the enable button once and wait for the ring-shaped light to turn blue, indicating that the robot is powered on.
       | Robot power off: Press the enable button once and wait for the ring-shaped light to go off, indicating that the robot is powered off.
       | Enable robot: When the robot is powered on, press and hold the lock button, and then press the enable button at the same time until the ring-shaped light turns green and a click is heard, which means the robot is enabled.
       | Disable robot: When the robot is enabled, press and hold the lock button, and then press the enable button at the same time. until the ring-shaped light turns blue, which means the robot is disabled.
   * - 9
     - Lock button and indicator
     - | Lock the control stick: Press and hold the lock button for until the indicator turns orange.
       | Unlock the control stick: Press and hold the lock button until the indicator turns off.
       | Combination function: Other buttons can be used with the lock button.
       | Lock state: In the lock state, the indicator is orange, and all buttons except the lock button and power button are disabled. The |jaka_app| can now control the robot.
       | Unlock state: In the unlock state, all lights turn off, and the control stick can be used. The |jaka_app| cannot be used to control the robot in this state.

.. note::

   - Once the control cabinet is powered up, the control stick will beep twice per second if any button is pressed.
   - When using the control stick to operate the robot, 
     ensure that the robot you are operating is within your sight and follow 
     the relevant safety guidelines to avoid any injury to personnel or equipment near the robot.

.. _Three-Position Enabling Device:

Three-Position Enabling Device
=================================

The JAKA robot supports a three-position enabling function, which can be used in conjunction with an external three-position enabling device. The standard product delivery of the JAKA robot does not include this device. The three-position enabling safety input interface is optional for matching hardware, which meets the design certification requirements. For this optional accessory, please contact the authorized supplier of JAKA.

When you use the three-position enabling device and configure the corresponding function in the software, the robot can only be moved and controlled after the three-position switch is pressed to a middle point. See Touch I/Touch II User Manual for wiring method.

The picture of the three-position enabling switch is as follows:

.. figure:: ../../images/06_技术规格/三位置使能按钮.*
   :width: 10cm
   :align: center

   Three-position enabling switch

The corresponding robot control states for different states of the three-position enabling switch are as follows:

.. list-table::
   :header-rows: 1
   :widths: 10 15 25 15 35
   :class: longtable merge-empty-vertical

   * - **Switch Position**
     - **Switch State**
     - **Robot State**
     - **Manual Control**
     - **Automatic Control (Program Operation)**

   * - 1
     - Release
     - Protective stop (Cat.2)
     - Off
     - When a program is running, the three-position enabling function is switched off.

   * - 2
     - Press lightly
     - Normal
     - On
     -
   
   * - 3
     - Press tightly
     - Protective stop (Cat.2)
     - Off
     -

.. note::

   - Manual control consists of dragging the robot by pressing and holding the Free button, dragging the robot by pressing and holding the pause/resume button, JOG robot in the manual operation interface, and debugging function in programming interface.
   - JOG refers to manually controlling robot movement in the JAKA App in the manual operation interface.