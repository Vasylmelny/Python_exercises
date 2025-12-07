# Define a global variable global_var = 10.
# Write a function that modifies a global variable value.

global_var = 10
def change_global_var(new_global_var):
    global global_var
    global_var = new_global_var
    print(global_var)

change_global_var(12)
change_global_var("Djonsoniuk")
change_global_var(100)