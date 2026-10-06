n_m_str = input()
nums = n_m_str.split('-')
n = int(nums[0])
m = int(nums[1])

if(n == 0):
    print(False)
elif m % n == 0:
    print(True)
else:
    print(False)
