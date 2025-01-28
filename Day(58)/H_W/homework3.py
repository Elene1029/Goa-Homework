# 3) Handshake problem

def get_participants(handshakes):
    for h in range(handshakes + 2):
        if h * (h - 1) // 2>= handshakes:
            return h

#. for h in range(handshakes + 2): ციკლი გადის h-ის ყველა შესაძლო მნიშვნელობაზე
# if h * (h - 1) // 2 >= handshakes: ვამოწმებთ შეუძლია თუ არა h ამდენი ხელის ჩამორთმევა h-სთვის საჭირო კომბინაცია
# return h: როგორც კი პირობა შესრულდება ციკლი წყდება და ვაბრუნებთ h      