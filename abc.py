import time
import datetime

print('Fist hello')
print(f'Time is : {datetime.datetime.now()}')
t1 = time.time()

time.sleep(3)


print('Hello again!')
t2 = time.time()
print(f"""And now time is {datetime.datetime.now()},
it takes {t2-t1} during two 'hello'""")


