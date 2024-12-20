from faker import Faker
import random
def generate_fake_profits(num_owners=5):
   fake = Faker()
   data = []
   for _ in range(num_owners):
       owner_email = fake.email()
       profits = [random.randint(1000, 5000) for _ in range(12)]  
       data.append({'email': owner_email, 'profits': profits})
   return data