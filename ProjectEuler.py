
# #Q1: if we list all the natural numbers below 10 that are multiples of 3 or 5 , we get 3,5,6 and  9. The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.
# total_sum = 0

# for number in range(1000):
#     if number % 3 == 0 or number % 5 == 0:
#         total_sum += number

# print(total_sum)         






# '''Q2: Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,  
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.'''
# # # Initialize the first two terms of the Fibonacci sequence
# a, b = 1, 2

# # Variable to store the sum of even-valued terms
# sum_even = 0

# # Loop until the Fibonacci term exceeds 4 million
# while b <= 4000000:
#     # Check if the term is even
#     if b % 2 == 0:
#         sum_even += b
    
#     # Move to the next term in the sequence
#     a, b = b, a + b

# # Print the result
# print("Sum of even-valued Fibonacci terms below 4 million:", sum_even)






# #Q3: The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime factor of the number 600851475143 ?
# def largest_prime_factor(n):
#     a = 2

#     while a * a <= n:
#         if n % a:
#             a += 1

#         else:
#             n //= a

#     return 

# n = 600851475143
# print(largest_prime_factor(n))





# '''Q4: A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.'''
# def is_palindrome(number):
#     return str(number) == str(number)[::-1]

# def find_largest_palindrome():
#     largest_palindrome = 0

#     for i in range(100, 1000):
#         for j in range(i, 1000):
#             product = i * j

#             if is_palindrome(product):
#                 if product > largest_palindrome:
#                     largest_palindrome = product

#     return largest_palindrome

# result = find_largest_palindrome()
# print(f"The largest palindrome made from the product of two 3_digit numbers are : {result}")





# '''Q5: 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?'''
# import math

# def lcm(x, y):
#     return x * y // math.gcd(x, y)

# smallest_multiple = 1

# for i in range(1, 21):
#     smallest_multiple = lcm(smallest_multiple, i)

# print(smallest_multiple)







# '''Q6: The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 + ... + 10^2 = 385. The square of the sum of the first ten natural numbers is, (1 + 2 + ... + 10)^2 = 55^2 = 3025.
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.'''
# # Step 1: Pehle 100 numbers ke squares ka sum nikalna
# sum_of_squares = sum(i ** 2 for i in range(1, 101))

# # Step 2: Pehle 100 numbers ka sum nikalna
# sum_of_numbers = sum(i for i in range(1, 101))

# # Step 3: Ab is sum ka square nikalna
# square_of_sum = sum_of_numbers ** 2

# # Step 4: Dono ka farq nikalna
# difference = square_of_sum - sum_of_squares

# # Result print karna
# print(difference)




# # Q7: By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13. What is the 10,001st prime number?
# def is_prime(n):
#     if n <= 1:
#         return False
        
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
    
# count = 0
# num = 2

# while True:
#     if is_prime(num):
#         count += 1
        
#         if count == 10001:
#             print(num)
#             break
            
#     num += 1
    

# '''Q8: The four adjacent digits in the 1000-digit number that have the greatest product are 9 x 9 x 8 x 9 = 5832.
# 73167176531330624919225119674426574742355349194934
# 96983520312774506326239578318016984801869478851843
# 85861560789112949495459501737958331952853208805511
# 12540698747158523863050715693290963295227443043557
# 66896648950445244523161731856403098711121722383113
# 62229893423380308135336276614282806444486645238749
# 30358907296290491560440772390713810515859307960866
# 70172427121883998797908792274921901699720888093776
# 65727333001053367881220235421809751254540594752243
# 52584907711670556013604839586446706324415722155397
# 53697817977846174064955149290862569321978468622482
# 83972241375657056057490261407972968652414535100474
# 82166370484403199890008895243450658541227588666881
# 16427171479924442928230863465674813919123162824586
# 17866458359124566529476545682848912883142607690042
# 24219022671055626321111109370544217506941658960408
# 07198403850962455444362981230987879927244284909188
# 84580156166097919133875499200524063689912560717606
# 05886116467109405077541002256983155200055935729725
# 71636269561882670428252483600823257530420752963450
# Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?'''
#ANSWER:
# number = (
#     "73167176531330624919225119674426574742355349194934"
#     "96983520312774506326239578318016984801869478851843"
#     "85861560789112949495459501737958331952853208805511"
#     "12540698747158523863050715693290963295227443043557"
#     "66896648950445244523161731856403098711121722383113"
#     "62229893423380308135336276614282806444486645238749"
#     "30358907296290491560440772390713810515859307960866"
#     "70172427121883998797908792274921901699720888093776"
#     "65727333001053367881220235421809751254540594752243"
#     "52584907711670556013604839586446706324415722155397"
#     "53697817977846174064955149290862569321978468622482"
#     "83972241375657056057490261407972968652414535100474"
#     "82166370484403199890008895243450658541227588666881"
#     "16427171479924442928230863465674813919123162824586"
#     "17866458359124566529476545682848912883142607690042"
#     "24219022671055626321111109370544217506941658960408"
#     "07198403850962455444362981230987879927244284909188"
#     "84580156166097919133875499200524063689912560717606"
#     "05886116467109405077541002256983155200055935729725"
#     "71636269561882670428252483600823257530420752963450"
# )

