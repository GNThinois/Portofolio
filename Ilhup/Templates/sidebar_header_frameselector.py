import tkinter as tk
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light")
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue")


class Sidebar(customtkinter.CTkFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.sidebar_button = customtkinter.CTkButton(self, text="Sidebar Button", command=self.sidebar_button_event)
        self.sidebar_button.pack(pady=(20, 10))

    def sidebar_button_event(self):
        print("Sidebar button clicked")


class Header(customtkinter.CTkFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)


        self.header_logo = customtkinter.CTkLabel(self, text="Logo", font=customtkinter.CTkFont(size=16))
        self.header_logo.pack(side="left", padx=10)

        self.menu_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.menu_frame.pack(side="right", padx=10)

        self.menu_item_1 = customtkinter.CTkButton(self.menu_frame, text="Menu 1", command=self.menu_item_1_clicked)
        self.menu_item_1.pack(side="right", padx=5)

        self.menu_item_2 = customtkinter.CTkButton(self.menu_frame, text="Menu 2", command=self.menu_item_2_clicked)
        self.menu_item_2.pack(side="right", padx=5)

        self.menu_item_3 = customtkinter.CTkButton(self.menu_frame, text="Menu 3", command=self.menu_item_3_clicked)
        self.menu_item_3.pack(side="right", padx=5)

    def menu_item_1_clicked(self):
        self.master.change_main_frame(MainFrame1)

    def menu_item_2_clicked(self):
        self.master.change_main_frame(MainFrame2)

    def menu_item_3_clicked(self):
        self.master.change_main_frame(MainFrame3)


class MainFrame1(customtkinter.CTkFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.main_content_label = customtkinter.CTkLabel(self, text="Main Content 1", font=customtkinter.CTkFont(size=20))
        self.main_content_label.pack(pady=50)


class MainFrame2(customtkinter.CTkFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.main_content_label = customtkinter.CTkLabel(self, text="Main Content 2", font=customtkinter.CTkFont(size=20))
        self.main_content_label.pack(pady=50)


class MainFrame3(customtkinter.CTkFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.main_content_label = customtkinter.CTkLabel(self, text="Main Content 3", font=customtkinter.CTkFont(size=20))
        self.main_content_label.pack(pady=50)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("App with Sidebar, Header, and MainFrames")
        self.geometry("800x600")

        # create header
        self.header = Header(self)
        self.header.pack(fill="x")

        # create sidebar
        self.sidebar = Sidebar(self)
        self.sidebar.pack(fill="y", side="left")

        # create main frames
        self.main_frames = {
            MainFrame1: MainFrame1(self),
            MainFrame2: MainFrame2(self),
            MainFrame3: MainFrame3(self)
        }

        # set initial main frame
        self.current_main_frame = None
        self.change_main_frame(MainFrame1)

    def change_main_frame(self, frame_class):
        if self.current_main_frame:
            self.current_main_frame.pack_forget()

        self.current_main_frame = self.main_frames[frame_class]
        self.current_main_frame.pack(fill="both", expand=True)


if __name__ == "__main__":
    app = App()
    app.mainloop()
