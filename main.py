import j2l.pytactx.agent as pytactx

agent = pytactx.Agent(playerId=input("👾 id: "),
            arena="rattleslide",
            username="demo",
            password=input("🔑 password: "),
            server="mqtt.jusdeliens.com",
            verbosity=2)

while True:
  agent.update()
  agent.lookAt((agent.dir + 1) % 4)