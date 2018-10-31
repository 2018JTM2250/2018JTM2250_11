#
#  @file ps1.py
#
#  @author Kartik Gupta
#  @date 31 October 2018
#


import pdb
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen,FadeTransition
from kivy.lang.builder import Builder
from systemd import login
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.button import Button
import operator
import matplotlib.pyplot as plt 
import numpy as np
from matplotlib.pyplot import gca


##############################
choice = 'a'
entryy = 'a'
studentid = ''
student_pass='a'

#################################################################################################################
#################################################################################################################


class SelectionPage(Screen):
    # function whether Student or Admin is selected and moving to login page
    def login_as(self,argc):
        if argc == "student":
            self.manager.current = "login_page"
            self.manager.transition.direction = 'left'
            
        if argc == "admin":
            self.manager.current = "login_page"
            self.manager.transition.direction = 'left'
        
        # global variable storing the choice : Student or Admin
        global choice
        choice = argc

#################################################################################################################
#################################################################################################################3

class LoginPage(Screen):
    
    # function verifying the entered credentials of student or admin
    def verify_credentials(self):
        flag=0
        student_login_list=[]
        student_passlist=[]
        admin_login_list=[]
        admin_passlist=[]
        
        # when choice = Student
        if choice == "student":
            
            f= open('student_id.txt', 'r+') 
            for r in f:
                r=r.split(',')
                student_login_list.append(r[0])
                student_passlist.append(r[1])
            
    
            for i in range(len(student_login_list)):    
                if str(self.ids["login"].text) == student_login_list[i] and str(self.ids["passw"].text) == student_passlist[i]:
                    global studentid
                    studentid = self.ids["login"].text
                    self.manager.current = "student_page"
                    flag=1
                    self.ids["login"].text = ""
                    self.ids["passw"].text = ""
                    self.manager.transition.direction = 'left'

                
            if flag != 1:
                content = Button(text='Please enter correct User Details')
                popup = Popup(title='Error', content=content, size_hint=(None, None), size=(400, 200))
                content.bind(on_press=popup.dismiss)
                popup.open() 
                self.ids["login"].text = ""
                self.ids["passw"].text = ""
            

        # When choice  = Admin    
        if choice == "admin":
            
            f= open('admin_id.txt', 'r') 
            for r in f:
                r=r.split(',')
                admin_login_list.append(r[0])
                admin_passlist.append(r[1])
              
            for i in range(len(admin_login_list)):    
                if self.ids["login"].text == admin_login_list[i] and self.ids["passw"].text == admin_passlist[i]:
                    self.manager.current = "admin_page"
                    flag=1          
                    self.ids["login"].text = ""
                    self.ids["passw"].text = ""
                    self.manager.transition.direction = 'left'
                    
                    
            if flag != 1:
                content = Button(text='Please enter correct User Details')
                popup = Popup(title='Error', content=content, size_hint=(None, None), size=(400, 200))
                content.bind(on_press=popup.dismiss)
                popup.open()            
                self.ids["login"].text = ""
                self.ids["passw"].text = ""    
                
    # function for clearing the entered data on the screenpage  
    def deleting_data(self):
        self.manager.current = "selection_page" 
        self.manager.transition.direction = 'right'
        
        self.ids["login"].text = ""
        self.ids["passw"].text = "" 
        


##################################################################################################################
##################################################################################################################

