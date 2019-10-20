# Training a new bot
To train a new bot, call `train_new_bot.py` from the root directory.

### Usage Example
```
python train_new_bot.py --bot-name=first_bot --epochs=15 --num-samples=300
```

### Arguments
```
--bot-name: REQUIRED! What the bot will be named. Must be a unique name! Meaning, 
    if a bot was previously trained with this given name in the past, the train job will fail.
--optimizer: What optimizer to use. By default, adadelta
--epochs: How many train epochs to do. The higher the better! Default: 10
--batch-size: How many data points to use per weight pass. The higher the worst it does. 
    However, too low will also be bad. Default: 128.
--num-samples: How many different games to draw samples from. Default 100. MINIMUML: 50
```

### Tips
Some errors may occur. I found that, sometimes, deleting the data/ directory and running the script again fixes some errors. Give this a try.


# Bot vs. Bot
Call `bot_v_bot.py` to watch two bots play a game of Go! I have included two trained bots (~90% accuracy each) that can work as a demo. They can be found in the Google Drive link at the bottom of this document.

### Usage Example
```
python bot_v_bot.py --bot-file-1 ./agents/deep_bot_2.h5 --bot-file-2 ./agents/deep_bot_3.h5
```

### Arguments
```
--bot-file-1: REQUIRED! The file path to the h5 file that has the bot to be used.
    i.e. ./agents/deep_bot_2.h5
--bot-file-2: REQUIRED! The file path to the h5 file that has the bot to be used.
    i.e. ./agents/deep_bot_3.h5
```


# Human vs. Bot
Call `human_v_bot.py` to watch two bots play a game of Go! I have included two trained bots (~90% accuracy each) that can work as a demo. They can be found in the Google Drive link at the bottom of this document.

### Usage Example
```
python human_v_bot.py --bot-file ./agents/deep_bot_2.h5
```

### Arguments
```
--bot-file: REQUIRED! The file path to the h5 file that has the bot to be used.
    i.e. ./agents/deep_bot_2.h5
```


# Evaluate bots in parallel
Using `eval_bots_parallel.py`, you can make two bots play multiple games to see which one is the best one!

### Usage Example
```
python eval_bots_parallel.py --agent1 ./agents/deep_bot_2.h5 --agent2 ./agents/deep_bot_3.h5 --num-games 20 --num-workers 5
```   

### Arguments
```
--agent1: REQUIRED! The file path to the h5 file that has the bot to be used.
    i.e. ./agents/deep_bot_2.h5
--agent2: REQUIRED! The file path to the h5 file that has the bot to be used.
    i.e. ./agents/deep_bot_2.h5
--num-games: How many games to play
--num-workers: If running in parallel, choose how many threads to run on.
    Note: If the num-games is not evenly divisible by this number, then the remainder
    will be ignored. i.e. if num-games == 20 and num-workers == 3, then each worker
    will get 6 games, for a total of 18.
```


   
# Generate games for training data
The script `generate_mcts_games.py` generates games using the MCTS algorithm. Use this to create features.py and labels.py before training the bot (note: this step shouldn't be necessary if you wish to use the files in the generated_games folder).

### Usage Example
```
python generate_mcts_games.py -n 20 --board-out features.npy --move-out labels.npy
```

### Arguments
```
--board-size: (default = 9) The size X, resulting in an X by X board.
--rounds: (default = 1000) Number of rounds per game.
--temperature: (default = 0.8): Affects the exponent used in MCTS algorithm.
--max-moves (default = 60): Maximum moves per game.
--num-games: (default = 10): The number of games to generate.
--board-out, --move-out: REQUIRED! This is where the training data gets stored
```

# Using the already trained bots
We've already trained two bots that perform at around 90% accuracy. If you'd like to use these bots
as demos for the above scripts, they can be found [in this Google Drive folder](https://drive.google.com/drive/folders/1HZUnoPckNOFC3Rw34y7YMT4-ILS_R9Hu?usp=sharing). 
