import streamlit as st

def show():    
    st.write('### Exercise 9.2')
    st.write("""
             Why does $(9.17)$ define $(n + 1)^k$ distinct features for dimension $k$?
             """)
    
    with st.expander('See Solution'):
        st.write("""
                 Let's recall the definitions:
                 - $n$ = order of polynomial (e.g. maximum exponent)
                 - $k$ = dimension of state space (e.g. a grid world would be $k = 2$ dimensional since it has a horizontal and vertical component)
                 
                 Let's look at an example to see why we need $(n+1)^k$ (instead of $n^k$) distinct features for k dimension:
                 
                 **Case 1 ($n = 1$ , $k = 2$):**
                 - $k = 2$ means that we have a 2 dimensional space. This means that each state $s$ corresponds to 2 numbers (a 2 dimensional vector) $s_1, s_2$
                 - our formula would tell us that we obtain $(n+1)^k = (1+1)^2 = 4$ distinct features
                 - we can spell these out:
                 
                    | 1 | 2     | 3     | 4        | 5       |
                    |---|-------|-------|----------|---------|
                    | 1 | $s_1$ | $s_2$ | $s_1s_2$ | $s_1^2$ | 
                 
                """)
        
        st.write("") 
         
        st.write(""" 
                 Now let's look at what happens if we increase n by 1
                 
                 **Case 2 ($n = 2$ , $k = 2$):**
                 - our formula would tell us that we obtain $(n+1)^k = (2+1)^2 = 9$ distinct features
                 - we can spell these out:
                 
                    | 1 | 2     | 3     | 4        | 5       | 6       | 7          | 8          | 9            |
                    |---|-------|-------|----------|---------|---------|------------|------------|--------------|
                    | 1 | $s_1$ | $s_2$ | $s_1s_2$ | $s_1^2$ | $s_2^2$ | $s_1^2s_2$ | $s_1s_2^2$ | $s_1^2s_2^2$ |
                 """)
        
        st.write("") 
         
        st.write(""" 
                 Notice what happens for the case of $n = 0$ 
                 
                 **Case 3 ($n = 0$ , $k = 2$):**
                 - our formula would tell us that we obtain $(n+1)^k = (1)^2 = 1$ distinct features
                                  
                    | 1 |
                    |---|
                    | 1 |
                 """)
        
        st.write("") 
         
        st.write(""" 
                 For completion here's what happens if we change k to  $k = 3$ 
                 
                 **Case 4 ($n = 1$ , $k = 3$):**
                 - our formula would tell us that we obtain $(n+1)^k = (1+1)^3 = 8$ distinct features
                 
                    | 1 | 2     | 3     | 4     | 5        | 6        | 7        | 8           |
                    |---|-------|-------|-------|----------|----------|----------|-------------|
                    | 1 | $s_1$ | $s_2$ | $s_3$ | $s_1s_2$ | $s_1s_3$ | $s_2s_3$ | $s_1s_2s_3$ | 
                 """)