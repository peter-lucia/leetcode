class Solution:
    def trap(self, height: List[int]) -> int:
      # get two list
      # a[i]= max height left of i
      # b[i]= max height right of i
      # c[i]= min(a[i],b[i])-h[i]
      # return sum of c
      h=height.copy()
      mx=0
      a=[0]
      for i in range(1,len(h)):
        mx=max(mx,a[i-1],h[i-1])
        a.append(mx)
      mx = 0
      b =[0 for _ in range(len(h))]
      for j in range(len(h)-2,-1,-1):
        mx=max(mx,b[j+1],h[j+1])
        b[j]=mx
      c=[]
      for i in range(len(h)):
        c.append(max(
          min(a[i],b[i])-h[i],
          0
        ))
      return sum(c)


        