# max_product = 0
# max_digits = ""

# # Hum total number of digits mein se 13 digits ke group ka product calculate karenge.
# for i in range(len(number) - 12):
#     product = 1
#     digits = number[i:i + 13]  # Ye line 13 digits ko ek group mein store kar rahi hai.

#     for digit in digits:
#         product *= int(digit)  # Ye line har digit ko multiply kar rahi hai.

#     if product > max_product:  # Agar current product maximum se zyada hai to use update karo.
#         max_product = product
#         max_digits = digits

# print(f"The 13 digits with the greatest product: {max_digits}")
# print(f"Their product: {max_product}")



'''Q9: A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = c^2. For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2. 
There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.'''
# for a in range(1, 1000):
#     for b in range(a + 1, 1000 - a):
#         c = 1000 - a - b
        
#         if a**2 + b**2 == c**2:
#             print(f"Triplet found: a={a}, b={b}, c={c}")
#             print(f"Product abc = {a * b * c}")
            
#             break
        
#     else:
#         continue
        
#     break



#Q10: The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17. Find the sum of all the primes below two million.
# def is_prime(n):
#     if n <= 1:
#         return False
    
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
        
#     return True

# total_sum = 0
# for num in range(2, 2000000):
#     if is_prime(num):
#         total_sum += num
        
# print(total_sum)



# '''Q11: In the 20 x 20 grid below, four numbers along a diagonal line have been marked in red.
# 08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
# 49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
# 81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
# 52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
# 22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
# 24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
# 32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
# 67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
# 24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
# 21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
# 78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
# 16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
# 86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
# 19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
# 04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
# 88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
# 04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
# 20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
# 20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
# 01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48
# The product of these numbers is 26 x 63 x 78 x 14 = 1788696 .What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20 x 20 grid?'''
# #ANSWER:

# def greatest_product(grid):
#     max_product = 0
#     num_rows = len(grid)
#     num_cols = len(grid[0])
    
#     # Calculate horizontal and vertical products
#     for row in range(num_rows):
#         for col in range(num_cols - 3):
#             # Horizontal product
#             horizontal_product = grid[row][col] * grid[row][col + 1] * grid[row][col + 2] * grid[row][col + 3]
#             max_product = max(max_product, horizontal_product)
            
#             # Vertical product (ensure enough rows below)
#             if row <= num_rows - 4:
#                 vertical_product = grid[row][col] * grid[row + 1][col] * grid[row + 2][col] * grid[row + 3][col]
#                 max_product = max(max_product, vertical_product)
    
#     # Calculate diagonal products (top-left to bottom-right)
#     for row in range(num_rows - 3):
#         for col in range(num_cols - 3):
#             diagonal1_product = grid[row][col] * grid[row + 1][col + 1] * grid[row + 2][col + 2] * grid[row + 3][col + 3]
#             max_product = max(max_product, diagonal1_product)
    
#     # Calculate diagonal products (top-right to bottom-left)
#     for row in range(num_rows - 3):
#         for col in range(3, num_cols):
#             diagonal2_product = grid[row][col] * grid[row + 1][col - 1] * grid[row + 2][col - 2] * grid[row + 3][col - 3]
#             max_product = max(max_product, diagonal2_product)
    
#     return max_product

