#!/usr/bin/env python
# coding: utf-8

# #question number 2?
# Part(a)
# T(n)=T(n-1)+c---------1
# T(n-1)= T ( n-2 )+2c
# T(n)=T(n-2)+2c----------2
# T(n)=T(n-3)+3c --------3
# .
# K times                       n-k=1   , k=n-1
# T(n)=T(n-k)+k.c
# T(n)=T(n-(n-1)) n-1.c
# T(n)=T(1) + n-1,c
# T(n)=1 + n.c
# T(n)+O(n)    linear time complexity
# 

# Part(d)
# T(n)=t(n/2)+c
# +
# T(n/2)=T(n/4)+2c
# T(n)=T(n/22)+2c---------2                       n/2k=1,n=2k
# T(n)=T(n/23)+3c --------3             Take log on both sides
# K times                                  Log2n=klog22,log2n=k
# T(n)=T(n/2k)+k
# T(n)=T(n/2log2n)+log2n.c
# T(n)=a.c.log2n
# T(n)=O(log2n)

# Part(b)
# T(n)=2T(n/2)+n  --------1
# T(n/2)=2T(n/4)+n/2------2
# T(n/4)=2T(n/8)+n/4 -------3
#               =2[(2T(n/4)+n/2]+n
#       =2^2 T(n/2^2)+2n
# 
#                   
#     =2^2T(n/4)+2n
# Now put the value of t(n/4) in above equation
# 2^2[2T(n/8)+n/4]+2n
# 2^3T(n/2^3)+3n
# 2^4 T (n/2^4) + 4n
# .
# .
# K times
# 2^k T(n/2^k)+k.n ------------- k equation
# Take n/2^k = 1 ,therefore n=2^k
# Take log on both sides
# Log n = log2 2^k
# Log n=k
# Equation k will become
# 2^k T(1)+k.n
# n + n.logn
# T(n)=O(nlogn)   this has a logarithmic time complexity

# Part(c)
# T(n)=T(n/2)+c------1       						
# T(n/2)=T(n/4)+2c 								n/2k=1 -> n=2k
# T(n)=T(n/4)+2c----------2 						Take log on both sides
# T(n)=T(n/23) + 3c --------3							 Log n=log 22k
# K times							Log2n=klog22  ->Log2n=k			
# T(n)=T(n/2k) + k.c      
# T(n)=T(n/2log2n) + log 2n.c
# T(n)=a.c.log2n
# T(n)=O(log2n)

# # question number 3
# # part (a)
# T(n) = 2 T(n-1) + 1
#        T(n)
#       /    \
#    T(n-1)  T(n-1)
#     /  \    /  \
#  T(n-2) T(n-2) T(n-2) ...
#    / \   / \   / \
# ...   T(1) T(1)   T(1)
# 1+2+22+23=--------+2k+2k+1-1                   A+ar+ar2+ar3+-----+ark=a(ark+1—1)/r-1
# A=1,r=2 =1(2k+1-1)/2-1   ->2k+1-1
# Assume n-k=0   ->n=k
# =>2k+1-1
# =>2n+1-1      =>O(n2)

# #question number 3
# Part(b)
# T(n) = 2T(n/2) +n                            
#        T(n)-------n
#       /    \
#    T(n/2)  T(n/2)-------n
#     /  \    /  \
#  T(n/4) T(n/4) T(n/4) ...------n
#    / \   / \   / \
# ...   T(1) T(1)   T(1)
# n*k
# assume n/2k=1
# n=2k
# log n =k
# O(nlogn) time complexity is logrithmic

#  # question number 1?
# 
# 
# We have a recurrence relation given by T(n)=3T(n−1)+12n with an initial condition T(0)=5. 
# T(0)=5
# our starting point.
# T(1)=3T(0)+12⋅1
# Substitute T(0) into the recurrence relation: 
# T(1)=3⋅5+12⋅1=15+12=27
# Now, we know that T(1)=27.
# T(2)=3T(1)+12⋅2
# Substitute T(1) into the recurrence relation: 
# T(2)=3⋅27+12⋅2=81+24=105
# Now, we know that T(2)=105.
