from dlgo.agent.naive import RandomBot
from dlgo.agent import load_prediction_agent
from dlgo.httpfrontend.server import get_web_app
import h5py

bots = {}
random_agent = RandomBot()
# bot_agent = load_prediction_agent(h5py.File("agents/GHGHbot1_rl_policy.h5", "r"))
bot_agent = load_prediction_agent(h5py.File('agents/deep_bot_2.h5', "r"))
web_app = get_web_app({'random': random_agent, 'predict': bot_agent})
web_app.run(threaded=False)
