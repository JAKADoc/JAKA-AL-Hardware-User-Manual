.. _Safety Standard:

Safety Standard
***************

.. _Introduction:

Introduction
++++++++++++

This chapter mainly introduces the safety principles and standards that should be followed while using the JAKA robot. Users should carefully read and strictly abide by the content related to safety in this manual. Operators should fully recognize the complexity and danger of the robot system, and pay special attention to the content related to warning signs.

.. _Important Safety Notice:

Important Safety Notice
+++++++++++++++++++++++

According to the 2006/42/EC Machinery Directive, the JAKA robot is **partly completed machinery**. A risk assessment must be performed for every robot installation. All safety instructions must be followed.

.. _Safety Signals and Symbols:

Safety Signals and Symbols
++++++++++++++++++++++++++

The danger level in this manual is described with the following safety symbols. Contents related to safety should be strictly observed.

.. list-table:: Safety Symbol Descriptions
   :widths: 20 80 
   :header-rows: 1
   
   * - **Symbol**
     - **Description**

   * - **WARNING: ELECTRICITY**
     - This symbol indicates a potentially dangerous power consumption situation which, if not avoided, may result in injuries to personnel or serious damage to equipment.  

   * - **WARNING** 
     - This symbol indicates a potentially dangerous situation which, if not avoided, may result in injuries to personnel or serious damage to equipment.

   * - **WARNING: HOT SURFACE** 
     - This symbol indicates a potentially dangerous hot surface that may result in injuries to personnel if touched.

   * - **ATTENTION** 
     - This symbol is used to indicate important facts and conditions.

   * - **NOTE**
     - This symbol is used to indicate additional information.

.. _Warnings and Cautions:

Warnings and Cautions
+++++++++++++++++++++

This section focuses on the protection of operators and the relevant precautions of the first installation. Users need to read the safety warnings in this manual carefully.

.. list-table:: General warnings
   :widths: 20 80      
   :header-rows: 1
   :class: longtable
   
   * - **Symbol**
     - **Description**
  
   * - .. figure:: ../../images/04_安全规范/触电.*
          :width: 1.5cm
     - **WARNING: ELECTRICITY** 

       - All JAKA hardware and software must be installed/configured in strict accordance with the    instructions and cautions provided in this manual.
       - The installation of the power cut-off switch should be positioned within the height range of 0.6~1.9 m (23.622~74.803 in) to facilitate prompt and convenient power disconnection in the event of an emergency.
       - Contact with live electrical components may result in electric shock. Do not touch any internal component while the robot is powered on.
       - During the operation, ensure proper connection of robot power cable and control cabinet. It is strictly forbidden to plug or unplug the power cables and terminals while the robot is running.

   * - .. figure:: ../../images/04_安全规范/危险.*
          :width: 1.5cm
     - **WARNING**
       
       - Ensure that the robot arm and tool are installed correctly.
       - Ensure that the robot arm has sufficient clearance to move freely.
       - Technical personnel are instructed to carry out the installation and commissioning procedures for any JAKA products in strict accordance with the provided specifications.
       - Adjustment and alteration of any JAKA product parameters must be executed exclusively by authorized personnel to safeguard against unauthorized modifications by individuals lacking appropriate operating expertise.
       - Tools and obstacles must not have sharp edges or points. Ensure that all personnel remain outside the robot's reach.
       - Frequently toggling the power on/off is not recommended. Each joint of the JAKA robot is equipped with a brake mechanism to maintain its pose for safety reasons in the event of a power failure. Brake mechanisms can be damaged during unexpected power outages.
       - In the event that the applied force on the robot surpasses a predefined threshold, JAKA's collision detection feature will be triggered and robot motion will be ceased to prevent potential harm to the robot itself or injury to operators. Associated risks of the use of control cabinets not supplied by JAKA is solely the responsibility of the operator.

   * - .. figure:: ../../images/04_安全规范/热表面.png
          :width: 1.5cm
     - **WARNING: HOT SURFACE**

       - Verify that there is adequate space available for unobstructed movement of the robot.

   * - .. figure:: ../../images/04_安全规范/危险.*
          :width: 1.5cm
     - **WARNING**

       - When connecting external equipment that may pose a threat to the robot, it is advisable to independently check all robot functions and programs. Utilize temporary waypoints located outside the mechanical workspace to verify the robot's program.
       - Exposure to strong magnetic fields can damage the robot; hence, avoid exposing it to permanent magnetic fields.
       - Operators who use the robot system are strictly prohibited to wear loose clothes and jewelry. Long hair should be tied up.
       - During operation, even if the robot appears to have stopped, it may be in a state of imminent action because it is waiting for a start signal. In such state, the robot should be regarded as running.
       - During the operation, ensure proper connection of robot power cable and control cabinet. It is strictly forbidden to plug or unplug the power cables and terminals while the robot is running.
       - Warning lines should be drawn on the floor to clearly mark the workspace of the robot.
       - In emergency situations, the robot arm may be manually repositioned by gently pushing or pulling the joints.
       - Avoid excessive force to prevent potential damage to the joints.

