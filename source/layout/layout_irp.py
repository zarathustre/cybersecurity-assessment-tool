
""" HERE IS THE LAYOUT OF EVERYTHING RELATED TO THE INHERENT RISK PROFILE """

import tkinter as tk
import DATA
import layout.layout_home as home


""" This class is responsible for the layout of the Inherent Risk Profile's Main page
    Contains the 5 categories and links to each one """
class IRP_Page(tk.Frame):
    #region
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title("Inherent Risk Profile")

        self.config(bg="ghost white")
        self.unbind_all("<MouseWheel>")

        home_button = tk.Button(self, width=10, text="Home", font="Calibri 14", relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                command=lambda: master.switch_frame(home.Home_Page))

        cat1_button = tk.Button(self, text="Technologies and Connection Types", 
                                font="Calibri 14", relief='groove', borderwidth=3, bg='light gray', activebackground='light blue',
                                command=lambda: master.switch_frame(IRP_Cat1_Page))

        cat2_button = tk.Button(self, text="Delivery Channels",  
                                font="Calibri 14", relief='groove', borderwidth=3, bg='light gray', activebackground='light blue',
                                command=lambda: master.switch_frame(IRP_Cat2_Page))

        cat3_button = tk.Button(self, text="Online/Mobile Products and Technology Services",  
                                font="Calibri 14", relief='groove', borderwidth=3, bg='light gray', activebackground='light blue',
                                command=lambda: master.switch_frame(IRP_Cat3_Page))

        cat4_button = tk.Button(self, text="Organizational Characteristics",  
                                font="Calibri 14", relief='groove', borderwidth=3, bg='light gray', activebackground='light blue',
                                command=lambda: master.switch_frame(IRP_Cat4_Page))

        cat5_button = tk.Button(self, text="External Threats",  
                                font="Calibri 14", relief='groove', borderwidth=3, bg='light gray', activebackground='light blue',
                                command=lambda: master.switch_frame(IRP_Cat5_Page))

        
        self.columnconfigure(0, weight=1)
        self.columnconfigure(3, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(8, weight=1)
        self.rowconfigure(6, minsize=50)
        self.rowconfigure(1, minsize=50)
        self.rowconfigure(2, minsize=50)
        self.rowconfigure(3, minsize=50)
        self.rowconfigure(4, minsize=50)
        self.rowconfigure(5, minsize=50)

        home_button.grid(row=0, column=0)
        cat1_button.grid(row=1, column=1, pady=10)
        cat2_button.grid(row=2, column=1, pady=10)
        cat3_button.grid(row=3, column=1, pady=10)
        cat4_button.grid(row=4, column=1, pady=10)
        cat5_button.grid(row=5, column=1, pady=10)

        cat1_label = tk.Label(self, font="Calibri 15", bg="ghost white",
                              text=str(calculate_total_per_category(IRP_Cat1_Page.values)[5]) + "/" + str(len(DATA.IRP_Category1)) + " Answered")

        cat2_label = tk.Label(self, font="Calibri 15", bg="ghost white",
                              text=str(calculate_total_per_category(IRP_Cat2_Page.values)[5]) + "/" + str(len(DATA.IRP_Category2)) + " Answered")
        
        cat3_label = tk.Label(self, font="Calibri 15", bg="ghost white",
                              text=str(calculate_total_per_category(IRP_Cat3_Page.values)[5]) + "/" + str(len(DATA.IRP_Category3)) + " Answered")
        
        cat4_label = tk.Label(self, font="Calibri 15", bg="ghost white",
                              text=str(calculate_total_per_category(IRP_Cat4_Page.values)[5]) + "/" + str(len(DATA.IRP_Category4)) + " Answered")
        
        cat5_label = tk.Label(self, font="Calibri 15", bg="ghost white",
                              text=str(calculate_total_per_category(IRP_Cat5_Page.values)[5]) + "/" + str(len(DATA.IRP_Category5)) + " Answered")
    
        cat1_label.grid(row=1, column=2, padx=30, sticky='nsew')
        cat2_label.grid(row=2, column=2, padx=30, sticky='nsew')
        cat3_label.grid(row=3, column=2, padx=30, sticky='nsew')
        cat4_label.grid(row=4, column=2, padx=30, sticky='nsew')
        cat5_label.grid(row=5, column=2, padx=30, sticky='nsew')

        submit_button = tk.Button(self, width=10, text="Final Score", font="Calibri 14", relief='raised', borderwidth=2, bg='azure3', 
                                  activebackground='light blue', command=lambda: master.switch_frame(IRP_Final), state="normal") ##### state=disabled

        submit_button.grid(row=7, column=2)

        ToolTip(widget=submit_button, text="Answer all the questions to proceed")

        # if all the questions are answered, then enable the submit button
        if (calculate_total()[0] + calculate_total()[1] + calculate_total()[2] + calculate_total()[3] + calculate_total()[4] == int(str(len(DATA.IRP_Category1))) + int(str(len(DATA.IRP_Category2))) + int(str(len(DATA.IRP_Category3))) + int(str(len(DATA.IRP_Category4))) + int(str(len(DATA.IRP_Category5)))):
            submit_button['state'] = "normal"
    #endregion


class IRP_Final(tk.Frame):
    #region
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title("Inherent Risk Profile - Final Score")

        home_button = tk.Button(self, text='HOME', width=10)
        back_button = tk.Button(self, text='BACK', width=10, command=lambda: master.switch_frame(IRP_Page))

        least_total_label = tk.Label(self, text='Least: ' + str(calculate_total()[0]) + ' Point(s)')
        minimal_total_label = tk.Label(self, text='Minimal: ' + str(calculate_total()[1]) + ' Point(s)')
        moderate_total_label = tk.Label(self, text='Moderate: ' + str(calculate_total()[2]) + ' Point(s)')
        significant_total_label = tk.Label(self, text='Significant: ' + str(calculate_total()[3]) + ' Point(s)')
        most_total_label = tk.Label(self, text='Most: ' + str(calculate_total()[4]) + ' Point(s)')
        final_score_label = tk.Label(self, text='Final Score: ' + IRP_Final.find_max())

        save_results_button = tk.Button(self, text='SAVE', width=10)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(2, minsize=25)
        self.rowconfigure(10, minsize=200)
        self.rowconfigure(11, weight=1)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(3, minsize=150)
        self.columnconfigure(6, minsize=400)
        self.columnconfigure(7, weight=1)

        home_button.grid(row=1, column=1)
        back_button.grid(row=1, column=2)

        least_total_label.grid(row=3, column=4)
        minimal_total_label.grid(row=4, column=4)
        moderate_total_label.grid(row=5, column=4)
        significant_total_label.grid(row=6, column=4)
        most_total_label.grid(row=7, column=4)
        final_score_label.grid(row=8, column=4, pady=20)

        save_results_button.grid(row=9, column=5)

    def find_max():
        max_value = max(calculate_total())
        indexes = [i for i, j in enumerate(calculate_total()) if j == max_value]
        if max_value == 0:
            return ''
        elif 4 in indexes:
            return 'Most Risk'
        elif 3 in indexes:
            return 'Significant Risk'
        elif 2 in indexes:
            return 'Moderate Risk'
        elif 1 in indexes:
            return 'Minimal Risk'
        elif 0 in indexes:
            return 'Least Risk'
    #endregion


""" Inherent Risk Profile - Category 1 (Technologies and Connection Types) 
    Responsible for the layout of Category 1 displaying all the questions and possible answers """
class IRP_Cat1_Page(tk.Frame):
    #region

    values = [] # holds references to the values in the radio buttons (possible answers to each question)

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title("Inherent Risk Profile - Technologies and Connection Types")

        self.config(bg="ghost white")

        # Top frame contains navigation widgets and labels
        top_frame = tk.Frame(self, bg="ghost white", relief='groove', borderwidth=3)
        top_frame.pack(side=tk.TOP, fill=tk.X, anchor="nw")

        home_button = tk.Button(top_frame, width=10, text="HOME", font="Calibri 11", relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                command=lambda: master.switch_frame(home.Home_Page))
        
        back_button = tk.Button(top_frame, width=10, text="BACK", font="Calibri 11", relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                command=lambda: master.switch_frame(IRP_Page))

        home_button.grid(row=0, column=0, padx=30, pady=15)
        back_button.grid(row=0, column=1)

        # Bottom frame contains the submit and clear buttons
        bottom_frame = tk.Frame(self, bg="ghost white", relief='groove', borderwidth=3)
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, anchor="se")

        submit_button = tk.Button(bottom_frame, width=10, text='SUBMIT', font="Calibri 11", relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                  command=lambda: master.switch_frame(IRP_Page))
        
        clear_button = tk.Button(bottom_frame, width=10, text='CLEAR', font="Calibri 11", relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                 command=lambda: clear_pressed(self.values))

        submit_button.pack(side=tk.RIGHT, padx=40, pady=20)
        clear_button.pack(side=tk.RIGHT)

        # Middle frame with a scrollbar and the questions
        my_canvas = tk.Canvas(self)
        my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1, anchor="center")
        my_scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        my_canvas.configure(yscrollcommand=my_scrollbar.set, bg="white")

        def _on_mouse_wheel(event):
            my_canvas.yview_scroll(-1 * int((event.delta / 120)), "units")

        my_canvas.bind_all("<MouseWheel>", _on_mouse_wheel)                                                     # Bind mouse wheel to scrollbar
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))      # Bind mouse event to scrollbar
        
        middle_frame = tk.Frame(my_canvas, bg="white")
        my_canvas.create_window((0,0), window=middle_frame, anchor="nw")

        # empty columns that keep the labels separated by a fixed size
        top_frame.columnconfigure(2, minsize=200)
        top_frame.columnconfigure(4, minsize=50)
        top_frame.columnconfigure(6, minsize=70)
        top_frame.columnconfigure(8, minsize=110)
        top_frame.columnconfigure(10, minsize=160)

        # Labels representing the risk levels
        label1 = tk.Label(top_frame, width=15, text="Least", font='Calibri 10', borderwidth=3, relief="groove")
        label2 = tk.Label(top_frame, width=15, text="Minimal", font='Calibri 10', borderwidth=3, relief="groove")
        label3 = tk.Label(top_frame, width=15, text="Moderate", font='Calibri 10', borderwidth=3, relief="groove")
        label4 = tk.Label(top_frame, width=15, text="Signigicant", font='Calibri 10', borderwidth=3, relief="groove")
        label5 = tk.Label(top_frame, width=15, text="Most", font='Calibri 10', borderwidth=3, relief="groove")

        label1.grid(row=1, column=3)
        label2.grid(row=1, column=5)
        label3.grid(row=1, column=7)
        label4.grid(row=1, column=9)
        label5.grid(row=1, column=11)

        # Get the questions from DATA and align them on screen
        i = 0
        for key, value in DATA.IRP_Category1.items():

            question = tk.Label(middle_frame, width=50, text=key, wraplength=400, justify=tk.LEFT, borderwidth=5, relief="groove", font="Calibri 12")
            question.grid(row=i+1, column=0, pady=10, sticky="W")
            self.values.append(tk.IntVar())

            for j in range(5):
                answer = tk.Radiobutton(middle_frame, text=value[j], variable=self.values[i], value=j+1, justify=tk.LEFT, font="Calibri 10", bg='white')
                answer.grid(row=i+1, column=j+1, padx=15, pady=20, sticky="W")

            i += 1
    #endregion


