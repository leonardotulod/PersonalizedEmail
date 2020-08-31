#This is a personalized email generator for recruiting users to online job searching and networking sites. I used this code to increase efficiency of outreach at my internship. 
#I hope you enjoy it and put it to good use. 

RecruiterName = input("Please enter your name: ")
ApplicantName = input("Please enter the name of the person you are sending this email to: ")
CompanyName= input("Please enter the name of company that you represent: ")
CompanyFunction =input("Enter what your company specializes in: ")
JobFunction = input("Please enter what your role is in the company (ex: recruiter, intern): ")
ApplicantMajor= input("Please enter your applicant's major: ")
CompaniesMajor= input("Please enter great companies that use your platform and that would be in your applicant's interest: ")
urlpersonal= input("Please enter the URL that you would like your applicant to visit:")
print("Generating your automated personalized email......")
print()
print("Below is your personalized email:")
print()
print("<<Start of personal message>>")



print()
print("Dear {0},".format(ApplicantName))
print()
print("My name is {0}. I am a {3} from {1} and we are looking for talented individuals like yourself. {1} specializes in {2}. I see that you are a {4} major and recruiters from companies like {5} frequently use our site to find qualified applicants like yourself. If this sounds interesting, visit our website at {6} and make an account. Thank you for your time and I would love to have you as part of our {1} team.".format(RecruiterName, CompanyName,
      CompanyFunction, JobFunction,ApplicantMajor,CompaniesMajor,urlpersonal))
print()
print("Sincerely,")
print()
print(RecruiterName)

print()

print("<<End of personal message>>")


