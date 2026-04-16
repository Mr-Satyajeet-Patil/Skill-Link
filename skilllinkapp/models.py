from django.db import models

class company(models.Model):
    companyname = models.CharField(max_length=100)
    email= models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    industrytype= models.CharField(max_length=100)
    contact = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    
    def __str__(self):
        return self.companyname
    
class freelancer(models.Model):
    name = models.CharField(max_length=100)
    email= models.EmailField()
    password = models.CharField(max_length=100)
    skills= models.CharField(max_length=200)
    contact = models.CharField(max_length=20)
    category = models.CharField(max_length=100)
    rating = models.FloatField(default=0.0)
    count= models.IntegerField(default=0)
    education = models.CharField(max_length=200)
    
    
    def __str__(self):
        return self.name

class freelancerexperience(models.Model):
    freelancername = models.ForeignKey(freelancer, on_delete=models.CASCADE)
    companyname = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    projecthandled= models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    
    
    def __str__(self):
        return self.freelancername.name + " - " + self.companyname
    
class project(models.Model):
    companyname = models.ForeignKey(company, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    requiredskills = models.CharField(max_length=200)
    budget = models.FloatField()
    duration = models.TextField()
    postedat= models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class bid(models.Model):
    projectname = models.ForeignKey(project, on_delete=models.CASCADE)
    freelancername = models.ForeignKey(freelancer, on_delete=models.CASCADE)
    bidamount = models.FloatField()
    duration= models.CharField(max_length=100)
    biddate= models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.freelancername.name + " - " + self.projectname.title
    
class allotment(models.Model):
    projectname = models.ForeignKey(project, on_delete=models.CASCADE)
    freelancername = models.ForeignKey(freelancer, on_delete=models.CASCADE)
    companyname = models.ForeignKey(company, on_delete=models.CASCADE)
    startdate= models.DateTimeField(auto_now_add=True) #
    allotdate= models.DateTimeField(auto_now_add=True) #
    status = models.CharField(max_length=100)
    rating = models.FloatField()
    
    def __str__(self):
        return self.freelancername.name + " - " + self.projectname.title + " - " + self.companyname.companyname
    
class enquiry(models.Model):
    name = models.CharField(max_length=100)
    email= models.EmailField()
    mobile = models.CharField(max_length=20)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.name} - {self.email}"
    
    
class feedback(models.Model):
    name = models.CharField(max_length=100)
    email= models.EmailField()
    companyname = models.CharField(max_length=100)
    rating = models.FloatField()
    comment = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name + " - " + self.email
    
class projectcategory(models.Model):
    categoryname = models.CharField(max_length=100)
    
    def __str__(self):
        return self.categoryname
    
class questionnaire(models.Model):
    questionid = models.AutoField(primary_key=True) ##
    categoryname = models.CharField(max_length=100)
    question = models.CharField(max_length=200)
    option1= models.CharField(max_length=100)
    option2= models.CharField(max_length=100)
    option3= models.CharField(max_length=100)
    option4= models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    
    def __str__(self):
        return self.categoryname + " - " + self.question
    
class quizresult(models.Model):
    questionid = models.ForeignKey(questionnaire, on_delete=models.CASCADE) ###
    freelancername = models.ForeignKey(freelancer, on_delete=models.CASCADE)
    categoryname = models.CharField(max_length=100)
    score = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.freelancername.name + " - " + self.categoryname
    
class notification(models.Model):
    freelancername = models.ForeignKey(freelancer, on_delete=models.CASCADE) ##
    companyname = models.ForeignKey(company, on_delete=models.CASCADE) ##
    projectname = models.ForeignKey(project, on_delete=models.CASCADE) ##
    message = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.freelancername.name + " - " + self.projectname.title + " - " + self.companyname.companyname
    
class paymentfreelancer(models.Model):
    freelancername = models.ForeignKey(freelancer, on_delete=models.CASCADE) ##
    upi_id = models.CharField(max_length=100)
    bankname = models.CharField(max_length=100)
    accountnumber = models.CharField(max_length=20)
    ifsc = models.CharField(max_length=20)
    mode= models.CharField(max_length=100)
    image= models.ImageField()
    upiform= models.CharField(max_length=50)
    
    def __str__(self):
        return self.freelancername.name + " - " + self.projectname.title + " - " + self.companyname.companyname
    
class paymentcompany(models.Model):
    freelancername = models.ForeignKey(freelancer, on_delete=models.CASCADE) ##
    projectname = models.ForeignKey(project, on_delete=models.CASCADE) ##
    amount = models.FloatField()
    commission = models.FloatField()
    paymentdate = models.DateTimeField(auto_now_add=True)
    paymentmode = models.CharField(max_length=100)    

    def __str__(self):
        return self.freelancername.name + " - " + self.projectname.title   



                             