import logging

logging.basicConfig(filename="InheritanceExamples.log", level=logging.DEBUG)


class NotStringException(Exception):
    def __init__(self, msg):
        self.message = msg
        print(msg)

    def __str__(self):
        return self.message


class NotIntegerException(Exception):
    def __init__(self, msg):
        self.message = msg
        print(msg)

    def __str__(self):
        return self.message


class NotRangeClassException(Exception):
    def __init__(self, msg):
        self.message = msg
        print(msg)

    def __str__(self):
        return self.message


# Example-1 on Hierarchical Inheritance and Method overriding Ineuron Students
class IneuronStudent:
    name = ""
    _servicetype = ""
    __qualification = ""
    __empStatus = ""

    def __init__(self, name, servicetype, qualification, empStatus):
        """
        :param name: Name of the student
        :param servicetype: The kind of service the student has opted in ineuron
        :param qualification: The qualification the student holds before joining into ineuron
        :param empStatus: The status of employment the student holds before joining into ineuron
        """
        try:
            logging.info("The given name is %s", name)
            if type(name) != str:
                raise (NotStringException("The given value is not of string type"))
            else:
                self.name = name
            logging.info("The given service type is %s", servicetype)
            if type(servicetype) != str:
                raise (NotStringException("The given value is not of string type"))
            else:
                self._servicetype = servicetype
            logging.info("The given qualification is %s", qualification)
            if type(qualification) != str:
                raise (NotStringException("The given value is not of string type"))
            else:
                self.__qualification = qualification
            logging.info("The given emp status is %s", empStatus)
            if type(empStatus) != str:
                raise (NotStringException("The given value is not of string type"))
            else:
                self.__empStatus = empStatus
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))
            self.name = ""
            self._servicetype = ""
            self.__qualification = ""
            self.__empStatus = ""

    def printDetails(self):
        """
        It prints the details of the students
        """
        print(self.name, self._servicetype, self.__qualification, self.__empStatus)

    def WelcomeNote(self):
        print("Hi {}, Welcome to Ineuron!".format(self.name))


class TechNeuron(IneuronStudent):
    courseName = ""

    def __init__(self, name, servicetype, qualification, empStatus, courseName):
        super().__init__(name, servicetype, qualification, empStatus)
        try:
            logging.info("The given name is %s", courseName)
            if type(courseName) != str:
                raise (NotStringException("The given value is not of string type"))
            else:
                self.courseName = courseName
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))
            self.courseName = ""

    def printTechNeuronDetails(self):
        """
        :return: It prints the details of the students present in TechNeuron with the courseName that they are doing
        """
        print(self.courseName, self.name, self._servicetype)

    def WelcomeNote(self):
        print("Hi {}, Welcome to TechNeuron!".format(self.name))


class FSDS(IneuronStudent):

    def __init__(self, name, servicetype, qualification, empStatus):
        super().__init__(name, servicetype, qualification, empStatus)

    def printFSDSDetails(self):
        """
        :return: It prints the details of the students present in TechNeuron with the courseName that they are doing
        """
        print(self.name, self._servicetype)

    def WelcomeNote(self):
        print("Hi {}, Welcome to FSDS!".format(self.name))


# Example-2 Ineuron Internship on Single Inheritance
# Using the super class IneuronStudent class of Example-1
class IneuronInternship(IneuronStudent):
    internshipProjectName = ""
    internshipDescription = ""

    def __init__(self, name, servicetype, qualification, empStatus, internshipProjectName, internshipDescription):
        super().__init__(name, servicetype, qualification, empStatus)
        try:
            logging.info("The given name is %s", internshipProjectName)
            if type(internshipProjectName) != str:
                raise (NotStringException("The given value is not of string type"))
            else:
                self.internshipProjectName = internshipProjectName
            logging.info("The given name is %s", internshipDescription)
            if type(internshipDescription) != str:
                raise (NotStringException("The given value is not of string type"))
            else:
                self.internshipDescription = internshipDescription
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))
            self.internshipProjectName = ""
            self.internshipDescription = ""

    def printInternshipDetails(self):
        """
        :return: It prints the details of the students present in Ineuron Internship with the projectName and
        description
        """
        print(self.name, self._servicetype, self.internshipProjectName, self.internshipDescription)

    def WelcomeNote(self):
        print("Hi {}, Welcome to Ineuron Internship!".format(self.name))


