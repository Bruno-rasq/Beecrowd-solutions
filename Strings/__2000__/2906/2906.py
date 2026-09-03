class Database_of_Clients:
    clients = set()
    @staticmethod
    def verify_email(email: str):
        local, domain = email.split('@')
        local = local.split('+')[0].replace('.', '')
        Database_of_Clients.clients.add(f"{local}@{domain}")
        
        
n_emails_tp_verify = int(input())
for _ in range(n_emails_tp_verify):
    email = input()
    
    Database_of_Clients.verify_email(email)
    
print(len(Database_of_Clients.clients))