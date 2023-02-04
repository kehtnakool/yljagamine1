from random import randint


class Model:
    def __init__(self):

        self.tasks_allocated = ""
        self.studentlist = []
        self.tasklist = []
        self.sdudentsfile = ''
        self.tasksfile = ''
        self.csvfile = ''

    def return_students(self):
        try:
            with open(self.sdudentsfile, encoding="utf-8") as f:
                students = "ÕPILASED:\n"
                self.studentlist = []
                for rida in f:
                    if len(rida.strip()) > 0:
                        students += rida
                        self.studentlist += [rida]
            if self.studentlist == []:
                return "Õpilaste fail oli tühi"
            return students
        except:
            return "ÕPILASED:"

    def return_tasks(self):
        try:
            with open(self.tasksfile, encoding="utf-8") as f:
                tasks = "ÜLEASNDED:\n"
                self.tasklist = []
                for rida in f:
                    if len(rida.strip()) > 0:
                        tasks += rida
                        self.tasklist += [rida]
            if self.tasklist == []:
                return "Ülesannete fail oli tühi"
            return tasks
        except:
            return "ÜLEASNDED:"

    def allocate_tasks(self):
        if (self.studentlist == []) or (self.tasklist == []):
            return "Ülesannete jagamiseks peavad olema avatud\nõpilaste fail ja ülesannete fail"
        elif len(self.tasklist) >= len(self.studentlist):
            tasklist_temp = self.tasklist[:]
            upper_limit = len(self.tasklist) - 1
            tekst = "\n"
            self.tasks_allocated = ""
            for student in self.studentlist:
                random_nr = randint(0, upper_limit)
                upper_limit -= 1
                tekst += student.strip() + " - " + tasklist_temp[random_nr]
                self.tasks_allocated += student.strip() + ";" + tasklist_temp[random_nr]
                tasklist_temp.remove(tasklist_temp[random_nr])
            return tekst
        else:
            self.tasklist = []
            return "Ülesandeid on selle õpilaste arvu kohta\nliiga vähe"

    def save_csv(self):
        if self.tasklist == []:
            return "Ülesandeid pole jagatud\nmidagi ei salvestatud"
        try:
            with open(self.csvfile, "w", encoding="utf-8") as f:
                f.write(self.tasks_allocated)
                return "Salvestati csv fail"
        except:
            return "Vajutati cancel või on fail\nmõnes muus programmis lahti\nja sinna ei saa kirjutada"
