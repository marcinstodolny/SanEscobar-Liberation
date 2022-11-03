import sys
from time import sleep
import util

intro_pic01 = r"""
    .                  .-.    .  _   *     _   .
           *          /   \     ((       _/ \       *    .
         _    .   .--'\/\_ \     `      /    \  *    ___
     *  / \_    _/ ^      \/\'__        /\/\  /\  __/   \ *
       /    \  /    .'   _/  /  \  *' /    \/  \/ .`'\_/\   .
  .   /\/\  /\/ :' __  ^/  ^/    `--./.'  ^  `-.\ _    _:\ _
     /    \/  \  _/  \-' __/.' ^ _   \_   .'\   _/ \ .  __/ \
   /\  .-   `. \/     \ / -.   _/ \ -. `_/   \ /    `._/  ^  \
  /  `-.__ ^   / .-'.--'    . /    `--./ .-'  `-.  `-. `.  -  `.
@/        `.  / /      `-.   /  .-'   / .   .'   \    \  \  .-  \%
@&8jgs@@%% @)&@&(88&@.-_=_-=_-=_-=_-=_.8@% &@&&8(8%@%8)(8@%8 8%@)%
@88:::&(&8&&8:::::%&`.~-_~~-~~_~-~_~-~~=.'@(&%::::%@8&8)::&#@8::::
`::::::8%@@%:::::@%&8:`.=~~-.~~-.~~=..~'8::::::::&@8:::::&8:::::'
 `::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::.'
    `:::::::::::::::::::::::::::::::::::::::::::::::::::::::.'
"""


def intro_txt01():
    return """In the far distant land of San Escobar, 
not so far away from Santo Domestos..."""


intro_pic02 = r"""
                     ,-~.
                    :  .o \
                    `.   _/`.
                      `.  `. `.
                        `.  `. `.
                          `.  `. `.
                  _._.-. -._`.  `. `.
              _.'            .`.  `. `.
           _.'            )     \   '
         .'             _.          "
       .'.-.'._     _.-'            "
     ;'       _'-.-'              "
    ; _._.-.-;  `.,,_;  ,..,,,.:"
   %-'      `._.-'   \_/   :;;
                     | |
                     : :
                     | |
                     { }
                      \|
                      ||
                      ||
                      ||         
                    _ ;; _
                   "-' ` -"
"""


def intro_txt02(player):
    return f"""A young hero was approached by a stork:
Stork: Greetings {player}! I came from Poland with a mission!
{player}: What mission?
Stork: You must establish San Escobar in the real world! Transform fantasy into a reality!
{player}: ...but how? Only Poland recognizes our existence!
You need to find a wizard! He will level you up and show you the way!
"""


story_pic1 = r"""
                       ,---.
                       /    |
                      /     |
                     /      |
                    /       |
               ___,'        |
             <  -'          :
              `-.__..--'``-,_\_
                 |o/ o :,.)_`>
                 :/ `     ||/)
                 (_.).__,-` |\
                 /( `.``   `| :
                 \'`-.)  `  ; ;
                 | `       /-<
                 |     `  /   `.
 ,-_-..____     /|  `    :__..-'\
/,'-.__\\  ``-./ :`      ;       \
`\ `\  `\\  \ :  (   `  /  ,   `. \
  \` \   \\   |  | `   :  :     .\ \
   \ `\_  ))  :  ;     |  |      ): :
  (`-.-'\ ||  |\ \   ` ;  ;       | |
   \-_   `;;._   ( `  /  /_       | |
    `-.-.// ,'`-._\__/_,'         ; |
       \:: :     /     `     ,   /  |
        || |    (        ,' /   /   |
        ||                ,'   /    |
"""


def story_txt01(player):
    return f"""{player}! You have finally found me!
I'll show you the way! You need to go right and down.
There should be a gate there...
I hope they didn't forget to place it there...
Anyway, let me level up you so you could kill the final boss.
"""


story_pic02 = r"""
         .            )        )
                  (  (|              .
              )   )\/ ( ( (
      *  (   ((  /     ))\))  (  )    )
    (     \   )\(          |  ))( )  (|
    >)     ))/   |          )/  \((  ) \
    (     (      .        -.     V )/   )(    (
     \   /     .   \            .       \))   ))
       )(      (  | |   )            .    (  /
      )(    ,'))     \ /          \( `.    )
      (\>  ,'/__      ))            __`.  /
     ( \   | /  ___   ( \/     ___   \ | ( (
      \.)  |/  /   \__      __/   \   \|  ))
     .  \. |>  \      | __ |      /   <|  /
          )/    \____/ :..: \____/     \ <
   )   \ (|__  .      / ;: \          __| )  (
  ((    )\)  ~--_     --  --      _--~    /  ))
   \    (    |  ||               ||  |   (  /
         \.  |  ||_             _||  |  /
           > :  |  ~V+-I_I_I-+V~  |  : (.
          (  \:  T\   _     _   /T  : ./
           \  :    T^T T-+-T T^T    ;<
            \..`_       -+-       _'  )
  )            . `--=.._____..=--'. ./ 
"""


