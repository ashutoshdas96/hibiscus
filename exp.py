from ocempgui.widgets import *
from ocempgui.widgets.Constants import *
import main, gui
def create_table_view ():
   # Crate and display a Table.

    data = main.grab_url()
    l = len(data)
    table = Table (l+2, 4)
    table.spacing = 5
    table.topleft = 5, 5



    #label = Label ("Nonaligned wide Label")
    #table.add_child (0, 0, label)
    #table.add_child (0, 1, Button ("Simple Button"))


    table.add_child (1, 0, Label ("Date"))
    table.add_child (1, 1, Label ("Title"))
    table.add_child (1, 2, Label ("Posted By"))
    table.add_child (1, 3, Label ("Attention"))

    for i in range(l):
        table.add_child (i+2, 0, Label (data[i][1]))
        button = Button (data[i][2])
        button.connect_signal (SIG_CLICKED, gui.print_message)
        table.add_child (i+2, 1, button)
        table.add_child (i+2, 2, Label (data[i][3]))
        table.add_child (i+2, 3, Label (data[i][4]))


    return table

if __name__ == "__main__":
    # Initialize the drawing window.
    re = Renderer ()
    re.create_screen (550, 350)     #250 350
    re.title = "Table examples"
    re.color = (234, 228, 223)

    window = ScrolledWindow (550, 300)
    re.add_widget (window)
    window.scrolling = SCROLL_AUTO
    window.child = create_table_view ()
    # Start the main rendering loop.
    re.start ()