.. _Intended Use:

Intended Use
++++++++++++

The JAKA robot is intended to be integrated into a manufacturing line and/or assembled with other components to build up a machine or process in an industrial environment. The JAKA robot is either an open type robot that is intended to be installed into an enclosure, or a collaborative operation product where it works with an operator within a collaborative workspace.

JAKA robot intended use cases:

- Loading and unloading.
- Packaging.
- Case erecting.
- Picking and placing.
- Palletizing.
- Assembling.
- Inspecting.
- Machine tending.
- Material working.
- Gluing and Bonding.
- Polishing/sanding.
- Soldering.

The JAKA robot is equipped with specially designed safety functions to support operation without safety fences and operation together with an operator. The following terms describe the different types of interaction with a JAKA robot:

1. **Coexistence:** The operator and robot work in adjacent areas, either simultaneously or at different times. They have separate workspaces and independently perform tasks toward the same objective. There is no direct contact between the operator and robot.
2. **Cooperation:** The operator and robot work at different times in the same workspace to achieve a common objective. There is no direct interaction between the operator and robot.
3. **Collaboration:** The operator and robot work simultaneously in the same workspace to achieve a common objective, such as assembling a product. Direct interaction occurs between the operator and robot.

Coexistent, cooperative, and collaborative operation is permitted only for non-hazardous applications. The risk assessment for the specific application must confirm that the complete application, including tools, workpieces, obstacles, and other machines, presents no significant hazards.

Any other use is considered unintended use.

.. figure:: ../../images/04_安全规范/机器人交互类型.*
   :width: 18cm
   :align: center

   Operator interactions with robot

.. warning::

   **Personal injury:**

   - Do not use the JAKA robot in a coexistent, cooperative, or collaborative operation if the application could cause potential injuries.
   - Please operate the robot in accordance with the requirements of the manual. If the robot is operated in the collaborative mode, additional safety input detection units must be used (such as scanners, light curtains, cameras, etc. with PLr=d or PLr=e), and a risk assessment must be conducted.

   ..

      Failure to follow these instructions can result in death, serious injury, or equipment damage.

.. _Liability and Risk:

Liability and Risk
++++++++++++++++++

**Liability**

| This manual does not contain full application examples, complete solution designs, or information on peripheral equipment that could affect the robot system's security.
| It is the responsibility of the user to ensure that relevant practical national laws and regulations are followed, and that there are no significant hazards in the workspace.
| The safety information in this manual does not constitute a guarantee from JAKA. Even when all safety instructions are followed, operator actions may still result in injury or damage.
| JAKA is committed to continuously improving the performance and reliability of our robots. However, we are not responsible for any errors or omissions in this manual and reserve the right to the final interpretation of its contents.

**Risk**

Operators engaging with the robot will inevitably experience direct or indirect physical contact. It is essential to maintain awareness of self-protection and adhere to safe operating procedures. The following hazards should be considered:

- Robot brake failure causing it to drop.
- Loose bolts and screws causing vibrations.
- Robot collision with operator.
- Lack of prompt repair.
- Danger when sharp-end effectors are used.
- Toxic or corrosive environments.
- Strong magnetic environment.

.. _Provide Protective Measures:

Provide Protective Measures
+++++++++++++++++++++++++++

Before installing the JAKA robot, provide appropriate protective devices in compliance with local and national standards. Do not commission components without appropriate protective devices. After installation, commissioning, or repair, test the protective devices used.

Other standards are applicable as guidelines for a JAKA robot integration into machinery such as (non-exhaustive list):