""" Inherent Risk Profile - Category 2 (Delivery Channels) 
    Responsible for the layout of Category 2 """
class IRP_Cat2_Page(tk.Frame):
    #region

    values = [] # holds references to the values in the radio buttons (possible answers to each question)

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title("Inherent Risk Profile - Delivery Channels")

        self.config(bg="white")

        # Top frame contains navigation widgets and labels
        top_frame = tk.Frame(self, bg="ghost white", relief='groove', borderwidth=3)
        top_frame.pack(side=tk.TOP, fill=tk.X, anchor="nw")

        home_button = tk.Button(top_frame, width=10, text="HOME", font="Calibri 11", relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                command=lambda: master.switch_frame(home.Home_Page))
        
        back_button = tk.Button(top_frame, width=10, text="BACK", font="Calibri 11", relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                command=lambda: master.switch_frame(IRP_Page))

        home_button.grid(row=0, column=0, padx=30, pady=15)
        back_button.grid(row=0, column=1)

        # Bottom frame contains the submit and clear buttons
        bottom_frame = tk.Frame(self, bg="ghost white", relief='groove', borderwidth=3)
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, anchor="se")

        submit_button = tk.Button(bottom_frame, width=10, text='SUBMIT', font="Calibri 11", relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                  command=lambda: master.switch_frame(IRP_Page))
        
        clear_button = tk.Button(bottom_frame, width=10, text='CLEAR', font="Calibri 11", relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                 command=lambda: clear_pressed(self.values))

        submit_button.pack(side=tk.RIGHT, padx=40, pady=20)
        clear_button.pack(side=tk.RIGHT)

        # Middle frame 
        middle_frame = tk.Frame(self, bg="white")
        middle_frame.pack(anchor='nw', fill='x')

        # empty columns that keep the labels separated by a fixed size
        top_frame.columnconfigure(2, minsize=130)
        top_frame.columnconfigure(4, minsize=100)
        top_frame.columnconfigure(6, minsize=130)
        top_frame.columnconfigure(8, minsize=120)
        top_frame.columnconfigure(10, minsize=130)

        # Labels representing the risk levels
        label1 = tk.Label(top_frame, width=15, text="Least", font='Calibri 10', borderwidth=3, relief="groove")
        label2 = tk.Label(top_frame, width=15, text="Minimal", font='Calibri 10', borderwidth=3, relief="groove")
        label3 = tk.Label(top_frame, width=15, text="Moderate", font='Calibri 10', borderwidth=3, relief="groove")
        label4 = tk.Label(top_frame, width=15, text="Signigicant", font='Calibri 10', borderwidth=3, relief="groove")
        label5 = tk.Label(top_frame, width=15, text="Most", font='Calibri 10', borderwidth=3, relief="groove")

        label1.grid(row=1, column=3)
        label2.grid(row=1, column=5)
        label3.grid(row=1, column=7)
        label4.grid(row=1, column=9)
        label5.grid(row=1, column=11)

        # Get the questions from DATA and align them on screen
        i = 0
        for key, value in DATA.IRP_Category2.items():

            question = tk.Label(middle_frame, width=40, text=key, wraplength=400, justify=tk.LEFT, borderwidth=5, relief="groove", font="Calibri 12")
            question.grid(row=i+1, column=0, pady=10, sticky="W")
            self.values.append(tk.IntVar())

            for j in range(5):
                answer = tk.Radiobutton(middle_frame, text=value[j], variable=self.values[i], value=j+1, justify=tk.LEFT, font="Calibri 10", bg='white')
                answer.grid(row=i+1, column=j+1, padx=15, pady=50, sticky="W")

            i += 1
    #endregion


