



def index_bin_search(nums, x):
	top = len(nums) / 2
	bottom = 0
	while x != nums[top] and top != bottom: 
		if x < nums[top]:
			top = top / 2
		else: # x > nums[top]:
			temp = top
			top = top + (top - bottom) / 2
			bottom = temp
	if x == nums[top]:
		return top
	else: return None



if __name__ == "__main__":
	nums = range(-5, 10)
	y = 5
	print nums
	print "Looking for index of: ", y
	import datetime
	i = index_bin_search(nums, y)
        print y, "is at index", i 


