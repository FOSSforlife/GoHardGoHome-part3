import bot_v_bot
import human_v_bot


def main():
    selection = input('Press 1 for human v bot, press 2 for bot v bot: ')
    print(selection)
    if selection == '1':
        human_v_bot.main()
    elif selection == '2':
        bot_v_bot.main()


if __name__ == '__main__':
    main()
