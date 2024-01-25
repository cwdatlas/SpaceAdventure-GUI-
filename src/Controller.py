import tkinter as tk
from CoreService import Core
from Models.PartButton import PartButton
from tkinter.font import Font


# By NASA - https://www.flickr.com/photos/nasa2explore/40336773593/in/photostream/, Public Domain, https://commons.wikimedia.org/w/index.php?curid=77702696
class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Part Buttons
        # Capsule buttons
        self.cap_buttons = {}
        # Tank buttons
        self.tank_buttons = {}
        # Engine buttons
        self.engine_buttons = {}

        # Aesthetics
        self.theme_color = "white"
        self.title("Extended Tkinter App")
        self.geometry("1000x700")
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.core_service = Core()
        # Creating the widgets
        self.create_title_section()
        self.create_action_section()
        self.create_info_section()
        self.create_stats_section()
        self.create_log_section()

        # configure sections
        self.f_info_display.grid_rowconfigure(0, weight=1)

        # creating widgets relating to items
        self.create_capsules()
        self.create_tanks()
        self.create_engines()

        # creating stats widgets
        self.capsule_label
        self.tank_label
        self.engine_label
        self.twr_label
        # Start updating stats continuously
        self.continuous_update()

    def create_title_section(self):
        self.f_Title = tk.Frame(self, bg=self.theme_color, width=250, height=100)
        self.f_Title.grid(row=0, column=0, padx=5, pady=5, columnspan=2, sticky="ew")

        self.label = tk.Label(self.f_Title, text="Rocket Builder", font=Font(size=25))
        self.label.pack(pady=3, padx=3)

    def create_action_section(self):
        # Button selection area. this is the place where all commands will be shown
        self.f_button_selection = tk.Frame(self, bg='blue')
        self.f_button_selection.grid(row=1, column=0, padx=5, pady=5, sticky="ns")

        label1 = tk.Label(self.f_button_selection, text="_____Actions_____", bg='blue', fg='white')
        label1.pack(padx=3, pady=3)

        # Create a button widget
        self.capsule_button = tk.Button(self.f_button_selection, text="Capsule", command=self.show_capsules)
        self.capsule_button.pack(padx=6, pady=6, fill='x')

        # Create a button widget
        self.tank_button = tk.Button(self.f_button_selection, text="Tank", command=self.show_tanks)
        self.tank_button.pack(padx=6, pady=6, fill='x')

        self.engine_button = tk.Button(self.f_button_selection, text="Engine", command=self.show_engines)
        self.engine_button.pack(padx=6, pady=6, fill='x')

        # Create a launch button
        self.launch_button = tk.Button(self.f_button_selection, text="Launch!", command=self.launch)
        self.launch_button.pack(padx=6, pady=6, fill='x')

        # Create a help button
        self.help_button = tk.Button(self.f_button_selection, text="Help", command=self.help)
        self.help_button.pack(padx=6, pady=6, fill='x')

        # Create an exit button
        self.exit_button = tk.Button(self.f_button_selection, text="Exit", command=self.quit)
        self.exit_button.pack(padx=6, pady=6, fill='x')

    def create_info_section(self):
        # Information display area. this is the place where all information will be displayed
        self.f_info_display = tk.Frame(self, bg='blue', width=250, height=100)
        self.f_info_display.grid(row=1, column=1, padx=10, pady=5, sticky="nwse")

    def create_stats_section(self):
        # Stats View area. this is the place where all stats are shown
        self.f_stats_selection = tk.Frame(self, bg='blue')
        self.f_stats_selection.grid(row=2, column=0, padx=5, pady=5, sticky="ew")

        label1 = tk.Label(self.f_stats_selection, text="______Stats______", bg='blue', fg='white')
        label1.pack(padx=3, pady=3)
        self.capsule_label = tk.Label(self.f_stats_selection, text="Capsule: ", bg='blue', fg='white')
        self.capsule_label.pack(padx=3, pady=3)
        self.tank_label = tk.Label(self.f_stats_selection, text="Tank: ", bg='blue', fg='white')
        self.tank_label.pack(padx=3, pady=3)
        self.engine_label = tk.Label(self.f_stats_selection, text="Engine: ", bg='blue', fg='white')
        self.engine_label.pack(padx=3, pady=3)
        self.twr_label = tk.Label(self.f_stats_selection, text="TWH: ", bg='blue', fg='white')
        self.twr_label.pack(padx=3, pady=3)
        self.deltav_label = tk.Label(self.f_stats_selection, text="Delta v: ", bg='blue', fg='white')
        self.deltav_label.pack(padx=3, pady=3)

    def create_log_section(self):
        # Log View area. this is the place where all logs
        self.f_log_section = tk.Frame(self, bg='blue')
        self.f_log_section.grid(row=2, column=1, padx=5, pady=5, sticky="nwse")

        label1 = tk.Label(self.f_log_section, text="______Logs______", bg='blue', fg='white')
        label1.pack(padx=3, pady=3)

        self.log_label = tk.Label(self.f_log_section, text="Welcome to Rocket Builder, click on buttons to get started",
                                  bg='blue', fg='white', font=Font(size=12))
        self.log_label.pack(padx=3, pady=3, side="top")

    def create_capsules(self):
        self.create_part(self.core_service.capsules, self.cap_buttons, "Capsules", self.core_service.set_capsule)

    def create_tanks(self):
        self.create_part(self.core_service.tanks, self.tank_buttons, "Tanks", self.core_service.set_tank)

    def create_engines(self):
        self.create_part(self.core_service.engines, self.engine_buttons, "Engines", self.core_service.set_engines)

    def create_part(self, parts, button_group, image_dir, command):
        column = 0
        for part_name in parts:
            self.f_info_display.grid_columnconfigure(column, weight=1)
            button_group[part_name] = PartButton(self.f_info_display,
                                                 self.theme_color,
                                                 200,
                                                 200,
                                                 image_dir,
                                                 parts[part_name],
                                                 0,
                                                 column,
                                                 lambda event, pname=parts[part_name].name: command(pname))
            column = column + 1

    def show_capsules(self):
        print("Attempt to show capsule")
        self.show_parts(self.cap_buttons)

    def show_tanks(self):
        self.show_parts(self.tank_buttons)

    def show_engines(self):
        self.show_parts(self.engine_buttons)

    def show_parts(self, button_group):
        info_children = self.f_info_display.children
        for part in info_children:
            info_children[part].set_invisible()
        for part in button_group:
            button_group[part].set_visible()

    def launch(self):
        if not self.core_service.rocket_launchable():
            self.log_label.config(text="Make sure to select all parts before launching")
        elif self.core_service.get_thrust_to_weight() < 1.5:
            self.log_label.config(text="Looks like your Twr is less than 1.5. try to increase thrust with more "
                                       "engines or decrease mass!")
        elif self.core_service.made_to_orbit():
            self.log_label.config(text="YOU MADE IT TO ORBIT!! GOOD JOB!!")
        elif self.core_service.made_to_orbit() is False:
            self.log_label.config(text="Darn! You didnt make it to orbit, check your stats to see your delta v")

    def help(self):
        self.log_label.config(text="Welcome to Rocket Builder, this is a more simple version compared to the console version \n"
                              "You will need to know Thrust to weight Ratio (TWR), ISP and Delta V to play the game \n"
                              "TWR is the measure of the rocket's push against gravity, if its over 1.5 you can make it tor orbit \n"
                              "ISP is rocket engine efficiency, think about it like miles/gallon \n"
                              "Delta V is the total change in velocity from the ground needed to get to low earth orbit \n"
                                   "You will need 7000 Delta V to make it to orbit! Goodluck and have fun!!")

    def continuous_update(self):
        # Update data here
        rocket = self.core_service.rocket
        if rocket["capsule"] is not None:
            self.capsule_label.config(text="Capsule: " + rocket["capsule"].name)
        if rocket["tank"] is not None:
            self.tank_label.config(text="Tank: " + rocket["tank"].name)
        if rocket["engine"] is not None:
            self.engine_label.config(text="Engine: " + rocket["engine"].name)
        if rocket["capsule"] is not None and rocket["tank"] is not None and rocket["engine"] is not None:
            self.twr_label.config(text="Twr: " + str(self.core_service.get_thrust_to_weight())[:6])
        self.deltav_label.config(text="Delta v: " + str(self.core_service.delta_v)[:6])

        # Schedule the next update
        self.after(250, self.continuous_update)  # 1000 milliseconds = 1 second
