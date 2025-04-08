import os

r, w = os.pipe()
pid = os.fork()
if pid == 0:
    os.close(w)
    data = os.read(r, 100)
    print("Filho recebeu:", data.decode())
    os.close(r)
else:
    os.close(r)
    os.write(w, b"Mensagem do pai para o filho")
    os.close(w)
