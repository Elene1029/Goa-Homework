# I love you, a little , a lot, passionately ... not at all

def how_much_i_love_you(nb_petals):
    my_list = ["I love you","a little","a lot","passionately","madly","not at all"]
    love = (nb_petals - 1) % 6
    return my_list[love]