""" Inherent Risk Profile - Category 3 (Online/Mobile Products and Technology Services) 
    Responsible for the layout of Category 3 """
class IRP_Cat3_Page(tk.Frame):
    #region
    
    values = [] # holds references to the values in the radio buttons (possible answers to each question)

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title("Inherent Risk Profile - Online/Mobile Products and Technology Services")

        self.config(bg="ghost white")

        # Top frame contains navigation widgets and labels
        top_frame = tk.Frame(self, bg="ghost white", relief='groove', borderwidth=3)
        top_frame.pack(side=tk.TOP, fill=tk.X, anchor="nw")

        home_button = tk.Button(top_frame, width=10, text="HOME", font="Calibri 11", relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                command=lambda: master.switch_frame(home.Home_Page))
        
        back_button = tk.Button(top_frame, width=10, text="BACK", font="Calibri 11", relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                command=lambda: master.switch_frame(IRP_Page))

        home_button.grid(row=0, column=0, padx=30, pady=15)
        back_button.grid(row=0, column=1)

        # Bottom frame contains the submit and clear buttons
        bottom_frame = tk.Frame(self, bg="ghost white", relief='groove', borderwidth=3)
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, anchor="se")

        submit_button = tk.Button(bottom_frame, width=10, text='SUBMIT', font="Calibri 11", relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                  command=lambda: master.switch_frame(IRP_Page))
        
        clear_button = tk.Button(bottom_frame, width=10, text='CLEAR', font="Calibri 11", relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                 command=lambda: clear_pressed(self.values))

        submit_button.pack(side=tk.RIGHT, padx=40, pady=20)
        clear_button.pack(side=tk.RIGHT)

        # Middle frame with a scrollbar and the questions
        my_canvas = tk.Canvas(self)
        my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1, anchor="center")
        my_scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        my_canvas.configure(yscrollcommand=my_scrollbar.set, bg="white")

        def _on_mouse_wheel(event):
            my_canvas.yview_scroll(-1 * int((event.delta / 120)), "units")

        my_canvas.bind_all("<MouseWheel>", _on_mouse_wheel)                                                     # Bind mouse wheel to scrollbar
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))      # Bind mouse event to scrollbar
        
        middle_frame = tk.Frame(my_canvas, bg="white")
        my_canvas.create_window((0,0), window=middle_frame, anchor="nw")

        # empty columns that keep the labels separated by a fixed size
        top_frame.columnconfigure(2, minsize=200)
        top_frame.columnconfigure(4, minsize=60)
        top_frame.columnconfigure(6, minsize=95)
        top_frame.columnconfigure(8, minsize=140)
        top_frame.columnconfigure(10, minsize=150)

        # Labels representing the risk levels
        label1 = tk.Label(top_frame, width=15, text="Least", font='Calibri 10', borderwidth=3, relief="groove")
        label2 = tk.Label(top_frame, width=15, text="Minimal", font='Calibri 10', borderwidth=3, relief="groove")
        label3 = tk.Label(top_frame, width=15, text="Moderate", font='Calibri 10', borderwidth=3, relief="groove")
        label4 = tk.Label(top_frame, width=15, text="Signigicant", font='Calibri 10', borderwidth=3, relief="groove")
        label5 = tk.Label(top_frame, width=15, text="Most", font='Calibri 10', borderwidth=3, relief="groove")

        label1.grid(row=1, column=3)
        label2.grid(row=1, column=5)
        label3.grid(row=1, column=7)
        label4.grid(row=1, column=9)
        label5.grid(row=1, column=11)

        # Get the questions from DATA and align them on screen
        i = 0
        for key, value in DATA.IRP_Category3.items():

            question = tk.Label(middle_frame, width=50, text=key, wraplength=400, justify=tk.LEFT, borderwidth=5, relief="groove", font="Calibri 12")
            question.grid(row=i+1, column=0, pady=10, sticky="W")
            self.values.append(tk.IntVar())

            for j in range(5):
                answer = tk.Radiobutton(middle_frame, text=value[j], variable=self.values[i], value=j+1, justify=tk.LEFT, font="Calibri 10", bg='white')
                answer.grid(row=i+1, column=j+1, padx=15, pady=20, sticky="W")

            i += 1
    #endregion


