from example.commons import Faker
from pyecharts import options as opts
from pyecharts.charts import Map


def map_base() -> Map:
    c = (
        Map()
        .add("商家A", [list(z) for z in zip(Faker.provinces, Faker.values())], "china")
        .set_global_opts(title_opts=opts.TitleOpts(title="Map-基本示例"))
    )
    print(Faker.values())
    print(type(Faker.values()))
    return c

a = map_base()