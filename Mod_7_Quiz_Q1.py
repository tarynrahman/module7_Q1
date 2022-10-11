#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Example 1
class Dog(): #here we create the class Dog
    def __init__(self, breed): #init - constructor for class called automatically
        self.breed = breed #self represents instance of object itself
my_dog = Dog(breed = 'Lab') #my_dog is the object
my_dog.breed #printing the breed of the dog - breed is an attribute


# In[24]:


#Example 2
class Course(): #define class - here it is Course
    
    def __init__(self,prof,level,title):
        self.prof = prof
        self.title = title
        self.level = level
    def assigned(self):
        print('I am {} for {} {}.' .format(self.prof,self.title, self.level))
my_course = Course('Dr.Rahman','200','Calc') #my_course is the object, and prof, level and title are the attributes 
                                            #associated with the course
                                            #here we use method 

my_course.assigned() 


# In[ ]:





# In[ ]:





# In[ ]:




