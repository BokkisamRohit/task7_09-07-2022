import logging

logging.basicConfig(filename="constructorExamples.log", level=logging.DEBUG)


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


# Example-1 on Ineuron Students


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


# Example-2 on TechNeuron

class TechNeuron:
    mainTopic = ""
    subtopics = []

    def setMainTopic(self, mt):
        """
        :param mt: It is a string variable with value for main topic
        :return: No return
        """
        try:
            logging.info("The given main topic is %s", mt)
            if type(mt) != str:
                raise (NotStringException("The given value is not of string type"))
            else:
                self.mainTopic = mt
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))
            self.mainTopic = ""

    def setSubTopics(self, *st):
        """
        :param st: It is a tuple of string variables ref to main topic
        :return: No return
        """
        logging.info("The given main topic is %s", str(st))
        self.subtopics = list(st)

    def getCourseDetails(self):
        """
        Prints Course Details
        """
        print("The Main Topic is: ", self.mainTopic)
        print("The Sub Topics is: ", self.subtopics)


# Example-3 on Ineuron Classes

class IneuronClasses:
    classTopic = ""
    classInstructorName = ""
    noOfHours = 0

    def __init__(self, classTopic, classInstructorName, noOfHours):
        """
        :param classTopic: The name of the topic that will be taken in the class
        :param classInstructorName: The name of the instructor who will take the class
        :param noOfHours: The number of hours the class will be conducted
        """
        try:
            logging.info("The given class topic is %s", str(classTopic))
            if type(classTopic) != str:
                raise (NotStringException("The given value is not of string type"))
            else:
                self.classTopic = classTopic
            logging.info("The given class instructor name is %s", str(classInstructorName))
            if type(classInstructorName) != str:
                raise (NotStringException("The given value is not of string type"))
            else:
                self.classInstructorName = classInstructorName
            logging.info("The given number of hours is %s", str(noOfHours))
            if type(noOfHours) != int:
                raise (NotIntegerException("The given value is not of integer type"))
            else:
                self.noOfHours = noOfHours
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))
            self.classTopic = ""
            self.classInstructorName = ""
            self.noOfHours = 0


# Example-4 on Instructor Details
class InstructorDetails:
    instructorName = ""
    instructorMainSkill = ""
    instructorGmailId = ""

    def setInstructorName(self, name):
        """
        :param name: The name of the instructor
        :return: No Return
        """
        try:
            logging.info("The given instructor name is %s", name)
            if type(name) != str:
                raise (NotStringException("The given value is not of string type"))
            else:
                self.instructorName = name
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))
            self.instructorName = ""

    def setInstructorMainSkill(self, skillname):
        """
        :param skillname: The name of the skill that instructor knows the best
        :return: No Return
        """
        try:
            logging.info("The given instructor main skill is %s", skillname)
            if type(skillname) != str:
                raise (NotStringException("The given value is not of string type"))
            else:
                self.instructorMainSkill = skillname
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))
            self.instructorMainSkill = ""

    def setInstructorGmailId(self, email):
        """
        :param email: The gmail id of the instructor
        :return: No Return
        """
        try:
            logging.info("The given gmail id is %s", email)
            if type(email) != str:
                raise (NotStringException("The given value is not of string type"))
            else:
                self.instructorGmailId = email
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))
            self.instructorGmailId = ""

    def getInstructorDetails(self):
        """
        Prints Instructor Details
        """
        print("The Instructor Name:", self.instructorName)
        print("The Instructor Main Skill:", self.instructorMainSkill)
        print("The Instructor Gmail Id:", self.instructorGmailId)


# Example-5 on Affiliate
class Affiliate:
    _affiliateName = ""

    def __init__(self, affiliateName):
        """
        :param affiliateName: The Affiliate's name
        """
        try:
            logging.info("The given affiliate Name is %s", str(affiliateName))
            if type(affiliateName) != str:
                raise (NotStringException("The given value is not of string type"))
            else:
                self._affiliateName = affiliateName
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))
            self._affiliateName = ""


# Example-6 on blog
class BlogDetails:
    def __init__(self, blogName, blogMainTopic, blogAuthor, blogDescription):
        try:
            logging.info("The given blog name is %s", str(blogName))
            if type(blogName) != str:
                raise (NotStringException("The given value is not of string type"))
            else:
                self.blogName = blogName
            logging.info("The given blog main topic is %s", str(blogMainTopic))
            if type(blogMainTopic) != str:
                raise (NotStringException("The given value is not of string type"))
            else:
                self.blogMainTopic = blogMainTopic
            logging.info("The given blog author is %s", str(blogAuthor))
            if type(blogAuthor) != str:
                raise (NotStringException("The given value is not of string type"))
            else:
                self.blogAuthor = blogAuthor
            logging.info("The given blog description is %s", str(blogDescription))
            if type(blogDescription) != str:
                raise (NotStringException("The given value is not of string type"))
            else:
                self.blogDescription = blogDescription
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))
            self.blogName = ""
            self.blogMainTopic = ""
            self.blogAuthor = ""
            self.blogDescription = ""

    def getBlogDetails(self):
        print("The Blog Name is: ", self.blogName)
        print("The Blog Main Topic is: ", self.blogMainTopic)
        print("The Blog Author is: ", self.blogAuthor)
        print("The Blog Description is: ", self.blogDescription)


