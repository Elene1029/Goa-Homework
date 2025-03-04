#3) Handshake problem

def get_participants(handshakes):
    for h in range(handshakes + 2):
        if h * (h - 1) // 2>= handshakes:
            return h