# Example-3 on Polymorphism on contact Info using 2 classes and 1 function which is specified outside all classes
class StudentContactInformation:
    studentMailId = ""
    studentPhoneNumber = 0

    def setStudentEmailId(self, email):
        """
        :param email: The email id of the student
        :return: No Return
        """
        try:
            logging.info("The given email id is %s", email)
            if type(email) != str:
                raise (NotStringException("The given value is not of string type"))
            else:
                self.studentMailId = email
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))
            self.studentMailId = ""

    def setStudentPhoneNumber(self, phno):
        """
        :param phno: The phone number of the student
        :return: No Return
        """
        try:
            logging.info("The given phone no is %s", phno)
            if type(phno) != int:
                raise (NotStringException("The given value is not of integer type"))
            else:
                self.studentPhoneNumber = phno
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))
            self.studentPhoneNumber = ""

    def getEmailId(self):
        """
        :return: Prints Student Email ID
        """
        print("The Student's Email ID is: ", self.studentMailId)

    def getPhoneNumber(self):
        """
        :return: Prints Student Phone Number
        """
        print("The Student's Phone Number is: ", self.studentPhoneNumber)


class InstructorContactInformation:
    InstructorMailId = ""
    InstructorPhoneNumber = 0

    def setInstructorEmailId(self, email):
        """
        :param email: The email id of the instructor
        :return: No Return
        """
        try:
            logging.info("The given email id is %s", email)
            if type(email) != str:
                raise (NotStringException("The given value is not of string type"))
            else:
                self.InstructorMailId = email
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))
            self.InstructorMailId = ""

    def setInstructorPhoneNumber(self, phno):
        """
        :param phno: The phone number of the instructor
        :return: No Return
        """
        try:
            logging.info("The given phone no is %s", phno)
            if type(phno) != int:
                raise (NotStringException("The given value is not of integer type"))
            else:
                self.InstructorPhoneNumber = phno
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))
            self.InstructorMailId = ""

    def getEmailId(self):
        """
        :return: Prints Instructor Email ID
        """
        print("The Instructor's Email ID is: ", self.InstructorMailId)

    def getPhoneNumber(self):
        """
        :return: Prints Instructor Phone Number
        """
        print("The Instructor's Phone Number is: ", self.InstructorPhoneNumber)


def check(a):
    a.getEmailId()
    a.getPhoneNumber()


'''
We can uncomment this lines to check Example-3
sconinfo = StudentContactInformation()
iconinfo = InstructorContactInformation()
sconinfo.setStudentEmailId("sivamani@gmail.com")
sconinfo.setStudentPhoneNumber(9848032919)
iconinfo.setInstructorEmailId("Rahul@ineuron.ai")
iconinfo.setInstructorPhoneNumber(9856321470)
check(iconinfo)
check(sconinfo)
'''


# Example-4 on method overriding over welcome notes this is to show method overriding as a concept separately
# I am using super class IneuronStudent present in example 1.
class TechNeuronWelcomeNote(IneuronStudent):
    def __init__(self, name, servicetype, qualification, empStatus):
        super().__init__(name, servicetype, qualification, empStatus)

    def WelcomeNote(self):
        print("Hi {}, Welcome to TechNeuron!".format(self.name))


# Example-5 Multilevel Inheritance
class TechNeuronCourse:
    courseName = ""

    def setCourseName(self, courseName):
        try:
            logging.info("The given course name is %s", courseName)
            if type(courseName) != str:
                raise (NotStringException("The given value is not of string type"))
            else:
                self.courseName = courseName
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))
            self.courseName = ""

    def getCourseName(self):
        """
        :return: Prints Course Name
        """
        print("The Course Name is: ", self.courseName)


class IneuronClass(TechNeuronCourse):
    subtopics = []
    instructorName = ""

    def setSubTopics(self, *st):
        """
        :param st: It is a tuple of string variables with values for main topic
        :return: No return
        """
        logging.info("The given sub topics are %s", str(st))
        self.subtopics = list(st)

    def getSubTopics(self):
        """
        :return: Prints SubTopics
        """
        print("The Sub Topics are: ", self.subtopics)

    def setInstructorName(self, instructorName):
        try:
            logging.info("The given Instructor Name is %s", instructorName)
            if type(instructorName) != int:
                raise (NotStringException("The given value is not of integer type"))
            else:
                self.instructorName = instructorName
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))
            self.instructorName = ""

    def getInstructorName(self):
        """
        :return: Prints Instructor Name
        """
        print("The Instructor Name is: ", self.instructorName)


class InstructorDetails(IneuronClass):
    LinkedInProfile = ""

    def setInstructorLinkedInProfile(self, email):
        """
        :param email: The email id of the instructor
        :return: No Return
        """
        try:
            logging.info("The given Instructor LinkedIn Profile Id is %s", email)
            if type(email) != str:
                raise (NotStringException("The given value is not of string type"))
            else:
                self.LinkedInProfile = email
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))
            self.LinkedInProfile = ""

    def getInstructorLinkedInProfile(self):
        """
        :return: Prints Instructor LinkedIn Profile Id
        """
        print("The Instructor's Email ID is: ", self.LinkedInProfile)