# Example-7 on student contact Information
class StudentContactInformation:
    _studentMailId = ""
    __studentPhoneNumber = 0

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
                self._studentMailId = email
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))
            self._studentMailId = ""

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
                self.__studentPhoneNumber = phno
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))
            self.__studentPhoneNumber = ""

    def getStudentEmailId(self):
        """
        :return: Prints Student Email ID
        """
        print("The Student's Email ID is: ", self._studentMailId)

    def getStudentPhoneNumber(self):
        """
        :return: Prints Student Phone Number
        """
        print("The Student's Phone Number is: ", self.__studentPhoneNumber)


# Example-8 on internship Details
class Internship:
    projectName = ""
    internshipDescription = ""

    def __init__(self, projectName, internshipDescription):
        """
        :param projectName: The Internship project name
        :param internshipDescription: The Internship description
        """
        try:
            logging.info("The given Project Name is %s", str(projectName))
            if type(projectName) != str:
                raise (NotStringException("The given value is not of string type"))
            else:
                self.projectName = projectName
            logging.info("The given Internship Description is %s", str(internshipDescription))
            if type(internshipDescription) != str:
                raise (NotStringException("The given value is not of string type"))
            else:
                self.internshipDescription = internshipDescription

        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))
            self.projectName = ""
            self.internshipDescription = ""


inp = Internship("Forcasting Weather", "We have to forecast the weather of a region")
print(inp.projectName)
print(inp.internshipDescription)


# Example-9 on jobs
class Jobs:
    companyName = ""
    companyJobDescription = ""
    _salaryRange = range(0, 1)

    def setCompanyName(self, cname):
        """
        :param cname: It is the company's name
        :return: No Return
        """
        try:
            logging.info("The given company's name is %s", cname)
            if type(cname) != str:
                raise (NotStringException("The given value is not of string type"))
            else:
                self.companyName = cname
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))
            self.companyName = ""

    def setCompanyJobDescription(self, jobdesc):
        """
        :param jobdesc: It is the company's job description
        :return: No Return
        """
        try:
            logging.info("The given company's description is %s", jobdesc)
            if type(jobdesc) != str:
                raise (NotStringException("The given value is not of string type"))
            else:
                self.companyJobDescription = jobdesc
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))
            self.companyJobDescription = ""

    def setSalaryRange(self, saldet):
        """
        :param saldet: The company's salary details
        :return: No Return
        """
        try:
            logging.info("The given email id is %s", saldet)
            if type(saldet) != range:
                raise (NotRangeClassException("The given value is not of range class type"))
            else:
                self._salaryRange = saldet
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))
            self._salaryRange = range(0, 1)

    def getJobDetails(self):
        """
        :return: Prints company's job details
        """
        print("The Company's name is: ", self.companyName)
        print("The Company's Job Description is: ", self.companyJobDescription)
        print("The Company's Salary Details is: ", self._salaryRange)


# Example-10 on Ineuron Testimonials
class IneuronTestimonials:
    studentName = ""
    studentTestimonial = ""
    jobRole = ""
    LinkedInId = ""

    def __init__(self, studentName, studentTestimonial, jobRole, LinkedInId):
        """
        :param studentName: Name of the student
        :param studentTestimonial: The Appreciation given by the student to Ineuron in career transition
        :param jobRole: The job secured by the student
        :param LinkedInId: The LinkedIn profile Id for contact
        """
        try:
            logging.info("The given student Name is %s", str(studentName))
            if type(studentName) != str:
                raise (NotStringException("The given value is not of string type"))
            else:
                self.studentName = studentName
            logging.info("The given student Testimonial is %s", str(studentTestimonial))
            if type(studentTestimonial) != str:
                raise (NotStringException("The given value is not of string type"))
            else:
                self.studentTestimonial = studentTestimonial
            logging.info("The given student job role is %s", str(jobRole))
            if type(jobRole) != str:
                raise (NotStringException("The given value is not of string type"))
            else:
                self.jobRole = jobRole
            logging.info("The given student LinkedIn profile ID is %s", str(LinkedInId))
            if type(LinkedInId) != str:
                raise (NotStringException("The given value is not of string type"))
            else:
                self.LinkedInId = LinkedInId
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))
            self.studentName = ""
            self.studentTestimonial = ""
            self.jobRole = ""
            self.LinkedInId = ""
