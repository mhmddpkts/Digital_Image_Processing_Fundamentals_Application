
"""
keskinlestirme*
ortanca+
kenar bul+
laplace*
bulanıklaştır*

"""

sharpen_filter = [[0,-1,0],
                  [-1,4,-1],
                  [0,-1,0]]


blur_filter = [[1/25,1/25,1/25,1/25,1/25],
               [1/25,1/25,1/25,1/25,1/25],
               [1/25,1/25,1/25,1/25,1/25],
               [1/25,1/25,1/25,1/25,1/25],
               [1/25,1/25,1/25,1/25,1/25]]

laplace_filter = [[-1,-1,-1],
                  [-1,8,-1],
                  [-1,-1,-1]]
