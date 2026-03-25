import dlt
from dlt.sources.rest_api import RESTAPIConfig, rest_api_resources

@dlt.source
def wikidata_entities_source(access_token=dlt.secrets.value):
    config: RESTAPIConfig = {
        "client": {
            "base_url": "https://www.wikidata.org/w/rest.php/wikibase/v1",
            "auth": {
                "type": "bearer",
                "access_token": access_token,
            },
        },
        "resources": [
            {"name": "entities_items", "endpoint": {"path": "entities/items/{item_id}"}},
            {"name": "entities_items_statements", "endpoint": {"path": "entities/items/{item_id}/statements", "data_selector": "statements"}}
        ],
    }
    yield from rest_api_resources(config)


def get_data() -> None:
    pipeline = dlt.pipeline(
        pipeline_name="wikidata_entities_pipeline",
        destination="duckdb",
        dataset_name="wikidata_entities_data",
    )
    load_info = pipeline.run(wikidata_entities_source)
    print(load_info)

if __name__ == "__main__":
    get_data()