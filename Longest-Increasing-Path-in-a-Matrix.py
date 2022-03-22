class Solution:
    def __init__ ( self ) :
        self.ans = []
        
    def increasingPath ( self , matrix , a , b ) :
        size = len ( matrix [ 0 ] )
        key = matrix [ a ] [ b ]
        path = [ key ]
        #print ( "key : ", key , "---------------")
        while True :
            #print ( "path : ", path )
            if a+1 != size : 
                if matrix [ a+1 ] [ b ] > key : 
                    key = matrix [ a+1 ] [ b ]
                    a += 1
            if b+1 != size :
                if matrix [ a ] [ b+1 ] > key : 
                    key = matrix [ a ] [ b+1 ]
                    b += 1
            if a-1 >= 0 :
                if matrix [ a-1 ] [ b ] > key : 
                    key = matrix [ a-1 ] [ b ]
                    a -= 1
            if b-1 >= 0 :
                if matrix [ a ] [ b-1 ] > key : 
                    key = matrix [ a ] [ b-1 ]
                    b -= 1

            if key not in path: path.append ( key )
            else : break
        
        if path not in self.ans and len(path)>1 : self.ans.append ( path )
        print (" ")
        #print ( "ans :")
        #print ( self.ans )
        return
        
    
    def longestIncreasingPath ( self, matrix ) -> int:
        size = len ( matrix [ 0 ] )
        for index_1 in range ( 0 , size ) :
            for index_2 in range ( 0 , size ) :
                self.increasingPath ( matrix , index_1 , index_2 )
        
        return max ( self.ans , key = lambda x : len ( x ) )

Obj = Solution ()
matrix = [ [ 3 , 4 , 5 ] , [ 3 , 2 , 6 ] , [ 2 , 2 , 1 ] ]
print ( Obj.longestIncreasingPath ( matrix ) )
