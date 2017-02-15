x = raw_input("Pata ena plhktro kai meta enter gia na emfanistoun oi arithmoi Harshad mexri to 1000: ")
if x != '':
 harshad = []
 for n in range(1,1001):
  s_digits = list(str(n))
  dsum = 0
  for s_digit in s_digits:
   dsum += int(s_digit)
  if n % dsum == 0:
   harshad.append(n)
 print harshad
y = raw_input("Pata ena plhktro kai meta enter gia na emfanistoun oi arithmoi mexri to 1000 pou diairountai apo to ginomeno twn pshfiwn tous: ")
if y !='':
 harshad_gin = []
 for h in range(1,1001):
  h_digits = list(str(h))
  dgin = 1
  for h_digit in h_digits:
   dgin = dgin*int(h_digit)
  if dgin != 0 :
   if h % dgin == 0 :
    harshad_gin.append(h)
 print harshad_gin

    