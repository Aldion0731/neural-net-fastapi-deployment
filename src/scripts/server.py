import uvicorn

from src.scripts.initialize import run as run_init
from src.server_client_utils.server_funcs import app
from src.utils.configurations import Config, load_config


def run(config: Config) -> None:
    run_init()
    uvicorn.run(app, host=config.server_info.host, port=config.server_info.port)


if __name__ == "__main__":
    run(load_config())