- Directive 2006/42/EC on machinery.
- Directive EMC 2014/30/EU.
- Standard ISO 10218-1 Robots and Robotic devices - Safety requirements for industrial Robots - Part 1: Robots.
- Standard ISO 10218-2 Robots and Robotic devices - Safety requirements for industrial Robots - Part 2: Robot systems and integration.
- Standard ISO 13849-1 Safety of machinery - Safety related parts of control systems - Part 1: General Principles for Design.
- Standard ISO/TS 15066 Robots and Robotic devices - Collaborative Robots.
- Standard ISO 13857 Safety of machinery - Safety distances to prevent hazard zones being reached by upper and lower limbs.
- Standard ISO 14120 Safety of machinery - Guards - General requirements for the design and construction of fixed and movable guards.
- Standard EN ISO 13854 Safety of machinery - Minimum gaps to avoid crushing of parts of the human body.
- Standard ISO 13855 Safety of machinery - Positioning of safeguards with respect to the approach speeds of parts of the human body.
- Standard NFPA 79 Electrical Standard for Industrial Machinery.
- Standard NFPA 70 National Electric Code.
- Standard UL 1740 Standard for Robots and Robotic Equipment.
- Standard UL 2011 Standard for Factory Automation Equipment.

Strong magnetic environment.

.. warning::

   **Unintended equipment operation:**

   - Use appropriate protective devices (functional safety devices) in compliance with local and national standards.
   - Ensure that a risk assessment is conducted and respected according to EN/ISO 12100 during the design process.
   - Apply all measures from the hazard and risk analysis before deployment.

   ..

      Failure to follow these instructions can result in death, serious injury, or equipment damage.

.. _Risk Assessment:

Risk Assessment
+++++++++++++++

Robots are partially completed machines, and their safe installation depends significantly on the integration process, including components such as end effectors and communication equipment. Conducting a risk assessment is essential and a critical responsibility of the integrator. It is recommended that the integrator performs the risk assessment in accordance with ISO 12100 and ISO 10218-2, while also considering ISO/TS 15066 as additional guidance. The risk assessment should cover all aspects of the robot's lifecycle, including but not limited to:

- Teaching of the robot during installation, set-up and development.
- Operations of the robot installation.
- Troubleshooting and maintenance.

**The risk assessment must be completed before the robot is powered on for the first time.** The integrator's risk assessment must determine the safety configuration and evaluate whether additional emergency stop buttons or other protective measures are required for the specific robot application.

Cobots have specific safety functions, which can be configured through settings. These functions are especially important when integrators conduct risk assessments:

1. Force limit: the force set by the controller to limit the servo from exceeding the threshold. When the actual force exceeds the force limit, the robot will enter collision protection mode.
2. Momentum limit: the momentum set by the controller to restrict the momentum of the robot during motion. The limit will directly affect the speed of the robot. When the momentum of the robot exceeds the limit, the robot speed will be reduced.
3. TCP speed limit: refers to limiting the absolute speed of the TCP during the robot motion. The path speed will be kept within the TCP speed limit.
4. Power limit: refers to limiting the mechanical power during the robot movement. This limit will directly affect the speed of the robot. When the mechanical power of the robot exceeds the limit, the robot speed will be reduced.

Integrators must prevent unauthorized personnel from modifying safety configurations.

When performing a risk assessment, the integrator should consider the following:

- Potential collision scenarios.
- How to avoid potential collisions
- The severity of the potential collision.

If the robot is installed in a non-collaborative robot application and the risk cannot be eliminated by configuring the robot's safety functions, integrators should consider adding additional protective measures when conducting assessments.

JAKA identifies the following significant dangers that integrators must consider.

- Sharp edges and points on end effectors.
- Sharp edges and points on obstacles in and near the robot workspace.
- Bruises due to contact with the robot.
- Sprain or fracture caused by the impact between the heavier load on the end of the robot and the hard surface.
- Consequences caused by loose bolts or screws used to fasten robots or end effectors.
- Consequences of items falling from end effectors.
- Mis-operation due to different emergency stop buttons on different machines.
- Error due to unauthorized changes to safety configuration parameters.

.. attention::

   Specific robotic applications may present other significant hazards.

.. _Pre-use Assessment:

Pre-use Assessment
++++++++++++++++++

