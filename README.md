# tensile-multiplication

In quantum computing we need to do multiplications of different size arrays (2x2)*(4x4) in which every single element of first array is multiplied with each element of second array, and the result is putted in the corresponding position on third array which has dimensions the (rows1*rows2, columns1*columns2)
For example:
[

 
{1, 2   *   { 1, 2, 3    =   { 1, 2, 3, 2, 4, 6
3, 4}        4, 5, 6          4, 5, 6, 8, 10, 12           
             7, 8, 9}         7, 8, 9, 14, 16, 18
                              
                              3, 6, 9, 4, 8, 12
                              
                              12, 15, 18, 16, 20, 24
                              
                              21, 24, 27, 28, 32, 36}
]

Basically is not that kind of multiplication for quantum computing as we are dealing only with zeros and ones, so the arrays containg only 0,1
but the concept is the same
