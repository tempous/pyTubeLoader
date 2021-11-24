import dearpygui.dearpygui as dpg

dpg.create_context()
with dpg.window(label='Input video link below and click on the button', width=494, height=100, pos=(0, 50),
no_collapse=True, no_close=True, no_move=True, no_resize=True, no_scrollbar=True, no_background=True):
    tb_url=dpg.add_input_text(label='URL', width=440, hint='https://www.youtube.com/watch?v=***********', no_spaces=True)
    tb_path=dpg.add_input_text(label='PATH', width=440, hint='D:\Downloads')
    dpg.add_button(label='Download video via URL')
dpg.create_viewport(title='YouTube Video Loader', max_width=500, max_height=250, resizable=False, clear_color=(28, 28, 28, 255))
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()