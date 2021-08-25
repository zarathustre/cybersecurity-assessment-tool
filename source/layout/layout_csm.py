import tkinter as tk
from tkinter import messagebox
import layout.layout_home as home
import layout.layout_login as login
import layout.layout_csm_domain1 as d1
import layout.layout_csm_domain2 as d2
import layout.layout_csm_domain3 as d3
import layout.layout_csm_domain4 as d4
import layout.layout_csm_domain5 as d5
import DATA
import db
from datetime import datetime

""" This class is responsible for the layout of the Cybersecurity Maturity's Main page
    Contains all the categories and links to each one """

class CSM_Page(tk.Frame):
    #region
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title("Cybersecurity Maturity")

        self.config(bg="ghost white")

        self.unbind_all("<MouseWheel>")

        home_button = tk.Button(self, width=10, text="HOME", font="Calibri 14", relief="raised", borderwidth=2, bg="azure3", activebackground='light blue',
                                command=lambda: master.switch_frame(home.Home_Page))

        domain1_button = tk.Button(self, text="Cyber Risk Management and Oversight", font='Calibri 14', relief="groove", borderwidth=2, bg='light gray', activebackground='light blue',
                                   command=lambda: master.switch_frame(d1.CSM_Domain1_Page))

        domain2_button = tk.Button(self, text="Threat Intelligence and Collaboration", font="Calibri 14", relief="groove", borderwidth=2, bg="light gray", activebackground='light blue',
                                   command=lambda: master.switch_frame(d2.CSM_Domain2_Page))

        domain3_button = tk.Button(self, text="Cybersecurity Controls", font="Calibri 14", relief="groove", borderwidth=2, bg="light gray", activebackground='light blue',
                                   command=lambda: master.switch_frame(d3.CSM_Domain3_Page))

        domain4_button = tk.Button(self, text="External Dependency Management", font="Calibri 14", relief="groove", borderwidth=2, bg="light gray", activebackground='light blue',
                                   command=lambda: master.switch_frame(d4.CSM_Domain4_Page))

        domain5_button = tk.Button(self, text="Cyber Incident Management and Resilience", font="Calibri 14", relief="groove", borderwidth=2, bg="light gray", activebackground='light blue', 
                                   command=lambda: master.switch_frame(d5.CSM_Domain5_Page))

        domain1_label = tk.Label(self, font="Calibri 15", bg="ghost white",
                                 text=str(submit_pressed(d1.CSM_Domain1_Governance_Page.values)[3] 
                                          + submit_pressed(d1.CSM_Domain1_RiskManagement_Page.values)[3]
                                          + submit_pressed(d1.CSM_Domain1_Resources_Page.values)[3] 
                                          + submit_pressed(d1.CSM_Domain1_TrainingAndCulture_Page.values)[3])
                                          + "/" 
                                          + str(sum([len(DATA.CSM_Domain1_Governance[i]) for i in DATA.CSM_Domain1_Governance]) 
                                          + sum([len(DATA.CSM_Domain1_RiskManagement[i]) for i in DATA.CSM_Domain1_RiskManagement])
                                          + sum([len(DATA.CSM_Domain1_Resources[i]) for i in DATA.CSM_Domain1_Resources])
                                          + sum([len(DATA.CSM_Domain1_TrainingAndCulture[i]) for i in DATA.CSM_Domain1_TrainingAndCulture]))
                                          + " Answered")

        domain2_label = tk.Label(self, font="Calibri 15", bg="ghost white",
                                 text=str(submit_pressed(d2.CSM_Domain2_ThreatIntelligence_Page.values)[3] 
                                          + submit_pressed(d2.CSM_Domain2_MonitoringAndAnalyzing_Page.values)[3]
                                          + submit_pressed(d2.CSM_Domain2_InformationSharing_Page.values)[3]) 
                                          + "/" 
                                          + str(sum([len(DATA.CSM_Domain2_ThreatIntelligence[i]) for i in DATA.CSM_Domain2_ThreatIntelligence]) 
                                          + sum([len(DATA.CSM_Domain2_MonitoringAndAnalyzing[i]) for i in DATA.CSM_Domain2_MonitoringAndAnalyzing])
                                          + sum([len(DATA.CSM_Domain2_InformationSharing[i]) for i in DATA.CSM_Domain2_InformationSharing]))
                                          + " Answered")

        domain3_label = tk.Label(self, font="Calibri 15", bg="ghost white",
                                 text=str(submit_pressed(d3.CSM_Domain3_PreventiveControls_Page.values)[3] 
                                          + submit_pressed(d3.CSM_Domain3_DetectiveControls_Page.values)[3]
                                          + submit_pressed(d3.CSM_Domain3_CorrectiveControls_Page.values)[3]) 
                                          + "/" 
                                          + str(sum([len(DATA.CSM_Domain3_PreventiveControls[i]) for i in DATA.CSM_Domain3_PreventiveControls]) 
                                          + sum([len(DATA.CSM_Domain3_DetectiveControls[i]) for i in DATA.CSM_Domain3_DetectiveControls])
                                          + sum([len(DATA.CSM_Domain3_CorrectiveControls[i]) for i in DATA.CSM_Domain3_CorrectiveControls]))
                                          + " Answered")

        domain4_label = tk.Label(self, font="Calibri 15", bg="ghost white",
                                 text=str(submit_pressed(d4.CSM_Domain4_Connections_Page.values)[3] 
                                          + submit_pressed(d4.CSM_Domain4_RelationshipManagement_Page.values)[3]) 
                                          + "/" 
                                          + str(sum([len(DATA.CSM_Domain4_Connections[i]) for i in DATA.CSM_Domain4_Connections]) 
                                          + sum([len(DATA.CSM_Domain4_RelationshipManagement[i]) for i in DATA.CSM_Domain4_RelationshipManagement]))
                                          + " Answered")

        domain5_label = tk.Label(self, font="Calibri 15", bg="ghost white",
                                 text=str(submit_pressed(d5.CSM_Domain5_IncidentPlanningAndStrategy_Page.values)[3] 
                                          + submit_pressed(d5.CSM_Domain5_DetectionResponseAndMitigation_Page.values)[3]
                                          + submit_pressed(d5.CSM_Domain5_EscalationAndReporting_Page.values)[3]) 
                                          + "/" 
                                          + str(sum([len(DATA.CSM_Domain5_IncidentPlanningAndStrategy[i]) for i in DATA.CSM_Domain5_IncidentPlanningAndStrategy]) 
                                          + sum([len(DATA.CSM_Domain5_DetectionResponseAndMitigation[i]) for i in DATA.CSM_Domain5_DetectionResponseAndMitigation])
                                          + sum([len(DATA.CSM_Domain5_EscalationAndReporting[i]) for i in DATA.CSM_Domain5_EscalationAndReporting]))
                                          + " Answered")

        reset_button = tk.Button(self, width=10, text="RESET", font="Calibri 14", relief="raised", borderwidth=2, bg="azure3", activebackground='light blue',
                                 command=lambda: CSM_Page.reset(master))

        final_score_button = tk.Button(self, width=10, text="Final Score", font="Calibri 14", relief="raised", borderwidth=2, bg="azure3", activebackground='light blue',
                                       command=lambda: master.switch_frame(CSM_Final), state='normal') # state = disabled
        
        ToolTip(widget=final_score_button, text="Answer all the questions to proceed")

        home_button.place(relx=0.1, rely=0.1)

        domain1_button.place(relx=0.5, rely=0.3, anchor='center')
        domain2_button.place(relx=0.5, rely=0.4, anchor='center')
        domain3_button.place(relx=0.5, rely=0.5, anchor='center')
        domain4_button.place(relx=0.5, rely=0.6, anchor='center')
        domain5_button.place(relx=0.5, rely=0.7, anchor='center')

        domain1_label.place(relx=0.75, rely=0.3, anchor='center')
        domain2_label.place(relx=0.75, rely=0.4, anchor='center')
        domain3_label.place(relx=0.75, rely=0.5, anchor='center')
        domain4_label.place(relx=0.75, rely=0.6, anchor='center')
        domain5_label.place(relx=0.75, rely=0.7, anchor='center')

        reset_button.place(relx=0.5, rely=0.85, anchor='center')
        final_score_button.place(relx=0.75, rely=0.85, anchor='center')

    def reset(frame):
        clear_pressed(d1.CSM_Domain1_Governance_Page.values)
        clear_pressed(d1.CSM_Domain1_RiskManagement_Page.values)
        clear_pressed(d1.CSM_Domain1_Resources_Page.values)
        clear_pressed(d1.CSM_Domain1_TrainingAndCulture_Page.values)
        clear_pressed(d2.CSM_Domain2_ThreatIntelligence_Page.values)
        clear_pressed(d2.CSM_Domain2_MonitoringAndAnalyzing_Page.values)
        clear_pressed(d2.CSM_Domain2_InformationSharing_Page.values)  
        clear_pressed(d3.CSM_Domain3_PreventiveControls_Page.values)
        clear_pressed(d3.CSM_Domain3_DetectiveControls_Page.values)
        clear_pressed(d3.CSM_Domain3_CorrectiveControls_Page.values) 
        clear_pressed(d4.CSM_Domain4_Connections_Page.values)
        clear_pressed(d4.CSM_Domain4_RelationshipManagement_Page.values)
        clear_pressed(d5.CSM_Domain5_IncidentPlanningAndStrategy_Page.values)
        clear_pressed(d5.CSM_Domain5_DetectionResponseAndMitigation_Page.values)
        clear_pressed(d5.CSM_Domain5_EscalationAndReporting_Page.values)
        frame.switch_frame(CSM_Page) 
    #endregion


