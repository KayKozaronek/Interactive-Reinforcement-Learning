import streamlit as st

def show():    
    st.write('### Exercise 9.3')
    st.write("""
             What $n$ and $c_{i,j}$ produce the feature vectors **x**(s) $= (1, s_1, s_2, s_1s_2, s_1^2, s_2^2, s_1s_2^2, s_1^2s_2, s_1^2s_2^2)$             """)
    
    with st.expander('See Solution'):
        st.write("""
                Following the Definition $(9.17)$ from the textbook we know that 
                
                $$
                x_i(s) = \prod^k_{j=1} s_j^{c_{i,j}}
                $$
                
                To arrive at the desired feature vector use the following table:
                
                | $c_{i,j}$ | $i = 1$ | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
                |-----------|---------|---|---|---|---|---|---|---|---|
                | $j = 1$   | 0       | 1 | 0 | 1 | 2 | 0 | 1 | 2 | 2 |
                | $j = 2$   | 0       | 0 | 1 | 1 | 0 | 2 | 2 | 1 | 2 |
                """)
        st.write("")
        st.write("""
                Let's look at an example:
                - $s_5$ of our feature vector $x(s)$ is $= s_1^2$
                - We can obtain the same by using our table for $c_{i,j}$
                - For $s_5$, $i = 5$. Looking at the corresponding $j$ values, we get $c_{5,1} = 2$ and $c_{5,2} = 0$
                - Plugging this into our formula we get the following: 
                $$
                x_5(s) = \prod^k_{j=1} s_j^{c_{i,j}}
                = s_1^{c_{5,1}} s_2^{c_{5,2}} 
                = s_1^2 s_2^0
                = s_1^2
                $$
                """)