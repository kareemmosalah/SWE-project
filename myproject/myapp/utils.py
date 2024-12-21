from faker import Faker
import random 
def generate_fake_profits(num_owners=5): #to generate fake profits. 
   fake = Faker()
   data = [] #to store the data.
   for _ in range(num_owners):
       owner_email = fake.email() #to generate a fake email.
       profits = [random.randint(1000, 5000) for _ in range(12)]  #to generate fake profits.
       data.append({'email': owner_email, 'profits': profits}) #to append the data to the list. 
   return data