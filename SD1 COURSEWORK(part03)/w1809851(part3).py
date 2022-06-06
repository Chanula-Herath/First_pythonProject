# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1809851
# Date: 11/11/2020

#Create variables
pass_credits=0
defer_credits=0
fail_credits=0
credit_range=(0,20,40,60,80,100,120)
progress_count=0
trailer_count=0
retriever_count=0
excluded_count=0
total_data=0

def histogram():    #horizontal histogram
    print("Progress  ",progress_count,":",progress_count*"*")
    print("Trailer   ",trailer_count,":",trailer_count*"*")
    print("Retriever ",retriever_count,":",retriever_count*"*")
    print("Exclued   ",excluded_count,":",excluded_count*"*")
    print("\n")
    print(total_data," outcomes in total.")
    
print("Staff Version with Histogram")
#Validations
while True:
    try:
        pass_credits =int(input("Please enter your credits at pass: ")) 
        if pass_credits not in credit_range:
            raise TypeError        
    except ValueError:
        print("Integer required\n")
    except TypeError:
        print("Out of range.\n")
    
    else:
        try:
            defer_credits =int(input("Please enter your credit at defer: "))
            if defer_credits not in credit_range:
                raise TypeError           
        except ValueError:
            print("Integer required\n")
        except TypeError:
            print("Out of range.\n")
            
        else:
            try:
                fail_credits =int(input("Please enter your credit at fail: ")) 
                if fail_credits not in credit_range:
                    raise TypeError
            except ValueError:
                print("Integer required\n")
            except TypeError:
                print("Out of range.\n")
            
            else:
                total_credits = pass_credits + defer_credits + fail_credits
                if total_credits!=120:
                    print("Total incorrect.\n")

                else:
                    #Conditional statements                    
                    if pass_credits==120:
                        print("Progress\n\n")
                        progress_count+=1
                        total_data+=1    
                    elif pass_credits==100:
                        print("Progress (module trailer)\n\n")
                        trailer_count+=1
                        total_data+=1
                    elif fail_credits>=80:
                        print("Exclude\n\n")
                        excluded_count+=1
                        total_data+=1
                    elif (pass_credits<=80)and(pass_credits>=0):
                        print("Do not Progress – module retriever\n\n")
                        retriever_count+=1
                        total_data+=1
                        
                    print("Would you like to enter another set of data?")
                    continue_quit=input("Enter 'y' for yes or 'q' to quit and view results: ")
                        
                    if continue_quit=="y":
                        print("\n")
                    #Quit and print vertical histogram
                    elif continue_quit=="q":
                        print("\n")
                        print("================================================================================")
                        print("Horizontal Histogram")
                        histogram() #horizontal histogram function callback
                        print("================================================================================")
                        break                     
                    else:
                        print("Invalid input\n")
                        break
                       
                        
    

                    

                    
