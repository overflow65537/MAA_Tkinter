from tool import *
from tkinter import *
from tkinter.ttk import *


class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        self.tk_button_Start_Task = self.__tk_button_Start_Task(self)
        self.tk_label_ADB_Part_Label = self.__tk_label_ADB_Part_Label(self)
        self.tk_label_ADB_Address_Label = self.__tk_label_ADB_Address_Label(self)
        self.tk_label_Resource_Type_Label = self.__tk_label_Resource_Type_Label(self)
        self.tk_label_Add_Task_Label = self.__tk_label_Add_Task_Label(self)
        self.tk_label_Add_Task_Label_2 = self.__tk_label_Add_Task_Label_2(self)
        self.tk_input_ADB_Path_Input = self.__tk_input_ADB_Path_Input(self)
        self.tk_input_ADB_Address_Input = self.__tk_input_ADB_Address_Input(self)
        self.tk_select_box_Resource_Type_Select = self.__tk_select_box_Resource_Type_Select(self)
        self.tk_select_box_Add_Task_Select = self.__tk_select_box_Add_Task_Select(self)
        self.tk_button_Add_Task_Button = self.__tk_button_Add_Task_Button(self)
        self.tk_label_Task_List_Label = self.__tk_label_Task_List_Label(self)
        self.tk_list_box_Task_List = self.__tk_list_box_Task_List(self)
        self.tk_button_Move_Up_Button = self.__tk_button_Move_Up_Button(self)
        self.tk_button_Move_Down_Button = self.__tk_button_Move_Down_Button(self)
        self.tk_button_Delete_Button = self.__tk_button_Delete_Button(self)
        self.tk_select_box_Add_Task_Select_1 = self.__tk_select_box_Add_Task_Select_1(self)
        self.tk_select_box_Add_Task_Select_2 = self.__tk_select_box_Add_Task_Select_2(self)
        self.tk_select_box_Add_Task_Select_3 = self.__tk_select_box_Add_Task_Select_3(self)
        self.tk_select_box_Add_Task_Select_4 = self.__tk_select_box_Add_Task_Select_4(self)
        self.tk_label_Add_Task_Label_3 = self.__tk_label_Add_Task_Label_3(self)
        self.tk_label_Add_Task_Label_4 = self.__tk_label_Add_Task_Label_4(self)
        self.tk_label_Add_Task_Label_5 = self.__tk_label_Add_Task_Label_5(self)
        self.tk_label_Add_Task_Label_6 = self.__tk_label_Add_Task_Label_6(self)
        self.tk_label_Controller_Type_Label = self.__tk_label_Controller_Type_Label(self)
        self.tk_select_box_Controller_Type_Select = self.__tk_select_box_Controller_Type_Select(self)
        self.tk_button_Update_button = self.__tk_button_Update_button(self)
        self.tk_label_Controller_Type_Label = self.__tk_label_Controller_Type_Label(self)
        self.tk_select_box_Controller_Type_Select = self.__tk_select_box_Controller_Type_Select(self)
        self.tk_progressbar_ProgressBar = self.__tk_progressbar_ProgressBar(self)
        self.tk_label_Stable_loca = self.__tk_label_Stable_loca(self)
        self.tk_label_Stable_online = self.__tk_label_Stable_online(self)
        self.tk_button_Check_Update_Button = self.__tk_button_Check_Update_Button(self)
    def __win(self):
        self.title("MAA-GUI")
        # 设置窗口大小、居中
        width = 600
        height = 450
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        
        self.resizable(width=False, height=False)
        
    def scrollbar_autohide(self,vbar, hbar, widget):
        """自动隐藏滚动条"""
        def show():
            if vbar: vbar.lift(widget)
            if hbar: hbar.lift(widget)
        def hide():
            if vbar: vbar.lower(widget)
            if hbar: hbar.lower(widget)
        hide()
        widget.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Leave>", lambda e: hide())
        if hbar: hbar.bind("<Enter>", lambda e: show())
        if hbar: hbar.bind("<Leave>", lambda e: hide())
        widget.bind("<Leave>", lambda e: hide())
    
    def v_scrollbar(self,vbar, widget, x, y, w, h, pw, ph):
        widget.configure(yscrollcommand=vbar.set)
        vbar.config(command=widget.yview)
        vbar.place(relx=(w + x) / pw, rely=y / ph, relheight=h / ph, anchor='ne')
    def h_scrollbar(self,hbar, widget, x, y, w, h, pw, ph):
        widget.configure(xscrollcommand=hbar.set)
        hbar.config(command=widget.xview)
        hbar.place(relx=x / pw, rely=(y + h) / ph, relwidth=w / pw, anchor='sw')
    def create_bar(self,master, widget,is_vbar,is_hbar, x, y, w, h, pw, ph):
        vbar, hbar = None, None
        if is_vbar:
            vbar = Scrollbar(master)
            self.v_scrollbar(vbar, widget, x, y, w, h, pw, ph)
        if is_hbar:
            hbar = Scrollbar(master, orient="horizontal")
            self.h_scrollbar(hbar, widget, x, y, w, h, pw, ph)
        self.scrollbar_autohide(vbar, hbar, widget)
    def __tk_button_Start_Task(self,parent):
        btn = Button(parent, text="开始任务", takefocus=False,)
        btn.place(x=270, y=320, width=70, height=30)
        return btn
    def __tk_label_ADB_Part_Label(self,parent):
        label = Label(parent,text="ADB路径",anchor="center", )
        label.place(x=0, y=0, width=70, height=30)
        return label
    def __tk_label_ADB_Address_Label(self,parent):
        label = Label(parent,text="ADB端口",anchor="center", )
        label.place(x=0, y=40, width=70, height=30)
        return label
    def __tk_label_Resource_Type_Label(self,parent):
        label = Label(parent,text="客户端",anchor="center", )
        label.place(x=0, y=80, width=70, height=30)
        return label
    def __tk_label_Add_Task_Label(self,parent):
        label = Label(parent,text="添加任务",anchor="center", )
        label.place(x=0, y=120, width=340, height=30)
        return label
    def __tk_label_Add_Task_Label_2(self,parent):
        label = Label(parent,text="任务类型",anchor="center", )
        label.place(x=0, y=160, width=70, height=30)
        return label
    def __tk_input_ADB_Path_Input(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=80, y=0, width=260, height=30)
        return ipt
    def __tk_input_ADB_Address_Input(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=80, y=40, width=260, height=30)
        return ipt
    def __tk_select_box_Resource_Type_Select(self,parent):
        cb = Combobox(parent, state="readonly", )
        cb['values'] = ()
        cb.place(x=80, y=80, width=140, height=30)
        return cb
    def __tk_select_box_Add_Task_Select(self,parent):
        cb = Combobox(parent, state="readonly", )
        cb['values'] = ()
        cb.place(x=80, y=160, width=180, height=30)
        return cb
    def __tk_button_Add_Task_Button(self,parent):
        btn = Button(parent, text="添加任务", takefocus=False,)
        btn.place(x=270, y=160, width=70, height=30)
        return btn
    def __tk_label_Task_List_Label(self,parent):
        label = Label(parent,text="任务列表",anchor="center", )
        label.place(x=380, y=0, width=180, height=30)
        return label
    def __tk_list_box_Task_List(self,parent):
        lb = Listbox(parent)
        for item in Get_Values_list_Option(os.getcwd()+"\MAA_bin\config\maa_pi_config.json","task"):
            lb.insert(END, item)
        lb.place(x=360, y=40, width=220, height=400)
        return lb
    def __tk_select_box_Controller_Type_Select(self,parent):
        cb = Combobox(parent, state="readonly", )
        cb['values'] = ()
        cb.place(x=260, y=80, width=80, height=30)
        return cb
    def __tk_select_box_Controller_Type_Select(self,parent):
        cb = Combobox(parent, state="readonly", )
        cb['values'] = ()
        cb.place(x=260, y=80, width=80, height=30)
        return cb
    def __tk_button_Move_Up_Button(self,parent):
        btn = Button(parent, text="上移", takefocus=False,)
        btn.place(x=270, y=200, width=70, height=30)
        return btn
    def __tk_button_Move_Down_Button(self,parent):
        btn = Button(parent, text="下移", takefocus=False,)
        btn.place(x=270, y=240, width=70, height=30)
        return btn
    def __tk_button_Delete_Button(self,parent):
        btn = Button(parent, text="删除", takefocus=False,)
        btn.place(x=270, y=280, width=70, height=30)
        return btn
    def __tk_select_box_Add_Task_Select_1(self,parent):
        cb = Combobox(parent, state="readonly", )
        cb['values'] = ("1号选项")
        cb.place(x=80, y=200, width=180, height=30)
        return cb
    def __tk_select_box_Add_Task_Select_2(self,parent):
        cb = Combobox(parent, state="readonly", )
        cb['values'] = ("2号选项")
        cb.place(x=80, y=240, width=180, height=30)
        return cb
    def __tk_select_box_Add_Task_Select_3(self,parent):
        cb = Combobox(parent, state="readonly", )
        cb['values'] = ("3号选项")
        cb.place(x=80, y=280, width=180, height=30)
        return cb
    def __tk_select_box_Add_Task_Select_4(self,parent):
        cb = Combobox(parent, state="readonly", )
        cb['values'] = ("4号选项")
        cb.place(x=80, y=320, width=180, height=30)
        return cb
    def __tk_label_Add_Task_Label_3(self,parent):
        label = Label(parent,text="1号标签",anchor="center", )
        label.place(x=0, y=200, width=70, height=30)
        return label
    def __tk_label_Add_Task_Label_4(self,parent):
        label = Label(parent,text="2号标签",anchor="center", )
        label.place(x=0, y=240, width=70, height=30)
        return label
    def __tk_label_Add_Task_Label_5(self,parent):
        label = Label(parent,text="3号标签",anchor="center", )
        label.place(x=0, y=280, width=70, height=30)
        return label
    def __tk_label_Add_Task_Label_6(self,parent):
        label = Label(parent,text="4号标签",anchor="center", )
        label.place(x=0, y=320, width=70, height=30)
        return label
    def __tk_label_Controller_Type_Label(self,parent):
        label = Label(parent,text="控制端",anchor="center", )
        label.place(x=180, y=80, width=70, height=30)
        return label
    def __tk_button_Update_button(self,parent):
        btn = Button(parent, text="更新", takefocus=False,)
        return btn
    def __tk_progressbar_ProgressBar(self,parent):
        progressbar = Progressbar(parent, orient=HORIZONTAL,)
        progressbar.place(x=60, y=385, width=275, height=30)
        return progressbar
    def __tk_label_Stable_loca(self,parent):
        try:  
            with open(os.getcwd()+"/config.json", "r", encoding='utf-8') as config_file:  
                config_data = json.load(config_file)  
                current_tag_name = config_data["tag_name"]
        except Exception as e:
            print(e)
            current_tag_name = ""  
        label = Label(parent,text="当前版本:"+current_tag_name,anchor="center", )
        label.place(x=60, y=420, width=130, height=30)
        return label
    def __tk_label_Stable_online(self,parent):
        label = Label(parent,text="标签",anchor="center", )
        label.place(x=205, y=420, width=130, height=30)
        return label
    def __tk_button_Check_Update_Button(self,parent):
        btn = Button(parent, text="检查", takefocus=False,)
        btn.place(x=0, y=420, width=50, height=30)
        return btn
