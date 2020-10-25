# swaps specific elements of one skin with those copied from another, gives the option to move the switched elements into
# a separate folder for customization

from pathlib import Path
from glob import glob
from shutil import move, copy2


# all possible options for swapping are lists of filenames
# '@2x' can/will be added to the end of any file
menu                       = ['menu-snow*.png', 'menu-back*.png', 'mode-*.png', 'selection-mode*.png', 'selection-mods*.png', 'selection-random*.png', 
                              'selection-options*.png', 'selection-tab*.png']
followpoints               = ['followpoint*.png']
ranking_letters            = ['ranking-*-small*.png']
ranking_panel              = ['ranking-[A-DSX].png', 'ranking-[A-DSX]H.png', 'ranking-[A-DSX]@2x.png', 'ranking-[A-DSX]H@2x.png', 
                              'ranking-graph*.png', 'ranking-maxcombo*.png', 'ranking-panel*.png', 'ranking-perfect*.png', 
                              'ranking-accuracy*.png', 'ranking-title*.png', 'ranking-winner*.png']
stars                      = ['star.png', 'star@2x.png']
section_pass_fail          = ['section-pass.png', 'section-fail.png']
skip                       = ['play-skip*.png']
health_bar                 = ['scorebar-*.png']
fail_pause                 = ['fail-background*.png', 'pause-overlay*.png', 'pause-back*.png', 'pause-continue*.png', 
                              'pause-replay*.png', 'pause-retry*.png']
mod_icons                  = ['selection-mod-*.png']
startup_menu_bg            = ['menu-background*.jpg']
cursor                     = ['cursor*.png']
hit_indicators             = ['hit0*.png', 'hit50*.png', 'hit100*.png', 'hit300*.png', 'particle*.png', 'lighting*.png', 'sliderpoint*.png']
hitcircles                 = ['hitcircle*.png']
input_overlay              = ['inputoverlay*.png']
approach_circle            = ['approachcircle*.png']
welcome_text               = ['welcome_text*.png']
slider                     = ['sliderb*.png', 'sliderscorepoint*.png', 'sliderfollowcircle*.png', 'sliderend*.png', 'sliderstart*.png', 'reversearrow*.png']
spinner                    = ['spinner-*.png']
menu_button_bg             = ['menu_button_background*.png', 'star2*.png']
skin_ini                   = ['skin.ini']
score_nums                 = ['score-*.png']
default_nums               = ['default-*.png']
countdown                  = ['ready*.png', 'count*.png', 'go*.png']
warning_arrows             = ['play-warningarrow*.png', 'arrow-*.png']
gameplay                   = hitcircles + approach_circle + slider + spinner + followpoints
gameplay                   = [x for x in {i for i in gameplay}]
sounds                     = ['*.wav', '*.ogg', '*.mp3']


# list of all the above lists
POSSIBLE_ELEMENTS = ['menu', 'gameplay', 'ranking_letters', 'ranking_panel', 'stars', 'section_pass_fail', 'skip', 'sounds', 'health_bar', 
                        'fail_pause', 'mod_icons', 'startup_menu_bg', 'cursor', 'hit_indicators', 'hitcircles', 
                        'input_overlay', 'approach_circle', 'welcome_text', 'slider', 'spinner', 'menu_button_bg', 'skin_ini', 'score_nums', 
                        'default_nums', 'combo_nums', 'countdown', 'warning_arrows', 'followpoints']

# list of skin names that exist in the user's Skins folder
LIST_OF_SKINS = [x[42:] for x in glob('C:\\Users\\*\\AppData\\Local\\osu!\\Skins\\*')]
# the '42' only works when the user's name is 7 characters, need to change this to check for 
# username length and then add 35 to it and insert that number here


# file shit
def run(skin1, skin2, delta_element, delete_or_move):
    skin1_path = Path('C:\\Users\\Matthew\\AppData\\Local\\osu!\\Skins\\' + skin1)
    #skin2_path = Path('C:\\Users\\Matthew\\AppData\\Local\\osu!\\Skins\\' + skin2)

    #skin1_list_of_element_paths = [x for x in skin1_path.iterdir() if skin1_path.is_dir()]
    #skin2_list_of_element_paths = [x for x in skin2_path.iterdir() if skin2_path.is_dir()]

    elements_to_remove = eval(delta_element)  # elements from skin1 that we are moving/deleting
    s1_elements_tbg = [f'C:\\Users\\Matthew\\AppData\\Local\\osu!\\Skins\\{skin1}\\{x}' for x in elements_to_remove]  # tbg stands for 'to be globbed' a.k.a. will use glob.glob() on each element
    s2_elements_tbg = [f'C:\\Users\\Matthew\\AppData\\Local\\osu!\\Skins\\{skin2}\\{x}' for x in elements_to_remove]  # tbg stands for 'to be globbed' a.k.a. will use glob.glob() on each element

    s1_element_paths = set()  # set of strings of paths to the elements we are either deleting or moving
    s2_element_paths = set()
    for i in s1_elements_tbg:  # could name these variables better lol
        e = glob(i)
        for x in e:
            s1_element_paths.add(x)
    for i in s2_elements_tbg:
        e = glob(i)
        for x in e:
            s2_element_paths.add(x)


    # either moves or deletes the files that are being replaced before bringing the new ones in
    if delete_or_move == 'move':
        for element_path in s1_element_paths:
            move(element_path, target_folder)
    elif delete_or_move == 'delete':
        for element in s1_element_paths:
            Path(element).unlink()


    # copy the targeted elements from skin2 into skin1
    for element_path in s2_element_paths:
        copy2(element_path, skin1_path)


if __name__ == '__main__':
    # input commands
    skin1 = input('Enter the exact name of the skin you want to edit: ')
    while skin1 not in LIST_OF_SKINS:
        skin1 = input('That skin does not exist in your Skins folder. Please enter the name of a skin that exists in your Skins folder: ')

    print(f'Possible Elements: {POSSIBLE_ELEMENTS}')
    delta_element = input('Enter the element from the list of possible elements of a skin that you want to change: ')
    while delta_element not in POSSIBLE_ELEMENTS:
        print(f'Possible Elements: {POSSIBLE_ELEMENTS}')
        delta_element = input('Your input was not valid, please enter a valid set of elements from the list: ')

    delete_or_move = input('Enter "delete" if you want to delete the specified elements from the edited skin, enter "move" if you '\
                            'want to copy the elements you are removing to another folder: ')
    while delete_or_move != 'delete' and delete_or_move != 'move':
        delete_or_move = input('That input was invalid. Enter "delete" if you want to delete the specified elements from the edited skin, enter "move" if you '\
                                'want to copy the elements you are removing to another folder: ')
    if delete_or_move == 'move':
        target_folder = input('Enter the path for the folder you want to move the copied files into: ')
        while Path(target_folder).is_dir() is False:
            target_folder = input('The path you entered did not lead to a directory. Please enter a valid path to the directory you want the files to be sent to: ')

    skin2 = input('Enter the exact name of the skin you want to take the specified element from: ')
    while skin2 not in LIST_OF_SKINS:
        skin2 = input('That skin does not exist in your Skins folder. Please enter the name of a skin that exists in your Skins folder: ')
    while skin2 == skin1:
        skin2 = input('Please enter a different skin than you entered ealier. This is the skin you are grabbing the element from: ')

    
    run(skin1, skin2, delta_element, delete_or_move)