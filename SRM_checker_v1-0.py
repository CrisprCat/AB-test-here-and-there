# %%
# importing required packages
import numpy as np
from scipy.stats import chisquare
from tkinter import *

# creating root window
root = Tk()

# changing root window title and dimension
root.title("SRM test")
# setting geometry (widthxheight)
root.geometry('550x200')

# adding Control Entry Field
sample_control = Entry(root, width=10)
sample_control.grid(column =1, row =0)
#adding a label to the Control entry field
lbl_control = Label(root, text = "What is your control sample size?")
lbl_control.grid(column =0, row =0)

# adding Variant Entry Field
sample_variant = Entry(root, width=10)
sample_variant.grid(column =1, row =1)
# adding label to the Variant Entry Field
lbl_variant = Label(root, text = "What is your variant sample size?")
lbl_variant.grid(column =0, row =1)

def result():
   # creating the input variables from the entry field input
   sample_size_contr = sample_control.get()
   sample_size_variant = sample_variant.get() 
   print(sample_size_contr)
   print(sample_size_variant)

   total_sample = int(sample_size_contr) + int(sample_size_variant)
   output_1 = f"""Your total sample size is {total_sample}."""
   Output_label = Label(root, text = output_1)
   Output_label.grid(column = 0, row = 2)

   # transformations
   frequency_samples = np.array([int(sample_size_contr), int(sample_size_variant)])
   # perform chisquare test with assumed equal distribution
   test_result = chisquare(frequency_samples, f_exp=None)

   # output
   if test_result.pvalue < 0.1:
         output_2 = f"""The p-value is smaller than 0.1 ({round(test_result.pvalue, 3)}). 
         A possible SRM (Sample Ratio Mismatch) is detected. 
         Please contact your AB test experts before analysing the test results."""
   else:
         output_2 = f"""The p-value is greater than 0.1 ({round(test_result.pvalue, 3)}). 
         No SRM (Sample Ratio Mismatch) is detected. 
         Happy analysing your test results."""

    # Remove previous output label if exists
   for widget in root.winfo_children():
        if isinstance(widget, Label) and widget.grid_info()['row'] == 3:
             widget.destroy()            

   Output_label_2 = Label(root, text = output_2)
   Output_label_2.grid(column = 0, row = 3)
  
# button widget with red color text inside
btn = Button(root, text = "Submit" ,
             fg = "red", command=result)
# Set Button Grid
btn.grid(column=2, row=1)

# all widgets will be here
# Execute Tkinter
root.mainloop()
