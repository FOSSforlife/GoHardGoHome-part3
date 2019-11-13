# Go Hard or Go Home: Part 3

- [x] Created an end-to-end application (DeepLearningAgent) to train/run a Go bot (ch 8.1)

- [x] Used the web interface and flask server to play your Go bot using an attractive UI (ch 8.2)

- [x] Have created an AWS account (one for yourself and one for your bot) to allow training of your bot and deploying it. (ch. 8.3 and Appendix C)

- [x] Have installed gnugo as a LOCAL GTP server using the Go Text Protocol. The server can berun using a user interface such as Sabaki, Lizzie, GoRilla, or q5Go (Appendix C).

- [x] Create a web application using a Flask server that allows you to play against your bot using a browser to: localhost:5000/static/play_random_99.html . The browser will show a traditional (graphic) view of a Go game, with black and white stones on a wooden board (ch 8) (pp. 229-30).

- [x] Created a GTP frontend for your bot (chs. 8.4 and 8.5)

- [x] Your bot can play against two other local Go bots (gnugo and pachi). Gnugo has strength 12 kyu. Pachi has strength 2d to 7d, depending on the strength of the computer running it.

- [x] Your bot has been deployed on the OGS (online Go Server) platform (Appendix E)

- [x] Make a self-improving Deep Learning agent using Reinforcement learning, collecting experience data by playing copies of itself. (ch. 9)

- [x] Made a self-improving Deep Learning agent that uses Keras to develop its policy gradient algorithm (ch. 10).

- [x] Made a self-improving Deep Learning agent with the Q-learning algorithm (ch. 11)

- [x] Made a self-improving Deep Learning agent with the actor-critic method (based on advantage: A = R – V(s), where R is an estimate of the action-value method Q(s, a). (ch. 12)

- [x] Create a 48 plane board encoder, to make your Go bot more powerful.

- [x] Create TWO deep CNN policy networks for move prediction – one for more accurate results, and the other for faster evaluation (ch. 13)

- [x] Use the strong self-play CNN policy network to build your self-play value network.

- [x] Use the fast self-play CNN policy network to guide your tree-search algorithm.

- [x] Train a value network using the AlphaGo board encoder, and by having the Go bot play itself

- [x] Improve your MCTS rollout policy to use your policy network to guide rollouts, instead of just making moves at random

- [ ] Winning percentage against other Go bot engines gets you into the top six in the class.

- [ ] Winning percentage against other Go bot engines gets your bot into the top three.

- [x] Train your Go bot using different hyper-parameters to get best performance.

- [x] Be written in Python. No issues are shown in PyCharm (all source code screens shown a green checkmark at the top right hand corner).

- [x] Project directory pushed to new GitHub repository listed above


For any machine intended to host our go bot locally, the following command should be entered onto the command prompt:

  Windows Users: SET PATH=/path/to/deep_learning_and_the_game_of_go/code:$PATH
  
  Linux Users: export PATH=/path/to/deep_learning_and_the_game_of_go/code:$PATH

You should have Node.js and all of its relevant dependencies downloaded for this process to work. Then run the following command with the bot of your choice:

  cd deep_learning_and_the_game_of_go/code npm install
  
  forever start gtp2ogs.js --username <bot> --apikey 2b52acfc62953e38df0b961524895dd81b25bf5c /
  
  --hidden --persist --boardsize 19 --debug -- run_gtp.py
  
Note that <bot> is the filename of the bot that you want people to play against. To stop running the bot on your computer, enter 'forever stopall' on the command line.
