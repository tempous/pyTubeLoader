import dearpygui.dearpygui as dpg
from pytube import YouTube

def download_via_pytube(sender, app_data, user_data):
    url = dpg.get_value(user_data[0])
    path = dpg.get_value(user_data[1])
    try:
        yt = YouTube(url)
    except:
        print('Connection Error or Incorrect URL!')
        return
    print(f"Downloading [{yt.title}] (by {yt.author})")
    yt.streams.get_highest_resolution().download(path)
    print('Operation completed!')


dpg.create_context()
with dpg.window(label='Input video link below and click on the button', width=494, height=100, pos=(0, 50),
no_collapse=True, no_close=True, no_move=True, no_resize=True, no_scrollbar=True, no_background=True):
    tb_url=dpg.add_input_text(label='URL', width=440, hint='https://www.youtube.com/watch?v=***********', no_spaces=True)
    tb_path=dpg.add_input_text(label='PATH', width=440, hint='D:\Downloads')
    tb_list=[tb_url, tb_path]
    dpg.add_button(label='Download video via URL', callback=download_via_pytube, user_data=tb_list)
dpg.create_viewport(title='YouTube Video Loader', max_width=500, max_height=250, resizable=False, clear_color=(28, 28, 28, 255))
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()