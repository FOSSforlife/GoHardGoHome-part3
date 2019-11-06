# Go Hard or Go Home: Part 3

For any machine intended to host our go bot locally, the following command should be entered onto the command prompt:
  Windows Users: SET PATH=/path/to/deep_learning_and_the_game_of_go/code:$PATH
  Linux Users: export PATH=/path/to/deep_learning_and_the_game_of_go/code:$PATH
You should have Node.js and all of its relevant dependencies downloaded for this process to work. Then run the following command with your version of the arguments specified:

  cd deep_learning_and_the_game_of_go/code npm install
  forever start gtp2ogs.js \   
  --username <bot> \   
  --apikey 2b52acfc62953e38df0b961524895dd81b25bf5c \   
  --hidden \   
  --persist \   
  --boardsize 19 \   
  --debug 
  -- run_gtp.py
  
  where <bot> is the filename of the bot that you want people to play against.
