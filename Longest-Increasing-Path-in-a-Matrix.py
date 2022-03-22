{\rtf1\ansi\ansicpg1252\cocoartf2636
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 class Solution:\
    def __init__ ( self ) :\
        self.ans = []\
        \
    def increasingPath ( self , matrix , a , b ) :\
        size = len ( matrix [ 0 ] )\
        key = matrix [ a ] [ b ]\
        path = [ key ]\
        #print ( "key : ", key , "---------------")\
        while True :\
            #print ( "path : ", path )\
            if a+1 != size : \
                if matrix [ a+1 ] [ b ] > key : \
                    key = matrix [ a+1 ] [ b ]\
                    a += 1\
            if b+1 != size : \
                if matrix [ a ] [ b+1 ] > key : \
                    key = matrix [ a ] [ b+1 ]\
                    b += 1\
            if a-1 >= 0 :\
                if matrix [ a-1 ] [ b ] > key : \
                    key = matrix [ a-1 ] [ b ]\
                    a -= 1\
            if b-1 >= 0 :\
                if matrix [ a ] [ b-1 ] > key : \
                    key = matrix [ a ] [ b-1 ]\
                    b -= 1\
\
            if key not in path: path.append ( key )\
            else : break\
        \
        if path not in self.ans and len(path)>1 : self.ans.append ( path )\
        print (" ")\
        #print ( "ans :")\
        #print ( self.ans )\
        return\
        \
    \
    def longestIncreasingPath ( self, matrix ) -> int:\
        size = len ( matrix [ 0 ] )\
        for index_1 in range ( 0 , size ) :\
            for index_2 in range ( 0 , size ) :\
                self.increasingPath ( matrix , index_1 , index_2 )\
        \
        return max ( self.ans , key = lambda x : len ( x ) )\
\
Obj = Solution ()\
matrix = [[3,4,5],[3,2,6],[2,2,1]]\
print ( Obj.longestIncreasingPath ( matrix ) )}