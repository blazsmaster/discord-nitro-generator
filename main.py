import random
import string
import time
import sys

f = open('code_chace.txt', 'a')

print('How many Nitro codes would you like?')
print ('')
print ('')
time.sleep(2)
amount = int(input("Number of codes:"))
print ('')
time.sleep(2.5)
print ('Generating...')
time.sleep(2.5)
print ('')

fix = 1
while fix <= amount:
    code = ('').join(random.choices(string.ascii_letters + string.digits, k=16))
    discord_url = "https://discord.gift/"
    f.write('https://discord.gift/' + code + '\n')
    discord_code = discord_url + code
    print(discord_code)
    fix += 1
time.sleep(2)
print ('')
