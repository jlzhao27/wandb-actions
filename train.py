import wandb
import random
import json
import os

config_str = os.environ.get("JOB_CONFIG", None)
config = {}
if config_str is not None:
    config = json.loads(config_str)

print(config)
is_ci = os.environ.get("CI", None)
name = None
if is_ci is not None:
    gitsha = os.environ["GITHUB_SHA"]
    name = f'{config["artifactCollection"]}-{gitsha[:8]}'

# HACK: since the artifact version uses a wandb-artifact://, the server will try to
# resolve it and fail
del config["artifactVersion"]
wandb.init(project="test", name=name, config=config)
epochs = config.get("epochs", 100)


for i in range(1, epochs):
    wandb.log({"loss": random.uniform(0, 1.0 / i),
               "precision": random.uniform(1 - 1.0 / i, 1)
    })


