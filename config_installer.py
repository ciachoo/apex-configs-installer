from tkinter import *
from tkinter.filedialog import askdirectory

class KeyCapture:
    def __init__(self, master):
        self.master = master
        self.key = None
        self.label_prompt = None
        self.label_response = None
        
        # Create a "Start" button
        self.start_button = Button(self.master, text="Choose a key to set as the toggle bind", command=self.capture_key)
        self.start_button.pack(pady=5)
        
        # Bind keyboard events to the root window
        self.master.bind("<Key>", self.key_pressed)

    def capture_key(self):
        # Disable the "Start" button and display instructions
        self.start_button.config(state=DISABLED, text="Press a key...")
        self.label_prompt = Label(self.master, text="Press a key on your keyboard or mouse.")
        self.label_prompt.pack(pady=5)

    def key_pressed(self, event):
        # Save the pressed key and update the UI
        if self.label_response is not None:
            self.label_response.destroy()
        self.key = event.keysym
        self.label_response = Label(self.master, text=f"Key '{self.key}' captured!")
        self.label_response.pack(pady=5)
        self.start_button.config(state=NORMAL, text="Start") # Re-enable the "Start" button
        self.label_prompt.destroy()

class DirectorySelector:
    def __init__(self, master):
        self.master = master
        self.selected_directory = None
        
        # Create a "Select directory" button
        select_directory_button = Button(self.master, text="Select directory", command=self.get_directory)
        select_directory_button.pack(pady=5)

    def get_directory(self):
        directory = askdirectory()
        self.selected_directory = directory
        
class GetStrafeType:
    def __init__(self, master):
        self.master = master
        self.strafe_type = None
        
        # Create a "Select directory" button
        strafe = StringVar(master)
        strafe.set("Select type of strafe")
        self.strafe = OptionMenu(master, strafe, "Neo strafe", "2 directional strafe", "Superglide", command=self.set_type)
        self.strafe.pack(pady=5)
        
    def set_type(self, selected_type):
        self.strafe_type = selected_type

def destroy():
    global error_label
    if get_key.key and get_directory.selected_directory and get_strafe_type.strafe_type:
        master.destroy()
    else:
        if not error_label:
            error_label = Label(master, text="Please select all 3 options before pressing the button")
            error_label.pack(pady=5)

global error_label
error_label = None

master = Tk()
master.minsize(350, 200)
get_key = KeyCapture(master)
get_directory = DirectorySelector(master)
get_strafe_type = GetStrafeType(master)

confirm = Button(master, text="Press this once all 3 options have been set to your liking", command=destroy)
confirm.pack(pady=5)

master.mainloop()

key = get_key.key
directory = get_directory.selected_directory + "/cfg/"
strafe_type = get_strafe_type.strafe_type