# StudentPage : page where student enter details
class StudentPage(Screen):
    
    # function for creating the file based on the entered details bt the student
    def creatingdata(self,argc):
        global entryy
        entryy = argc
  
        # fetching all the entered details in variables
        a=self.ids["name"].text
        b=self.ids["entryno"].text 
        c=self.ids["branch"].text
        d=self.ids["passingyear"].text
        e=self.ids["address"].text
        fi=self.ids["subject1"].text
        g=self.ids["subject2"].text
        h=self.ids["subject3"].text
        i=self.ids["subject4"].text
        j=self.ids["subject5"].text
        
        #read file for reading the subjects name
        f=open("marks.txt" , "r+")
        qq=f.readline()
        qq=qq.split(',')
        
        #Verifying whether entered entryno is equal to login id or not
        if studentid == entryy:
            # Verifying whether entered subject name match the subjects in database
            if (fi in qq) and (g in qq) and (h in qq) and (i in qq) and (j in qq) :
            
                f = open("student_info/"+studentid+".txt", "w+")
                f.write(
                         "Name : ," + a + ",\n" +
                         "Entry Number : ," + b + ",\n" + 
                         "Branch : ," + c + ",\n" + 
                         "Year of Passing : ," + d + ",\n" +
                         "Address : ," + e + ",\n" + 
                         "Subject1 : ," + fi + ",\n" +
                         "Subject2 : ," +  g + ",\n" + 
                         "Subject3 : ," +  h + ",\n" + 
                         "Subject4 : ," +  i + ",\n" + 
                         "Subject5 : ," +  j + ","
                        
                        )  
                
                # opening popup when details are successfully submitted
                content = Button(text='Details have been submitted')
                popup = Popup(title='Success', content=content, size_hint=(None, None), size=(400, 200))
                content.bind(on_press=popup.dismiss)
                popup.open()            
                
                # Move to next page when all details are successfully submitted
                self.manager.current = "student_details_page" 
                
                self.ids["name"].text = ""
                self.ids["entryno"].text = ""
                self.ids["branch"].text = ""
                self.ids["passingyear"].text = ""
                self.ids["address"].text = ""
                self.ids["subject1"].text = ""
                self.ids["subject2"].text = "" 
                self.ids["subject3"].text = ""
                self.ids["subject4"].text = ""
                self.ids["subject5"].text = ""
                
            # when subjects do no match the database subject names
            else:
                content = Button(text='Invalid Subjects')
                popup = Popup(title='Error', content=content, size_hint=(None, None), size=(400, 200))
                content.bind(on_press=popup.dismiss)
                popup.open() 
                
        # when entry no is not equal to login id        
        else:
            content = Button(text='Invalid Entry no.')
            popup = Popup(title='Error', content=content, size_hint=(None, None), size=(400, 200))
            content.bind(on_press=popup.dismiss)
            popup.open()   
            
        
    #function for clearing data    
    def deleting_data(self,argc):
     
        self.ids["name"].text = ""
        self.ids["entryno"].text = ""
        self.ids["branch"].text = ""
        self.ids["passingyear"].text = ""
        self.ids["address"].text = ""
        self.ids["subject1"].text = ""
        self.ids["subject2"].text = "" 
        self.ids["subject3"].text = ""
        self.ids["subject4"].text = ""
        self.ids["subject5"].text = ""
        
        
        
        if argc == "logout":
            self.manager.current = "login_page" 

#############################################################################################################
#############################################################################################################