class CSM_Final(tk.Frame):
    #region
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title("Cybersecurity Maturity - Final Score")
        self.config(bg="ghost white")

        # limit entry to alphanumeric characters only
        def only_alphanumeric(char):
            return char.isalnum()

        alpha_num_validation = self.register(only_alphanumeric)

        home_button = tk.Button(self, font='Calibri 14', relief='raised', borderwidth=2, bg='azure3', activebackground='light blue', 
                                text='HOME', width=10, command=lambda: master.switch_frame(home.Home_Page))

        back_button = tk.Button(self, font='Calibri 14', relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                text='BACK', width=10, command=lambda: master.switch_frame(CSM_Page))

        yes_total_label = tk.Label(self, font='Calibri 15', bg='ghost white', text='Yes: ' + str(calculate_total()[0]) + ' Point(s)')
        yes_compensating_label = tk.Label(self, font='Calibri 15', bg='ghost white', text='Yes (Compensating): ' + str(calculate_total()[1]) + ' Point(s)')
        no_total_label = tk.Label(self, font='Calibri 15', bg='ghost white', text='No: ' + str(calculate_total()[2]) + ' Point(s)')

        final_score_label = tk.Label(self, font='Calibri 15', bg='ghost white', text='Maturity Level: ' + CSM_Final.find_max())                      
        
        assessment_name_entry = tk.Entry(self, font="Calirbi 11 bold", relief='groove', borderwidth=3, fg='white', insertbackground='white', cursor='top_left_arrow',
                                         bg='SlateGray4', width=20, validate='key', validatecommand=(alpha_num_validation, '%S'))

        ToolTip(widget=assessment_name_entry, text="Enter a unique name for the assessment")
        
        save_results_button = tk.Button(self, font='Calibri 14', relief='raised', borderwidth=2, bg='azure3', activebackground='light blue',
                                        text='SAVE', width=10, command=lambda: CSM_Final.save(master, assessment_name_entry.get()))

        home_button.place(relx=0.1, rely=0.1, anchor='nw')
        back_button.place(relx=0.25, rely=0.1, anchor='nw')

        yes_total_label.place(relx=0.51, rely=0.3, anchor='center')
        yes_compensating_label.place(relx=0.51, rely=0.36, anchor='center')
        no_total_label.place(relx=0.51, rely=0.42, anchor='center')

        final_score_label.place(relx=0.51, rely=0.66, anchor='center')

        assessment_name_entry.place(relx=0.51, rely=0.8, anchor='center')
        save_results_button.place(relx=0.68, rely=0.8, anchor='center')

    def find_max():
        max_value = max(calculate_total())
        indexes = [i for i, j in enumerate(calculate_total()) if j == max_value]
        if max_value == 0:
            return ''
        elif 2 in indexes:
            return 'No'
        elif 1 in indexes:
            return 'Yes (Compensating)'
        elif 0 in indexes:
            return 'Yes'

    def save(frame, name):
        get_userInfo_query = """ SELECT uid,company FROM users WHERE username=%s; """
        u_value = [login.Login_Page.logged_in]

        db_connection = db.create_db_connection("localhost", "root", "TempNewPass#158", "CSA") # open db connection
        uInfo = db.read_query_data(db_connection, get_userInfo_query, u_value)

        insert_irp_query = """ 
        INSERT INTO csm (name, date, user, company, yes, yes (compensating), no, maturity_level) VALUES (%s,%s,%s,%s,%s,%s,%s,%s); 
        """
        values = [name, datetime.now(), uInfo[0][0], uInfo[0][1], calculate_total()[0], calculate_total()[1], calculate_total()[2], CSM_Final.find_max()]
        
        get_assessment_name_query = """ SELECT name FROM irp WHERE name=%s; """
        name_value = [name]
        assessment_name = db.read_query_data(db_connection, get_assessment_name_query, name_value)

        if name == "":
            messagebox.showwarning("Warning", "You need to enter a name for the assessment")
        elif assessment_name:
            messagebox.showwarning("Warning", "An assessment with this name already exists")
        else:
            db.execute_query_data(db_connection, insert_irp_query, values)
            frame.switch_frame(home.Home_Page)

        db_connection.close()
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


