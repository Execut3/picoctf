flag = [' ' for i in range(4*8)]
flag[:4] = 'pico'
flag[4*6:4*7] = '706c'
flag[4:2*4] = 'CTF{'
flag[4*4:4*5] = 'ts_p'
flag[4*3:4*4] = 'lien'
flag[4*5:4*6] = 'lz_b'
flag[4*2:4*3] = 'no_c'
flag[4*7:4*8] = '5}'
print(''.join(flag))