# AdminPage : Page after login of admin
class AdminPage(Screen):
     
    # function showing details of student after entering entry no. 
    def display_student_details(self):
        aa=self.ids["student_entryno"].text

        #Exception handling
        try:
            
            #if there is some data in the entryno column
            if aa:
                count=0
                data2=[]
                entry_list2=[]
                f = open('marks.txt', 'r+') 
                for r in f:
                    r=r.split(',')
                    count += 1 
                    # 2_D list of the marks database
                    data2.append(r)
                
                #entry no. of all students
                for i in range(1,count):
                    entry_list2.append(data2[i][0])
                
                #When entered entry no. is valid     
                if aa in entry_list2:
                    
                    list=[]
                    f = open("student_info/"+str(aa)+'.txt', 'r+') 
                    for r in f:
                        r=r.split(',')
                        #student details
                        list.append(r[1])
            
            
                    self.ids["label_name"].text = "Name"
                    self.ids["label_entryno"].text = "Entry Number"
                    self.ids["label_branch"].text = "Branch"
                    self.ids["label_passingyear"].text = "Year of Passing"
                    self.ids["label_address"].text = "Address"
                    self.ids["label_subject1"].text = "Subject1"
                    self.ids["label_subject2"].text = "Subject2"
                    self.ids["label_subject3"].text = "Subject3"
                    self.ids["label_subject4"].text = "Subject4"
                    self.ids["label_subject5"].text = "Subject5"
                    self.ids["label_subject6"].text = "Subject6"
                    self.ids["label_subject7"].text = "Subject7"
            
                   
                    self.ids["Name"].text = list[0]
                    self.ids["entryno"].text = list[1]
                    self.ids["branch"].text = list[2]
                    self.ids["passingyear"].text = list[3]
                    self.ids["address"].text = list[4]
                    
                    self.ids["subject1"].text = data2[0][1]
                    self.ids["subject2"].text = data2[0][2]
                    self.ids["subject3"].text = data2[0][3]
                    self.ids["subject4"].text = data2[0][4]
                    self.ids["subject5"].text = data2[0][5]
                    self.ids["subject6"].text = data2[0][6]
                    self.ids["subject7"].text = data2[0][7]
            
            
                                   
                    for i in range(1,count):
                        if data2[i][0] == aa:
                    
                            self.ids["subject1marks"].text = data2[i][1]
                            self.ids["subject2marks"].text = data2[i][2]
                            self.ids["subject3marks"].text = data2[i][3]
                            self.ids["subject4marks"].text = data2[i][4]
                            self.ids["subject5marks"].text = data2[i][5]
                            self.ids["subject6marks"].text = data2[i][6]
                            self.ids["subject7marks"].text = data2[i][7]
                                                                  
                #when entry no. is not valid
                else:
                    content = Button(text='Invalid Entry no.')
                    popup = Popup(title='Error', content=content, size_hint=(None, None), size=(400, 200))
                    content.bind(on_press=popup.dismiss)
                    popup.open()
                    
                    # clearing all the data on the screen
                    self.ids["student_entryno"].text = "" 
                    self.ids["label_name"].text = ""
                    self.ids["label_entryno"].text = ""
                    self.ids["label_branch"].text = ""
                    self.ids["label_passingyear"].text = ""
                    self.ids["label_address"].text = ""
                    self.ids["label_subject1"].text = ""
                    self.ids["label_subject2"].text = ""
                    self.ids["label_subject3"].text = ""
                    self.ids["label_subject4"].text = ""
                    self.ids["label_subject5"].text = ""  
                    self.ids["label_subject6"].text = ""  
                    self.ids["label_subject7"].text = ""   
                    
                    self.ids["Name"].text = ""   
                    self.ids["entryno"].text = ""   
                    self.ids["branch"].text = ""   
                    self.ids["passingyear"].text = ""
                    self.ids["address"].text = ""  
                    self.ids["subject1"].text = ""
                    self.ids["subject2"].text = "" 
                    self.ids["subject3"].text = ""
                    self.ids["subject4"].text = ""
                    self.ids["subject5"].text = ""
                    self.ids["subject6"].text = ""
                    self.ids["subject7"].text = ""
                    self.ids["subject1marks"].text = ""
                    self.ids["subject2marks"].text = ""
                    self.ids["subject3marks"].text = ""
                    self.ids["subject4marks"].text = ""
                    self.ids["subject5marks"].text = ""
                    self.ids["subject6marks"].text = ""
                    self.ids["subject7marks"].text = "" 
            
            # when nothign is written in the entryno column
            else:
                content = Button(text='Please enter Entry No. of the student')
                popup = Popup(title='Error', content=content, size_hint=(None, None), size=(400, 200))
                content.bind(on_press=popup.dismiss)
                popup.open() 
                
                #clearing all the data
                self.ids["student_entryno"].text = "" 
                self.ids["label_name"].text = ""
                self.ids["label_entryno"].text = ""
                self.ids["label_branch"].text = ""
                self.ids["label_passingyear"].text = ""
                self.ids["label_address"].text = ""
                self.ids["label_subject1"].text = ""
                self.ids["label_subject2"].text = ""
                self.ids["label_subject3"].text = ""
                self.ids["label_subject4"].text = ""
                self.ids["label_subject5"].text = ""  
                self.ids["label_subject6"].text = ""  
                self.ids["label_subject7"].text = ""   
                
                self.ids["Name"].text = ""   
                self.ids["entryno"].text = ""   
                self.ids["branch"].text = ""   
                self.ids["passingyear"].text = ""
                self.ids["address"].text = ""  
                self.ids["subject1"].text = ""
                self.ids["subject2"].text = "" 
                self.ids["subject3"].text = ""
                self.ids["subject4"].text = ""
                self.ids["subject5"].text = ""
                self.ids["subject6"].text = ""
                self.ids["subject7"].text = ""
                self.ids["subject1marks"].text = ""
                self.ids["subject2marks"].text = ""
                self.ids["subject3marks"].text = ""
                self.ids["subject4marks"].text = ""
                self.ids["subject5marks"].text = ""
                self.ids["subject6marks"].text = ""
                self.ids["subject7marks"].text = "" 
        
        # When file does not exist
        except IOError:
                content=Button(text='Student Details File not found')
                popup = Popup(title='Oops!!', content=content, size_hint=(None, None), size=(300, 200))
                content.bind(on_press=popup.dismiss)
                popup.open()
                print("cannot open the file") 
                
                
    # function plotting marks of student in each subject after entering entry no.
    def plot_student_details(self):
        
        marks=[]
        subjects=[]
        aa=self.ids["student_entryno"].text

        try:
            if aa:
                count=0
                data2=[]
                entry_list2=[]
                f = open('marks.txt', 'r+') 
                for r in f:
                    r=r.split(',')
                    count += 1 
                    data2.append(r)
            
                for i in range(1,count):
                    entry_list2.append(data2[i][0])
                    
                if aa in entry_list2:
                    
                    for j in range(1,8):
                        subjects.append(data2[0][j])
                                   
                    for i in range(1,count):
                        if data2[i][0] == aa:
                            for k in range(1,8):
                                marks.append(int(data2[i][k]))
                    
                    print(subjects)
                    print(marks)
                
                    # plotting bar graph of marks vs subjects               
                    index = np.arange(len(subjects))
                    plt.bar(index, marks)
                    plt.xlabel('Subject', fontsize=15)
                    plt.ylabel(' Marks', fontsize=15)
                    plt.xticks(index, subjects, fontsize=15, rotation=0)
                    plt.title(' Subject Marks ')
                    ax=plt.gca()
                    ax.set_ylim([0,100])
                    plt.show() 
                    
                # when entryno. is not valid
                else:
                    content = Button(text='Invalid Entry no.')
                    popup = Popup(title='Error', content=content, size_hint=(None, None), size=(400, 200))
                    content.bind(on_press=popup.dismiss)
                    popup.open()

            #when nothing is written in entryno column                
            else:
                content = Button(text='Please enter Entry No. of the student')
                popup = Popup(title='Error', content=content, size_hint=(None, None), size=(400, 200))
                content.bind(on_press=popup.dismiss)
                popup.open() 
                

        # when file does not exist        
        except IOError:
                content=Button(text='Student Details File not found')
                popup = Popup(title='Oops!!', content=content, size_hint=(None, None), size=(300, 200))
                content.bind(on_press=popup.dismiss)
                popup.open()
                print("cannot open the file")

    #clearing all the data        
    def deleting_data(self,argc):
        
        
        self.ids["student_entryno"].text = "" 
        self.ids["label_name"].text = ""
        self.ids["label_entryno"].text = ""
        self.ids["label_branch"].text = ""
        self.ids["label_passingyear"].text = ""
        self.ids["label_address"].text = ""
        self.ids["label_subject1"].text = ""
        self.ids["label_subject2"].text = ""
        self.ids["label_subject3"].text = ""
        self.ids["label_subject4"].text = ""
        self.ids["label_subject5"].text = ""  
        self.ids["label_subject6"].text = ""  
        self.ids["label_subject7"].text = ""   
        
        self.ids["Name"].text = ""   
        self.ids["entryno"].text = ""   
        self.ids["branch"].text = ""   
        self.ids["passingyear"].text = ""
        self.ids["address"].text = ""  
        self.ids["subject1"].text = ""
        self.ids["subject2"].text = "" 
        self.ids["subject3"].text = ""
        self.ids["subject4"].text = ""
        self.ids["subject5"].text = ""
        self.ids["subject6"].text = ""
        self.ids["subject7"].text = ""
        self.ids["subject1marks"].text = ""
        self.ids["subject2marks"].text = ""
        self.ids["subject3marks"].text = ""
        self.ids["subject4marks"].text = ""
        self.ids["subject5marks"].text = ""
        self.ids["subject6marks"].text = ""
        self.ids["subject7marks"].text = "" 

        if argc=="logout":
            self.manager.current = "login_page" 
                
        if argc == "details":
            self.manager.current = "details_page" 

