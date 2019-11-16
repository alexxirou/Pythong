def geometrique(c,n,t):
    CA=c
    SI2=0
    SI1=n*c*t
    for i in range (1,n+1):
            I2=CA*(t)
            I1=c*(t)
            CA=CA+I2
            print(f'{i:3d}     {CA:8.2f}    {I1:8.2f} {I2:8.2f}')

            SI2=SI2+I2
    print(f'                     {SI1:8.2f} {SI2:8.2f}')

geometrique(10000,10,0.003)