""" Inherent Risk Profile - Category 4 (Organizational Characteristics) 
    Responsible for the layout of Category 4 """
class IRP_Cat4_Page(tk.Frame):
    #region
    
    values = [] # holds references to the values in the radio buttons (possible answers to each question)

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title("Inherent Risk Profile - Organizational Characteristics")

        self.config(bg="ghost white")

        # Top frame contains navigation widgets and labels
        top_frame = tk.Frame(self, bg="ghost white", relief='groove', borderwidth=3)
        top_frame.pack(side=tk.TOP, fill=tk.X, anchor="nw")

        home_button = tk.Button(top_frame, width=10, text="HOME", font="Calibri 11", relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                command=lambda: master.switch_frame(home.Home_Page))
        
        back_button = tk.Button(top_frame, width=10, text="BACK", font="Calibri 11", relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                command=lambda: master.switch_frame(IRP_Page))

        home_button.grid(row=0, column=0, padx=30, pady=15)
        back_button.grid(row=0, column=1)

        # Bottom frame contains the submit and clear buttons
        bottom_frame = tk.Frame(self, bg="ghost white", relief='groove', borderwidth=3)
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, anchor="se")

        submit_button = tk.Button(bottom_frame, width=10, text='SUBMIT', font="Calibri 11", relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                  command=lambda: master.switch_frame(IRP_Page))
        
        clear_button = tk.Button(bottom_frame, width=10, text='CLEAR', font="Calibri 11", relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                 command=lambda: clear_pressed(self.values))

        submit_button.pack(side=tk.RIGHT, padx=40, pady=20)
        clear_button.pack(side=tk.RIGHT)

        # Middle frame with a scrollbar and the questions
        my_canvas = tk.Canvas(self)
        my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1, anchor="center")
        my_scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        my_canvas.configure(yscrollcommand=my_scrollbar.set, bg="white")

        def _on_mouse_wheel(event):
            my_canvas.yview_scroll(-1 * int((event.delta / 120)), "units")

        my_canvas.bind_all("<MouseWheel>", _on_mouse_wheel)                                                     # Bind mouse wheel to scrollbar
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))      # Bind mouse event to scrollbar
        
        middle_frame = tk.Frame(my_canvas, bg="white")
        my_canvas.create_window((0,0), window=middle_frame, anchor="nw")

        # empty columns that keep the labels separated by a fixed size
        top_frame.columnconfigure(2, minsize=200)
        top_frame.columnconfigure(4, minsize=60)
        top_frame.columnconfigure(6, minsize=115)
        top_frame.columnconfigure(8, minsize=140)
        top_frame.columnconfigure(10, minsize=110)

        # Labels representing the risk levels
        label1 = tk.Label(top_frame, width=15, text="Least", font='Calibri 10', borderwidth=3, relief="groove")
        label2 = tk.Label(top_frame, width=15, text="Minimal", font='Calibri 10', borderwidth=3, relief="groove")
        label3 = tk.Label(top_frame, width=15, text="Moderate", font='Calibri 10', borderwidth=3, relief="groove")
        label4 = tk.Label(top_frame, width=15, text="Signigicant", font='Calibri 10', borderwidth=3, relief="groove")
        label5 = tk.Label(top_frame, width=15, text="Most", font='Calibri 10', borderwidth=3, relief="groove")

        label1.grid(row=1, column=3)
        label2.grid(row=1, column=5)
        label3.grid(row=1, column=7)
        label4.grid(row=1, column=9)
        label5.grid(row=1, column=11)

        # Get the questions from DATA and align them on screen
        i = 0
        for key, value in DATA.IRP_Category4.items():

            question = tk.Label(middle_frame, width=50, text=key, wraplength=400, justify=tk.LEFT, borderwidth=5, relief="groove", font="Calibri 12")
            question.grid(row=i+1, column=0, pady=10, sticky="W")
            self.values.append(tk.IntVar())

            for j in range(5):
                answer = tk.Radiobutton(middle_frame, text=value[j], variable=self.values[i], value=j+1, justify=tk.LEFT, font="Calibri 10", bg='white')
                answer.grid(row=i+1, column=j+1, padx=15, pady=20, sticky="W")

            i += 1
    #endregion


