.. _Power On and Shut Down the Robot System:

Power On and Shut Down the Robot System
=======================================

The robot can be powered on, enabled, disabled, and powered off in either of the following ways:

- Control Using the Control Stick
- Control Using |jaka_app|

To power on and enable the robot via the control stick, proceed as follows:

Enable the robot with the control stick as follows:

1. Power up control cabinet: Press the Power button. The buzzer makes a noise, and the control cabinet is powered up.
2. Unlock the control stick: Press and hold the Lock button for 3 seconds, and the lock indicator goes out, which means the control stick is unlocked.
3. Power on robot: Press the Enable button, waiting for the ring-shaped light to turn blue, which means the robot is powered on.
4. Enable robot: When the robot is powered on, press and hold the Lock button, then press the Enable button at the same time until the ring-shaped light turns green, which means the robot is enabled.
5. Lock control stick: App cannot be operated when control stick is unlocked, you should lock control stick first. Press and hold the Lock button for 3 seconds, and the lock indicator turns orange, which means control stick is locked. You can use App now.

Steps of powering down control cabinet are as follows:

1. Unlock the control stick: Press and hold the Lock button for 3 seconds, and the lock indicator goes out, which means the control stick is unlocked.
2. Disable robot: When the robot is enabled, press and hold the Lock button, and then press the Enable button at the same time until the ring-shaped light turns blue, which means the robot is disabled.
3. Power off the robot: Press the Enable button briefly and wait for the ring-shaped light on the robot wrist to turn off, indicating that the robot is powered off.
4. Power down control cabinet: Press and hold the Power button for 3 seconds or more. The control stick beeps 6-7 times, and the control cabinet is powered down. After powering off the control cabinet, please do not cut off the power immediately. Wait until the control stick light goes out, and after waiting for 5 to 10 seconds, you can disconnect the power.

.. attention::

   Under non-emergency conditions, the robot system shall be operated strictly in accordance with the standard power-on/shutdown procedures. Forced power disruption is prohibited, as it will cause data loss and compromise system reliability.

.. _Set the Limits:

Set the Limits
==============

Before commissioning the robot, the following items should be verified:

- Verify the emergency stops and the operator protective devices.
- The robot complies with the relevant standards and protective devices are designed to stop the robot without leaving the path (category 1 stop).
- Robot functions successfully within preset limits. Slowly move the robot beyond the limits of the preset working space in order to verify that this is prevented by the preset limits.
- Individually move the robot beyond the maximum/minimum angles in order to verify that this is prevented by the preset limits.

.. _Start-Up:

Start-Up
==========

When the robot is operated for the first time, there is a risk of unintended equipment operation caused by possible wiring errors, improper mounting and fastening, or unsuitable parameters.

.. warning::

   Unintended equipment operation:

   - Unintended equipment operation:
   - Verify that the robot is properly and firmly fastened.
   - Take all necessary measures to ensure that the moving parts of the robot cannot move in an unanticipated way.
   - Verify that emergency stop equipment is operational and within reach of the zone of operation.
   - Verify that the system is obstacle-free and ready for the movement before starting the system.

   ..

      Failure to follow these instructions can result in death, serious injury, or equipment damage.

If the robot power supply is disabled unintentionally, for example as a result of power outage or errors, the robot is no longer decelerated in a controlled way.

.. warning::

   Unintended equipment operation:

      Verify that movements without braking effect cannot cause injuries or equipment damage.

      Failure to follow these instructions can result in death, serious injury, or equipment damage.

.. warning::

   Hot surfaces:

   - Hot surfaces:
   - Do not allow flammable or heat-sensitive parts in the immediate vicinity of hot surfaces.

   ..

      Failure to follow these instructions can result in death, serious injury, or equipment damage.

.. _Commissioning Procedure:

Commissioning Procedure
-----------------------

To commission the robot, proceed as follows:

#. Comply with the instructions provided in this manual.
#. Verify that the load conforms to the specified payloads for the robot before operating.
#. Connect to the robot using |jaka_app|. See the |jaka_app| Software User Manual for details.
#. Configure the robot mounting parameters. See the |jaka_app| Software User Manual for details.
#. Verify the calibration and position and direction of the joints.
#. Verify the world-coordinate-system directions on the manual operation screen. See the |jaka_app| Software User Manual for details.

   .. note::

      The world coordinate system depends on the mounting position.

#. Configure the collision protection parameters according to the safety requirements of the application. See the |jaka_app| Software User Manual for the configuration procedure.
#. Perform initial tests at reduced velocity and verify the functionality of the robot.
#. Verify that the operating condition of set cycles is lower than 80% of the total cycle time.

   .. note::

      For a total cycle time of 10 seconds take care of maximum 8 seconds cycle running time and 2 seconds waiting period. If you exceed the duty cycle proportion of 80%, you may reduce the lifetime of the gearboxes of the robot joints.

#.  (Optional) Configure an initial position for the control stick Reset button. For control stick operation, see :ref:`Control Stick Buttons <Control-Stick-Buttons>`. For initial-position configuration, see the |jaka_app| Software User Manual.
#.  (Optional) If multiple robot systems are present, assign each robot a unique name for identification. See the |jaka_app| Software User Manual for the configuration procedure.

.. _Starting the Default Program:

Starting the Default Program
----------------------------

There are two options for automatically starting the program set as default on the robot:

- Starting via control stick
- Run Using |jaka_app|

To run the default program using the control stick, briefly press the **Start/Stop** button on the control stick.

To configure and run the default program using |jaka_app|, see the |jaka_app| Software User Manual.