def clear_pressed(values):
    for i in range(len(values)):
        values[i].set(0)

def submit_pressed(values):
    y = y_c = n = total_selected = 0

    for i in range(len(values)):
        if (values[i].get() == 1):
            y += 1
            total_selected += 1
        elif (values[i].get() == 2):
            y_c += 1
            total_selected += 1
        elif (values[i].get() == 3):
            n += 1
            total_selected += 1

    return [y, y_c, n, total_selected]


def calculate_total():
    yes_total = (submit_pressed(d1.CSM_Domain1_Governance_Page.values)[0] + submit_pressed(d1.CSM_Domain1_RiskManagement_Page.values)[0]
                + submit_pressed(d1.CSM_Domain1_Resources_Page.values)[0] + submit_pressed(d1.CSM_Domain1_TrainingAndCulture_Page.values)[0]
                + submit_pressed(d2.CSM_Domain2_ThreatIntelligence_Page.values)[0] + submit_pressed(d2.CSM_Domain2_MonitoringAndAnalyzing_Page.values)[0]
                + submit_pressed(d2.CSM_Domain2_InformationSharing_Page.values)[0] 
                + submit_pressed(d3.CSM_Domain3_PreventiveControls_Page.values)[0] + submit_pressed(d3.CSM_Domain3_DetectiveControls_Page.values)[0] 
                + submit_pressed(d3.CSM_Domain3_CorrectiveControls_Page.values)[0]
                + submit_pressed(d4.CSM_Domain4_Connections_Page.values)[0] + submit_pressed(d4.CSM_Domain4_RelationshipManagement_Page.values)[0]
                + submit_pressed(d5.CSM_Domain5_IncidentPlanningAndStrategy_Page.values)[0] + submit_pressed(d5.CSM_Domain5_DetectionResponseAndMitigation_Page.values)[0]
                + submit_pressed(d5.CSM_Domain5_EscalationAndReporting_Page.values)[0])

    yes_compensating_total = (submit_pressed(d1.CSM_Domain1_Governance_Page.values)[1] + submit_pressed(d1.CSM_Domain1_RiskManagement_Page.values)[1]
                + submit_pressed(d1.CSM_Domain1_Resources_Page.values)[1] + submit_pressed(d1.CSM_Domain1_TrainingAndCulture_Page.values)[1]
                + submit_pressed(d2.CSM_Domain2_ThreatIntelligence_Page.values)[1] + submit_pressed(d2.CSM_Domain2_MonitoringAndAnalyzing_Page.values)[1]
                + submit_pressed(d2.CSM_Domain2_InformationSharing_Page.values)[1] 
                + submit_pressed(d3.CSM_Domain3_PreventiveControls_Page.values)[1] + submit_pressed(d3.CSM_Domain3_DetectiveControls_Page.values)[1] 
                + submit_pressed(d3.CSM_Domain3_CorrectiveControls_Page.values)[1]
                + submit_pressed(d4.CSM_Domain4_Connections_Page.values)[1] + submit_pressed(d4.CSM_Domain4_RelationshipManagement_Page.values)[1]
                + submit_pressed(d5.CSM_Domain5_IncidentPlanningAndStrategy_Page.values)[1] + submit_pressed(d5.CSM_Domain5_DetectionResponseAndMitigation_Page.values)[1]
                + submit_pressed(d5.CSM_Domain5_EscalationAndReporting_Page.values)[1])

    no_total = (submit_pressed(d1.CSM_Domain1_Governance_Page.values)[2] + submit_pressed(d1.CSM_Domain1_RiskManagement_Page.values)[2]
                + submit_pressed(d1.CSM_Domain1_Resources_Page.values)[2] + submit_pressed(d1.CSM_Domain1_TrainingAndCulture_Page.values)[2]
                + submit_pressed(d2.CSM_Domain2_ThreatIntelligence_Page.values)[2] + submit_pressed(d2.CSM_Domain2_MonitoringAndAnalyzing_Page.values)[2]
                + submit_pressed(d2.CSM_Domain2_InformationSharing_Page.values)[2] 
                + submit_pressed(d3.CSM_Domain3_PreventiveControls_Page.values)[2] + submit_pressed(d3.CSM_Domain3_DetectiveControls_Page.values)[2] 
                + submit_pressed(d3.CSM_Domain3_CorrectiveControls_Page.values)[2]
                + submit_pressed(d4.CSM_Domain4_Connections_Page.values)[2] + submit_pressed(d4.CSM_Domain4_RelationshipManagement_Page.values)[2]
                + submit_pressed(d5.CSM_Domain5_IncidentPlanningAndStrategy_Page.values)[2] + submit_pressed(d5.CSM_Domain5_DetectionResponseAndMitigation_Page.values)[2]
                + submit_pressed(d5.CSM_Domain5_EscalationAndReporting_Page.values)[2])

    return [yes_total, yes_compensating_total, no_total]

    