# Example-6 on Multiple Inheritance
class FSDSDet:
    FSDSDetails = ""

    def setFSDSDetails(self, FSDSDetails):
        try:
            logging.info("The given FSDSDetails is %s", FSDSDetails)
            if type(FSDSDetails) != str:
                raise (NotStringException("The given value is not of string type"))
            else:
                self.FSDSDetails = FSDSDetails
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))
            self.FSDSDetails = ""

    def getFSDSDetails(self):
        """
        :return: Prints FSDSDetails
        """
        print("The FSDSDetails is: ", self.FSDSDetails)


class DataAnalyticsBootCamp:
    dataAnalyticsBootCampDetails = ""

    def setDataAnalyticsBootCampDetails(self, dataAnalyticsBootCampDetails):
        try:
            logging.info("The given dataAnalyticsBootCampDetails is %s", dataAnalyticsBootCampDetails)
            if type(dataAnalyticsBootCampDetails) != str:
                raise (NotStringException("The given value is not of string type"))
            else:
                self.dataAnalyticsBootCampDetails = dataAnalyticsBootCampDetails
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))
            self.dataAnalyticsBootCampDetails = ""

    def getDataAnalyticsBootCampDetails(self):
        """
        :return: Prints dataAnalyticsBootCampDetails
        """
        print("The dataAnalyticsBootCampDetails is: ", self.dataAnalyticsBootCampDetails)


class TechNeuronCourses(FSDSDet, DataAnalyticsBootCamp):
    pass


# Example-7 Inheritance Example for Job Registration
# Taking superclass from Example-1 i.e., IneuronStudent
class JobsRegistration(IneuronStudent):
    companyName = ""
    interestedStatus = ""

    def __init__(self, name, servicetype, qualification, empStatus, interestedStatus, companyName):
        super().__init__(name, servicetype, qualification, empStatus)
        try:
            logging.info("The given interested status is %s", interestedStatus)
            if type(interestedStatus) != str:
                raise (NotStringException("The given value is not of string type"))
            else:
                self.interestedStatus = interestedStatus
            logging.info("The given companyName is %s", companyName)
            if type(companyName) != str:
                raise (NotStringException("The given value is not of string type"))
            else:
                self.companyName = companyName
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))
            self.interestedStatus = ""
            self.companyName = ""

    def ThankYouNote(self):
        print("Hi {}, Thanks for applying for {}".format(self.name, self.companyName))


# Example-8 Inheritance Example for Internship Registration
# Taking superclass from Example-1 i.e., IneuronStudent
class InternshipRegistration(IneuronStudent):
    projectName = ""

    def __init__(self, name, servicetype, qualification, empStatus, projectName):
        super().__init__(name, servicetype, qualification, empStatus)
        try:
            logging.info("The given project Name is %s", projectName)
            if type(projectName) != str:
                raise (NotStringException("The given value is not of string type"))
            else:
                self.projectName = projectName
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))
            self.projectName = ""

    def ThankYouNote(self):
        print("Hi {}, Thanks for applying for {}".format(self.name, self.projectName))


# Example-9 on polymorphism of Example-7 and Example-8 common function that is ThankYouNote
def checkThankYouNote(a):
    a.ThankYouNote()


'''
If we uncomment then we can check Example-9
inpReg = InternshipRegistration("Rohit", "Internship", "B TECH", "EXP-1", "Forecasting Weather")
jobReg = JobsRegistration("Rohit", "FSDS", "B TECH", "EXP-1", "Yes", "EY")
checkThankYouNote(inpReg)
checkThankYouNote(jobReg)
'''


# Example-10 on LoginClass
class LoginClass:
    studentName = ""
    studentEmailId = ""
    __studentPassword = ""

    def setStudentName(self, studentName):
        try:
            logging.info("The given studentName is %s", studentName)
            if type(studentName) != str:
                raise (NotStringException("The given value is not of string type"))
            else:
                self.studentName = studentName
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))
            self.studentName = ""

    def getStudentName(self):
        """
        :return: Prints studentName
        """
        print("The studentName is: ", self.studentName)

    def setStudentEmailId(self, studentEmailId):
        try:
            logging.info("The given studentEmailId is %s", studentEmailId)
            if type(studentEmailId) != str:
                raise (NotStringException("The given value is not of string type"))
            else:
                self.studentEmailId = studentEmailId
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))
            self.studentEmailId = ""

    def getStudentEmailId(self):
        """
        :return: Prints studentEmailId
        """
        print("The studentEmailId is: ", self.studentEmailId)

    def setStudentPassword(self, studentPassword):
        try:
            logging.info("The given studentName is %s", studentPassword)
            if type(studentPassword) != str:
                raise (NotStringException("The given value is not of string type"))
            else:
                self.__studentPassword = studentPassword
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))
            self.__studentPassword = ""


class IneuronLogin(LoginClass):
    def WelcomeNote(self):
        print("Hi {}, Welcome to Ineuron!".format(self.studentName))