After first use or any modifications, perform the following tests:

- Verify that all safety inputs and outputs are correctly connected.
- Test the functionality of all safety inputs and outputs.
- Ensure the payload is configured correctly.

The following tests are required:

- Test if the emergency stop button and emergency stop input (P8) can stop the robot and engage brakes.
- Test whether the safeguard input can stop the robot motion. If safeguard reset is configured, check if activation is required before resuming motion.
- Check whether the reduced mode input can switch the motion to the reduced mode.
- Test whether the 3-position enabling device must be pressed to enable motion in manual mode and if the robot is under deceleration control.
- Test whether the emergency stop output of the system can bring the entire system into a safety state.
- Test whether the system connected to the robot moving output, robot non-stop output, reduced mode output, or non-reduced mode output can detect output changes.
- Test whether the payload configuration matches the current actual payload of the robot.

.. _Emergency stop:

Emergency stop
++++++++++++++

In an emergency, press the emergency stop button to stop all robot motion immediately. Emergency stop must not be used as a risk-reduction measure; it is a secondary protective device intended only for emergencies. Under normal conditions, use another method to stop robot motion. If the risk assessment requires an additional emergency stop button, it must comply with IEC 60947-5-5. JAKA has tested the emergency stopping time and stopping distance; see :ref:`Appendix 1: Stopping Time and Distance <Appendix 1: Stopping Time and Distance>` for the test data.

.. warning::

   When the emergency stop button is pressed, the cabinet power will cut off. In this case, even though the joints lock automatically, there will still be a slight downward movement of the robot under gravity, and therefore a risk of pinching or collision.

.. _Emergency Release of the Brake:

Emergency Release of the Brake
++++++++++++++++++++++++++++++

.. warning::

   - If the brake is released manually, the joint of the robot may move under gravity, so it is necessary to effectively support the robot, tools and workpieces installed on the robot before manually releasing the brake.
   - At least two persons should be present when releasing the brakes.

When the robot is in an emergency stop state or power has failed, the joints can be moved forcibly as shown below.

#. Remove the screw securing the joint cover plug.
#. Remove the joint lid.
#. Press the plunger in the small solenoid to release the brake manually.

   .. figure:: ../../images/04_安全规范/释放制动器.*
      :width: 6.16cm
      :align: center

      Brake pin

When the robot is powered on, the brake can be released by |jaka_app| . Operation steps are as follows:

#. Ensure that the robot is powered on and disabled.
#. Open |jaka_app| and go to the manual operation screen.
#. Press and hold the "Backdrive" button to release the joint brake (shown in Figure below).

   .. figure:: ./images/Backdrive_button_on_Coboπ.*
      :width: 20cm
      :align: center

      Backdrive button on |jaka_app|

#. Press and hold the pause/resume button on the robot flange (see :ref:`Pause/Resume Button` for its location) while moving the joint to release the brake of the joint being moved.

.. _Labels:

Labels
++++++++++

The following labels are safety warnings and product labels on the robot and the control cabinet. During operation, be sure to follow the instructions and warnings on the labels to ensure safety. Do not remove the labels casually. Handle labeled parts or units and their surrounding area with caution to avoid damage to the labels. Product labels and robot model figures are only for reference. Please see the figures and tables below for detailed description on product labels.

.. figure:: ../../images/04_安全规范/机器人铭牌及标签.*
   :width: 12cm
   :align: center

   Robot label and symbols

.. figure:: ../../images/04_安全规范/CAB_L、CAB_H控制柜标签位置（正门）.*
   :width: 13.81cm
   :align: center

   Label position of CAB L/H (front)

.. figure:: ../../images/04_安全规范/CAB_L、CAB_H控制柜标签位置.*
   :width: 9.95cm
   :align: center

   Label position of CAB L/H

.. figure:: ../../images/04_安全规范/CAB_L、CAB_H控制柜标签位置_2.*
   :width: 11.09cm
   :align: center

   Label position of CAB L/H

.. figure:: ../../images/04_安全规范/CAB_LiteAC、CAB_LiteDC控制柜标签位置（正门）.*
   :width: 9.51cm
   :align: center

   Label position of CAB LiteAC、CAB LiteDC (front)