###############################################################################################################
###############################################################################################################

#StudentDetailsPage : page after successfully submitting the details
class StudentDetailsPage(Screen):
    
    #showing data on the screen
    def show_data(self):
        
        list=[]
        
        f = open("student_info/"+studentid+'.txt', 'r+') 
        for r in f:
            r=r.split(',')
            list.append(r[1])
        
        # filling data
        self.ids["Name"].text = list[0]
        self.ids["entryno"].text = list[1]
        self.ids["branch"].text = list[2]
        self.ids["passingyear"].text = list[3]
        self.ids["address"].text = list[4]
        self.ids["subject1"].text = list[5]
        self.ids["subject2"].text = list[6]
        self.ids["subject3"].text = list[7]
        self.ids["subject4"].text = list[8]
        self.ids["subject5"].text = list[9]

        # filling data according to the subjects mentioned
        count=0
        data=[]
        entry_list=[]
        f = open('marks.txt', 'r+') 
        for r in f:
            r=r.split(',')
            count += 1
            
            # 2-D list of the data 
            data.append(r)
            
        
        for i in range(1,count):
            print(data[i][0])
              
        for i in range(1,count):
            # selecting entryno
            if data[i][0] == entryy:
                
                for j in range(1,8):
                    
                    # verifying subject name
                    if data[0][j] == list[5]:
                        
                        self.ids["subject1marks"].text = data[i][j]
                        
                    if data[0][j] == list[6]:
                        self.ids["subject2marks"].text = data[i][j]                     