def story_txt02(player):
    return f"""Turn back or I will end you, {player}!
San Escobar never meant to be a real country!
{player}: So why Polish Ministry of Foreign Affairs claims to have such good relationships with us, huh?!
Evil boss: RRrrraraaaargh! Take that!
"""


outro_pic = r"""
  ........::::::::::::..           .......|...............::::::::........
     .:::::;;;;;;;;;;;:::::.... .     \   | ../....::::;;;;:::::.......
         .       ...........   / \\_   \  |  /     ......  .     ........./\
...:::../\\_  ......     ..._/'   \\\_  \###/   /\_    .../ \_.......   _//
.::::./   \\\ _   .../\    /'      \\\\#######//   \/\   //   \_   ....////
    _/      \\\\   _/ \\\ /  x       \\\\###////      \////     \__  _/////
  ./   x       \\\/     \/ x X           \//////                   \/////
 /     XxX     \\/         XxX X                                    ////   x
-----XxX-------------|-------XxX-----------*--------|---*-----|------------X--
       X        _X      *    X      **         **             x   **    *  X
      _X                    _X           x                *          x     X_
"""


def outro_text(player):
    return f""" It was a great day for whole nation of San Escobar.
What was previously a pure fantasy, became a reality - a true
South American country with all it's modern-day problems.
Thank you, {player}!
"""


game_over = r"""
 / _____)  /\  |  ___ \(_______)   / ___ \| |  | (_______|_____ \ 
| /  ___  /  \ | | _ | |_____     | |   | | |  | |_____   _____) )
| | (___)/ /\ \| || || |  ___)    | |   | |\ \/ /|  ___) (_____ ( 
| \____/| |__| | || || | |_____   | |___| | \  / | |_____      | |
 \_____/|______|_||_||_|_______)   \_____/   \/  |_______)     |_|
"""


credits = r"""
  __  __                _         ____  _            _       _                                            
 |  \/  | __ _ _ __ ___(_)_ __   / ___|| |_ ___   __| | ___ | |_ __  _   _                                
 | |\/| |/ _` | '__/ __| | '_ \  \___ \| __/ _ \ / _` |/ _ \| | '_ \| | | |                               
 | |  | | (_| | | | (__| | | | |  ___) | || (_) | (_| | (_) | | | | | |_| |                               
 |_|  |_|\__,_|_|  \___|_|_| |_| |____/ \__\___/ \__,_|\___/|_|_| |_|\__, |                               
  __  __            _       _   _____         _                      |___/                                
 |  \/  | __ _  ___(_) ___ (_) |_   _| __ ___| |__   __ _  ___ ____                                       
 | |\/| |/ _` |/ __| |/ _ \| |   | || '__/ _ \ '_ \ / _` |/ __|_  /                                       
 | |  | | (_| | (__| |  __/| |   | || | |  __/ |_) | (_| | (__ / /                                        
 |_|  |_|\__,_|\___|_|\___|/ |   |_||_|  \___|_.__/ \__,_|\___/___|                                       
  _____                  |__/          ____ _ _   _                                                       
 |_   _|__  _ __ ___   __ _ ___ ____  / ___(_) |_| | _____                                                
   | |/ _ \| '_ ` _ \ / _` / __|_  / | |   | | __| |/ / _ \                                               
   | | (_) | | | | | | (_| \__ \/ /  | |___| | |_|   < (_) |                                              
   |_|\___/|_| |_| |_|\__,_|___/___|  \____|_|\__|_|\_\___/                                               
  __  __            _                       __  __                _       _                     _         
 |  \/  | __ _ _ __| |_ _   _ _ __   __ _  |  \/  | __ _ _ __ ___(_)_ __ | | _______      _____| | ____ _ 
 | |\/| |/ _` | '__| __| | | | '_ \ / _` | | |\/| |/ _` | '__/ __| | '_ \| |/ / _ \ \ /\ / / __| |/ / _` |
 | |  | | (_| | |  | |_| |_| | | | | (_| | | |  | | (_| | | | (__| | | | |   < (_) \ V  V /\__ \   < (_| |
 |_|  |_|\__,_|_|   \__|\__, |_| |_|\__,_| |_|  |_|\__,_|_|  \___|_|_| |_|_|\_\___/ \_/\_/ |___/_|\_\__,_|
                        |___/                                                                             
"""

BOSS_art = r"""
 /\   /\
 |0   0|
(_  ^  _)
 |V\"""V|
 \_____/
"""

enemy1 = r"""
     `oo.'
 ,.  `-')
'^\`-' '
   c-L'-
"""
enemy2 = r"""
`oo.'
`-')  ,.
( `-'/^`
 -`J-d 
"""

def intro(player):
    print(intro_pic01)
    for character in intro_txt01():
        write(character)
    sleep(2)
    util.clear_screen()
    print(intro_pic02)
    for character in intro_txt02(player):
        write(character)
    sleep(2)

def write(character):
    sys.stdout.write(character)
    sys.stdout.flush()
    sleep(0.05)

def story_wizard(player):
    print(story_pic1)
    for character in story_txt01(player):
        write(character)
    sleep(2)

def story_final_boss(player):
    print(story_pic02)
    for character in story_txt02(player):
        write(character)
    sleep(2)

def outro(player):
    print(outro_pic)
    for character in outro_text(player):
        write(character)
    sleep(2)