# grid = [
#     [8, 2, 22, 97, 38, 15, 0, 40, 0, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8],
#     [49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 0],
#     [81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65],
#     [52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91],
#     [22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80],
#     [24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50],
#     [32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70],
#     [67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21],
#     [24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72],
#     [21, 36, 23, 9, 75, 0, 76, 44, 20, 45, 35, 14, 0, 61, 33, 97, 34, 31, 33, 95],
#     [78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92],
#     [16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 0, 17, 54, 24, 36, 29, 85, 57],
#     [86, 56, 0, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58],
#     [19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40],
#     [4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66],
#     [88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69],
#     [4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36],
#     [20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16],
#     [20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54],
#     [1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48]
# ]

# print(greatest_product(grid))




# '''Q12: The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55....
# Let us list the factors of the first seven triangle numbers:
#             1 : 1
#             3 : 1 , 3
#             6 : 1 , 2 , 3 , 6
#            10 : 1 , 2 , 5 , 10
#            15 : 1 , 3 , 5 , 15
#            21 : 1 , 3 , 7 , 21
#            28 : 1 , 2 , 4 , 7 , 14 , 28
# We can see that 28 is the first triangle number to have over five divisors.
# What is the value of the first triangle number to have over five hundred divisors?'''
# def numbers_of_divisors(n):
#     count = 0
    
#     for i in range(1, int(n**0.5) + 1):
#         if n % i == 0:
#             if i * i == 0:
#                 count += 1
#             else:
#                 count += 2
                
#     return count

# def find_triangle_numbers_with_divisors(limit):
#     triangle_number  = 0
#     i =  1
    
#     while True:
#         triangle_number += i
        
#         if numbers_of_divisors(triangle_number) > limit:
#             return triangle_number
        
#         i += 1
        
# result = find_triangle_numbers_with_divisors(500)
# print(result)


