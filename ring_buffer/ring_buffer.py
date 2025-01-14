#example 1-----------------------------------------------------------http://code.activestate.com/recipes/68429-ring-buffer/
# class RingBuffer:
# 	def __init__(self,size_max):
# 		self.max = size_max
# 		self.data = []
# 	def append(self,x):
# 		"""append an element at the end of the buffer"""
# 		self.data.append(x)
# 		if len(self.data) == self.max:
# 			self.cur=0
# 			self.__class__ = RingBufferFull
# 	def get(self):
#   		""" return a list of elements from the oldest to the newest"""
# 		return self.data

# class RingBufferFull:
# 	def __init__(self,n):
# 		raise "you should use RingBuffer"
# 	def append(self,x):		
# 		self.data[self.cur]=x
# 		self.cur=(self.cur+1) % self.max
# 	def get(self):
# 		return self.data[self.cur:]+self.data[:self.cur]

# # sample of use
# x=RingBuffer(5)
# x.append(1); x.append(2); x.append(3); x.append(4)
# print x.__class__,x.get()
# x.append(5)
# print x.__class__,x.get()
# x.append(6)
# print x.data,x.get()
# x.append(7); x.append(8); x.append(9); x.append(10)
# print x.data,x.get()

# example 2----------------------------------------------------------------- https://www.oreilly.com/library/view/python-cookbook/0596001673/ch05s19.html
# class RingBuffer:
#     """ class that implements a not-yet-full buffer """
#     def _ _init_ _(self,size_max):
#         self.max = size_max
#         self.data = []

#     class _ _Full:
#         """ class that implements a full buffer """
#         def append(self, x):
#             """ Append an element overwriting the oldest one. """
#             self.data[self.cur] = x
#             self.cur = (self.cur+1) % self.max
#         def get(self):
#             """ return list of elements in correct order """
#             return self.data[self.cur:]+self.data[:self.cur]

#     def append(self,x):
#         """append an element at the end of the buffer"""
#         self.data.append(x)
#         if len(self.data) == self.max:
#             self.cur = 0
#             # Permanently change self's class from non-full to full
#             self._ _class_ _ = self._ _Full

#     def get(self):
#         """ Return a list of elements from the oldest to the newest. """
#         return self.data

# # sample usage
# if _ _name_ _=='_ _main_ _':
#     x=RingBuffer(5)
#     x.append(1); x.append(2); x.append(3); x.append(4)
#     print x._ _class_ _, x.get(  )
#     x.append(5)
#     print x._ _class_ _, x.get(  )
#     x.append(6)
#     print x.data, x.get(  )
#     x.append(7); x.append(8); x.append(9); x.append(10)
#     print x.data, x.get(  )



# #actual problem----------------------------------------------------------------
class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity
    #wanted to add a full state
    self.full = 0
    #and then i noticed the test uses length on self storage 
  def append(self, item):
    #storage becomes the current item and eventually the capacity
    #seeing the above examples I used it the same way 
    #  """ Append an element overwriting the oldest one. """
    # self.data[self.cur] = x
    # self.cur = (self.cur+1) % self.max
    self.storage[self.current] = item
    self.current += 1
    self.current %= self.capacity
    #depending on the state of being full or not, it will go with full or capacity
    self.full += 1 if self.full < self.capacity else self.capacity
  
  def get(self): 
    # there is always a state of full and what the capacity is and the get method needs to return the correct data
    if self.full < self.capacity:
      #atorage will match the fullness
      return self.storage[:self.full]
    else:
      #or just return itself
      return self.storage


# HOW TO GET RID OF THE NONE!?!?!??!
#   First list contains 1 additional elements.
# First extra element 4:
# None

# - ['a', 'b', 'c', 'd', None]
# ?                    ------

# + ['a', 'b', 'c', 'd']  