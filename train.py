import wandb
import random
import json
import os

wandb.init(project="test")

config_str = os.environ.get("CONFIG", None)

config = {}
if config_str is not None:
    config = json.loads(config_str)

epochs = config.get("epochs", 100)

for i in range(1, epochs):
    wandb.log({"loss": random.uniform(0, 1.0 / i),
               "precision": random.uniform(1 - 1.0 / i, 1)
    })


