from rsserpent_rev.models import Persona, Plugin

from . import route


plugin = Plugin(
    name="rsserpent-plugin-csj-sdk-update",
    author=Persona(
        name="EkkoG",
        link="https://github.com/EkkoG",
        email="beijiu572@gmail.com",
    ),
    prefix="/csj-sdk-update",
    repository="https://github.com/rsserpent-rev/rsserpent-plugin-csj-sdk-update",
    routers={route.path: route.provider},
)
