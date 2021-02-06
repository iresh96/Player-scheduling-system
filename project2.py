from tabulate import tabulate

player_gametime =[(1,60)]
counter=1

def add_player(gametime):
    global player_gametime
    global counter
    player_gametime.append((counter+1,gametime))
    counter += 1

def remove_player(player,list):
    for i in list:
        if(player == i[0]):
            list.pop(list.index(i))


def waiting_time(list):
    waiting_times = []
    for i in range(len(list)):
        waiting_times.append(i*20)
    return waiting_times


def play_gameround(list):
    poped_player = list.pop(0)
    if(poped_player[1]-20 >0):
        list.append((poped_player[0],poped_player[1]-20))


#initially adds 5 players to the que
def add_players():
    for i in range (0,4):
        add_player(60)

add_players()

def print_schedule(list):
    print_list = []
    for i in range(len(list)):
        waiting_t=waiting_time(list)
        player = list[i][0]
        game_time = list[i][1]
        time_to_next = waiting_t[i]
        print_list.append([player,game_time,time_to_next])
    print(tabulate((print_list),headers=["Player","Game time","Waiting time"]))


keep_running = True

while (keep_running):
    print("\n")
    print("Initially 5 players added to the queue")
    print("Current schedule:")
    print_schedule(player_gametime)
    print("Press 1 to Add player with game time\nPress 2 to Remove player\nPress 3 to Play one Game round\nPress 4 to print Schedule\nPress 5 to EXIT")
    userinput = int(input("Pick a action:\n"))
    if(userinput==1):
        g_time = int(input("Input player playing time:\n"))
        add_player(g_time)
    elif(userinput==2):
        player = int(input("Insert player number to remove:"))
        remove_player(player,player_gametime)
        print("Player %d removed from queue" % player)
    elif(userinput==3):
        play_gameround(player_gametime)
    elif(userinput==4):
        print("-------------------------------------------------------------------------")
        print_schedule(player_gametime)
    elif(userinput==5):
        keep_running = False