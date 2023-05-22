import tkinter
import tkinter.messagebox
import customtkinter as ctk

ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class MyTabView(ctk.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # create tabs
        self.add("IS")
        self.add("RTCP")


        # add widgets on tab IS
        self.button1 = ctk.CTkButton(master=self.tab("IS"), text = "Import fichier unique", command= self.import_fichier_unique)
        self.button1.grid(row=0, column=0, padx=20, pady=10)

        self.button2 = ctk.CTkButton(master=self.tab("IS"), text="Import dossier", command= self.import_dossier)
        self.button2.grid(row=2, column=0, padx=20, pady=10)

        # add widgets on tab RTCP
        self.button3 = ctk.CTkButton(master=self.tab("RTCP"), text = "Tmp", command= self.import_RTCP)
        self.button3.grid(row=0, column=0, padx=20, pady=10)




    def import_fichier_unique(self):
        print('1')
    def import_dossier(self):
        print('2')
    def import_RTCP(self):
        print('3')

class Dataloader(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame, for example:
        self.label = ctk.CTkLabel(self, text="AAA")
        self.label.grid(row=0, column=0, padx=20)

        self.button1 = ctk.CTkButton(master=self, text="CTkButton1", command=self.button_event)
        self.button1.grid(row=1, column=0, padx=20, pady=10)
        self.button2 = ctk.CTkButton(master=self, text="CTkButton2", command=self.button_event)
        self.button2.grid(row=2, column=0, padx=20, pady=10)
        self.button3 = ctk.CTkButton(master=self, text="CTkButton3", command=self.button_event)
        self.button3.grid(row=3, column=0, padx=20, pady=10)

    def button_event(self):
        print("button pressed")

class Radio_buttons(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # create radiobutton frame
        self.radiobutton_frame = ctk.CTkFrame(self)
        self.radiobutton_frame.grid(row=0, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.radio_var = tkinter.IntVar(value=0)
        self.label_radio_group = ctk.CTkLabel(master=self.radiobutton_frame, text="CTkRadioButton Group:")
        self.label_radio_group.grid(row=0, column=2, columnspan=1, padx=10, pady=10, sticky="")
        self.radio_button_1 = ctk.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=0)
        self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")
        self.radio_button_2 = ctk.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=1)
        self.radio_button_2.grid(row=2, column=2, pady=10, padx=20, sticky="n")
        self.radio_button_3 = ctk.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=2)
        self.radio_button_3.grid(row=3, column=2, pady=10, padx=20, sticky="n")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('Application bureau ILHUP')
        self.geometry('700*500')
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure(0, weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = ctk.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)



        # create radiobutton frame
        self.radiobutton_frame = ctk.CTkFrame(self.sidebar_frame)
        self.radiobutton_frame.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.radio_var = tkinter.IntVar(value=0)
        self.label_radio_group = ctk.CTkLabel(master=self.radiobutton_frame, text="Type d'action:")
        self.label_radio_group.grid(row=0, column=2, columnspan=1, padx=10, pady=10, sticky="")
        self.sidebar_button_1 = ctk.CTkRadioButton(master=self.radiobutton_frame, text = "IS", command=self.action_IS, variable=self.radio_var, value=0)
        self.sidebar_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")
        self.sidebar_button_2 = ctk.CTkRadioButton(master=self.radiobutton_frame, text = "RTCP", command=self.action_RTCP, variable=self.radio_var, value=1)
        self.sidebar_button_2.grid(row=2, column=2, pady=10, padx=20, sticky="n")
        self.sidebar_button_3 = ctk.CTkRadioButton(master=self.radiobutton_frame, text = "ABS", command=self.action_ABS, variable=self.radio_var, value=2)
        self.sidebar_button_3.grid(row=3, column=2, pady=10, padx=20, sticky="n")

        self.appearance_mode_label = ctk.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = ctk.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = ctk.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = ctk.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        self.tab_view = MyTabView(master=self)
        self.tab_view.grid(row=0, column=1, padx=20, pady=20)

        self.frame_dataloader = Dataloader(master=self)
        self.frame_dataloader.grid(row=0, column=2, padx=20, pady=20)

        self.frame_radiobuttons = Radio_buttons(master=self)
        self.frame_radiobuttons.grid(row=1, column=2, padx=20, pady=20)

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")

    def action_IS(self):
        print('Ok')
    def action_RTCP(self):
        print('Ok')
    def action_ABS(self):
        print('Ok')



if __name__ == "__main__":
    app = App()
    app.mainloop()