.. figure:: ../../images/04_安全规范/CAB_LiteAC、CAB_LiteDC控制柜标签位置.*
   :width: 10.52cm
   :align: center

   Label position of CAB LiteAC、CAB LiteDC

.. figure:: ../../images/04_安全规范/CAB_LiteAC、CAB_LiteDC控制柜标签位置_2.*
   :width: 10.35cm
   :align: center

   Label position of CAB LiteAC、CAB LiteDC

.. list-table:: Description of labels
   :widths: 7 71 22
   :header-rows: 1
   :class: longtable

   * -
     - **Labels**
     - **Description**

   * - A
     - .. figure:: ../../images/04_安全规范/机器人铭牌.*
          :width: 5cm
          :align: center
     - Robot nameplate

   * -
     - .. figure:: ../../images/04_安全规范/CAB_L铭牌.*
          :width: 5cm
          :align: center
     - CAB L nameplate

   * -
     - .. figure:: ../../images/04_安全规范/CAB_H铭牌.*
          :width: 5cm
          :align: center
     - CAB H nameplate

   * -
     - .. figure:: ../../images/04_安全规范/CAB_LiteAC铭牌.*
          :width: 8cm
          :align: center
     - CAB LiteAC nameplate

   * -
     - .. figure:: ../../images/04_安全规范/CAB_LiteDC铭牌.*
          :width: 8cm
          :align: center
     - CAB LiteDC nameplate

   * - B
     - .. figure:: ../../images/04_安全规范/阅读说明书.*
          :width: 1.5cm
          :align: center
     - Read manual

   * - C
     - .. figure:: ../../images/04_安全规范/热表面.png
          :width: 1.5cm
          :align: center
     - Warning hot surface

   * - D
     - .. figure:: ../../images/04_安全规范/触电.*
          :width: 1.5cm
          :align: center
     - Beware of electric shock

   * - E
     - .. figure:: ../../images/04_安全规范/电源挂锁.*
          :width: 3cm
          :align: center
     - Lock out electrical power

   * - F
     - .. figure:: ../../images/04_安全规范/接地.png
          :width: 1.5cm
          :align: center
     - Grounding

   * - G
     - .. figure:: ../../images/04_安全规范/必须拔出插头.png
          :width: 1.5cm
          :align: center
     - Unplug before operation

   * - H
     - .. figure:: ../../images/04_安全规范/CE认证标识.png
          :width: 1.5cm
          :align: center
     - CE certification

   * - I
     - .. figure:: ../../images/04_安全规范/WEEE认证标识.png
          :width: 1.5cm
          :align: center
     - WEEE certification

   * - J
     - .. figure:: ../../images/04_安全规范/cSGSus认证标识.png
          :width: 1.5cm
          :align: center
     - cSGSus certification

   * - K
     - .. figure:: ../../images/04_安全规范/TUVsaar功能安全认证标识.png
          :width: 3cm
          :align: center
     - TUV saar functional safety certification

   * - L
     - .. figure:: ../../images/04_安全规范/CAB_L无线电认证标识.jpg
          :width: 4cm
          :align: center
     - CAB L wireless product certification

   * - 
     - .. figure:: ../../images/04_安全规范/CAB_H无线电认证标识.jpg
          :width: 4cm
          :align: center
     - CAB H wireless product certification

   * - 
     - .. figure:: ../../images/04_安全规范/CAB_LiteAC无线电认证标识.jpg
          :width: 4cm
          :align: center
     - CAB LiteAC wireless product certification

   * - 
     - .. figure:: ../../images/04_安全规范/CAB_LiteDC无线电认证标识.jpg
          :width: 4cm
          :align: center
     - CAB LiteDC wireless product certification

   * - M
     - .. figure:: ../../images/04_安全规范/夹手.*
          :width: 1.5cm
          :align: center
     - Beware of pinching

   * - N
     - .. figure:: ../../images/04_安全规范/撞击.*
          :width: 1.5cm
          :align: center
     - Beware of collision

   * - O
     - .. figure:: ../../images/04_安全规范/危险.png
          :width: 1.5cm
          :align: center
     - Beware of danger

.. note::

   - The serial numbers of both the robot and control cabinet are on the respective labels. The labels of robots are on the lower arm, and the label of control cabinet is on the front cover of the control cabinet.
   - Product labels and robot figures are only for reference, labels vary by robot and control cabinet model.
