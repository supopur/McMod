from mcstatus import MinecraftServer


def getup(ip : str, port : str = '25565'):
    
    try:
        server = MinecraftServer.lookup(f"{ip}:{port}")
        ping = server.ping()
        status = server.status()
        print(status)
        return True
    except:
        return False
def getplayers(ip : str, port : str = '25565'):

    server = MinecraftServer.lookup(f"{ip}:{port}")
    query = server.query()
    players = f"The server has the following players online: {', '.join(query.players.names)}"
    print(f"The server has the following players online: {', '.join(query.players.names)}")
    return players




if __name__ == "__main__":
    ip = input("IP: ")
    port = input("Port 25565: ")
    if port == '':
        port = "25565"
    main(ip, port)
