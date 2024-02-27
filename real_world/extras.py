import tkinter as tk
import sys
import tree
# --- main ---

root = tk.Tk()

# - Frame with Text and Scrollbar -

frame = tk.Frame(root)
frame.pack(expand=True, fill='both')

text = tk.Text(frame)
text.pack(side='left', fill='both', expand=True)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side='right', fill='y')

text['yscrollcommand'] = scrollbar.set
scrollbar['command'] = text.yview

old_stdout = sys.stdout
sys.stdout = tree.Redirect(text)


# - rest -

button = tk.Button(root, text='TEST', command=tree.run)
button.pack()



# - after close window -

sys.stdout = old_stdout
