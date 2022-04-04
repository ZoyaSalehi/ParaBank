from faker import Faker

fake = Faker(locale=['en_CA', 'en_US'])

app = 'Para Bank'
para_url = 'https://parabank.parasoft.com/parabank/index.htm'
para_home_title = 'ParaBank | Welcome | Online Banking'
para_registraion_url = 'https://parabank.parasoft.com/parabank/register.htm;jsessionid='
para_registration_title = 'ParaBank | Register for Free Online Account Access'

first_name = fake.first_name()
last_name = fake.last_name()
full_name = f'{first_name} {last_name}'
address = fake.address().replace("\n", " ")
city = fake.city()
state = fake.state()
zip_code = fake.zipcode()
phonenum = fake.phone_number()
ssn = fake.ssn()

new_username = f'{fake.pyint(1, 90000)}zoya{fake.pyint(1, 90000)}'
new_password = fake.password()
email = fake.email()