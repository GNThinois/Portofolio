import win32com.client as win32

def inject_macro(file_path, macro_code):
    # Dispatch an Excel application
    excel = win32.gencache.EnsureDispatch('Excel.Application')

    # Open the workbook
    workbook = excel.Workbooks.Open(file_path)

    # Add the VBA code to the workbook
    vbaproject = workbook.VBProject
    vbacomponent = vbaproject.VBComponents.Add(1)  # 1 is the type for a standard module

    # Add the macro code to the module
    vbacomponent.CodeModule.AddFromString(macro_code)

    # Save and close
    workbook.Save()
    workbook.Close()

    # Quit Excel
    excel.Quit()

# Define your VBA macro as a string
macro_code = """
Sub MyMacro()
    ' Your VBA code here
End Sub
"""

# Use the function to inject the macro
inject_macro("C:/path_to_your_file/your_file.xlsm", macro_code)
