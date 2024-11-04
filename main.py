import utils
from Entity import Entity

if __name__ == '__main__':
    brands = Entity.parse(utils.get_page('/all-forums-by-manufacturer'))
    print(f'Saved {len(brands)} brands to {utils.write_to('_brands.json', brands)}')

    combined: list[Entity] = []
    for brand in brands:
        models = Entity.parse(utils.get_page(brand.path))
        combined.extend(models)
        print(f'Saved {len(models)} models to {utils.write_to(f'{brand.name}.json', models)}')

    print(f'Saved {len(combined)} models to {utils.write_to(f'_combined.json', combined)}')