if strafe_type == "2 directional strafe":
    filenames = ['2directionalstrafe1.cfg', '2directionalstrafe00010.cfg', '2directionalstrafe00011.cfg', '2directionalstrafe00012.cfg', '2directionalstrafe00013.cfg', '2directionalstrafe00014.cfg', '2directionalstrafe00015.cfg', '2directionalstrafe00016.cfg', '2directionalstrafe00017.cfg', '2directionalstrafe0002.cfg', '2directionalstrafe0003.cfg', '2directionalstrafe0004.cfg', '2directionalstrafe0005.cfg', '2directionalstrafe0006.cfg', '2directionalstrafe0007.cfg', '2directionalstrafe0008.cfg', '2directionalstrafe0009.cfg', '2directionalstrafe0010.cfg', '2directionalstrafe0011.cfg', '2directionalstrafe0012.cfg', '2directionalstrafe0013.cfg', '2directionalstrafe0014.cfg', '2directionalstrafe0015.cfg', '2directionalstrafe0016.cfg', '2directionalstrafe0017.cfg', '2directionalstrafe002.cfg', '2directionalstrafe003.cfg', '2directionalstrafe004.cfg', '2directionalstrafe005.cfg', '2directionalstrafe006.cfg', '2directionalstrafe007.cfg',
                 '2directionalstrafe008.cfg', '2directionalstrafe009.cfg', '2directionalstrafe010.cfg', '2directionalstrafe011.cfg', '2directionalstrafe012.cfg', '2directionalstrafe013.cfg', '2directionalstrafe014.cfg', '2directionalstrafe015.cfg', '2directionalstrafe016.cfg', '2directionalstrafe017.cfg', '2directionalstrafe02.cfg', '2directionalstrafe03.cfg', '2directionalstrafe04.cfg', '2directionalstrafe05.cfg', '2directionalstrafe06.cfg', '2directionalstrafe07.cfg', '2directionalstrafe08.cfg', '2directionalstrafe09.cfg', '2directionalstrafe10.cfg', '2directionalstrafe11.cfg', '2directionalstrafe12.cfg', '2directionalstrafe13.cfg', '2directionalstrafe14.cfg', '2directionalstrafe15.cfg', '2directionalstrafe16.cfg', '2directionalstrafe17.cfg', '2directionalstrafe2.cfg', '2directionalstrafe3.cfg', '2directionalstrafe4.cfg', '2directionalstrafe5.cfg', '2directionalstrafe6.cfg', '2directionalstrafe7.cfg', '2directionalstrafe8.cfg', '2directionalstrafe9.cfg']
    content = ['bind "MWHEELDOWN" "+jump"\nbind "MWHEELUP" "+forward; +jump"\nbind "5" "exec 2directionalstrafe0002.cfg" ', 'bind "MWHEELDOWN" "+jump; +backward; exec 2directionalstrafe0010.cfg" \nbind "MWHEELUP" "+jump; exec 2directionalstrafe0007.cfg"\nbind "5" "exec 2directionalstrafe1.cfg" ', 'bind "MWHEELDOWN" "+jump; +backward; +moveright; exec 2directionalstrafe0011.cfg" \nbind "MWHEELUP" "+jump; exec 2directionalstrafe0006.cfg" \nbind "5" "exec 2directionalstrafe1.cfg" \n', 'bind "MWHEELDOWN" "+jump; +moveright; exec 2directionalstrafe0012.cfg" \nbind "MWHEELUP" "+jump; exec 2directionalstrafe0005.cfg"\nbind "5" "exec 2directionalstrafe1.cfg" ', 'bind "MWHEELDOWN" "+jump; +moveright; +forward; exec 2directionalstrafe0013.cfg" \nbind "MWHEELUP" "+jump; exec 2directionalstrafe0004.cfg"\nbind "5" "exec 2directionalstrafe1.cfg" \n', 'bind "MWHEELDOWN" "+jump; +forward; exec 2directionalstrafe0014.cfg" \nbind "MWHEELUP" "+jump; exec 2directionalstrafe0003.cfg" \nbind "5" "exec 2directionalstrafe1.cfg" \n ', 'bind "MWHEELDOWN" "+jump; +forward; +moveleft; exec 2directionalstrafe0015.cfg"\nbind "MWHEELUP" "+jump; exec 2directionalstrafe0002.cfg"  \nbind "5" "exec 2directionalstrafe1.cfg" ', 'bind "MWHEELDOWN" "+jump; +moveleft; exec 2directionalstrafe0016.cfg" \nbind "MWHEELup" "+jump; exec 2directionalstrafe0009.cfg" \nbind "5" "exec 2directionalstrafe1.cfg" \n ', 'bind "MWHEELDOWN" "+jump; +moveleft; +backward; exec 2directionalstrafe0017.cfg"\nbind "MWHEELUP" "+jump; exec 2directionalstrafe0008.cfg"  \nbind "5" "exec 2directionalstrafe1.cfg" ', 'bind "MWHEELDOWN" "+jump; exec 2directionalstrafe00015.cfg" \nbind "MWHEELUP" "+jump; +forward; exec 2directionalstrafe002.cfg"\nbind "5" "exec 2directionalstrafe1.cfg" \n', 'bind "MWHEELDOWN" "+jump; exec 2directionalstrafe00014.cfg" \nbind "MWHEELUP" "+jump; +forward; +moveright; exec 2directionalstrafe003.cfg" \nbind "5" "exec 2directionalstrafe1.cfg" \n ', 'bind "MWHEELDOWN" "+jump; exec 2directionalstrafe00013.cfg"\nbind "MWHEELUP" "+jump; +moveright; exec 2directionalstrafe004.cfg"  \nbind "5" "exec 2directionalstrafe1.cfg" ', 'bind "MWHEELDOWN" "+jump; exec 2directionalstrafe00012.cfg" \nbind "MWHEELup" "+jump; +backward; +moveright; exec 2directionalstrafe005.cfg" \nbind "5" "exec 2directionalstrafe1.cfg" \n ', 'bind "MWHEELDOWN" "+jump; exec 2directionalstrafe00011.cfg"\nbind "MWHEELUP" "+jump; +backward; exec 2directionalstrafe006.cfg"  \nbind "5" "exec 2directionalstrafe1.cfg" ', 'bind "MWHEELDOWN" "+jump; exec 2directionalstrafe00010.cfg" \nbind "MWHEELUP" "+jump; +backward; +moveleft; exec 2directionalstrafe007.cfg"\nbind "5" "exec 2directionalstrafe1.cfg" ', 'bind "MWHEELDOWN" "+jump; exec 2directionalstrafe00017.cfg" \nbind "MWHEELUP" "+jump; +moveleft; exec 2directionalstrafe008.cfg" \nbind "5" "exec 2directionalstrafe1.cfg" \n', 'bind "MWHEELDOWN" "+jump; exec 2directionalstrafe00016.cfg" \nbind "MWHEELUP" "+jump; +forward; +moveleft; exec 2directionalstrafe009.cfg"\nbind "5" "exec 2directionalstrafe1.cfg" ', 'bind "MWHEELDOWN" "+jump; +backward; exec 2directionalstrafe010.cfg" \nbind "MWHEELUP" "+jump; exec 2directionalstrafe0007.cfg"\nbind "5" "exec 2directionalstrafe1.cfg" ', 'bind "MWHEELDOWN" "+jump; +backward; +moveright; exec 2directionalstrafe011.cfg" \nbind "MWHEELUP" "+jump; exec 2directionalstrafe0006.cfg" \nbind "5" "exec 2directionalstrafe1.cfg" \n', 'bind "MWHEELDOWN" "+jump; +moveright; exec 2directionalstrafe012.cfg" \nbind "MWHEELUP" "+jump; exec 2directionalstrafe0005.cfg"\nbind "5" "exec 2directionalstrafe1.cfg" ', 'bind "MWHEELDOWN" "+jump; +moveright; +forward; exec 2directionalstrafe013.cfg" \nbind "MWHEELUP" "+jump; exec 2directionalstrafe0004.cfg" \nbind "5" "exec 2directionalstrafe1.cfg" \n', 'bind "MWHEELDOWN" "+jump; +forward; exec 2directionalstrafe014.cfg" \nbind "MWHEELUP" "+jump; exec 2directionalstrafe0003.cfg"\nbind "5" "exec 2directionalstrafe1.cfg" \n', 'bind "MWHEELDOWN" "+jump; +forward; +moveleft; exec 2directionalstrafe015.cfg" \nbind "MWHEELUP" "+jump; exec 2directionalstrafe0002.cfg" \nbind "5" "exec 2directionalstrafe1.cfg" \n ', 'bind "MWHEELDOWN" "+jump; +moveleft; exec 2directionalstrafe016.cfg"\nbind "MWHEELUP" "+jump; exec 2directionalstrafe0009.cfg"  \nbind "5" "exec 2directionalstrafe1.cfg" ', 'bind "MWHEELDOWN" "+jump; +moveleft; +backward; exec 2directionalstrafe017.cfg" \nbind "MWHEELup" "+jump; exec 2directionalstrafe0008.cfg" \nbind "5" "exec 2directionalstrafe1.cfg" \n ', 'bind "MWHEELDOWN" "+jump; exec 2directionalstrafe00015.cfg" \nbind "MWHEELUP" "+jump; +forward; exec 2directionalstrafe02.cfg" \nbind "5" "exec 2directionalstrafe1.cfg" \n', 'bind "MWHEELDOWN" "+jump; exec 2directionalstrafe00014.cfg" \nbind "MWHEELUP" "+jump; +forward; +moveright; exec 2directionalstrafe03.cfg"\nbind "5" "exec 2directionalstrafe1.cfg" \n', 'bind "MWHEELDOWN" "+jump; exec 2directionalstrafe00013.cfg" \nbind "MWHEELUP" "+jump; +moveright; exec 2directionalstrafe04.cfg" \nbind "5" "exec 2directionalstrafe1.cfg" \n ', 'bind "MWHEELDOWN" "+jump; exec 2directionalstrafe00012.cfg"\nbind "MWHEELUP" "+jump; +backward; +moveright; exec 2directionalstrafe05.cfg"  \nbind "5" "exec 2directionalstrafe1.cfg" ', 'bind "MWHEELDOWN" "+jump; exec 2directionalstrafe00011.cfg" \nbind "MWHEELup" "+jump; +backward; exec 2directionalstrafe06.cfg" \nbind "5" "exec 2directionalstrafe1.cfg" \n ', 'bind "MWHEELDOWN" "+jump; exec 2directionalstrafe00010.cfg" \nbind "MWHEELUP" "+jump; +backward; +moveleft; exec 2directionalstrafe07.cfg"\nbind "5" "exec 2directionalstrafe1.cfg" ', 'bind "MWHEELDOWN" "+jump; exec 2directionalstrafe00017.cfg" \nbind "MWHEELUP" "+jump; +moveleft; exec 2directionalstrafe08.cfg" \nbind "5" "exec 2directionalstrafe1.cfg" \n', 'bind "MWHEELDOWN" "+jump; exec 2directionalstrafe00016.cfg" \nbind "MWHEELUP" "+jump; +forward; +moveleft; exec 2directionalstrafe09.cfg"\nbind "5" "exec 2directionalstrafe1.cfg" ',
               'bind "MWHEELDOWN" "+jump; +backward; exec 2directionalstrafe10.cfg" \nbind "MWHEELUP" "+jump; exec 2directionalstrafe0007.cfg"\nbind "5" "exec 2directionalstrafe1.cfg" ', 'bind "MWHEELDOWN" "+jump; +backward; +moveright; exec 2directionalstrafe11.cfg" \nbind "MWHEELUP" "+jump; exec 2directionalstrafe0006.cfg" \nbind "5" "exec 2directionalstrafe1.cfg" \n', 'bind "MWHEELDOWN" "+jump; +moveright; exec 2directionalstrafe12.cfg" \nbind "MWHEELUP" "+jump; exec 2directionalstrafe0005.cfg"\nbind "5" "exec 2directionalstrafe1.cfg" ', 'bind "MWHEELDOWN" "+jump; +moveright; +forward; exec 2directionalstrafe13.cfg" \nbind "MWHEELUP" "+jump; exec 2directionalstrafe0004.cfg" \nbind "5" "exec 2directionalstrafe1.cfg" \n', 'bind "MWHEELDOWN" "+jump; +forward; exec 2directionalstrafe14.cfg" \nbind "MWHEELUP" "+jump; exec 2directionalstrafe0003.cfg"\nbind "5" "exec 2directionalstrafe1.cfg" \n', 'bind "MWHEELDOWN" "+jump; +forward; +moveleft; exec 2directionalstrafe15.cfg" \nbind "MWHEELUP" "+jump; exec 2directionalstrafe0002.cfg" \nbind "5" "exec 2directionalstrafe1.cfg" \n ', 'bind "MWHEELDOWN" "+jump; +moveleft; exec 2directionalstrafe16.cfg"\nbind "MWHEELUP" "+jump; exec 2directionalstrafe0009.cfg"  \nbind "5" "exec 2directionalstrafe1.cfg" ', 'bind "MWHEELDOWN" "+jump; +moveleft; +backward; exec 2directionalstrafe17.cfg" \nbind "MWHEELup" "+jump; exec 2directionalstrafe0008.cfg" \nbind "5" "exec 2directionalstrafe1.cfg" \n ', 'bind "MWHEELDOWN" "+jump; exec 2directionalstrafe00015.cfg" \nbind "MWHEELUP" "+jump; +forward; exec 2directionalstrafe2.cfg" \nbind "5" "exec 2directionalstrafe1.cfg" \n', 'bind "MWHEELDOWN" "+jump; exec 2directionalstrafe00014.cfg" \nbind "MWHEELUP" "+jump; +forward; +moveright; exec 2directionalstrafe3.cfg"\nbind "5" "exec 2directionalstrafe1.cfg" \n', 'bind "MWHEELDOWN" "+jump; exec 2directionalstrafe00013.cfg" \nbind "MWHEELUP" "+jump; +moveright; exec 2directionalstrafe4.cfg" \nbind "5" "exec 2directionalstrafe1.cfg" \n ', 'bind "MWHEELDOWN" "+jump; exec 2directionalstrafe00012.cfg"\nbind "MWHEELUP" "+jump; +backward; +moveright; exec 2directionalstrafe5.cfg"  \nbind "5" "exec 2directionalstrafe1.cfg" ', 'bind "MWHEELDOWN" "+jump; exec 2directionalstrafe00011.cfg" \nbind "MWHEELup" "+jump; +backward; exec 2directionalstrafe6.cfg" \nbind "5" "exec 2directionalstrafe1.cfg" \n ', 'bind "MWHEELDOWN" "+jump; exec 2directionalstrafe00010.cfg" \nbind "MWHEELUP" "+jump; +backward; +moveleft; exec 2directionalstrafe7.cfg"\nbind "5" "exec 2directionalstrafe1.cfg" ', 'bind "MWHEELDOWN" "+jump; exec 2directionalstrafe00017.cfg" \nbind "MWHEELUP" "+jump; +moveleft; exec 2directionalstrafe8.cfg" \nbind "5" "exec 2directionalstrafe1.cfg" \n', 'bind "MWHEELDOWN" "+jump; exec 2directionalstrafe00016.cfg" \nbind "MWHEELUP" "+jump; +forward; +moveleft; exec 2directionalstrafe9.cfg"\nbind "5" "exec 2directionalstrafe1.cfg" ', 'bind "MWHEELDOWN" "+jump; +backward; exec 2directionalstrafe00011.cfg" \nbind "MWHEELUP" "+jump; exec 2directionalstrafe0007.cfg" \nbind "5" "exec 2directionalstrafe1.cfg" \n', 'bind "MWHEELDOWN" "+jump; +backward; +moveright; exec 2directionalstrafe00012.cfg" \nbind "MWHEELUP" "+jump; exec 2directionalstrafe0006.cfg"\nbind "5" "exec 2directionalstrafe1.cfg" ', 'bind "MWHEELDOWN" "+jump; +moveright; exec 2directionalstrafe00013.cfg" \nbind "MWHEELUP" "+jump; exec 2directionalstrafe0005.cfg"\nbind "5" "exec 2directionalstrafe1.cfg"  ', 'bind "MWHEELDOWN" "+jump; +moveright; +forward; exec 2directionalstrafe00014.cfg" \nbind "MWHEELUP" "+jump; exec 2directionalstrafe0004.cfg" \nbind "5" "exec 2directionalstrafe1.cfg" \n', 'bind "MWHEELDOWN" "+jump; +forward; exec 2directionalstrafe00015.cfg" \nbind "MWHEELUP" "+jump; exec 2directionalstrafe0003.cfg"\nbind "5" "exec 2directionalstrafe1.cfg" \n', 'bind "MWHEELDOWN" "+jump; +forward; +moveleft; exec 2directionalstrafe00016.cfg" \nbind "MWHEELUP" "+jump; exec 2directionalstrafe0002.cfg" \nbind "5" "exec 2directionalstrafe1.cfg" \n ', 'bind "MWHEELDOWN" "+jump; +moveleft; exec 2directionalstrafe00017.cfg"\nbind "MWHEELUP" "+jump; exec 2directionalstrafe0009.cfg"  \nbind "5" "exec 2directionalstrafe1.cfg" ', 'bind "MWHEELDOWN" "+jump; +moveleft; +backward; exec 2directionalstrafe00010.cfg" \nbind "MWHEELup" "+jump; exec 2directionalstrafe0008.cfg" \nbind "5" "exec 2directionalstrafe1.cfg" \n ', 'bind "MWHEELDOWN" "+jump; exec 2directionalstrafe00015.cfg" \nbind "MWHEELUP" "+jump; +forward; exec 2directionalstrafe0003.cfg" \nbind "5" "exec 2directionalstrafe1.cfg" \n', 'bind "MWHEELDOWN" "+jump; exec 2directionalstrafe00014.cfg" \nbind "MWHEELUP" "+jump; +forward; +moveright; exec 2directionalstrafe0004.cfg"\nbind "5" "exec 2directionalstrafe1.cfg" \n', 'bind "MWHEELDOWN" "+jump; exec 2directionalstrafe00013.cfg" \nbind "MWHEELUP" "+jump; +moveright; exec 2directionalstrafe0005.cfg" \nbind "5" "exec 2directionalstrafe1.cfg" \n ', 'bind "MWHEELDOWN" "+jump; exec 2directionalstrafe00012.cfg"\nbind "MWHEELUP" "+jump; +backward; +moveright; exec 2directionalstrafe0006.cfg"  \nbind "5" "exec 2directionalstrafe1.cfg" ', 'bind "MWHEELDOWN" "+jump; exec 2directionalstrafe00011.cfg" \nbind "MWHEELup" "+jump; +backward; exec 2directionalstrafe0007.cfg" \nbind "5" "exec 2directionalstrafe1.cfg" \n ', 'bind "MWHEELDOWN" "+jump; exec 2directionalstrafe00010.cfg" \nbind "MWHEELUP" "+jump; +backward; +moveleft; exec 2directionalstrafe0008.cfg"\nbind "5" "exec 2directionalstrafe1.cfg" ', 'bind "MWHEELDOWN" "+jump; exec 2directionalstrafe00017.cfg" \nbind "MWHEELUP" "+jump; +moveleft; exec 2directionalstrafe0009.cfg" \nbind "5" "exec 2directionalstrafe1.cfg" \n', 'bind "MWHEELDOWN" "+jump; exec 2directionalstrafe00016.cfg" \nbind "MWHEELUP" "+jump; +forward; +moveleft; exec 2directionalstrafe0002.cfg"\nbind "5" "exec 2directionalstrafe1.cfg" ']