""" Inherent Risk Profile - Category 5 (External Threats) 
    Responsible for the layout of Category 5 """
class IRP_Cat5_Page(tk.Frame):
    #region
    
    values = [] # holds references to the values in the radio buttons (possible answers to each question)

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title("Inherent Risk Profile - External Threats")

        self.config(bg="white")

        # Top frame contains navigation widgets and labels
        top_frame = tk.Frame(self, bg="ghost white", relief='groove', borderwidth=3)
        top_frame.pack(side=tk.TOP, fill=tk.X, anchor="nw")

        home_button = tk.Button(top_frame, width=10, text="HOME", font="Calibri 11", relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                command=lambda: master.switch_frame(home.Home_Page))
        
        back_button = tk.Button(top_frame, width=10, text="BACK", font="Calibri 11", relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                command=lambda: master.switch_frame(IRP_Page))

        home_button.grid(row=0, column=0, padx=30, pady=15)
        back_button.grid(row=0, column=1)

        # Bottom frame contains the submit and clear buttons
        bottom_frame = tk.Frame(self, bg="ghost white", relief='groove', borderwidth=3)
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, anchor="se")

        submit_button = tk.Button(bottom_frame, width=10, text='SUBMIT', font="Calibri 11", relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                  command=lambda: master.switch_frame(IRP_Page))
        
        clear_button = tk.Button(bottom_frame, width=10, text='CLEAR', font="Calibri 11", relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                 command=lambda: clear_pressed(self.values))

        submit_button.pack(side=tk.RIGHT, padx=40, pady=20)
        clear_button.pack(side=tk.RIGHT)

        # Middle frame
        middle_frame = tk.Frame(self, bg="white")
        middle_frame.pack(anchor='nw', fill='x')

        # empty columns that keep the labels separated by a fixed size
        top_frame.columnconfigure(2, minsize=200)
        top_frame.columnconfigure(4, minsize=80)
        top_frame.columnconfigure(6, minsize=115)
        top_frame.columnconfigure(8, minsize=110)
        top_frame.columnconfigure(10, minsize=140)

        # Labels representing the risk levels
        label1 = tk.Label(top_frame, width=15, text="Least", font='Calibri 10', borderwidth=3, relief="groove")
        label2 = tk.Label(top_frame, width=15, text="Minimal", font='Calibri 10', borderwidth=3, relief="groove")
        label3 = tk.Label(top_frame, width=15, text="Moderate", font='Calibri 10', borderwidth=3, relief="groove")
        label4 = tk.Label(top_frame, width=15, text="Signigicant", font='Calibri 10', borderwidth=3, relief="groove")
        label5 = tk.Label(top_frame, width=15, text="Most", font='Calibri 10', borderwidth=3, relief="groove")

        label1.grid(row=1, column=3)
        label2.grid(row=1, column=5)
        label3.grid(row=1, column=7)
        label4.grid(row=1, column=9)
        label5.grid(row=1, column=11)

        # Get the questions from DATA and align them on screen
        i = 0
        for key, value in DATA.IRP_Category5.items():

            question = tk.Label(middle_frame, width=50, text=key, wraplength=400, justify=tk.LEFT, borderwidth=5, relief="groove", font="Calibri 12")
            question.grid(row=i+1, column=0, pady=10, sticky="W")
            self.values.append(tk.IntVar())

            for j in range(5):
                answer = tk.Radiobutton(middle_frame, text=value[j], variable=self.values[i], value=j+1, justify=tk.LEFT, font="Calibri 10", bg='white')
                answer.grid(row=i+1, column=j+1, padx=15, pady=150, sticky="W")

            i += 1
    #endregion


