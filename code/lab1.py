
servers={"server1":"on","server2":"on","server3":"off"}                                           
server= input("give a server\n")

try:
    if(server not in servers):
       raise ValueError("server not recognize")
except TypeError as te:
    print(f"error is {te}")
print(f"{server} is {servers[server]}")

# else:
#     if(server in servers.keys and servers[server].values=="on"):
#         print("server is running")
#     else:
#         print("server is not running")

