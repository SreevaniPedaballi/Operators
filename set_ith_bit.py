"""
set 4th bit
n= 101010
ans=1
if 1 is there at 4th place just keep it as it is otherwise replace with 1
formula(n|(1<<(n-1)))
101010
001000
------
001000(ans)
"""