""" This class handles the display of the tooltip """
class ToolTip(object):
    #region
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text

        def enter(event):
            self.showTooltip()
        def leave(event):
            self.hideTooltip()
        widget.bind('<Enter>', enter)
        widget.bind('<Leave>', leave)

    def showTooltip(self):
        self.tooltipwindow = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(1) # window without border and no normal means of closing
        tw.wm_geometry("+{}+{}".format(self.widget.winfo_rootx()-10, self.widget.winfo_rooty()-15))
        label = tk.Label(tw, text = self.text, background = "#ffffe0", relief = 'solid', borderwidth = 1).pack()

    def hideTooltip(self):
        tw = self.tooltipwindow
        if tw is not None:
            tw.destroy()
        self.tooltipwindow = None
    #endregion


""" This function clears the selection of radio buttons 
    @Arg = List[] | contains the variable that is a reference to the radio buttons """
def clear_pressed(values):
    for i in range(len(values)):
        values[i].set(0)


""" This function counts the number of answers in each risk level in every category independently
    @Arg = List[] | contains the variable that is a reference to the radio buttons """
def calculate_total_per_category(values):
    least = minimal = moderate = significant = most = total_selected = 0
    
    for i in range(len(values)):
        if (values[i].get() == 1):
            least += 1
            total_selected += 1
        elif (values[i].get() == 2):
            minimal += 1
            total_selected += 1
        elif (values[i].get() == 3):
            moderate += 1
            total_selected += 1
        elif (values[i].get() == 4):
            significant += 1
            total_selected += 1
        elif (values[i].get() == 5):
            most += 1
            total_selected += 1

    return [least, minimal, moderate, significant, most, total_selected]


