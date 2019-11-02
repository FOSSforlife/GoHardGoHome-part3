# Go Hard or Go Home: Part 2

## Requirements
- [x] Create the [generate_mcts_games](./generate_mcts_games.py) file, which generates games by encoding the game state before each move, encodes the move as a one-hot vector, and applies it.
- [x] Implement Monte-Carlo tree search, alpha-beta pruning and minimax (ch. 4). Create an MCTSAgent and let it play against itself.
    - We created minimax and alphabeta agents, and we subsequently created a program to have them play against each other to prove they are correctly implemented (alphabeta_minimax_test.py). We did this by downloading and observing the code for alpha-beta pruning and depth-pruned minimax (seen in the minimax folder), as well as a default MCTSAgent from the author's GitHub.
    - We wrote code enabling the MCTSAgent to play against itself in our [generate_mcts_games.py](./generate_mcts_games.py)
- [x] Create a program to create, and run Go games, and save them. Use it to generate 20 9x9 Go games, and store the features in features.py, and the labels in labels.py.
    - This is done using [generate_mcts_games.py](./generate_mcts_games.py)
- [x] Confirm the CNN from listings 6.24-26 of your text runs, and produces the output shown in your text. Print out the probabilities of its recommended moves (see 6.26).
    - [training_cnn.py](./training_cnn.py)
    - To see the probabilities of all moves, play a bot_v_bot or human_v_bot game with the `--print-probs` flag.
        - See "Bot vs Bot" and "Human vs Bot" sections below.
- [x] Create the KGSIndex class that downloads SGF files from https://u-go.net/gamerecords, and download the files. (see listing 7.1).
    - [dlgo/data/index_processor.py](./dlgo/data/index_processor.py)
- [x] Replay the (pretend) game from Listing 7.2. Make sure it replays the game correctly.
    - [game_replay.py](./game_replay.py)
- [x] Create the Go data processor that can transform raw SGF data into features and labels for a machine learning algorithm.
    - [dlgo/data/parallel_processor.py](./dlgo/data/parallel_processor.py)
- [x] Create the OnePlaneEncoder and SevenPlaneEncoder, and verify that they produce the correct output from the text.
    - [dlgo/encoders/oneplane.py](./dlgo/encoders/oneplane.py)
    - [dlgo/encoders/sevenplane.py](./dlgo/encoders/sevenplane.py)
- [x] Create the training and test generators that use the GoDataProcessor, so that Keras can use those generators to fit the model and to evaluate it.
    - [train_generator.py](./train_generator.py)
- [x] Add the Adagrad optimizer to allow adaptive gradient methods.
    - The Adagrad optimizer is utilized [train_generator.py](./train_generator.py), as seen on line 43.
- [x] Train your Go bot using different hyperparameters to get best performance.
    - Trained bots can be found in [this Google Drive folder](https://drive.google.com/drive/u/2/folders/1HZUnoPckNOFC3Rw34y7YMT4-ILS_R9Hu).
    - For instructions on running the trained bots as well as training new ones, see the section below.
- [X] Be written in Python. No issues are shown in PyCharm (all source code screens shown a green checkmark at the top right hand corner).
    - Upon completing the code on one of our group member's computers, the project is able to be scanned through in PyCharm with no errors, or warnings, but there are formatting complaints. Please ignore these as all aspects of the program runs properly and the formatting is a matter of our preference for readablility and farmiliarity's sake.



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
Some errors may occur. We found that, sometimes, deleting the data/ directory and running the script again fixes some errors. Give this a try.


# Bot vs. Bot
Call `bot_v_bot.py` to watch two CNN bots play a game of Go! we have included two trained bots (~90% accuracy each) that can work as a demo. They can be found in the Google Drive link at the bottom of this document.

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
--print-probs: If set, the probabilities of each bot move will be printed on each step
```


# Human vs. Bot
Call `human_v_bot.py` to play against one of our bots in a game of Go! We have included a trained bot (~90% accuracy each) that can work as a demo. It can be found in the Google Drive link at the bottom of this document.

### Usage Example
```
python human_v_bot.py --bot-file ./agents/deep_bot_2.h5
```

### Arguments
```
--bot-file: REQUIRED! The file path to the h5 file that has the bot to be used.
    i.e. ./agents/deep_bot_2.h5
--print-probs: If set, the probabilities of each bot move will be printed on each step
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


# Testing our alpha beta and depth-pruned minimax agents
Using 'alphabeta_minimax_test', you can make these two agents play against themselves and witness that they are correctly implemented.


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
