import os
import time

import mujoco
import numpy as np

from mujoco.glfw import glfw


def keyboard():
    pass


def mouse_move():
    pass


def mouse_button():
    pass


def scroll():
    pass


def main():
    # Get the full path
    file_name = "box.xml"
    dir_path = os.path.dirname(__file__)
    xml_path = os.path.join(dir_path + '/models/' + file_name)

    # Separation of model and data structures
    model = mujoco.MjModel.from_xml_path(xml_path)
    data = mujoco.MjData(model)
    camera = mujoco.MjvCamera()
    option = mujoco.MjvOption()

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
    scene = mujoco.MjvScene(model, maxgeom=10000)  # Everything to Render 3D in opengl

    # Get custom opengl rendering context resources uploaded to gpu
    context = mujoco.MjrContext(model, mujoco.mjtFontScale.mjFONTSCALE_150.value)

    # Set GLFW I/O (mouse, keyboard) callbacks
    # glfw.set_key_callback(window, keyboard)
    # glfw.set_cursor_pos_callback(window, mouse_move)
    # glfw.set_mouse_button_callback(window, mouse_button)
    # glfw.set_scroll_callback(window, scroll)

    duration = 5
    start = time.time()
    while not glfw.window_should_close(window):
        while time.time() - start < duration:
            mujoco.mj_step(model, data)

            # NOTE: Review all code bellow
            # get framebuffer viewport
            viewport_width, viewport_height = glfw.get_framebuffer_size(
                window)
            viewport = mujoco.MjrRect(0, 0, viewport_width, viewport_height)

            mujoco.mjv_updateScene(model,
                                   data,
                                   option,
                                   None,
                                   camera,
                                   mujoco.mjtCatBit.mjCAT_ALL.value,
                                   scene)

            mujoco.mjr_render(viewport, scene, context)

            # Swap OpenGL buffers
            glfw.swap_buffers(window)

            # Process pending GUI events, call GLFW callbacks
            glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()
