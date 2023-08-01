import os
import customtkinter
from PIL import Image
from scripts import Salesforce_func
from assets.logins import logins
from simple_salesforce import Salesforce

# Salesforce Login
Contact_ID = logins.Contact_ID
security_token = logins.security_token
username = logins.username
pw = logins.pw

width = 1100
height = 600
customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light")
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue")

sf = Salesforce(username=username, password=pw, security_token=security_token)
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Header and Sidebar Example")
        self.geometry(f"1100x600")
        #self.geometry(f"{width}*{height}")

        # configure grid layout
        self.grid_columnconfigure(0, weight=0)  # Sidebar
        self.grid_columnconfigure(1, weight=1)  # Main Frame
        self.grid_rowconfigure(0, weight=0)  # Header
        self.grid_rowconfigure(1, weight=1)  # Sidebar

        # create header
        self.header = Header(self)
        self.header.grid(row=0, column=0, columnspan=2, sticky="ew")

        # create sidebar
        self.sidebar = Sidebar(self)
        self.sidebar.grid(row=1, column=0, sticky="nsew")

        # create main frame container
        self.main_frame_container = customtkinter.CTkFrame(self)
        self.main_frame_container.grid(row=1, column=1, sticky="nsew")

        # create main frames
        self.main_frame_1 = MainFrame1(self.main_frame_container)
        self.main_frame_2 = MainFrame2(self.main_frame_container)
        self.main_frame_3 = MainFrame3(self.main_frame_container)

        # set main frame 1 as the initial main frame
        self.current_main_frame = self.main_frame_1
        self.current_main_frame.grid(row=0, column=0, sticky="nsew")

        # set main frame container to fill the remaining space
        self.main_frame_container.grid_rowconfigure(0, weight=1)
        self.main_frame_container.grid_columnconfigure(0, weight=1)

    def change_main_frame(self, new_frame_class):
        new_frame = new_frame_class(self.main_frame_container)
        self.current_main_frame.grid_forget()
        new_frame.grid(row=0, column=0, sticky="nsew")
        self.current_main_frame = new_frame

class Header(customtkinter.CTkFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "assets/images")
        logo_image = Image.open(os.path.join(image_path, "logo3.png"))
        logo_image = logo_image.resize((25, 25))  # Resize the logo image if needed

        self.logo_image = customtkinter.CTkImage(logo_image)
        self.logo_label = customtkinter.CTkLabel(self, text="", image=self.logo_image)
        self.logo_label.pack(side="left", padx=10)

        self.menu_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.menu_frame.pack(side="right", padx=10)

        self.menu_item_1 = customtkinter.CTkButton(self.menu_frame, text="Menu 1", command=self.menu_item_1_clicked)
        self.menu_item_1.pack(side="right", padx=5)

        self.menu_item_2 = customtkinter.CTkButton(self.menu_frame, text="Menu 2", command=self.menu_item_2_clicked)
        self.menu_item_2.pack(side="right", padx=5)

        self.menu_item_3 = customtkinter.CTkButton(self.menu_frame, text="Import des ABS", command=self.menu_item_3_clicked)
        self.menu_item_3.pack(side="right", padx=5)

    def menu_item_1_clicked(self):
        self.master.change_main_frame(MainFrame1)

    def menu_item_2_clicked(self):
        self.master.change_main_frame(MainFrame2)

    def menu_item_3_clicked(self):
        self.master.change_main_frame(MainFrame3)

    def change_appearance_mode(self, new_mode):
        customtkinter.set_appearance_mode(new_mode)

    def change_scaling(self, new_scaling):
        scaling_factor = int(new_scaling[:-1]) / 100
        customtkinter.set_widget_scaling(scaling_factor)

class Sidebar(customtkinter.CTkFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.sidebar_button = customtkinter.CTkButton(self, text="Sidebar Button", corner_radius=20,command=self.sidebar_button_event)
        self.sidebar_button.pack(pady=(20, 10))

        self.appearance_mode_label = customtkinter.CTkLabel(self, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.pack(padx=20, pady=(400, 0))

        self.appearance_mode_optionmenu = customtkinter.CTkOptionMenu(self, values=["Light", "Dark", "System"],
                                                                     command=self.change_appearance_mode)
        self.appearance_mode_optionmenu.pack(padx=20, pady=(10, 0))


    def sidebar_button_event(self):
        print("Sidebar button clicked")

    def change_appearance_mode(self, new_mode):
        customtkinter.set_appearance_mode(new_mode)

class MainFrame1(customtkinter.CTkFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        main_content_label = customtkinter.CTkLabel(self, text="Main Frame 1", font=customtkinter.CTkFont(size=20))
        main_content_label.pack(pady=50)

class MainFrame2(customtkinter.CTkFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        main_content_label = customtkinter.CTkLabel(self, text="Main Frame 2", font=customtkinter.CTkFont(size=20))
        main_content_label.pack(pady=50)

class MainFrame3(customtkinter.CTkFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        main_content_label = customtkinter.CTkLabel(self, text="Import des ABS", font=customtkinter.CTkFont(size=20))
        main_content_label.pack(pady=50)

        # Creating the Text widget
        self.text_box = customtkinter.CTkTextbox(self, height=350, width=200)
        self.text_box.pack(pady=10)

        # Creating the button widget
        self.process_button = customtkinter.CTkButton(self, text="Process", command=self.process_text)
        self.process_button.pack(pady=10)

    def process_text(self):
        # Getting the text from the text box
        text = self.text_box.get("1.0", "end-1c")
        # Here is where you process the text
        i = 0
        lines = text.splitlines()
        for line in lines:
            if line.strip() == "":
                continue
            Salesforce_func.add_NIL_to_abs(sf, line)



if __name__ == "__main__":
    app = App()
    app.mainloop()