class Win(WinGUI):
    def __init__(self, controller):
        self.ctl = controller
        super().__init__()
        self.__event_bind()
        self.ctl.init(self)

    def __event_bind(self):
        self.tk_button_Start_Task.bind('<Button-1>',self.ctl.Start_Task)
        self.tk_input_ADB_Path_Input.bind('<Return>',self.ctl.Save_ADB_Path)
        self.tk_input_ADB_Address_Input.bind('<Return>',self.ctl.Save_ADB_Address)
        self.tk_select_box_Resource_Type_Select.bind('<<ComboboxSelected>>',self.ctl.Save_Resource_Type_Select)
        self.tk_select_box_Resource_Type_Select.bind('<Button-1>',self.ctl.Save_ADB_Path)
        self.tk_select_box_Add_Task_Select.bind('<<ComboboxSelected>>',self.ctl.Add_Task_Select_More_Select)
        self.tk_select_box_Add_Task_Select.bind('<Enter>',self.ctl.Save_ADB_Address)
        self.tk_button_Add_Task_Button.bind('<Button-1>',self.ctl.Add_Task)
        self.tk_button_Move_Up_Button.bind('<Button-1>',self.ctl.Click_Move_Up_Button)
        self.tk_button_Move_Down_Button.bind('<Button-1>',self.ctl.Click_Move_Down_Button)
        self.tk_button_Delete_Button.bind('<Button-1>',self.ctl.Click_Delete_Button)
        self.tk_select_box_Controller_Type_Select.bind('<<ComboboxSelected>>',self.ctl.Save_Controller_Type_Select)
        self.tk_list_box_Task_List.bind('<Delete>',self.ctl.Click_Delete_Button)
        self.tk_button_Update_button.bind('<Button-1>',self.ctl.Update)
        self.tk_select_box_Resource_Type_Select.bind('<Button-1>',self.ctl.Save_ADB_Path)
        self.tk_select_box_Add_Task_Select.bind('<Enter>',self.ctl.Save_ADB_Address)
        self.tk_button_Check_Update_Button.bind('<Button-1>',self.ctl.Check_Update)
        self.tk_select_box_Controller_Type_Select.bind('<<ComboboxSelected>>',self.ctl.Save_Controller_Type_Select)
if __name__ == "__main__":
    win = WinGUI()
    win.mainloop()