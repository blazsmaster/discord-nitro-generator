# import
import random
import string
import time
import sys 

# open output file
f = open('output.txt', 'a')

# write to console
print('How many Nitro codes would you like?')

# write to console
print ('')

# wait
time.sleep(1)

# amount of codes
amount = int(

    # write to console
    input("Number of codes: ")
)

# write to console
print ('')

# wait
time.sleep(1)

# write to console
print ('Generating...')

# wait
time.sleep(1)

# write to console
print ('')

# amount
fix = 1

# generator
while fix <= amount:

    # create code
    code = ('').join(random.choices(string.ascii_letters + string.digits, k=16))

    # discord url
    discord_url = "https://discord.gift/"

    # write to file
    f.write(discord_url + code + '\n')

    # code output
    discord_code = discord_url + code

    # write to console
    print(discord_code)


    # amount +1
    fix += 1

# wait
time.sleep(2)

# write to console
print ('')
