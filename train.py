import wandb
import random
import json
import os

config_str = os.environ.get("CONFIG", None)
config = {}
if config_str is not None:
    config = json.loads(config_str)

is_ci = config.get("CI", None)
name = None
if is_ci is not None:
    gitsha = config["GITHUB_SHA"]
    name = "github-" + gitsha[:6]

wandb.init(project="test", name=name)



epochs = config.get("epochs", 100)


for i in range(1, epochs):
    wandb.log({"loss": random.uniform(0, 1.0 / i),
               "precision": random.uniform(1 - 1.0 / i, 1)
    })