#         
                    if data[0][j] == list[7]:
                        self.ids["subject3marks"].text = data[i][j]
                        
                    if data[0][j] == list[8]:
                        self.ids["subject4marks"].text = data[i][j]
                        
                    if data[0][j] == list[9]:
                        self.ids["subject5marks"].text = data[i][j]

    #clearing all the data on the screen  
    def deleting_data(self,argc):
            
        self.ids["Name"].text = ""
        self.ids["entryno"].text = ""
        self.ids["branch"].text = ""
        self.ids["passingyear"].text = ""
        self.ids["address"].text = ""
        self.ids["subject1"].text = ""
        self.ids["subject2"].text = "" 
        self.ids["subject3"].text = ""
        self.ids["subject4"].text = ""
        self.ids["subject5"].text = ""
        
        self.ids["subject1marks"].text = ""
        self.ids["subject2marks"].text = "" 
        self.ids["subject3marks"].text = ""
        self.ids["subject4marks"].text = ""
        self.ids["subject5marks"].text = ""         
    
        if argc == "logout":
            self.manager.current = "login_page" 
            self.manager.transition.direction = 'right'
        
        if argc == "back":
            self.manager.current = "student_page" 
            self.manager.transition.direction = 'right'

#################################################################################################################
#################################################################################################################