elif strafe_type == "Neo strafe": 
    filenames = ['neo_strafe1.cfg', 'neostrafe00010.cfg', 'neostrafe00011.cfg', 'neostrafe00012.cfg', 'neostrafe00013.cfg', 'neostrafe00014.cfg', 'neostrafe00015.cfg', 'neostrafe00016.cfg', 'neostrafe00017.cfg', 'neostrafe0002.cfg', 'neostrafe0003.cfg', 'neostrafe0004.cfg', 'neostrafe0005.cfg', 'neostrafe0006.cfg', 'neostrafe0007.cfg', 'neostrafe0008.cfg', 'neostrafe0009.cfg', 'neostrafe0010.cfg', 'neostrafe0011.cfg', 'neostrafe0012.cfg', 'neostrafe0013.cfg', 'neostrafe0014.cfg', 'neostrafe0015.cfg', 'neostrafe0016.cfg', 'neostrafe0017.cfg', 'neostrafe002.cfg', 'neostrafe003.cfg', 'neostrafe004.cfg', 'neostrafe005.cfg', 'neostrafe006.cfg', 'neostrafe007.cfg',
                 'neostrafe008.cfg', 'neostrafe009.cfg', 'neostrafe010.cfg', 'neostrafe011.cfg', 'neostrafe012.cfg', 'neostrafe013.cfg', 'neostrafe014.cfg', 'neostrafe015.cfg', 'neostrafe016.cfg', 'neostrafe017.cfg', 'neostrafe02.cfg', 'neostrafe03.cfg', 'neostrafe04.cfg', 'neostrafe05.cfg', 'neostrafe06.cfg', 'neostrafe07.cfg', 'neostrafe08.cfg', 'neostrafe09.cfg', 'neostrafe10.cfg', 'neostrafe11.cfg', 'neostrafe12.cfg', 'neostrafe13.cfg', 'neostrafe14.cfg', 'neostrafe15.cfg', 'neostrafe16.cfg', 'neostrafe17.cfg', 'neostrafe2.cfg', 'neostrafe3.cfg', 'neostrafe4.cfg', 'neostrafe5.cfg', 'neostrafe6.cfg', 'neostrafe7.cfg', 'neostrafe8.cfg', 'neostrafe9.cfg']
    content = ['bind "MWHEELDOWN" "+jump"\nbind "MWHEELUP" "+forward; +jump;"\nbind "4" "exec neo_strafe0002.cfg" ', 'bind "MWHEELDOWN" "+jump; +backward; exec neostrafe0010.cfg" \nbind "MWHEELUP" "+jump; exec neostrafe0007.cfg"\nbind "5" "exec neostrafe1.cfg" ', 'bind "MWHEELDOWN" "+jump; +backward; +moveright; exec neostrafe0011.cfg" \nbind "MWHEELUP" "+jump; exec neostrafe0006.cfg" \nbind "5" "exec neostrafe1.cfg" \n', 'bind "MWHEELDOWN" "+jump; +moveright; exec neostrafe0012.cfg" \nbind "MWHEELUP" "+jump; exec neostrafe0005.cfg"\nbind "5" "exec neostrafe1.cfg" ', 'bind "MWHEELDOWN" "+jump; +moveright; +forward; exec neostrafe0013.cfg" \nbind "MWHEELUP" "+jump; exec neostrafe0004.cfg"\nbind "5" "exec neostrafe1.cfg" \n', 'bind "MWHEELDOWN" "+jump; +forward; exec neostrafe0014.cfg" \nbind "MWHEELUP" "+jump; exec neostrafe0003.cfg" \nbind "5" "exec neostrafe1.cfg" \n ', 'bind "MWHEELDOWN" "+jump; +forward; +moveleft; exec neostrafe0015.cfg"\nbind "MWHEELUP" "+jump; exec neostrafe0002.cfg"  \nbind "5" "exec neostrafe1.cfg" ', 'bind "MWHEELDOWN" "+jump; +moveleft; exec neostrafe0016.cfg" \nbind "MWHEELup" "+jump; exec neostrafe0009.cfg" \nbind "5" "exec neostrafe1.cfg" \n ', 'bind "MWHEELDOWN" "+jump; +moveleft; +backward; exec neostrafe0017.cfg"\nbind "MWHEELUP" "+jump; exec neostrafe0008.cfg"  \nbind "5" "exec neostrafe1.cfg" ', 'bind "MWHEELDOWN" "+jump; exec neostrafe00015.cfg" \nbind "MWHEELUP" "+jump; +forward; exec neostrafe002.cfg"\nbind "5" "exec neostrafe1.cfg" \n', 'bind "MWHEELDOWN" "+jump; exec neostrafe00014.cfg" \nbind "MWHEELUP" "+jump; +forward; +moveright; exec neostrafe003.cfg" \nbind "5" "exec neostrafe1.cfg" \n ', 'bind "MWHEELDOWN" "+jump; exec neostrafe00013.cfg"\nbind "MWHEELUP" "+jump; +moveright; exec neostrafe004.cfg"  \nbind "5" "exec neostrafe1.cfg" ', 'bind "MWHEELDOWN" "+jump; exec neostrafe00012.cfg" \nbind "MWHEELup" "+jump; +backward; +moveright; exec neostrafe005.cfg" \nbind "5" "exec neostrafe1.cfg" \n ', 'bind "MWHEELDOWN" "+jump; exec neostrafe00011.cfg"\nbind "MWHEELUP" "+jump; +backward; exec neostrafe006.cfg"  \nbind "5" "exec neostrafe1.cfg" ', 'bind "MWHEELDOWN" "+jump; exec neostrafe00010.cfg" \nbind "MWHEELUP" "+jump; +backward; +moveleft; exec neostrafe007.cfg"\nbind "5" "exec neostrafe1.cfg" ', 'bind "MWHEELDOWN" "+jump; exec neostrafe00017.cfg" \nbind "MWHEELUP" "+jump; +moveleft; exec neostrafe008.cfg" \nbind "5" "exec neostrafe1.cfg" \n', 'bind "MWHEELDOWN" "+jump; exec neostrafe00016.cfg" \nbind "MWHEELUP" "+jump; +forward; +moveleft; exec neostrafe009.cfg"\nbind "5" "exec neostrafe1.cfg" ', 'bind "MWHEELDOWN" "+jump; +backward; exec neostrafe010.cfg" \nbind "MWHEELUP" "+jump; exec neostrafe0007.cfg"\nbind "5" "exec neostrafe1.cfg" ', 'bind "MWHEELDOWN" "+jump; +backward; +moveright; exec neostrafe011.cfg" \nbind "MWHEELUP" "+jump; exec neostrafe0006.cfg" \nbind "5" "exec neostrafe1.cfg" \n', 'bind "MWHEELDOWN" "+jump; +moveright; exec neostrafe012.cfg" \nbind "MWHEELUP" "+jump; exec neostrafe0005.cfg"\nbind "5" "exec neostrafe1.cfg" ', 'bind "MWHEELDOWN" "+jump; +moveright; +forward; exec neostrafe013.cfg" \nbind "MWHEELUP" "+jump; exec neostrafe0004.cfg" \nbind "5" "exec neostrafe1.cfg" \n', 'bind "MWHEELDOWN" "+jump; +forward; exec neostrafe014.cfg" \nbind "MWHEELUP" "+jump; exec neostrafe0003.cfg"\nbind "5" "exec neostrafe1.cfg" \n', 'bind "MWHEELDOWN" "+jump; +forward; +moveleft; exec neostrafe015.cfg" \nbind "MWHEELUP" "+jump; exec neostrafe0002.cfg" \nbind "5" "exec neostrafe1.cfg" \n ', 'bind "MWHEELDOWN" "+jump; +moveleft; exec neostrafe016.cfg"\nbind "MWHEELUP" "+jump; exec neostrafe0009.cfg"  \nbind "5" "exec neostrafe1.cfg" ', 'bind "MWHEELDOWN" "+jump; +moveleft; +backward; exec neostrafe017.cfg" \nbind "MWHEELup" "+jump; exec neostrafe0008.cfg" \nbind "5" "exec neostrafe1.cfg" \n ', 'bind "MWHEELDOWN" "+jump; exec neostrafe00015.cfg" \nbind "MWHEELUP" "+jump; +forward; exec neostrafe02.cfg" \nbind "5" "exec neostrafe1.cfg" \n', 'bind "MWHEELDOWN" "+jump; exec neostrafe00014.cfg" \nbind "MWHEELUP" "+jump; +forward; +moveright; exec neostrafe03.cfg"\nbind "5" "exec neostrafe1.cfg" \n', 'bind "MWHEELDOWN" "+jump; exec neostrafe00013.cfg" \nbind "MWHEELUP" "+jump; +moveright; exec neostrafe04.cfg" \nbind "5" "exec neostrafe1.cfg" \n ', 'bind "MWHEELDOWN" "+jump; exec neostrafe00012.cfg"\nbind "MWHEELUP" "+jump; +backward; +moveright; exec neostrafe05.cfg"  \nbind "5" "exec neostrafe1.cfg" ', 'bind "MWHEELDOWN" "+jump; exec neostrafe00011.cfg" \nbind "MWHEELup" "+jump; +backward; exec neostrafe06.cfg" \nbind "5" "exec neostrafe1.cfg" \n ', 'bind "MWHEELDOWN" "+jump; exec neostrafe00010.cfg" \nbind "MWHEELUP" "+jump; +backward; +moveleft; exec neostrafe07.cfg"\nbind "5" "exec neostrafe1.cfg" ', 'bind "MWHEELDOWN" "+jump; exec neostrafe00017.cfg" \nbind "MWHEELUP" "+jump; +moveleft; exec neostrafe08.cfg" \nbind "5" "exec neostrafe1.cfg" \n', 'bind "MWHEELDOWN" "+jump; exec neostrafe00016.cfg" \nbind "MWHEELUP" "+jump; +forward; +moveleft; exec neostrafe09.cfg"\nbind "5" "exec neostrafe1.cfg" ',
               'bind "MWHEELDOWN" "+jump; +backward; exec neostrafe10.cfg" \nbind "MWHEELUP" "+jump; exec neostrafe0007.cfg"\nbind "5" "exec neostrafe1.cfg" ', 'bind "MWHEELDOWN" "+jump; +backward; +moveright; exec neostrafe11.cfg" \nbind "MWHEELUP" "+jump; exec neostrafe0006.cfg" \nbind "5" "exec neostrafe1.cfg" \n', 'bind "MWHEELDOWN" "+jump; +moveright; exec neostrafe12.cfg" \nbind "MWHEELUP" "+jump; exec neostrafe0005.cfg"\nbind "5" "exec neostrafe1.cfg" ', 'bind "MWHEELDOWN" "+jump; +moveright; +forward; exec neostrafe13.cfg" \nbind "MWHEELUP" "+jump; exec neostrafe0004.cfg" \nbind "5" "exec neostrafe1.cfg" \n', 'bind "MWHEELDOWN" "+jump; +forward; exec neostrafe14.cfg" \nbind "MWHEELUP" "+jump; exec neostrafe0003.cfg"\nbind "5" "exec neostrafe1.cfg" \n', 'bind "MWHEELDOWN" "+jump; +forward; +moveleft; exec neostrafe15.cfg" \nbind "MWHEELUP" "+jump; exec neostrafe0002.cfg" \nbind "5" "exec neostrafe1.cfg" \n ', 'bind "MWHEELDOWN" "+jump; +moveleft; exec neostrafe16.cfg"\nbind "MWHEELUP" "+jump; exec neostrafe0009.cfg"  \nbind "5" "exec neostrafe1.cfg" ', 'bind "MWHEELDOWN" "+jump; +moveleft; +backward; exec neostrafe17.cfg" \nbind "MWHEELup" "+jump; exec neostrafe0008.cfg" \nbind "5" "exec neostrafe1.cfg" \n ', 'bind "MWHEELDOWN" "+jump; exec neostrafe00015.cfg" \nbind "MWHEELUP" "+jump; +forward; exec neostrafe2.cfg" \nbind "5" "exec neostrafe1.cfg" \n', 'bind "MWHEELDOWN" "+jump; exec neostrafe00014.cfg" \nbind "MWHEELUP" "+jump; +forward; +moveright; exec neostrafe3.cfg"\nbind "5" "exec neostrafe1.cfg" \n', 'bind "MWHEELDOWN" "+jump; exec neostrafe00013.cfg" \nbind "MWHEELUP" "+jump; +moveright; exec neostrafe4.cfg" \nbind "5" "exec neostrafe1.cfg" \n ', 'bind "MWHEELDOWN" "+jump; exec neostrafe00012.cfg"\nbind "MWHEELUP" "+jump; +backward; +moveright; exec neostrafe5.cfg"  \nbind "5" "exec neostrafe1.cfg" ', 'bind "MWHEELDOWN" "+jump; exec neostrafe00011.cfg" \nbind "MWHEELup" "+jump; +backward; exec neostrafe6.cfg" \nbind "5" "exec neostrafe1.cfg" \n ', 'bind "MWHEELDOWN" "+jump; exec neostrafe00010.cfg" \nbind "MWHEELUP" "+jump; +backward; +moveleft; exec neostrafe7.cfg"\nbind "5" "exec neostrafe1.cfg" ', 'bind "MWHEELDOWN" "+jump; exec neostrafe00017.cfg" \nbind "MWHEELUP" "+jump; +moveleft; exec neostrafe8.cfg" \nbind "5" "exec neostrafe1.cfg" \n', 'bind "MWHEELDOWN" "+jump; exec neostrafe00016.cfg" \nbind "MWHEELUP" "+jump; +forward; +moveleft; exec neostrafe9.cfg"\nbind "5" "exec neostrafe1.cfg" ', 'bind "MWHEELDOWN" "+jump; +backward; exec neostrafe00011.cfg" \nbind "MWHEELUP" "+jump; exec neostrafe0007.cfg" \nbind "5" "exec neostrafe1.cfg" \n', 'bind "MWHEELDOWN" "+jump; +backward; +moveright; exec neostrafe00012.cfg" \nbind "MWHEELUP" "+jump; exec neostrafe0006.cfg"\nbind "5" "exec neostrafe1.cfg" ', 'bind "MWHEELDOWN" "+jump; +moveright; exec neostrafe00013.cfg" \nbind "MWHEELUP" "+jump; exec neostrafe0005.cfg"\nbind "5" "exec neostrafe1.cfg"  ', 'bind "MWHEELDOWN" "+jump; +moveright; +forward; exec neostrafe00014.cfg" \nbind "MWHEELUP" "+jump; exec neostrafe0004.cfg" \nbind "5" "exec neostrafe1.cfg" \n', 'bind "MWHEELDOWN" "+jump; +forward; exec neostrafe00015.cfg" \nbind "MWHEELUP" "+jump; exec neostrafe0003.cfg"\nbind "5" "exec neostrafe1.cfg" \n', 'bind "MWHEELDOWN" "+jump; +forward; +moveleft; exec neostrafe00016.cfg" \nbind "MWHEELUP" "+jump; exec neostrafe0002.cfg" \nbind "5" "exec neostrafe1.cfg" \n ', 'bind "MWHEELDOWN" "+jump; +moveleft; exec neostrafe00017.cfg"\nbind "MWHEELUP" "+jump; exec neostrafe0009.cfg"  \nbind "5" "exec neostrafe1.cfg" ', 'bind "MWHEELDOWN" "+jump; +moveleft; +backward; exec neostrafe00010.cfg" \nbind "MWHEELup" "+jump; exec neostrafe0008.cfg" \nbind "5" "exec neostrafe1.cfg" \n ', 'bind "MWHEELDOWN" "+jump; exec neostrafe00015.cfg" \nbind "MWHEELUP" "+jump; +forward; exec neostrafe0003.cfg" \nbind "5" "exec neostrafe1.cfg" \n', 'bind "MWHEELDOWN" "+jump; exec neostrafe00014.cfg" \nbind "MWHEELUP" "+jump; +forward; +moveright; exec neostrafe0004.cfg"\nbind "5" "exec neostrafe1.cfg" \n', 'bind "MWHEELDOWN" "+jump; exec neostrafe00013.cfg" \nbind "MWHEELUP" "+jump; +moveright; exec neostrafe0005.cfg" \nbind "5" "exec neostrafe1.cfg" \n ', 'bind "MWHEELDOWN" "+jump; exec neostrafe00012.cfg"\nbind "MWHEELUP" "+jump; +backward; +moveright; exec neostrafe0006.cfg"  \nbind "5" "exec neostrafe1.cfg" ', 'bind "MWHEELDOWN" "+jump; exec neostrafe00011.cfg" \nbind "MWHEELup" "+jump; +backward; exec neostrafe0007.cfg" \nbind "5" "exec neostrafe1.cfg" \n ', 'bind "MWHEELDOWN" "+jump; exec neostrafe00010.cfg" \nbind "MWHEELUP" "+jump; +backward; +moveleft; exec neostrafe0008.cfg"\nbind "5" "exec neostrafe1.cfg" ', 'bind "MWHEELDOWN" "+jump; exec neostrafe00017.cfg" \nbind "MWHEELUP" "+jump; +moveleft; exec neostrafe0009.cfg" \nbind "5" "exec neostrafe1.cfg" \n', 'bind "MWHEELDOWN" "+jump; exec neostrafe00016.cfg" \nbind "MWHEELUP" "+jump; +forward; +moveleft; exec neostrafe0002.cfg"\nbind "5" "exec neostrafe1.cfg" ']
else:
    filenames = ['superglide1.cfg', 'superglide2.cfg', 'superglide3.cfg']
    content = ['bind "CAPSLOCK" "+jump; exec superglide2.cfg"\nbind "MWHEELDOWN" "+jump"', 'bind "MWHEELDOWN" "+jump; fps_max 30; exec superglide3.cfg"', 'bind "MWHEELDOWN" "+duck; fps_max 190; exec superglide1.cfg"']
    
def autoexec(location, strafe_type):
    if strafe_type == "2 directional strafe":
        execute = "exec 2directionalstrafe1.cfg"
    elif strafe_type == "Neo strafe":
        execute = "exec neo_strafe0.cfg"
    else:
        execute = "exec superglide1.cfg"
        
    with open(location+"autoexec.cfg", "a") as autoexec:
        autoexec.write(f'\n{execute}\n')

autoexec(directory, strafe_type)

for index, script in enumerate(content):
    with open(f"{directory}{filenames[index]}", "w") as f:
        f.write(script)
