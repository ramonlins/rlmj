"""
MuJoCo 3D Visualization with Camera Interaction

This script creates a 3D visualization of a box model using the MuJoCo physics engine
and the GLFW library. The script allows users to interactively manipulate the camera
view in the 3D scene using mouse and keyboard inputs. The camera can be rotated,
zoomed, and moved horizontally and vertically.

Mouse Interactions:
- Left Mouse Button + Shift Key: Rotate the camera horizontally and vertically.
- Right Mouse Button + Shift Key: Move the camera horizontally and vertically.
- Middle Mouse Button: Zoom the camera.

Keyboard Interactions:
- Left Shift Key or Right Shift Key (in combination with mouse interactions):
  Controls the behavior of camera rotation and movement.

The 3D scene is rendered using OpenGL, and the visualization is updated in real-time
at 60 frames per second. The box model can be dynamically simulated using the MuJoCo
physics engine.

Please note that this code requires the MuJoCo and GLFW libraries installed and their
Python bindings available. Additionally, a box model file in XML format is loaded for
visualization. The script uses the 'mujoco' and 'numpy' modules to interface with MuJoCo
and perform numerical computations.

The main function sets up the visualization window, camera, and input callbacks,
and then runs a real-time loop to update and render the 3D scene with user interactions.

To execute this script, ensure that the required libraries and resources are available.

This code is adapted from :
    [1] Deepmind/mujoco/sample/basic.cc

    [2] https://www.youtube.com/watch?v=ieOY0dR44iE&list=PLc7bpbeTIk75dgBVd07z6_uKN1KQkwFRK&index=9

"""
import os
import time
import sys

import mujoco
import numpy as np

from mujoco.glfw import glfw

# Buttons state
button_right = False
button_left = False
button_middle = False

# Callback initiation
lastx = 0
lasty = 0

# Get the full path
file_name = "box.xml"
dir_path = os.path.dirname(__file__)
xml_path = os.path.join(dir_path + '/models/' + file_name)

# Start data structure
model = mujoco.MjModel.from_xml_path(xml_path)
data = mujoco.MjData(model)
camera = mujoco.MjvCamera()
option = mujoco.MjvOption()

# Everything to Render 3D in opengl
scene = mujoco.MjvScene(model, maxgeom=10000)


def keyboard(window, key, scancode, action, mods):
    pass


def mouse_button(window, button, action, mods):
    # Update button state
    global button_left
    global button_middle
    global button_right

    button_left = (glfw.get_mouse_button(window, glfw.MOUSE_BUTTON_LEFT) == glfw.PRESS)
    button_middle = (glfw.get_mouse_button(window, glfw.MOUSE_BUTTON_MIDDLE) == glfw.PRESS)
    button_right = (glfw.get_mouse_button(window, glfw.MOUSE_BUTTON_RIGHT) == glfw.PRESS)

    # Update mouse position
    glfw.get_cursor_pos(window)


def mouse_move(window, xpos, ypos):
    global lastx
    global lasty

    # Compute mouse displacement; save
    dx = xpos - lastx
    dy = ypos - lasty
    lastx = xpos
    lasty = ypos

    # Get current window size
    width, height = glfw.get_window_size(window)

    # No button pressed
    if (not button_left) and (not button_right) and (not button_middle):
        return

    # Get key state from pressed button
    press_left_shift = glfw.get_key(window, glfw.KEY_LEFT_SHIFT) == glfw.PRESS

    press_right_shift = glfw.get_key(window, glfw.KEY_RIGHT_SHIFT) == glfw.PRESS

    mod_shift = (press_left_shift or press_right_shift)

    # Actions based on button key state
    if button_right:
        action = mujoco.mjtMouse.mjMOUSE_MOVE_H if mod_shift else mujoco.mjtMouse.mjMOUSE_MOVE_V
    elif button_left:
        action = mujoco.mjtMouse.mjMOUSE_ROTATE_H if mod_shift else mujoco.mjtMouse.mjMOUSE_ROTATE_V
    else:
        action = mujoco.mjtMouse.mjMOUSE_ZOOM

    # Move camera
    mujoco.mjv_moveCamera(model,
                          action,
                          dx/width,
                          dy/height,
                          scene,
                          camera)


def scroll(window, xoffset, yoffset):
    action = mujoco.mjtMouse.mjMOUSE_ZOOM

    mujoco.mjv_moveCamera(model,
                          action,
                          0.0,
                          -0.05 * yoffset,  # NOTE: Why change yoffset ?
                          scene,
                          camera
                          )


def main():
    # Create opengl context
    glfw.init()

    window = glfw.create_window(1200,
                                900,
                                "Box move demo",
                                None,
                                None)

    glfw.make_context_current(window)
    glfw.swap_interval(1)   # vsync

    # Initialize visualization data structures for proper rendering
    mujoco.mjv_defaultCamera(camera)
    mujoco.mjv_defaultOption(option)

    # Get custom opengl rendering context resources uploaded to gpu
    context = mujoco.MjrContext(model, mujoco.mjtFontScale.mjFONTSCALE_150.value)

    # Set GLFW I/O (mouse, keyboard) callbacks
    glfw.set_key_callback(window, keyboard)
    glfw.set_cursor_pos_callback(window, mouse_move)    # Track mouse position to the window
    glfw.set_mouse_button_callback(window, mouse_button)# Track mouse state
    glfw.set_scroll_callback(window, scroll)

    # Top down perspective
    camera.azimuth = 90.0
    camera.elevation = -90.0
    camera.distance = 5.0
    camera.lookat = np.array([0.0, 0.0, 0.0])

    start = time.time()
    while not glfw.window_should_close(window):
        while time.time() - start < 1.0/60.0:
            mujoco.mj_step(model, data)

        # Get framebuffer viewport to ensure right pixel and screen coordinates map
        viewport_width, viewport_height = glfw.get_framebuffer_size(window)
        viewport = mujoco.MjrRect(0, 0, viewport_width, viewport_height)

        # Update scene
        # The mjtCatBit type specifies which geom category should be rendered in this case all
        mujoco.mjv_updateScene(model,
                                data,
                                option,
                                None,
                                camera,
                                mujoco.mjtCatBit.mjCAT_ALL.value,
                                scene)

        # Render scene
        mujoco.mjr_render(viewport, scene, context)

        # Swap OpenGL buffers front (display) and back (render)
        glfw.swap_buffers(window)

        # Process pending GUI events, call GLFW callbacks
        glfw.poll_events()

    glfw.terminate()


if __name__ == "__main__":
    main()
