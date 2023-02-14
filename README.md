da correggere alcune implementazioni fallaci + rifare una piccola parte del user_db

Idee ->

2) 2fa via email 
3) check di sicurezza ( al login )
4) anti token grabbing ( secure )
[
    2. ip
    3. user-agent
    4. pepper + hash(ip, user_agent, lang)
]

"""
verificazione di un nuovo client 
es se ip e user-agent son diversi da quelli messi al register
ti mette in verifica in cui l'utente dovra' accettarti
"""

progresso: 33 %


cosa da fare:

1) sicurezza - controllo Device validation
2) user ( 50% )
3) ticket ( 70% )
4) video ( current = 40 % )