""" This functions calculates the total value of each risk level across all the categories of the Inherent Risk Profile """           
def calculate_total():
    least_total = calculate_total_per_category(IRP_Cat1_Page.values)[0] + calculate_total_per_category(IRP_Cat2_Page.values)[0] + calculate_total_per_category(IRP_Cat3_Page.values)[0] + calculate_total_per_category(IRP_Cat4_Page.values)[0] + calculate_total_per_category(IRP_Cat5_Page.values)[0]
    minimal_total = calculate_total_per_category(IRP_Cat1_Page.values)[1] + calculate_total_per_category(IRP_Cat2_Page.values)[1] + calculate_total_per_category(IRP_Cat3_Page.values)[1] + calculate_total_per_category(IRP_Cat4_Page.values)[1] + calculate_total_per_category(IRP_Cat5_Page.values)[1]
    moderate_total = calculate_total_per_category(IRP_Cat1_Page.values)[2] + calculate_total_per_category(IRP_Cat2_Page.values)[2] + calculate_total_per_category(IRP_Cat3_Page.values)[2] + calculate_total_per_category(IRP_Cat4_Page.values)[2] + calculate_total_per_category(IRP_Cat5_Page.values)[2]
    significant_total = calculate_total_per_category(IRP_Cat1_Page.values)[3] + calculate_total_per_category(IRP_Cat2_Page.values)[3] + calculate_total_per_category(IRP_Cat3_Page.values)[3] + calculate_total_per_category(IRP_Cat4_Page.values)[3] + calculate_total_per_category(IRP_Cat5_Page.values)[3]
    most_total = calculate_total_per_category(IRP_Cat1_Page.values)[4] + calculate_total_per_category(IRP_Cat2_Page.values)[4] + calculate_total_per_category(IRP_Cat3_Page.values)[4] + calculate_total_per_category(IRP_Cat4_Page.values)[4] + calculate_total_per_category(IRP_Cat5_Page.values)[4]

    return [least_total, minimal_total, moderate_total, significant_total, most_total]
