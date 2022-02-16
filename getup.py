from mcstatus import MinecraftServer


def getup(ip : str, port : str = '25575'):
    
    try:
        server = MinecraftServer.lookup(f"{ip}:{port}")
        server.query()
        return True
    except:
        return False
    
    
def getplayers(ip : str, port : str = '25575'):

    server = MinecraftServer.lookup(f"{ip}:{port}")
    query = server.query()
    players = f"The server has the following players online: {', '.join(query.players.names)}"
    print(f"The server has the following players online: {', '.join(query.players.names)}")
    return players




if __name__ == "__main__":
    ip = input("IP: ")
    port = input("Port 25575: ")
    if port == '':
        port = "25575"
    main(ip, port)