# DetailsPage : page after selecting detailed analysis option
class DetailsPage(Screen):
    # printing average marks with name and entry no of the top 5 student
    def detailed_details(self):
        
        self.ids["sno"].text = "S.No."
        self.ids["name"].text = "Name"
        self.ids["entryno"].text = "Entry No."
        self.ids["marks"].text = "Marks"
        self.ids["sno1"].text = "1"
        self.ids["sno2"].text = "2"
        self.ids["sno3"].text = "3"
        self.ids["sno4"].text = "4"
        self.ids["sno5"].text = "5"
        
        # calculating average marks
        count=0
        data=[]
        average=[]    
        marks=0
        total=[]
        average_marks=[]
        entry=[]
        list_sorted_entry=[]
        list_sorted_marks=[]
        name=[]
         
         
        f = open('marks.txt', 'r+') 
        for r in f:
            r=r.split(',')
            count += 1
            data.append(r)
 
        # lists containing elements all equal to 0
        for i in range(count):
            total.append(marks)
            average_marks.append(marks)
                
             
        for i in range(1,count):
            for j in range(1,8):
                total[i] += int(data[i][j])
            average_marks[i] = total[i]/7
            average.append(average_marks[i])
            entry.append(data[i][0])
        print(average)   # Average marks of each student
        print(entry)     # Entry no. of each student
         
        # creating dictionary
        d = dict(zip(entry,average))
        print(d)
 
        # sorting entryno and marks in 2-D list
        cd = sorted(d.items(),key=operator.itemgetter(1),reverse=True)
        print(cd)
        
        #seperating entryno and marks in 2 different list
        for i in range(len(cd)):
            list_sorted_entry.append(cd[i][0])
            list_sorted_marks.append(cd[i][1])
         
        print(list_sorted_entry)
        print(list_sorted_marks)
        
        #fetching name according to the entry no
        for i in range(5):
            f = open("student_info/"+list_sorted_entry[i]+'.txt', 'r+') 
            r=f.readline()
            r=r.split(',')
            name.append(r[1])
            
        print(name)
        
        
        self.ids["entryno1"].text = list_sorted_entry[0] 
        self.ids["entryno2"].text = list_sorted_entry[1]
        self.ids["entryno3"].text = list_sorted_entry[2]
        self.ids["entryno4"].text = list_sorted_entry[3]
        self.ids["entryno5"].text = list_sorted_entry[4]
            
        self.ids["name1"].text = name[0] 
        self.ids["name2"].text = name[1]
        self.ids["name3"].text = name[2]
        self.ids["name4"].text = name[3]
        self.ids["name5"].text = name[4]   
           
           
        self.ids["marks1"].text = str(round(list_sorted_marks[0],2))   
        self.ids["marks2"].text = str(round(list_sorted_marks[1],2))
        self.ids["marks3"].text = str(round(list_sorted_marks[2],2))
        self.ids["marks4"].text = str(round(list_sorted_marks[3],2))
        self.ids["marks5"].text = str(round(list_sorted_marks[4],2))
#         
        
    # function for plotting the average marks with respect to entryno
    def plot(self):
        
        count=0
        data=[]
        average=[]    
        marks=0
        total=[]
        average_marks=[]
        entry=[]
         
        f = open('marks.txt', 'r+') 
        for r in f:
            r=r.split(',')
            count += 1
            data.append(r)
 
 
        for i in range(count):
            total.append(marks)
            average_marks.append(marks)
                
             
        for i in range(1,count):
            for j in range(1,8):
                total[i] += int(data[i][j])
            average_marks[i] = total[i]/7
            average.append(average_marks[i])
            entry.append(data[i][0])
        print(average)
        print(entry)
        
        
        # Bar graph showing average marks with respect to entryno
        index = np.arange(len(entry))
        plt.bar(index, average)
        plt.xlabel('Entry Number', fontsize=15)
        plt.ylabel('Average Marks', fontsize=15)
        plt.xticks(index, entry, fontsize=15, rotation=0)
        plt.title('Average Marks of Students')
        ax=plt.gca()
        ax.set_ylim([0,100])
        plt.show()  

    #function for clearing data
    def deleting_data(self,argc):
        self.ids["sno"].text = ""
        self.ids["name"].text = ""
        self.ids["entryno"].text = ""
        self.ids["marks"].text = ""
        self.ids["sno1"].text = ""
        self.ids["sno2"].text = ""
        self.ids["sno3"].text = ""
        self.ids["sno4"].text = ""
        self.ids["sno5"].text = ""
        self.ids["name1"].text = ""
        self.ids["name2"].text = ""
        self.ids["name3"].text = ""
        self.ids["name4"].text = ""
        self.ids["name5"].text = ""
        self.ids["entryno1"].text = ""
        self.ids["entryno2"].text = ""
        self.ids["entryno3"].text = ""
        self.ids["entryno4"].text = ""
        self.ids["entryno5"].text = ""
        self.ids["marks1"].text = ""
        self.ids["marks2"].text = ""
        self.ids["marks3"].text = ""
        self.ids["marks4"].text = ""
        self.ids["marks5"].text = ""
        
        if argc == "logout":
            self.manager.current = "login_page"
        
        if argc == "back":
            self.manager.current = "admin_page" 
        
#         if argc == "homepage":
#             self.manager.current = "selection_page"           
            
###################################################################################################################
##################################################################################################################            

class ScreenManagement(ScreenManager):
    pass

kv_file = Builder.load_file('ps1.kv')

class ps1App(App):
    def builder(self):
        return kv_file


ps1App().run()