# '''Q13: Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
# 37107287533902102798797998220837590246510135740250
# 46376937677490009712648124896970078050417018260538
# 74324986199524741059474233309513058123726617309629
# 91942213363574161572522430563301811072406154908250
# 23067588207539346171171980310421047513778063246676
# 89261670696623633820136378418383684178734361726757
# 28112879812849979408065481931592621691275889832738
# 44274228917432520321923589422876796487670272189318
# 47451445736001306439091167216856844588711603153276
# 70386486105843025439939619828917593665686757934951
# 62176457141856560629502157223196586755079324193331
# 64906352462741904929101432445813822663347944758178
# 92575867718337217661963751590579239728245598838407
# 58203565325359399008402633568948830189458628227828
# 80181199384826282014278194139940567587151170094390
# 35398664372827112653829987240784473053190104293586
# 86515506006295864861532075273371959191420517255829
# 71693888707715466499115593487603532921714970056938
# 54370070576826684624621495650076471787294438377604
# 53282654108756828443191190634694037855217779295145
# 36123272525000296071075082563815656710885258350721
# 45876576172410976447339110607218265236877223636045
# 17423706905851860660448207621209813287860733969412
# 81142660418086830619328460811191061556940512689692
# 51934325451728388641918047049293215058642563049483
# 62467221648435076201727918039944693004732956340691
# 15732444386908125794514089057706229429197107928209
# 55037687525678773091862540744969844508330393682126
# 18336384825330154686196124348767681297534375946515
# 80386287592878490201521685554828717201219257766954
# 78182833757993103614740356856449095527097864797581
# 16726320100436897842553539920931837441497806860984
# 48403098129077791799088218795327364475675590848030
# 87086987551392711854517078544161852424320693150332
# 59959406895756536782107074926966537676326235447210
# 69793950679652694742597709739166693763042633987085
# 41052684708299085211399427365734116182760315001271
# 65378607361501080857009149939512557028198746004375
# 35829035317434717326932123578154982629742552737307
# 94953759765105305946966067683156574377167401875275
# 88902802571733229619176668713819931811048770190271
# 25267680276078003013678680992525463401061632866526
# 36270218540497705585629946580636237993140746255962
# 24074486908231174977792365466257246923322810917141
# 91430288197103288597806669760892938638285025333403
# 34413065578016127815921815005561868836468420090470
# 23053081172816430487623791969842487255036638784583
# 11487696932154902810424020138335124462181441773470
# 63783299490636259666498587618221225225512486764533
# 67720186971698544312419572409913959008952310058822
# 95548255300263520781532296796249481641953868218774
# 76085327132285723110424803456124867697064507995236
# 37774242535411291684276865538926205024910326572967
# 23701913275725675285653248258265463092207058596522
# 29798860272258331913126375147341994889534765745501
# 18495701454879288984856827726077713721403798879715
# 38298203783031473527721580348144513491373226651381
# 34829543829199918180278916522431027392251122869539
# 40957953066405232632538044100059654939159879593635
# 29746152185502371307642255121183693803580388584903
# 41698116222072977186158236678424689157993532961922
# 62467957194401269043877107275048102390895523597457
# 23189706772547915061505504953922979530901129967519
# 86188088225875314529584099251203829009407770775672
# 11306739708304724483816533873502340845647058077308
# 82959174767140363198008187129011875491310547126581
# 97623331044818386269515456334926366572897563400500
# 42846280183517070527831839425882145521227251250327
# 55121603546981200581762165212827652751691296897789
# 32238195734329339946437501907836945765883352399886
# 75506164965184775180738168837861091527357929701337
# 62177842752192623401942399639168044983993173312731
# 32924185707147349566916674687634660915035914677504
# 99518671430235219628894890102423325116913619626622
# 73267460800591547471830798392868535206946944540724
# 76841822524674417161514036427982273348055556214818
# 97142617910342598647204516893989422179826088076852
# 87783646182799346313767754307809363333018982642090
# 10848802521674670883215120185883543223812876952786
# 71329612474782464538636993009049310363619763878039
# 62184073572399794223406235393808339651327408011116
# 66627891981488087797941876876144230030984490851411
# 60661826293682836764744779239180335110989069790714
# 85786944089552990653640447425576083659976645795096
# 66024396409905389607120198219976047599490197230297
# 64913982680032973156037120041377903785566085089252
# 16730939319872750275468906903707539413042652315011
# 94809377245048795150954100921645863754710598436791
# 78639167021187492431995700641917969777599028300699
# 15368713711936614952811305876380278410754449733078
# 40789923115535562561142322423255033685442488917353
# 44889911501440648020369068063960672322193204149535
# 41503128880339536053299340368006977710650566631954
# 81234880673210146739058568557934581403627822703280
# 82616570773948327592232845941706525094512325230608
# 22918802058777319719839450180888072429661980811197
# 77158542502016545090413245809786882778948721859617
# 72107838435069186155435662884062257473692284509516
# 20849603980134001723930671666823555245252804609722
# 53503534226472524250874054075591789781264330331690'''
# # ANSWER
# numbers_str = """
# 37107287533902102798797998220837590246510135740250
# 46376937677490009712648124896970078050417018260538
# 74324986199524741059474233309513058123726617309629
# 91942213363574161572522430563301811072406154908250
# 23067588207539346171171980310421047513778063246676
# 89261670696623633820136378418383684178734361726757
# 28112879812849979408065481931592621691275889832738
# 44274228917432520321923589422876796487670272189318
# 47451445736001306439091167216856844588711603153276
# 70386486105843025439939619828917593665686757934951
# 62176457141856560629502157223196586755079324193331
# 64906352462741904929101432445813822663347944758178
# 92575867718337217661963751590579239728245598838407
# 58203565325359399008402633568948830189458628227828
# 80181199384826282014278194139940567587151170094390
# 35398664372827112653829987240784473053190104293586
# 86515506006295864861532075273371959191420517255829
# 71693888707715466499115593487603532921714970056938
# 54370070576826684624621495650076471787294438377604
# 53282654108756828443191190634694037855217779295145
# 36123272525000296071075082563815656710885258350721
# 45876576172410976447339110607218265236877223636045
# 17423706905851860660448207621209813287860733969412
# 81142660418086830619328460811191061556940512689692
# 51934325451728388641918047049293215058642563049483
# 62467221648435076201727918039944693004732956340691
# 15732444386908125794514089057706229429197107928209
# 55037687525678773091862540744969844508330393682126
# 18336384825330154686196124348767681297534375946515
# 80386287592878490201521685554828717201219257766954
# 78182833757993103614740356856449095527097864797581
# 16726320100436897842553539920931837441497806860984
# 48403098129077791799088218795327364475675590848030
# 87086987551392711854517078544161852424320693150332
# 59959406895756536782107074926966537676326235447210
# 69793950679652694742597709739166693763042633987085
# 41052684708299085211399427365734116182760315001271
# 65378607361501080857009149939512557028198746004375
# 35829035317434717326932123578154982629742552737307
# 94953759765105305946966067683156574377167401875275
# 88902802571733229619176668713819931811048770190271
# 25267680276078003013678680992525463401061632866526
# 36270218540497705585629946580636237993140746255962
# 24074486908231174977792365466257246923322810917141
# 91430288197103288597806669760892938638285025333403
# 34413065578016127815921815005561868836468420090470
# 23053081172816430487623791969842487255036638784583
# 11487696932154902810424020138335124462181441773470
# 63783299490636259666498587618221225225512486764533
# 67720186971698544312419572409913959008952310058822
# 95548255300263520781532296796249481641953868218774
# 76085327132285723110424803456124867697064507995236
# 37774242535411291684276865538926205024910326572967
# 23701913275725675285653248258265463092207058596522
# 29798860272258331913126375147341994889534765745501
# 18495701454879288984856827726077713721403798879715
# 38298203783031473527721580348144513491373226651381
# 34829543829199918180278916522431027392251122869539
# 40957953066405232632538044100059654939159879593635
# 29746152185502371307642255121183693803580388584903
# 41698116222072977186158236678424689157993532961922
# 62467957194401269043877107275048102390895523597457
# 23189706772547915061505504953922979530901129967519
# 86188088225875314529584099251203829009407770775672
# 11306739708304724483816533873502340845647058077308
# 82959174767140363198008187129011875491310547126581
# 97623331044818386269515456334926366572897563400500
# 42846280183517070527831839425882145521227251250327
# 55121603546981200581762165212827652751691296897789
# 32238195734329339946437501907836945765883352399886
# 75506164965184775180738168837861091527357929701337
# 62177842752192623401942399639168044983993173312731
# 32924185707147349566916674687634660915035914677504
# 99518671430235219628894890102423325116913619626622
# 73267460800591547471830798392868535206946944540724
# 76841822524674417161514036427982273348055556214818
# 97142617910342598647204516893989422179826088076852
# 87783646182799346313767754307809363333018982642090
# 10848802521674670883215120185883543223812876952786
# 71329612474782464538636993009049310363619763878039
# 62184073572399794223406235393808339651327408011116
# 66627891981488087797941876876144230030984490851411
# 60661826293682836764744779239180335110989069790714
# 85786944089552990653640447425576083659976645795096
# 66024396409905389607120198219976047599490197230297
# 64913982680032973156037120041377903785566085089252
# 16730939319872750275468906903707539413042652315011
# 94809377245048795150954100921645863754710598436791
# 78639167021187492431995700641917969777599028300699
# 15368713711936614952811305876380278410754449733078
# 40789923115535562561142322423255033685442488917353
# 44889911501440648020369068063960672322193204149535
# 41503128880339536053299340368006977710650566631954
# 81234880673210146739058568557934581403627822703280
# 82616570773948327592232845941706525094512325230608
# 22918802058777319719839450180888072429661980811197
# 77158542502016545090413245809786882778948721859617
# 72107838435069186155435662884062257473692284509516
# 20849603980134001723930671666823555245252804609722
# 53503534226472524250874054075591789781264330331690
# """
# numbers = numbers_str.split()
# total_sum = sum(int(number) for number in numbers)
# first_ten_digits = str(total_sum)[:10]
# print(first_ten_digits)




# '''Q14: The following iterative sequence is defined for the set of positive integers:
#             n --> n/2(n is even)
#             n --> n/3 + 1(n is odd)
# Using the rule above and starting with 13, we generate the following sequence:
#             13 --> 40 --> 20 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1.
# It can be seen that this sequence (starting at 13and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem),
# it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?
# NOTE: Once the chain starts the terms are allowed to go above one million.'''

# def sequence_length(n):
#     length = 1
    
#     while n != 1:
#         if n % 2 == 0:
#             n = n // 2
#         else:
#             n =(n * 3) + 1
            
#         length += 1
        
#     return length

# starting_number = 0
# max_length = 0

# for i in range(1, 1000000):
#     current_length = sequence_length(i)
    
#     if current_length > max_length:
#         max_length = current_length
#         starting_number = i
        
# print("Longest chain starts with", starting_number, "with a length of", max_length)






#Q15: Starting in the top left corner of a 2 x 2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20 x 20 grid?
