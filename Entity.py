from dataclasses import dataclass

from bs4 import Tag

import utils


@dataclass
class Entity:
    name: str
    path: str
    threads: int
    messages: int

    @classmethod
    def parse(cls, tag: Tag) -> list['Entity']:
        entities: list[Entity] = []

        for node in tag.select('.block-body > .node'):
            info = node.select_one('.node-title > a')
            stats = node.select('.node-stats dd')

            entities.append(Entity(
                utils.safe_value(lambda: info.text),
                utils.safe_value(lambda: info.get('href')),
                utils.safe_value(lambda: utils.format_num(stats[0].text)),
                utils.safe_value(lambda: utils.format_num(stats[1].text)),
            ))

        return entities
